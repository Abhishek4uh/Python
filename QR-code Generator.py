# Library Which I used in this program is 'qrcode'
# you can install this library using "pip install qrcode"
# and you can read python docs of this lib! "https://pypi.org/project/qrcode/"

import qrcode
qr=qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
data="Hello I am Python Programmer!"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill='black',back_color='white')
img.save('myqr.png')