import PyPDF2
a = PyPDF2.PdfFileReader('backend.pdf')
print(a.documentInfo)
print(a.getNumPages())
_str = ""
for i in range(1,7):
    _str += a.getPage(i).extractText()

with open("backend.txt", "w", encoding="utf-8") as f:
   f.write(_str)