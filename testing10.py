from PIL import Image, ImageGrab   # pip install pillow
# from numpy import asarray
image = ImageGrab.grab().convert('L')  
_image = ImageGrab.grab().convert('1')  
# print(asarray(image))
image.show()
_image.show()