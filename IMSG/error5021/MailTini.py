import smtplib
fromaddr = 'tienerschoolnut@gmail.com'
toaddrs  = 'tsterenborg@odysseescholen.nl'
msg = 'Er is rook in de kast aanwezig IMSG is actief u krijgt elke 10 minuten een update bericht wilt u dat niet antwoord stuur dit terug Onderwerp = IMSG eerste regel NutBox tweede regel !stop'
username = 'tienerschoolnut@gmail.com'
password = 'J0r@n2006'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
