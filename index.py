import pyqrcode
from pyqrcode import QRCode
s = "https://github.com/charu08dhingra"
url = pyqrcode.create(s)
url.svg("mygithub.svg", scale=8)
