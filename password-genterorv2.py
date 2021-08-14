from tkinter.constants import COMMAND
import pyperclip
from tkinter import Tk,Label,Entry,Button ,Menu
from tkinter import messagebox
import random
import  os ,array
import win32gui, win32con


my_text=["ifk","third button is w","fourh button is r"]
ix = 0


# declare arrays of the character that we need in out password
# Represented as chars to enable easy string concatenation
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
DIGITS_REAPTED = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  

LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

LOCASE_Repated_CHARACTERS=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
  
  
UPCASE_CHARACTERS_REAPTED = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']


SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
           '*', '(', ')', '<']

SYMBOLS_REAPTED = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
           '*', '(', ')', '<']


LOCASE_Repated=[]
REST_LOW_ORIGNAL=[]
LOCASE_SPREATED=[]
UPCASE_SPREATED=[]
DIGITS_SPREATED=[]
SYMBOLS_SPREATED=[]


Deafutil = ('''
             *********************************
            *      Hello There                *
            *      -1 encrypt password        *
            *      -2 extract password        *
            *      example : 1                *
             *********************************
            : ''')
Deafutil_2 = ('''
             *********************************
            *    Hello There                  *
            *    Will You Like to use         *
            *      -1 grapchic                *
            *      -2 code                    *
            *      example : 1                *
             *********************************
            : ''')
Password_1 = ('''
             *********************************
            *    Pls Type The Password        *
             *********************************
             : ''')
Password_2 = ('''
             *********************************
            *   Pls Enter The Password        *
            *   You Have been Given           *
             *********************************
             : ''')
Password_notgood=('''
                 ************************************
                *  The Password You Should           *
                *  Give Must be bigger than Nothing  *
                 ************************************
                  : ''')

look_at_example=('''
                 ************************   
                * Pls Use What Was Given  *
                * -> Look At Example      *
                 ************************
                ''')

def random_randomir():
    #switch an array random
    
    UPCASE_CHARACTERS_REAPTED=random.sample(UPCASE_CHARACTERS,len(UPCASE_CHARACTERS))
    DIGITS_REAPTED=random.sample(DIGITS,len(DIGITS))
    SYMBOLS_REAPTED=random.sample(SYMBOLS,len(SYMBOLS))
    LOCASE_Repated_CHARACTERS=random.sample(LOCASE_CHARACTERS,len(LOCASE_CHARACTERS))
    return LOCASE_Repated_CHARACTERS
     

def missingwithstuff_post(ALL_MIXED_RANDOM1 , xw = "null" ):
    for i in range(0,len(LOCASE_Repated_CHARACTERS)):
        #for lowcase length
        LOCASE_SPREATED.append(ALL_MIXED_RANDOM1[i])
    for i in range(len(LOCASE_Repated_CHARACTERS),len(UPCASE_CHARACTERS_REAPTED) * 2 + 1):
        #for uppercase length
        UPCASE_SPREATED.append(ALL_MIXED_RANDOM1[i])
            
    for i in range(len(UPCASE_CHARACTERS_REAPTED) * 2 + 1 ,len(UPCASE_CHARACTERS_REAPTED) * 2 + len(DIGITS_REAPTED) + 1 ):
        #for DIGITS length
        DIGITS_SPREATED.append(ALL_MIXED_RANDOM1[i])

    for i in range(len(UPCASE_CHARACTERS_REAPTED) * 2 + len(DIGITS_REAPTED) + 1,len(UPCASE_CHARACTERS_REAPTED) * 2 + len(DIGITS_REAPTED) + len(SYMBOLS_REAPTED) ):
        #for SYMBOLS length
        SYMBOLS_SPREATED.append(ALL_MIXED_RANDOM1[i])
    global Saved
    if xw == "null" :
            xw=str(input(f'{Password_1}'))
            Saved=xw
    if(len(xw) == 0 or len(Saved) == 0): 
            print(f'{Password_notgood}')
            exit
    for i in xw : #spreated the input
        for m in range(0,len(LOCASE_CHARACTERS)): #locasepart
            if(i==LOCASE_CHARACTERS[m]) :
                    LOCASE_Repated.append(ALL_MIXED_RANDOM1[random.randrange(0,len(ALL_MIXED_RANDOM))])
                    LOCASE_Repated.append(LOCASE_SPREATED[m])
        for m in range(0,len(UPCASE_CHARACTERS)): #upperpart
            if(i==UPCASE_CHARACTERS[m]) :
                    LOCASE_Repated.append(ALL_MIXED_RANDOM1[random.randrange(0,len(ALL_MIXED_RANDOM))])
                    LOCASE_Repated.append(UPCASE_SPREATED[m])
        for m in range(0,len(DIGITS)): #digitpart
            if(i==DIGITS[m]) :
                    LOCASE_Repated.append(ALL_MIXED_RANDOM1[random.randrange(0,len(ALL_MIXED_RANDOM))])
                    LOCASE_Repated.append(DIGITS_SPREATED[m])
        for m in range(0,len(SYMBOLS)): #symbol
            if(i==SYMBOLS[m]) :
                    LOCASE_Repated.append(ALL_MIXED_RANDOM1[random.randrange(0,len(ALL_MIXED_RANDOM))])
                    LOCASE_Repated.append(SYMBOLS_SPREATED[m])
    return LOCASE_Repated
                  


