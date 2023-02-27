import fdb
from dotenv import load_dotenv
from os import environ
import requests
import webbrowser


load_dotenv()
host = environ.get('HOST_LICZ')
database = environ.get('DATABASE_LICZ')
station_name = environ.get('STATION')
password = environ.get('PASS_LICZ')
url = environ.get('URL')
api_url = f'{url}{station_name}/api/liczniki/'
api_tok = f'{url}{station_name}/api/auth/'
ilosc_licznikow= int(environ.get('ILOSC_LICZNIKOW'))
select_run = int(environ.get('SELECT_RUN'))
qry = """select pos_all.id_dys , pos_all.id_waz+1 as id_waz, pos_pal.symbol, pos_all.total , mat_art.artykul ,pos_all.kiedy from pos_all
inner join pos_pal on pos_all.id_dys=pos_pal.id_dys and pos_all.id_waz=pos_pal.id_waz
inner join mat_art on pos_pal.id_pal = mat_art.id
order by id_dys"""


def create_conection(inquiry):
    with fdb.connect(
            host=host,
            database=database,
            user='sysdba',
            password='masterkey',
            charset='ISO8859_2') as con:
        #con.__exit__()
        cur = con.cursor()
        cur.execute(inquiry)
        print(cur)
        rows = [x for x in cur]
        cols = [x[0] for x in cur.description]

        return rows, cols


def get_total(rows, cols):
    liczniki= []
    tes = "id"
    i = 1
    for row in rows:
        licz = {}
        licz[tes] = i
        i += 1
        for prop, val in zip(cols, row):
            licz[prop] = val
        liczniki.append(licz)
    return liczniki


def get_token():
    response = requests.post(api_tok, data={'username': station_name, 'password': password})
    header = {'Authorization': f'Token {response.json()}'}
    return header


def put_data():
    """ Tylko po wprowadzeniu do bazy tulu rekordów
     ile mają liczniki w bazie hermes """
    print('Zaczynam wgrywać liczniki...')
    header = get_token()
    for s in liczniki:
        url_api = api_url + f'{s["id"]}/'
        todo = s
        response = requests.patch(url_api, json=todo, headers=header)
        response.json()
        response.status_code
        print(response.text)
    print('Skończyłem :) status=', response.status_code)


def first_run(ile):
    """Za pierwszym uruchomieniem aby wprowadzić
    do bazy tyle liczników ile jest na stacji"""
    header = get_token()
    for i in range(ile):
        todo = {
            "ID_DYS": 1,
            "ID_WAZ": 3,
            "SYMBOL": "ON",
            "TOTAL": "245014.26",
            "ARTYKUL": "OLEJ NAPEDOWY",
            "KIEDY": "2022.11.24 21:53:49"}
        response = requests.post(api_url, json=todo, headers=header)
        response.json()
    return print(response.status_code)


try:
    if select_run == 1:
        print(type(select_run))
        first_run(ilosc_licznikow)
        input('Wciśnij ENTER aby przejść dajej!!')

    else:
        liczniki = get_total(*create_conection(qry))
        put_data()
        input('Wciśnij ENTER aby przejść dajej!!')
        webbrowser.open(url)
except fdb.fbcore.DatabaseError as e:
    print("Błąd w połączeniu z bazą", ("Wprowadź poprawną ścieżkę lokalizacji bazy!!\n", e))
