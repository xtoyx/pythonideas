import requests,time,os,pickle
from bs4 import BeautifulSoup
company_names=[]
skills_important=[]
more_infos=[]
subject='web'
first_url='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=#'
first_url_10pages='https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords='+f'{subject}'+'&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords='+f'{subject}'+'&pDate=I&sequence='
def find_next_page():
    for i in range(0,2):
        for y in range(1,11):
            find_jobs(first_url_10pages + f'{i*10+y}'+'&startPage='+f'{i*10 + 1}')
        print('finished until page : ', first_url_10pages + f'{i*10+y}'+'&startPage='+f'{i*10 + 1}')
        time.sleep(30)

            

def find_jobs(first_url1):   
    html_text= requests.get(first_url1)
    soup =BeautifulSoup(html_text.text , 'lxml')
    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for job in jobs:
        published_date = job.find('span',class_='sim-posted').span.text
        if 'few' in published_date:
            company_name=job.find('h3',class_='joblist-comp-name').text.strip()
            company_names.append(company_name)
            skills=job.find('span',class_='srp-skills').text.strip()
            skills_important.append(skills)
            more_info=job.header.h2.a['href']
            more_infos.append(more_info)
                    
def make_adir():
    dir = os.path.join(f'{os.getcwd()}','/pages-jobpost',f'pages-jobpost-{subject}')
    if not os.path.exists(dir):
        os.mkdir(dir)

def write_to_file():
    make_adir()
    for index in range(0,int(len(skills_important)/10)):
        with open(f'pages-jobpost/pages-jobpost-{subject}/pickledump-untilpage{(index+1)*1}.txt', "w")as r:
            r.write('')
            r.close
      
    for howmanytimes in range(0,int(len(skills_important)/10)):
        for index in range(howmanytimes*10,int(len(skills_important)/10 )+howmanytimes*10):
            for unfamilar_skill in unfamilar_skills:#not alot
                if index < len(skills_important):
                    if unfamilar_skill not in skills_important[index].lower():
                        data={
                        'Number :': index,
                        "\n Company Name:":company_names[index],
                        "\n Skills:":skills_important[index] ,
                        "\n more_info": more_infos[index],
                        }

                            #dump
                        with open(f'pages-jobpost/pages-jobpost-{subject}/pickledump-untilpage{(howmanytimes+1)*1}.txt', "ab") as fp:
                            pickle.dump(data, fp)
            fp.close()
                

    



def loadData():
    dbs=[]
    # for reading also binary mode is important  
    with (open("jobs/pickledump.txt", "rb")) as openfile:  
        while True:
            try:
                dbs.append(pickle.load(openfile))
            except EOFError:
                break
    for db_l in dbs:
        for key in db_l:
            print(f'{key} {db_l[key]}')
        print('\n')
    
def listToStringWithoutBrackets(list1):
    list1=str(list1).replace('[','').replace(']','')
    list1=str(list1).replace("'","")
    return list1
if __name__ == '__main__':
    print('deafutil is python will you like to change it ')
    subject=input('>')
    if len(subject) == 0:
        subject='python'
    else:
        subject=str(subject.lower())
    
    print('Put a skill you dont want. \n-If You dont want multipe skills put space bettwen')
    unfamilar_skills = list(map(str, input(">").split()))
    print('Filerting out : ',listToStringWithoutBrackets(unfamilar_skills))
    while True:
        find_next_page()
        write_to_file()
        # loadData()
        time_wait=10
        print('Waiting 10 Mins...')
        time.sleep(time_wait * 60)