def gettingpassword_get(ALL_MIXED_RANDOM1): 
    for i in range(0,len(LOCASE_Repated_CHARACTERS)):
        #for lowcase length
        LOCASE_SPREATED.append(ALL_MIXED_RANDOM1[i])
    for i in range(len(LOCASE_Repated_CHARACTERS),len(UPCASE_CHARACTERS_REAPTED) * 2 + 1):
        #for uppercase length
        UPCASE_SPREATED.append(ALL_MIXED_RANDOM1[i])
            
    for i in range(len(UPCASE_CHARACTERS_REAPTED) * 2 + 1 ,len(UPCASE_CHARACTERS_REAPTED) * 2 + len(DIGITS_REAPTED) + 1 ):
        #for DIGITS length
        DIGITS_SPREATED.append(ALL_MIXED_RANDOM1[i])

    for i in range(len(UPCASE_CHARACTERS_REAPTED) * 2 + len(DIGITS_REAPTED) + 1,len(UPCASE_CHARACTERS_REAPTED) * 2 + len(DIGITS_REAPTED) + len(SYMBOLS_REAPTED) ):
        #for SYMBOLS length
        SYMBOLS_SPREATED.append(ALL_MIXED_RANDOM1[i])
    
    #get password from the list in all_mixed
    xw=str(input(f'{Password_2}'))
    if(len(xw) == 0): 
        print(f'{Password_notgood}')
        exit
    xw=aragnearrayOddandEven(xw)
    #make a funaction arr[i + 1 * m] m+=1
    for i in xw:
        for y in range(0,len(LOCASE_SPREATED)):
            if(i == LOCASE_SPREATED[y]) :
                REST_LOW_ORIGNAL.append(LOCASE_CHARACTERS[y])

        for y in range(0,len(UPCASE_SPREATED)):
            if(i == UPCASE_SPREATED[y]) :
                REST_LOW_ORIGNAL.append(UPCASE_CHARACTERS[y])

        for y in range(0,len(DIGITS_SPREATED)):
            if(i == DIGITS_SPREATED[y]) :
                REST_LOW_ORIGNAL.append(DIGITS[y])

        for y in range(0,len(SYMBOLS_SPREATED)):
            if(i == SYMBOLS_SPREATED[y]) :
                REST_LOW_ORIGNAL.append(SYMBOLS[y])

    return REST_LOW_ORIGNAL

def aragnearrayOddandEven(xw):
    xw1=[]
    m=1
    for i in range(0,int(len(xw)/2)):
        xw1.append(xw[i+m])
        m+=1
    return xw1


def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 
        

