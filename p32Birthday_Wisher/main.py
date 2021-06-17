##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
import pandas
import smtplib
import datetime as dt
import random
PATH = "./p32Birthday_Wisher"

my_email = "aryansri009@gmail.com"
my_password = "Prioryofsion09"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user= my_email, password= my_password)

ch = random.randint(1,3)
lettername = "/letter_templates/letter_" + str(ch) + ".txt"
fhand = open(PATH + lettername)
letter = fhand.read()

bd = pandas.read_csv(PATH + "/birthdays.csv")
months = bd.month
days = bd.day
birthdays_dict = {}
for i in range(0, len(months)):
    key = (int(months[i]), int(days[i]))
    bdm = bd[bd.month == months[i]]
    bdd = bdm[bdm.day == days[i]]
    birthdays_dict[key] = bdd

### or dict comprehension like
# birthdays_dict = {(bd["month"], bd["day"]): data_row for (index,data_row) in bd.iterrows()}

currentdt = dt.datetime.now()
currentd = currentdt.day
currentm = currentdt.month
for keys in birthdays_dict:
    if (currentm, currentd) == keys:
        name = birthdays_dict[keys].name.to_string(index = False)
        email = birthdays_dict[keys].email.to_string(index = False)

        l = letter.replace("[NAME]", name)
        connection.sendmail(from_addr = my_email, to_addrs= email, msg = f"Subject:Happy Birthday!\n\n{l}")
    else:
        print("No birthdays today")
        
        
connection.close()
fhand.close()

