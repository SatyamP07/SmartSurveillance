import os.path
from os import path
import elementpath
from xml.etree import ElementTree as ET



for i in range(0,300):
	
    a = str(i)
    if path.exists('IMG_20200315_20500'+a+'.xml')==True:
        print (a+'.........')
        tree = ET.parse('IMG_20200315_20500'+a+'.xml')
	
        root = tree.getroot()
	
        for elem in root.iter('folder'):
            elem.text = "test"
    
        for elem in root.iter('path'):
            elem.text = "C:\\tensorflow7\\models\\research\\object_detection\\images\\test\\IMG_20200315_20500"+a+".jpg"

        for elem in root.iter('filename'):
            elem.text = 'IMG_20200315_20500'+a+'.jpg'


        tree.write('IMG_20200315_20500'+a+'.xml')
    else:
        print (a)
        
