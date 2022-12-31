import smtplib
import datetime as dt
from random import choice
import pandas

MY_EMAIL = "micaelpython@outlook.com" #gitignore
MY_PASSWORD = "pyth@n123" #gitignore

# Get date 
now = dt.datetime.now()
YEAR = now.year
MONTH = now.month
DAY = now.day
today = (MONTH, DAY)

# Load the letters
letter1 = open('letter_templates/letter_1.txt', 'r').read()
letter2 = open('letter_templates/letter_2.txt', 'r').read()
letter3 = open('letter_templates/letter_3.txt', 'r').read()
letters = [letter1, letter2, letter3]

# Load the birthday data base
data = pandas.read_csv('birthdays.csv')
birthdays_dict = {
    (data_row["month"], data_row["day"]): data_row
    for (index, data_row) in data.iterrows()
    }

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    contents = choice(letters)
    contents = contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("outlook.office365.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
    print("Email sent to " + birthday_person["name"])