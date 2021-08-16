import requests,time,os,pickle ,re , logging
from bs4 import BeautifulSoup
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
            Chapter_Page=listToStringWithoutBrackets(Mangas_list_Name).replace(",","")
            Num_CH_DIC=f'{listToStringWithoutBrackets(Number_Chapter).replace(",","")}-'f'{ix}'
            make_dirs(f'{Website}',f'{Chapter_Page}',f'{Num_CH_DIC}')
            for index_mwx in range(0,len(Pages_Chapter)):
                Download_Pages(os.getcwd(),listToStringWithoutBrackets(Pages_Chapter[index_mwx]),index_mwx)#Did Get The Page Link
                time.sleep(0.2)
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
    response = requests.get(url)
    file = open(f'{Path}\manga\{Website}\{Chapter_Page}\{Num_CH_DIC}\{Number_Page_Paste}.png', "wb")
    file.write(response.content)
    file.close()


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
    

if __name__=='__main__':
    logging.basicConfig(filename="logsManga.log", level=logging.INFO)
    find_mangas_link()