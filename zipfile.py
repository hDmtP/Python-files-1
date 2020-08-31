from pyzip import PyZip
pyzip=PyZip()
pyzip['key1']=b"content_bytes"
pyzip['key2']=b"file_bytes"
# pyzip.save(r"C:\Users\user\Documents\OneDrive\python practice folder\file.zip")
# zip_bytes=pyzip.to_bytes()
print(pyzip)