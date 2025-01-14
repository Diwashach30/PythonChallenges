##Create a QR code that stores URLs. https://technologychannel.org/

import qrcode

qr = qrcode.make("https://technologychannel.org/")

qr.save("technology_channel_qr.png")

qr.show()
