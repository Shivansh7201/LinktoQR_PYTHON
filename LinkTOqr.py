import qrcode as qr #acessing the library

# NOTE: you need to install the library first by typing "pip install qrcode" in the terminal.

img= qr.make("https://beacons.ai/shivansh7201") #making the qr code for the link
img.save("Codekarr_qr_code.png") #saving the qr code as png file

# NOTE: you can also save the qr code as svg file by typing "img.save("Codekarr_qr_code.svg")" in the terminal.

# YOU will get the QR_code image in the same folder where you have saved this file.