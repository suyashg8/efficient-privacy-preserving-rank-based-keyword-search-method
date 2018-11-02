import allocator
import caeser
import extract_and_create
import os
import search

#Login
Auth = None

print("Enter username to proceed")
usname = input("Username: ")
dirname = allocator.crypt(usname)
path = os.getcwd()
dirs = os.listdir(path)

if dirname in dirs:
    print("welcome back")
    Auth = 1
else:
    print("No user records founds. New record created")
    os.mkdir(dirname)
    Auth = 1



def Addfile(dirname, path,name):
    os.rename(path+"/"+name, os.getcwd()+"/"+dirname+"/"+name)
    npath = os.getcwd()+"/"+dirname
    extract_and_create.extract(dirname,npath,name)
    data = []
    f = open(npath+"/"+name,"r")
    for i in f:
        data.append(caeser.getTranslatedMessage('e',i,len(dirname)))
    f.close()
    f = open(npath+"/"+name,"w")
    for i in data:
        f.write(i)
    f.close()

if Auth == 1:
    while Auth == 1:
        print("1. Add a file\n2. Search\n3. Stop")
        option = int(input())
        if option == 3:
            break
        if option == 1:
            path = input("Enter file path: ")
            name = input("Enter file name: ")
            Addfile(dirname,path,name)
        if option == 2:
            search.search(os.getcwd()+"/"+dirname)



