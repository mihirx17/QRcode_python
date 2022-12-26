# QRcode_Scanner
import qrcode
import image
import imghdr
import PIL

print("hellow".capitalize())
My_data = input("Enter your data".capitalize())
img = qrcode.make(My_data)
img.save("file_loaction")
