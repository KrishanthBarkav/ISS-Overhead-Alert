import requests
from datetime import datetime
import time
import smtplib

HOME_LATITUDE = 11.289087
HOME_LONGITUDE = 76.940971
email = ''      # credentials of a gmail account with less security
password = ''


def isNight():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    if int(current_time.split(':')[0]) > 18 or int(current_time.split(':')[0]) < 4:
        return True
    return False


def isISSOverhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    if HOME_LATITUDE + 5 > float(response.json()['iss_position']['latitude']) > HOME_LATITUDE - 5:
        if HOME_LONGITUDE + 5 > float(response.json()['iss_position']['longitude']) > HOME_LONGITUDE - 5:
            return True
    return False


def sendMail():
    connection = smtplib.SMTP('smtp.gmail.com')
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs='barkavk@gmail.com', msg='SUBJECT:Hey Krishanth, look up\n\nThe ISS is above you')
    connection.close()


while True:
    if isNight() and isISSOverhead(): # ISS can be clearly visible clearly only at night
        sendMail()
    time.sleep(60)
