import qrcode

data = "www.google.com"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")

# Save the QR code image to a file
img.save("qrcode_example.png")

# Show the QR code image
img.show()
