import os

path = './'

for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file))==True:
    	if file.find('.') == 0:
            newnamelist = file.split('.')
            print newnamelist[0]
            print newnamelist[1]
            if newnamelist[1].find('png') == 0:
         	     newname = newnamelist[0] + '.jpg'
         	     os.rename(os.path.join(path,file),os.path.join(path,newname))
