import smtplib
import datetime as dt
from random import choice
import pandas

quotes = open('day-32-birthday-wisher\quotes.txt', 'r')
quotes_array = quotes.readlines()


my_email = "micaelpython@outlook.com" #gitignore
password = "pyth@n123" #gitignore
now = dt.datetime.now()
day_of_week = now.weekday()

connection = smtplib.SMTP("outlook.office365.com", port=587)
connection.starttls()
connection.login(user=my_email, password=password)

if day_of_week == 6:
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="micaelmuniz6@gmail.com",
        msg=f"Subject:Happy Monday\n\n{quotes_array[randint(0, len(quotes_array))]}"
        )

connection.close()
