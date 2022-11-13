import smtplib

my_email = "micaelpython@outlook.com" #gitignore
password = "pyth@n123" #gitignore


with smtplib.SMTP("outlook.office365.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="micaelmuniz6@gmail.com",
        msg="Subject:Hello world\n\nOla esta e uma mensagem de teste"
        )