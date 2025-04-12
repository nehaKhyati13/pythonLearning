mport qrcode
import image
qr = qrcode.QRCode(
    version = 20, 
    box_size = 5,
    border = 5
)

data = "Hi"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="red",back_color ="green")
img.save("qr.png")
