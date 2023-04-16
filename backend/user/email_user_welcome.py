from django.core.mail import send_mail
from dotenv import load_dotenv
import os

load_dotenv()


def get_message(full_name: str, receiver_email: str, user_password: str) -> None:
    subject = "Вітаємо вас на курсах Евріка"
    message = (f"\n\n"
               f"{full_name}\n"
               f"Дякуємо вам за реєстрацію на нашій всесвітньо відомій "
               f"платформі де ви зможете обрати найкращі курси для ваших дітей\n"
               f"Ви можете увійти у свій профіль"
               f" за допомогою електронної адреси та паролю:\n\n"
               f"Електронна адреса вашого аккаунта: {receiver_email}\n"
               f"Пароль до вашого аккаутна: {user_password}\n\n"
               f"Дякуємо що ви обрали саме наші курси\n"
               f"Бажаємо вашим дітьям найлегшого вдосконалення своїх навичок\n"
               f"Розвитку та досягнення нових висот\n")

    from_email = "bantyc8@gmail.com"
    password = "catpcfvguuttxtsf"
    recipient_list = [receiver_email]

    send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=False,
        auth_user=from_email,
        auth_password=password
    )
