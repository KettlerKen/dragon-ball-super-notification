import bs4
import requests
import smtplib
from email.message import EmailMessage
from apscheduler.schedulers.blocking import BlockingScheduler

def check_site():
    r = requests.get("https://www.thewatchcartoononline.tv/anime/dragon-ball-super")
    soup = bs4.BeautifulSoup(r.text, features="html.parser")

    dbs_list = soup.find_all(attrs={"class": "cat-eps"})
    curr_num_eps = dbs_list.__len__()

    file = open("num_episodes.txt", "r")
    prev_num_eps = int(file.readline())
    file.close()

    if curr_num_eps > prev_num_eps:
        file = open("num_episodes.txt", "w")
        file.write(str(curr_num_eps))
        file.close()
        server.send_message(msg=msg)
        print("New Episode!")
    else:
        print("No New Episode...")




msg = EmailMessage()

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login("shitgarbageemail", "508Eastlowave?")
msg['From'] = 'shitgarbageemail@gmail.com'
msg['To'] = 'gtdubuque@gmail.com'
msg['Subject'] = 'New Episode of Dragon Ball Super!'

schedular = BlockingScheduler()
schedular.add_job(check_site, 'interval', hours=1)
schedular.start()
