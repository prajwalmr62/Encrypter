#Python Encrypter
#Put something that you want to encrypt and Save it in a file.
#or directly enter here, It will encrypt and save it in a diff file.
#open the same program enter path, run program and it will decrypt it and
#and will save in a file in same directory.
import random as rdm
import os
def encrypt(text):
    num=rdm.randrange(2,5,1)
    encrypted = list()
    encrypted.append(num)
    encrypted.append("\n")
    for word in text:
        length=len(word)
        for i in range(0,length,1):
            getnu1=ord(word[i])
            char=chr(getnu1+num)
            encrypted.append(char)
    encrypted1=''.join(str(e) for e in encrypted)
    return encrypted1

def decrypt(text):
    num=int(text[0])
    decrypted=list()
    for word in text:
        if not(text[0]==word or word=="\n"):
            length=len(word)
            for i in range(0,length,1):
                getnu1=ord(word[i])
                char=chr(getnu1-num)
                decrypted.append(char)
    decrypted1=''.join(str(e) for e in decrypted)
    return decrypted1

def find(flis,text):
    for word in flis:
        if(word==text):
            return 1
    return 0
line="Encripted"
lis= os.listdir(".")
if not(find(lis,"text")):
    os.mkdir("text",777)
    os.chdir("text")
else :
    os.chdir("text")
print os.getcwd()
lis= os.listdir(".")
for files in lis:
    print files
filename=raw_input("Enter file name")
file1=file(filename,"r") #Get doc name , and open it
option = input("Enter 1 to encrypt \n 2 to decrypt")
if(option ==1):
    file2=open(filename+"_enc.txt","w+")
    for line in file1:
        file2.write(encrypt(line))
    file2.close()
    file2=open(filename+"_enc.txt","r")
    for line in file2:
        print (line)
    file2.close()
    file1.close()
if(option ==2):
    file2=open(filename+"_dec.txt","w+")
    file2.write(decrypt(file1.read()))
    file2.close()
    file2=open(filename+"_dec.txt","r")
    for line in file2:
        print (line)