def write_or_create(ALL_MIXED_RANDOM1):
    if not os.path.isfile("key2.key"):
        with open("key2.key", "w") as file1:
            # Writing data to a file
            file1.write(listToString(ALL_MIXED_RANDOM1))
            file1.close()  
            # to change file access modes
    if os.path.isfile("key2.key"):
        with open("key2.key", "r+") as file1:
            # Reading from a file
            ALL_MIXED_RANDOM1=file1.read()
    return ALL_MIXED_RANDOM1    


	
def repeatWhatYouDone(var1):
    xwm=str(input(f'''
                 **********************************
                *Do You Want To Restart It [Y/N] : *
                 **********************************
                   : '''))
    xwm=xwm.lower()
    global LOCASE_Repated
    del LOCASE_Repated[:]
    if(xwm == 'y' or xwm == 'yes' or xwm == 'ye'):
        LOCASE_Repated=missingwithstuff_post(ALL_MIXED_RANDOM , Saved)
        print(f'''
                 ******************************
                * Your Public Password :       *
                *{listToString(LOCASE_Repated)}*
                 ******************************
                    ''')
        repeatWhatYouDone(1)
    elif(xwm == 'n' or xwm == 'no'):
        exit
    return 1
    
def repeatWhatYouDone_graphic():
    global LOCASE_Repated
    del LOCASE_Repated[:]
    e1.delete(0,len(e1.get()))
    LOCASE_Repated=missingwithstuff_post_graphic(ALL_MIXED_RANDOM)
    password_end.configure(text=f'{listToString(LOCASE_Repated)}')
    pyperclip.copy(listToString(LOCASE_Repated))

    

    

def missingwithstuff_post_graphic(ALL_MIXED_RANDOM1):
    for i in range(0,len(LOCASE_Repated_CHARACTERS)):
        #for lowcase length
        LOCASE_SPREATED.append(ALL_MIXED_RANDOM1[i])
    for i in range(len(LOCASE_Repated_CHARACTERS),len(UPCASE_CHARACTERS_REAPTED) * 2 + 1):
        #for uppercase length
        UPCASE_SPREATED.append(ALL_MIXED_RANDOM1[i])
            
    for i in range(len(UPCASE_CHARACTERS_REAPTED) * 2 + 1 ,len(UPCASE_CHARACTERS_REAPTED) * 2 + len(DIGITS_REAPTED) + 1 ):
        #for DIGITS length
        DIGITS_SPREATED.append(ALL_MIXED_RANDOM1[i])

    for i in range(len(UPCASE_CHARACTERS_REAPTED) * 2 + len(DIGITS_REAPTED) + 1,len(UPCASE_CHARACTERS_REAPTED) * 2 + len(DIGITS_REAPTED) + len(SYMBOLS_REAPTED) ):
        #for SYMBOLS length
        SYMBOLS_SPREATED.append(ALL_MIXED_RANDOM1[i])
    global Saved    
    Saved=password_text_get
    if(len(password_text_get) == 0 or len(Saved) == 0): 
        e1.configure('The Password You Should \n Give Must be bigger than Nothing')
        exit
    for i in password_text_get : #spreated the input
        for m in range(0,len(LOCASE_CHARACTERS)): #locasepart
            if(i==LOCASE_CHARACTERS[m]) :
                    LOCASE_Repated.append(ALL_MIXED_RANDOM1[random.randrange(0,len(ALL_MIXED_RANDOM))])
                    LOCASE_Repated.append(LOCASE_SPREATED[m])
        for m in range(0,len(UPCASE_CHARACTERS)): #upperpart
            if(i==UPCASE_CHARACTERS[m]) :
                    LOCASE_Repated.append(ALL_MIXED_RANDOM1[random.randrange(0,len(ALL_MIXED_RANDOM))])
                    LOCASE_Repated.append(UPCASE_SPREATED[m])
        for m in range(0,len(DIGITS)): #digitpart
            if(i==DIGITS[m]) :
                    LOCASE_Repated.append(ALL_MIXED_RANDOM1[random.randrange(0,len(ALL_MIXED_RANDOM))])
                    LOCASE_Repated.append(DIGITS_SPREATED[m])
        for m in range(0,len(SYMBOLS)): #symbol
            if(i==SYMBOLS[m]) :
                    LOCASE_Repated.append(ALL_MIXED_RANDOM1[random.randrange(0,len(ALL_MIXED_RANDOM))])
                    LOCASE_Repated.append(SYMBOLS_SPREATED[m])

    return LOCASE_Repated

