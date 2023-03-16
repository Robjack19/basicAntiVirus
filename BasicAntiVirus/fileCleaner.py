#!/usr/bin/env python 

def cleanerNpacker():
    #removing unwanted text
    dpath = "" #path of 'Downloads'
    unwanted = ["ECHO is off.","CertUtil: -hashfile command completed successfully.","CertUtil: The system cannot find the file specified.","CertUtil: -hashfile command FAILED"]
    with open(".\dirNhash.txt", "r+") as f:
        dpath = f.readline() 
        d = f.readlines()
        
        f.seek(0)
        for line in d:
            if dpath not in line and unwanted[0] not in line and unwanted[1] not in line and unwanted[2] not in line and unwanted[3] not in line:
                f.write(line)
        f.truncate()
    f.close()

    #storing values
    name = []
    hash = []
    with open(".\dirNhash.txt","r+") as f:
        d = f.readlines()
        f.seek(0)
        for line in d:
            if "SHA256 hash of" in line:
                name.append(line)
            
            else:
                hash.append(line)            
    f.close()

    #preparing dpath
    dpath = dpath.replace('\\','')
    dpath = dpath.replace(':','')
    remove_path = "SHA256 hash of "+dpath

    #removing \n and \\
    name = [i.replace('\n','') for i in name]
    name = [i.replace('\\','') for i in name]
    name = [i.replace(':','') for i in name]
    hash = [i.replace('\n','') for i in hash]

    #remove remove_path from name
    name = [i.lstrip(remove_path) for i in name]

    #merge lists into tuple     
    name_hash = [(name[i], hash[i]) for i in range(len(name))]
    
    return name_hash
