import qrcode

data = input("enter text or link for QR code:")

qr=qrcode.make(data)

print("Qr code generated successfully")