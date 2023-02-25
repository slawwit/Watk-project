from django.core.mail import send_mail


def send_my_email(dostawca, user_login, user_email, station):
    tytul_email = f'Dostawa {station} - {dostawca}'
    message = """
                            Witam!!

                            Dodano nową dostawę z %s na stacji paliw %s.
                            Wejdź i sprawdź https://slawekwitek.smallhost.pl/
                            Miłego dnia :)
                            Dostawę dodał/a użytkownik - %s .
                            """ % (dostawca, station, user_login)
    responder_email = 'dostawy_watkem@slawekwitek.smallhost.pl'
    admin_address = 'slawwit@vp.pl'
    email_two = user_email
    send_mail(tytul_email, message, responder_email, [admin_address, email_two])
