import smtplib
import ssl
import os

from dotenv import load_dotenv

load_dotenv('var.env')

# secret dotenv variables
login = os.getenv("USER")
password = os.getenv("PASS")

# variables
email_from = "cyberopa@mein.gmx"
email_to = "cyberopa@gmx.net"
my_name = "Paul"
friend_name = "Viktor"
dvmn_akt = "https://dvmn.org/profession-ref-program/paul-r6/BM3Ra/"

# Source text
text = '''Привет, %friend_name%!

%my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию.
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя.

Как будет проходить ваше обучение на %website%?

→ Попрактикуешься на реальных кейсах.
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей.
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят.

Регистрируйся → %website%
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''

# Postkarte
letter = f'''From: {email_from}
To: {email_to}
Subject: Devman Kurs
Content-Type: text/plain; charset="UTF-8";

'''
letter = letter.encode("UTF-8")

# replaced text
new_text = text.replace("%friend_name%", friend_name).replace("%my_name%", my_name).replace("%website%", dvmn_akt)

# total massege
message = letter + new_text.encode("UTF-8")

# server access, massage sent und quit
server = smtplib.SMTP_SSL('mail.gmx.net', 465)
server.login(login, password)
server.sendmail(email_from, email_to, message)
server.quit()
