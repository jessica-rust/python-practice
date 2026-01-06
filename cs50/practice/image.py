from PIL import Image
from PIL import ImageFilter


""" Using Pillow library to return size and file type"""

# def main():
#     with Image.open("og_wave.jpeg") as img:
#         print(img.size) # returns the size of the image
#         print(img.format) # returns to you the file type



""" Using Pillow library to rotate and blur image and save as new """

# def main():
#     with Image.open("og_wave.jpeg") as img:
#         img = img.rotate(180) # rotates image 180 degrees
#         img = img.filter(ImageFilter.BLUR) # applies blur filter
#         img.save("new_wave.jpeg") # saves the rotated image



"" Using Pillow library to rotate and filter image and save as new """

def main():
    with Image.open("og_wave.jpeg") as img:
        img = img.rotate(180) # rotates image 180 degrees
        img = img.filter(ImageFilter.FIND_EDGES) # applies edges filter
        img.save("new_wave.jpeg") # saves the rotated image

main()
