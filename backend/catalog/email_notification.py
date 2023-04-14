import os
import smtplib
from dotenv import load_dotenv

load_dotenv()


class MessageError(Exception):
    pass


def send_email(message: str, receiver_email: str) -> str:
    sender_email = "bantyc8@gmail.com"
    password = os.getenv("APP_PASS")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, f"Subject: Welcome to Evrika\n{message}")

        return "Message recipe!"
    except MessageError:
        return f"{MessageError}\nCheck your login or password"


# def main():
#     message = "Thanks for your registration in our school"
#     receiver_email = "yevhenii.nevmyvako@gmail.com"
#     print(send_email(message=message, receiver_email=receiver_email))
#
#
# if __name__ == "__main__":
#     main()
