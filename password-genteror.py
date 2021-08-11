import random
import  os ,array

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
            *      -2 extract password :      *
            *      example : use 1            *
             *********************************
            : ''')

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
        xw=str(input('pls enter your password: '))
        Saved=xw
    if(len(xw) == 0 or len(Saved) == 0): 
        print('The Password You Should Give Must be bigger than Nothing')
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
    xw=str(input('pls enter The Public Password : '))
    if(len(xw) == 0): 
        print('The Password You Should Give Must be bigger than Nothing')
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
    xwm=str(input("Do You Want To Restart It [Y/N] : "))
    xwm=xwm.lower()
    global LOCASE_Repated
    del LOCASE_Repated[:]
    if(xwm == 'y' or xwm == 'yes' or xwm == 'ye'):
        LOCASE_Repated=missingwithstuff_post(ALL_MIXED_RANDOM , Saved)
        print("Your Public Password : " , listToString(LOCASE_Repated))
        repeatWhatYouDone(1)
    elif(xwm == 'n' or xwm == 'no'):
        exit

    return 1 
    

    



if( __name__ == "__main__" ):
    
    xwm=input(f'{Deafutil}')
    if ("use 1" == xwm):
        #switch an array random  , Make it Work when u get a file or not 
        LOCASE_Repated_CHARACTERS=random.sample(LOCASE_CHARACTERS,len(LOCASE_CHARACTERS))
        UPCASE_CHARACTERS_REAPTED=random.sample(UPCASE_CHARACTERS,len(UPCASE_CHARACTERS))
        DIGITS_REAPTED=random.sample(DIGITS,len(DIGITS))
        SYMBOLS_REAPTED=random.sample(SYMBOLS,len(SYMBOLS))

        ALL_MIXED_RANDOM=LOCASE_Repated_CHARACTERS + UPCASE_CHARACTERS_REAPTED + DIGITS_REAPTED + SYMBOLS_REAPTED
        ALL_MIXED_RANDOM=write_or_create(ALL_MIXED_RANDOM)
        LOCASE_Repated=missingwithstuff_post(ALL_MIXED_RANDOM)
        print("Your Public Password : " , listToString(LOCASE_Repated))
        repeatWhatYouDone(1)
        
    elif('use 2' == xwm ):
        ALL_MIXED_RANDOM=LOCASE_Repated_CHARACTERS + UPCASE_CHARACTERS_REAPTED + DIGITS_REAPTED + SYMBOLS_REAPTED
        ALL_MIXED_RANDOM=write_or_create(ALL_MIXED_RANDOM)
        REST_LOW_ORIGNAL=gettingpassword_get(ALL_MIXED_RANDOM)

        print("Your Private Password : " , listToString(REST_LOW_ORIGNAL))
    else :
        print('pls Use What Was Given -> Look At Example')
        exit

