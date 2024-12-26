""" 
Before running this code make sure that qrcode module is installed in your system 
if not then run this command in you terminal or command-prompt;
(i)_For windows:
  (pip install qrcode)
(ii)_For macos:
  pip3 install qrcode
(iii)_For linux:
  pip3 install qrcode
"""
import qrcode as qr

img = qr.make("paste link here:")
img.save("qwerty123.png")

