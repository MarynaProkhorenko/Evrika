import os
import smtplib
from dotenv import load_dotenv

load_dotenv()


class MessageError(Exception):
    pass


def send_email(full_name: str, receiver_email: str, user_password: str) -> str:
    sender_email = "bantyc8@gmail.com"
    password = os.getenv("APP_PASS")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    message = (f"\n\n"
               f"{full_name}\n"
               f"Дякуємо вам за реєстрацію на нашій всесвітньо відомій "
               f"платформі де ви зможете обрати найкращі курси для ваших дітей\n"
               f"Ви можете увійти у свій профіль"
               f" за допомогою електронної адреси та паролю:\n\n"
               f"Електронна адреса вашого аккаунта: {receiver_email}\n"
               f"Пароль до вашого аккауна: {user_password}\n\n"
               f"Дякуємо що ви обрали саме наші курси\n"
               f"Бажаємо вашим дітьям найлегшого вдосконалення своїх навичок\n"
               f"Розвитку та досягнення нових висот\n")

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
