import os
from django.core.mail import send_mail
#from dotenv import load_dotenv
#load_dotenv()


def send_my_email(dostawca, user_login, user_email, user_firstname, user_lastname):
    tytul_email = f'Dostawa {user_lastname} - {dostawca}'
    message = """
                            Witam!!

                            Dodano nową dostawę z %s na stacji paliw %s.
                            Wejdź i sprawdź https://slawekwitek.smallhost.pl/
                            Miłego dnia :)
                            Dostawę dodał/a użytkownik - %s .
                            """ % (dostawca, user_lastname, user_firstname)
    responder_email = os.environ.get('EMAIL_HOST_USER')
    admin_address = os.environ.get('ADMIN_ADDRES')
    email_two = user_email
    send_mail(tytul_email, message, responder_email, [admin_address, email_two])
