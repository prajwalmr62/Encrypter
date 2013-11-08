# Definition library
# includes all encrypt, decrypt, password adding and removing
#functions

#Functions List
#1.File_open - returns: file handler
#2.Remvpas - returns: password removed string
#3.encrypt - returns: encrypted string
#4.Decrypt - returns: decrypted string
#5.find - finds the file name in list of file name returns: boolean
#6.passwordcheck - checks the password is correct or not. returns: boolean
#7.getoptions - Gets option from the user. returns : integer (option)
#8.list_file() - prints current file list and pwd returns :None
#9.print_my_name() - print my details + current version returns :none
#10.getfilename() - gets filename returns: string (filename)

# Current version 0.8a

import os #for file_open() and list_file()
import random as rdm #for decrypt
def file_open(filename,ftype):
    filename=filename+ftype
    lis= os.listdir(".")
    if(find(lis,filename)):
        file1=file(filename,"r+") #Get doc name , and open it
    else :
        file1=file(filename,"w+") # create doc ,and open it
    return file1

def remvpas(text,pwd):
    text2=list()
    for i in range (len(pwd)+1,len(text),1):
        text2.append(text[i])
    text=''.join(str(e) for e in text2)
    return text

def encrypt(text): #encrypt function
    num=rdm.randrange(1,9,1) #get a random number from 1 to 5
    encrypted = list()
    encrypted.append(num)
    for word in text: # encrypting
        length=len(word)
        for i in range(0,length,1):
            getnu1=ord(word[i])
            char=chr(getnu1+num)
            if (word[i]=='\n'):
                    encrypted.append('\n')
                    continue
            encrypted.append(char)
    encrypted1=''.join(str(e) for e in encrypted)
    return encrypted1

def decrypt(text): #decrypting function
    num=int(text[0]) # get first number
    decrypted=list()
    count=0
    for word in text:
        if (count):
            length=len(word)
            for i in range(0,length,1):
                getnu1=ord(word[i])
                char=chr(getnu1-num)
                if (word[i]=='\n'):
                    decrypted.append('\n')
                    continue
                decrypted.append(char)
        count+=1
    decrypted1=''.join(str(e) for e in decrypted)
    return decrypted1

def find(flis,text): # find function for checking file existence
    for word in flis:
        if(word==text):
            return 1
    return 0
def passwordcheck(pwdu,text):
    word=list()
    i=0
    for i in range(0,len(pwdu)+1,1):
        word.append(text[i])
    pwd=''.join(str(e) for e in word)
    if(pwdu==decrypt(pwd)):
        return 1
    else :
        return 0

def getoptions():
    print "Enter 1 to encrypt"
    print "2 to decrypt from file and save to file"
    print "3 to enter message and encrypt"
    print "4 to decrypt (won't be saved to a file)"
    print "5 to enter and decrypt"
    print "6 to enter and encrypt (Won't be saved to a file)"
    print "7 to about me!"
    option = int(input("Your Option :"))
    return option

def list_files():
    #print current dir and check dirs
    #os.chdir("..") #only for py2exe
    lis= os.listdir(".") # get list of file and folders
    if not(find(lis,"encrypt")): # check whether encrypt folder exists
        os.mkdir("encrypt",777)
        os.chdir("encrypt")
    else :
        os.chdir("encrypt")
    print os.getcwd()
    lis= os.listdir(".")
    return lis
def getfilename():
    #get file name 
    filename=raw_input("Enter file name\n")
    return filename

def print_my_name():
    print "****************************"
    print "* Nagendra Prajwal M       *"
    print "* Mechanical Engineering!  *"
    print "* 5th semester,VCET puttur *"
    print "* USN : 4VP11ME070         *"
    print "****************************"
    print "current version : 0.9alpha"
