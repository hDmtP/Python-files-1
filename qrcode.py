import pyqrcode
import png

from pyqrcode import QRCode
print("Please paste your link")
QRstr = input("")
url = pyqrcode.create(QRstr)
url.png(r"C:\Users\user\Pictures\Screenshots\qr2.png", scale=8)
print("Your QR Code has been successfully created")