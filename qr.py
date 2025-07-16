import qrcode
from PIL import Image #Importing Image file from Pillow library
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=10) #QRCode changes the functionality of qr code such as version
qr.add_data("link") #Enter your link
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="white")
img.save("imgname.png")
