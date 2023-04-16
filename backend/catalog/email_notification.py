from datetime import datetime

from django.core.mail import send_mail
from dotenv import load_dotenv
import os

load_dotenv()


def get_message(
        courses: str,
        full_name: str,
        total_cost: str,
        receiver_email: str
) -> None:

    subject = "Вітаємо вас на курсах Евріка"
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
    from_email = os.getenv("EMAIL_HOST_USER")
    recipient_list = [receiver_email]

    send_mail(subject, message, from_email,
              recipient_list, fail_silently=False)
