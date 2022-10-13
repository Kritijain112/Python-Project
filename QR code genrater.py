# qrcode -pip install qrcode
# image- pip install image 
!pip install qrcode
!pip install image
qr=qrcode.QRCode(
    version=15, # 15 mean the version of qrcode high the number bigger the code image and compitatic picture 
    box_size=10, # size of box where qr code display 
    Border =5 #it is white part of image ( boarder in all 4 side with white color)
)

 data="https://github.com/Kritijain112" # as i have given the path of my github site like as way u can give any thing 

qr.add_data(data)
qr.make(fit=true)
img=qr.make_image(fill="black",back_color="white")
img.save("test.png")