def retry_now():
    global password_text_get
    global ALL_MIXED_RANDOM
    password_text_get=e1.get()# this get the entry selection
    # e1.delete(0,len(e1.get())) delete all text
    LOCASE_Repated_CHARACTERS=random.sample(LOCASE_CHARACTERS,len(LOCASE_CHARACTERS))
    UPCASE_CHARACTERS_REAPTED=random.sample(UPCASE_CHARACTERS,len(UPCASE_CHARACTERS))
    DIGITS_REAPTED=random.sample(DIGITS,len(DIGITS))
    SYMBOLS_REAPTED=random.sample(SYMBOLS,len(SYMBOLS))

    ALL_MIXED_RANDOM=LOCASE_Repated_CHARACTERS + UPCASE_CHARACTERS_REAPTED + DIGITS_REAPTED + SYMBOLS_REAPTED
    ALL_MIXED_RANDOM=write_or_create(ALL_MIXED_RANDOM)
    LOCASE_Repated=missingwithstuff_post_graphic(ALL_MIXED_RANDOM)
    password_end.configure(text=f'{listToString(LOCASE_Repated)}')
    button_try.configure(command=repeatWhatYouDone_graphic)
    pyperclip.copy(listToString(LOCASE_Repated))


def messagebox_dfdsjfdj():
    messagebox.showinfo("Pass-genartor","""

        Well To Start with :
        you give a password or your name anything is weak then it gentear a passowrd for you
        well this password will be given to you in your clipboard
        for now :
            thinking of adding remeber me
            you have password you forget what it was the accutal old password -dont know if you going use it
        This all enjoy
        """)

def gettingpassword_get_grapcic(ALL_MIXED_RANDOM1,password_text_get1):
    del REST_LOW_ORIGNAL[:]
    del LOCASE_SPREATED[:],UPCASE_SPREATED[:],DIGITS_SPREATED[:],SYMBOLS_SPREATED[:]
    for i in range(0,len(LOCASE_Repated_CHARACTERS)):
        #for lowcase length
        LOCASE_SPREATED.append(ALL_MIXED_RANDOM1[i])
    for i in range(len(LOCASE_Repated_CHARACTERS),len(UPCASE_CHARACTERS_REAPTED) * 2 + 1):
        #for uppercase length
        UPCASE_SPREATED.append(ALL_MIXED_RANDOM1[i])
            
    for i in range(len(UPCASE_CHARACTERS_REAPTED) * 2 + 1 ,len(UPCASE_CHARACTERS_REAPTED) * 2 + len(DIGITS_REAPTED) + 1 ):
        #for DIGITS length
        DIGITS_SPREATED.append(ALL_MIXED_RANDOM1[i])

    for i in range(len(UPCASE_CHARACTERS_REAPTED) * 2 + len(DIGITS_REAPTED) + 1,len(UPCASE_CHARACTERS_REAPTED) * 2 + len(DIGITS_REAPTED) + len(SYMBOLS_REAPTED) ):
        #for SYMBOLS length
        SYMBOLS_SPREATED.append(ALL_MIXED_RANDOM1[i])
    
    if(len(password_text_get1) == 0): 
        e1.configure(text='The Password You Should Give Must be bigger than Nothing')
        exit
    password_text_get1=aragnearrayOddandEven(str(password_text_get1))
    password_text_get1=str(password_text_get1)
    for i in password_text_get1:
        for y in range(0,len(LOCASE_SPREATED)):
                if(i == LOCASE_SPREATED[y]) :
                    REST_LOW_ORIGNAL.append(LOCASE_CHARACTERS[y])

        for y in range(0,len(UPCASE_SPREATED)):
                if(i == UPCASE_SPREATED[y]) :
                    REST_LOW_ORIGNAL.append(UPCASE_CHARACTERS[y])

        for y in range(0,len(DIGITS_SPREATED)):
                if(i == DIGITS_SPREATED[y]) :
                    REST_LOW_ORIGNAL.append(DIGITS[y])

        for y in range(0,len(SYMBOLS_SPREATED)):
                if(i == SYMBOLS_SPREATED[y]) :
                    REST_LOW_ORIGNAL.append(SYMBOLS[y])

    return REST_LOW_ORIGNAL


