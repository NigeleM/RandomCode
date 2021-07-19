


# Tree function


from os import path as ls
from os import listdir as dr
import time
def tree(strs=None):
    if strs == None:
        print("here")
        content = dr(strs)
        files = []
        drs = []
        for objects in content:
            if ls.isfile(objects) == True:
                print('Root...\033[92m..........',objects)
            elif ls.isdir(objects) == True:
                print('Root---\033[96m------------>',objects)
                tree(objects)
        
    else:
        print("here 2")
        contents = dr(strs)
        path, filename = ls.split(strs)
        print("\033[96m<-- {} -->".format(strs))
        #print("\033[96m-- {} -->".format(contents)) 
        for obj in contents:
            if ls.isfile(obj) == True:
                print(obj)
                #print('\033[92m..........',obj)
            elif ls.isdir(obj) == True and obj != filename:
                print('\033[96m',obj)
                tree(ls.realpath(obj))
        #time.sleep(0.3)
        

    
tree()
print('\033[37m')
