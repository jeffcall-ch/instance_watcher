import yagmail
import urllib.request

external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

receiver = "szivalaszlo@gmail.com"
body = f"Machine external IP is: {external_ip}"
#filename = "document.pdf"

yag = yagmail.SMTP("ezegycoolemailcim@gmail.com")
yag.send(
    to=receiver,
    subject="Instance details",
    contents=body,
    #attachments=filename,
)