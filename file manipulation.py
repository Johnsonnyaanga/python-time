import urllib
def read_text():
    quote=open("C:\hello\detect.txt")
    statement=quote.read()
    print(statement)
    quote.close()
    read_web()
print(read_text())
def read_web():
    connection=urllib.urlopen("https://thenextweb.com/google/2011/08/17/google-inadvertently-creates-a-profanity-api/")    
    output=connection.read()
    print(output)
    connection.close()

import os
def rename_file():
    file_list=os.listdir(r"C:\Users\Johnson\Desktop\setups")
    saved_path=os.getcwd
    print(file_list)
    print(rename_file())
    os.chdir(r"C:\Users\Johnson\Desktop\setups")
    for file_name in file_list:
             os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(saved_path)
    print(file_list)

print(rename_file())
