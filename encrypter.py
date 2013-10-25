#Python Encrypter
#Put something that you want to encrypt and Save it in a file.
#or directly enter here, It will encrypt and save it in a diff file.
#open the same program enter path, run program and it will decrypt it and
#and will save in a file in same directory.
#Encrypted files will be saved as .pmr
#decrypted files will be saved ass .txt
# Won't work if there is a new line in the file. Still working on it.
#creates a folder "encrypt" from where the script is running.
#saves and reads all files from the same directory.
#so make sure that you'll save all files in the same directory.
import random as rdm
import os
import sys
def file_open(filename,ftype):
    filename=filename+ftype
    global file1
    if(find(lis,filename)):
        file1=file(filename,"r+") #Get doc name , and open it
    else :
        file1=file(filename,"w+") # create doc ,and open it    
def encrypt(text): #encrypt function
    num=rdm.randrange(2,5,1) #get a random number from 1 to 5
    encrypted = list()
    encrypted.append(num)
    for word in text: # encrypting
        length=len(word)
        for i in range(0,length,1):
            getnu1=ord(word[i])
            char=chr(getnu1+num)
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
                decrypted.append(char)
        count+=1
    decrypted1=''.join(str(e) for e in decrypted)
    return decrypted1

def find(flis,text): # find function for checking file existence
    for word in flis:
        if(word==text):
            return 1
    return 0
lis= os.listdir(".") # get list of file and folders
if not(find(lis,"encrypt")): # check whether encrypt folder exists
    os.mkdir("encrypt",777)
    os.chdir("encrypt")
else :
    os.chdir("encrypt")
print os.getcwd()
lis= os.listdir(".")
for files in lis:
    print files
filename=raw_input("Enter file name\n")
option = input("Enter 1 to encrypt \n 2 to decrypt\n 3 to enter data and encrypt\n Your Option :")
if(option ==1):#encrypt and save to file
    file_open(filename,".txt")
    filename=filename+".pmr"
    file2=open("e_"+filename,"w+")
    for line in file1:
        file2.write(encrypt(line))
    file2.close()
    file2=open("e_"+filename,"r")
    print "This is the content of e_"+filename
    for line in file2:
        print (line)
    file2.close()
    file1.close()
if(option ==2): # decrypt and save to file
    file_open(filename,".pmr")
    filename=filename+".txt"
    file2=open("d_"+filename,"w+")
    file2.write(decrypt(file1.read()))
    file2.close()
    file2=open("d_"+filename,"r")
    print "This is the content of d_"+filename
    for line in file2:
        print (line)
    file2.close()
    file1.close()
if(option ==3): # get input and sace to file
    print "Enter your message..\n"
    file_open(filename,".pmr")
    file2=raw_input()
    file1.write(encrypt(file2))
    file1.close()
    file1=open(filename+".pmr","r")
    print "This is the content of "+filename
    for line in file1:
        print (line)
    file1.close()
