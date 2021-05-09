import smtplib
import datetime
import smtpd

SERVER = 'localhost'
PORT = 1025

FROM = "zrinka.jankovic@test.com"
TO = "zrinka2@test.com"

SUBJECT = "Hello!"

dt = datetime.datetime.now()
TEXT = "Pokusaj 12313123. @ " + str(dt)

message = """\
From: %s
To: %s
Subject: %s
%s
""" % (FROM, ",".join(TO), SUBJECT, TEXT)

server = smtplib.SMTP(SERVER, PORT)
server.sendmail(FROM,TO,message)
server.quit()