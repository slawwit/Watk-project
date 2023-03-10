import os
from django.core.mail import send_mail


def send_my_email(dostawca, user_firstname, name_stacji ):
    tytul_email = f'Dostawa {name_stacji} - {dostawca}'
    message = """
    Witam!!

    Dodano nową dostawę z %s na stacji paliw %s.
    Wejdź i sprawdź https://slawekwitek.smallhost.pl/
    Miłego dnia :)
    Dostawę dodał/a użytkownik - %s .
    """ % (dostawca, name_stacji, user_firstname)
    responder_email = os.environ.get('EMAIL_HOST_USER')
    admin_address = os.environ.get('ADMIN_ADDRES')
    send_mail(tytul_email, message, responder_email, [admin_address, name_stacji.adress_email])


def send_my_email_modified(dostawa_number, user_firstname, name_stacji):
    tytul_email = f'Uwaga zmodyfikowano dostawę numer {dostawa_number} stacja {name_stacji}'
    message = """
    Uwaga!!

    Zmodyfikowano dostawę numer %s na stacji paliw %s .
    Wejdź i sprawdź https://slawekwitek.smallhost.pl/
    Miłego dnia :)
    Dostawę edytował użytkownik - %s .
    """ % (dostawa_number, name_stacji, user_firstname)
    responder_email = os.environ.get('EMAIL_HOST_USER')
    admin_address = os.environ.get('ADMIN_ADDRES')
    send_mail(tytul_email, message, responder_email, [admin_address, name_stacji.adress_email])
