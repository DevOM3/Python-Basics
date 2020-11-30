import pyqrcode

q = pyqrcode.QRCode
link = "https://console.mahadiscom.in/MobileAppWebConsole"
qr = pyqrcode.create(link)
qr.svg('qr.svg')
