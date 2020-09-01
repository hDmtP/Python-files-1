# Importing Image and ImageGrab module from PIL package 
from PIL import Image, ImageGrab 
	
# creating an image object 
# im1 = Image.open(r"C:\Users\user\OneDrive\Pictures\Images\mc5.jpg") 
	
# using the grab method 
im1 = ImageGrab.grab(bbox =(100, 20, 320, 400)) 
	
im1.show() 