def discover_password():
    global password_text_get
    global ALL_MIXED_RANDOM
    password_text_get=e1.get()# this get the entry selection
    ALL_MIXED_RANDOM=LOCASE_Repated_CHARACTERS + UPCASE_CHARACTERS_REAPTED + DIGITS_REAPTED + SYMBOLS_REAPTED
    ALL_MIXED_RANDOM=write_or_create(ALL_MIXED_RANDOM)
    REST_LOW_ORIGNAL=gettingpassword_get_grapcic(ALL_MIXED_RANDOM,password_text_get)
    password_end.configure(text=f'{ listToString(REST_LOW_ORIGNAL)}')
    pyperclip.copy(listToString(REST_LOW_ORIGNAL))



if( __name__ == "__main__" ):
    xwm=input(f'{Deafutil_2}')  
    if(xwm == "1"):
        hide = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hide , win32con.SW_HIDE)
        global button_try
        master = Tk()
        master.title("Password-Ah Youu Have Seen Me")
        password=Label(master, text='Password').grid(row=0)
        password_end=Label(master, text='Password-Given')
        menubar = Menu(master)  
        menubar.add_command(label="info!", command=messagebox_dfdsjfdj)
        menubar.add_command(label="exit",command=master.quit)
        button_try=Button(master,text="try",command=retry_now)
        Button(master,text="Discover",command=discover_password).grid(row=2,column=1,sticky='E')
        e1 = Entry(master)
        e1.grid(row=0, column=1)
        button_try.grid(row=2,column=2,sticky='E')
        password_end.grid(row=1,column=1)
        master.config(menu=menubar)
        master.mainloop()
    elif (xwm == "2"):
        xwm=input(f'{Deafutil}')
        if ("1" == xwm):
                    #switch an array random  , Make it Work when u get a file or not 
                    LOCASE_Repated_CHARACTERS=random.sample(LOCASE_CHARACTERS,len(LOCASE_CHARACTERS))
                    UPCASE_CHARACTERS_REAPTED=random.sample(UPCASE_CHARACTERS,len(UPCASE_CHARACTERS))
                    DIGITS_REAPTED=random.sample(DIGITS,len(DIGITS))
                    SYMBOLS_REAPTED=random.sample(SYMBOLS,len(SYMBOLS))

                    ALL_MIXED_RANDOM=LOCASE_Repated_CHARACTERS + UPCASE_CHARACTERS_REAPTED + DIGITS_REAPTED + SYMBOLS_REAPTED
                    ALL_MIXED_RANDOM=write_or_create(ALL_MIXED_RANDOM)
                    LOCASE_Repated=missingwithstuff_post(ALL_MIXED_RANDOM)
                    print(f'''
                             ******************************
                            * Your Public Password :       *
                            *{listToString(LOCASE_Repated)}*
                             ******************************
                                ''')
                    repeatWhatYouDone(1)
                    
        elif('2' == xwm ):
                    ALL_MIXED_RANDOM=LOCASE_Repated_CHARACTERS + UPCASE_CHARACTERS_REAPTED + DIGITS_REAPTED + SYMBOLS_REAPTED
                    ALL_MIXED_RANDOM=write_or_create(ALL_MIXED_RANDOM)
                    REST_LOW_ORIGNAL=gettingpassword_get(ALL_MIXED_RANDOM)

                    print(f'''
                            *******************************
                            * Your Private Password :       *
                            *{listToString(REST_LOW_ORIGNAL)}*
                            ********************************
                            ''')
        else :
                print(f'{look_at_example}')
                exit

