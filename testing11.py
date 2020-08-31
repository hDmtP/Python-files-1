# Importing Image and ImageGrab module from PIL package 
from PIL import Image, ImageGrab 
	
# creating an image object 
# im1 = Image.open(r"C:\Users\user\OneDrive\Pictures\Images\mc5.jpg") 
	
# using the grab method 
im1 = ImageGrab.grab(bbox =(0, 0, 300, 600)) 
	
im1.show() 

