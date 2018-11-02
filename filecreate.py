import caeser
import os

def create_file(name):
    file = open(name,"w+")
    print("enter the content of the file "+name)
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    text = '\n'.join(lines)
    file.write(text)  
    file.close()


def encrypt_file(name,enc):
    enc+=".txt"
    file = open(name,"r")
    encfile = open(enc,"w+")
    key=caeser.getKey()
    print("Encrypting file content...")
    while True:
        line = file.readline()
        encline=caeser.getTranslatedMessage("e",line, key)    
        encfile.write(encline)
        if not line:
            break
    file.close()
    os.remove(name)
    encfile.close()
    os.rename(enc,name)
    

name=input("enter the name of the file to be created:")
enc=name+"enc"
name=name+".txt"


create_file(name)
encrypt_file(name,enc)

