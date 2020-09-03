import os.path
from os import path
import elementpath
from xml.etree import ElementTree as ET



for i in range(1,3000):
	
    a = str(i)
    if path.exists('vid4frame'+a+'.xml')==True:
        print (a+'.........')
        tree = ET.parse('vid4frame'+a+'.xml')
	
        root = tree.getroot()
	
        for elem in root.iter('folder'):
            elem.text = "train"
    
        for elem in root.iter('path'):
            elem.text = "C:\\tensorflow7\\models\\research\\object_detection\\images\\train\\vid4frame"+a+".jpg"

        for elem in root.iter('filename'):
            elem.text = 'vid4frame'+a+'.jpg'


        tree.write('vid4frame'+a+'.xml')
    else:
        print (a)
        
