import smtplib
fromaddr = 'tienerschoolnut@gmail.com'
toaddrs  = 'tsterenborg@odysseescholen.nl'
msg = 'De NutBox is oververhit IMSG in actief de brakes zijn actief(stroom is uit) de Arduino heeft nog 20 minuten batterij Joran en Indy komen zo spoedig mogelijk'
username = 'tienerschoolnut@gmail.com'
password = '***'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
