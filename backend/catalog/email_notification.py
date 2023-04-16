import os
import smtplib
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()


class MessageError(Exception):
    pass


def send_email(
        courses: str,
        full_name: str,
        total_cost: str,
        receiver_email: str
) -> str:

    sender_email = "bantyc8@gmail.com"
    password = os.getenv("APP_PASS")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    message = (f"\n\n"
               f"Evrika вітає вас: {full_name}, "
               f"дякуємо що обрали нашу освітню программу.\n\n"
               f"Ваше замовлення:\n\n"
               f"Час вашого замовлення: \n{date_time}.\n\n"
               f"Курси які ви обрали для своєї дитини:\n"
               f" {courses}\n"
               f"Загальна вартість: {total_cost} грн.\n\n"
               f"Бажаємо вашій дитині гарної освіти,\n"
               f"Гарного настрою і міцного здоров'я\n\n"
               f"З найкращіми побажаннями від Evrika\n")

    try:
        server.login(sender_email, password)
        server.sendmail(
            sender_email,
            receiver_email,
            f"Subject: Повідомлення від Evrika\n{message}".encode()
        )

        return "Message recipe!"
    except MessageError:
        return f"{MessageError}\nCheck your login or password"
