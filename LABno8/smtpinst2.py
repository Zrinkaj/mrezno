import smtplib
import datetime
import smtpd

content = 'Pozdrav, saljem mail preko pythona, valjda. Lp, Zrinka Jankovic' 

mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()
mail.starttls()
mail.login('zrinkajankovich@gmail.com', 'password')

mail.sendmail('zrinkajankovich@gmail.com', 'anteprojic@gmail.com', content)

mail.close()