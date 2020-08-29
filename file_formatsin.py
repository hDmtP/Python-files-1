import csv
import json
import xml.etree.ElementTree as ET
import docx2txt
from PyPDF2 import PdfFileReader
# CSV file
'''
with open("file.csv") as f1 :
    content = csv.reader(f1)
    for row in content:
        print(row)
f1.close()
'''

# JSON file
'''
with open("file.json") as f2:
    content = json.load(f2)
    print(content.get("python"))
f2.close()
'''

# XML file
'''
# with open("file.xml") as f3:
content = ET.parse("file.xml")
root = content.getroot()
for child in root:
    print(child.tag, child.text)
'''

# Docx file
'''
# with open("file.docx", "a") as f4:
#     f4.write("Hello there")
content = docx2txt.process("file.docx")
print(content)
#---> will throw error cauze file should be a zip file. More details are available on Google
'''
# PDF file
'''
file = open("file.pdf", "rb")
# file.write("pip install PyPDF2")
content = PdfFileReader(file)
text = content.getPage(0)
text.extractText()
'''