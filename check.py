def check(text,name,password):
    f=open(r'D:\python\minor1\database.txt',"r")
    f1=f.readlines()
    for i in f1:
        if(i==(text+name+password) or i==(text+name+password+'\n')):
            f.close()
            return True

        
        
    f.close()
    return False
