
from threading import Timer
from pytesseract.pytesseract import Output
import requests,time,os,io ,re , logging
import pickle # Havent used It
import fileb
import pytesseract , cv2
from bs4 import BeautifulSoup
from PIL import Image
first_url='https://mangareader.tv/'
Website='mangareader'

#Check If There Something exists in A file like images etc
def find_mangas_link():
    html_text= requests.get(first_url)
    soup =BeautifulSoup(html_text.text , 'lxml')
    mangas_links=soup.find_all('div',class_='d47')
    for manga_links in mangas_links :
        manga_link=manga_links.find('div',class_='d53').a['href'] #found the link
        #getting Name of chapter
        Mangas_List=list(dict.fromkeys(str(manga_links.text).split()))
        for index in range(0,len(Mangas_List)):
            if(Mangas_List[index]=='Chapter'):
                index_name=index
        global Mangas_list_Name
        Mangas_list_Name=[]
        for index in range(0,index_name):
            Mangas_list_Name.append(Mangas_List[index])
        
        find_chapters(f'{first_url}'+f'{manga_link}')

def find_chapters(chapters_links1):
    html_text= requests.get(chapters_links1)
    soup =BeautifulSoup(html_text.text , 'lxml')
    chapters_links=soup.find_all('table',class_='d48')
    for chapter_link1 in chapters_links:
        t=Timer(30.0,check_files_duplicates)
        t.start()
        global ix
        Chapter_clink=chapter_link1.find_all('a')
        ix=0
        for index in range(0,len(Chapter_clink)):
            Title_forchapter=[]
            Number_Chapter=[]
            Link_ForChapter=[]
            look_atthisChapter=str(Chapter_clink[index]).split()
            for index_1 in range(0,len(look_atthisChapter)):
                if index_1 > 3:
                    
                    Title_forchapter.append(look_atthisChapter[index_1].strip())
                if index_1 ==3:
                    
                    Number_Chapter.append(look_atthisChapter[index_1].strip().replace(':','').replace('<','').replace('>','').replace('a','').replace(',','').replace('/',''))
                if index_1 == 1:
                    Link_ForChapter.append(look_atthisChapter[index_1].strip())
                    #1 for link ,3 For Number ,3 ->
            for ChPages_Link in Link_ForChapter:
                ix+=1
                url = re.findall('/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ChPages_Link)
                find_Pages(f'{first_url}'+f'{url[0]}')
            global Chapter_Page,Num_CH_DIC
            Chapter_Page=listToStringWithoutBrackets(Mangas_list_Name).replace(",","").replace('"','')
            logging.info(f'Manga : {Chapter_Page}')
            Num_CH_DIC=f'{listToStringWithoutBrackets(Number_Chapter).replace(",","")}-'f'{ix}'
            make_dirs(f'{Website}',f'{Chapter_Page}',f'{Num_CH_DIC}')
            for index_mwx in range(0,len(Pages_Chapter)):
                Download_Pages(os.getcwd(),listToStringWithoutBrackets(Pages_Chapter[index_mwx]),index_mwx)#Did Get The Page Link
            logging.info(f'Finished Chapter - : {ix}')
            time.sleep(1.5)
            
                    
    time.sleep(12) #increase if u get blocked 

def listToStringWithoutBrackets(list1):
    list1=str(list1).replace('[','').replace(']','')
    list1=str(list1).replace("'","")
    return list1

def find_Pages(Chapter_url):
    global Pages_Chapter
    Pages_Chapter=[]
    html_text= requests.get(Chapter_url)
    soup =BeautifulSoup(html_text.text , 'lxml')
    images=soup.find_all('img',class_='img-loading')
    for image in images:
        Pages_Chapter.append(image['data-src'])

def Download_Pages(Path,url,Number_Page_Paste):
    if not (load_files(f'{Path}\manga\{Website}\{Chapter_Page}\{Num_CH_DIC}\{Number_Page_Paste}.png')):
        response = requests.get(url)
        img = Image.open(io.BytesIO(response.content))
        logging.info(f'Finshed Page : {Number_Page_Paste}')
        img.thumbnail((800,600))
        destination=f'{Path}\manga\{Website}\{Chapter_Page}\{Num_CH_DIC}\{Number_Page_Paste}.png'
        img.save(f'{destination}', optimize=True, quality=50)


def make_dirs(Website,Name,Chapter):
    dir = os.path.join(f'{os.getcwd()}',f'manga')
    if not os.path.exists(dir):
        os.mkdir(dir)
    dir = os.path.join(f'{os.getcwd()}\manga',f'{Website}')
    if not os.path.exists(dir):
        os.mkdir(dir)
    dir = os.path.join(f'{os.getcwd()}\manga\{Website}',f'{Name}')
    if not os.path.exists(dir):
        os.mkdir(dir)
    dir = os.path.join(f'{os.getcwd()}\manga\{Website}\{Name}',f'{Chapter}')
    if not os.path.exists(dir):
        os.mkdir(dir)


#for pic text not good
def extract_image_text():
    # Defining paths to tesseract.exe 
    # and the image we would be using
    destination=r'C:\Users\maxpa\Desktop\stuuff\testscan\Mangas_Server\\0.png'
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img2=cv2.imread(destination)
    text2=pytesseract.image_to_string(img2)
    print(text2)
    # reading image using opencv

    image2 = cv2.imread(destination)

    #converting image into gray scale image

    gray_image = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    threshold_img = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    custom_config = r'--oem 3 --psm 6'

    details = pytesseract.image_to_data(threshold_img, output_type=Output.DICT, config=custom_config, lang='eng')

    total_boxes = len(details['text'])

    for sequence_number in range(total_boxes):
        if (int(float(details['conf'][sequence_number])) >30):
            (x, y, w, h) = (details['left'][sequence_number], details['top'][sequence_number], details['width'][sequence_number],  details['height'][sequence_number])
            threshold_img = cv2.rectangle(threshold_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # display image

    cv2.imshow('captured text', threshold_img)

    # Maintain output window until user presses a key

    cv2.waitKey(0)

    # Destroying present windows on screen

    cv2.destroyAllWindows()
    
def load_files(listString):
    dir = os.path.join(f'{os.getcwd()}')
    all_directory_presnt=([x[0] for x in os.walk(dir)])
    if(len(all_directory_presnt) > 1):
        for index in range(1,len(all_directory_presnt)):
                if listString in all_directory_presnt[index]:
                    return True
                    break

def check_files_duplicates():
    array=[]
    dir = os.path.join(f'{os.getcwd()}',f'manga')
    if os.path.exists(dir):
        array.append(rf'{os.getcwd()}')
        fileb.check_for_duplicates(array)

if __name__=='__main__':
    logging.basicConfig(filename="logsManga.log", level=logging.INFO) 
    find_mangas_link()
    
