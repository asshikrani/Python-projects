import qrcode as qr
# from PIL import image

img = qr.make("paste link here:")
img.save("qwerty123.png")

# qrc = qr.QRCode(version=1,
#                 error_correction=qr.constant.ERROR_CORRECT_H,
#                 box_size=10,border=4,)

# qrc.add_data("https://youtu.be/TH9NCT-q1Fs?si=aDK-HGSH4DpI3SqM")

# qrc.make(fit=True)

# img = qrc.make_image(fill_color='brown', back_color='cyan')

# img.save("video.png  ")