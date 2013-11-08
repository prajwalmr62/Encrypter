#Current version 0.9a

#Python Encrypter
#Put something that you want to encrypt and Save it in a file.
#or directly enter here, It will encrypt and save it in a diff file.
#open the same program enter path, run program and it will decrypt it and
#will save in a file in same directory.
#Encrypted files will be saved as .pmr
#decrypted files will be saved as .txt
#creates a folder "encrypt" from where the script is running.
#saves and reads all files from the same directory.
#so make sure that you'll save all files in the same directory.

#importing def files

import enclib as en

#Get List of all files in encrypt folder
lis = en.list_files()
for line in lis:
    print line
#Get option value
option=8
while(option>7 or not(option)):
    option=en.getoptions()
    if (option>7 or not(option)):
        print "*Enter valid options*"

if(option<5):
    filename=en.getfilename()

#Options defs
    
if(option ==1):#encrypt and save to file
    if (en.find(lis,filename+".txt")):
        password=raw_input("Enter password\n")
        file1=en.file_open(filename,".txt")
        filename=filename+".pmr"
        file2=open("e_"+filename,"w+")
        line=file1.read()
        file2.write(en.encrypt(password)+en.encrypt(line))
        file2.close()
        file2=open("e_"+filename,"r")
        print "This is the content of e_"+filename
        for line in file2:
            print (line)
        file2.close()
        file1.close()
    else :
        print "invalid file name.."
        print "File does  not exists.."
        print "Please check file name.."


if(option ==2): # decrypt and save to file
    if(en.find(lis,filename+".pmr")):
        file1=en.file_open(filename,".pmr")
        filename=filename+".txt"
        file2=open("d_"+filename,"w+")
        password=raw_input("Enter the file password\n")
        text=str(file1.read())
        if(en.passwordcheck(password,text)):
            text=en.remvpas(text,password)
            file2.write(en.decrypt(text))
            file2.close()
            file2=open("d_"+filename,"r")
            print "This is the content of d_"+filename
            for line in file2:
                print (line)
            file2.close()
            file1.close()
        else:
            print "Invalid password"
    else:
        print "Invalid file name.."
        print "File does not exists.."
        print "Please check file name"


if(option ==3): # get input and save to file
    if(en.find(lis,filename+".pmr")):
        print "File name exists"
        count=1
        filename2=filename
        while(en.find(lis,filename2+'.pmr')):
            filename2=filename+'_'+str(count)
            count+=1
        filename=filename2
        print "now your file renamed to "+filename
    file1=open(filename+".pmr","w+")
    print "Enter your message..\n"
    file2=raw_input()
    password=raw_input("Enter the password\n")
    file1.write(en.encrypt(password)+en.encrypt(file2))
    file1.close()
    file1=open(filename+".pmr","r")
    print "This is the content of "+filename+".pmr"
    for line in file1:
        print (line)
    file1.close()

if(option==4):
    if(en.find(lis,filename+".pmr")):
        file1=en.file_open(filename,".pmr")
        password=raw_input("Enter the file password\n")
        text=str(file1.read())
        if(en.passwordcheck(password,text)):
            text=en.remvpas(text,password)
            print "Your decoded message is below"
            print en.decrypt(text)
        else :
            print "Invalid Password!"
    else :
        print "Invalid file name.."
        print "File does not exists"

if(option==5):
    text=raw_input("Enter coded message\n")
    password=raw_input("Enter password\n")
    if(en.passwordcheck(password,text)):
        text=en.remvpas(text,password)
        print "Your decoded message is below"
        print en.decrypt(text)
    else :
        print "invalid Password!"
if(option==6):
    text=raw_input("Enter your message:")
    password=raw_input("Enter password:")
    text=en.encrypt(password)+en.encrypt(text)
    print "your encrypted message is below"
    print text

if (option==7):
    en.print_my_name()

#none=input("press enter to close....") # only for py2exe
