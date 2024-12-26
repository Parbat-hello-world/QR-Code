import qrcode

# Data to be encoded in the QR code
data = "name=Parbat, age=18, grade=Bachelor"

# Create a QRCode instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QRCode
qr.add_data(data)
qr.make(fit=True)

# Generate the image
img = qr.make_image(fill="black", back_color="white")

# Save the QR code image to a file
img.save("qrcode_with_info.png")

# Show the QR code image
img.show()
