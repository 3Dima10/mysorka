import requests
from pyfiglet import Figlet
import folium

def get_info_by_ip(ip='127.0.0.1'):
    try:
        requese = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        #print(requese)
        data = {
            '[IP]': requese.get('query'),
            '[Провайдер(Int Prov)]': requese.get('isp'),
            '[Организация(Org)]':requese.get('org'),
            '[Страна(Countre)]':requese.get('country'),
            '[Регион(Region Name)]':requese.get('regionName'),
            '[Город(City)]':requese.get('city'),
            '[Почтовый индекс(ZIP)]':requese.get('zip'),
            '[Широта(Lat)]':requese.get('lat'),
            '[Долгота(Lon)]':requese.get('lon'),
        }
        for k,v in data.items():
            print(f'{k} : {v}' )
        map = folium.Map(location=[requese.get('lat'),requese.get('lon')])
        map.save(f'{requese.get("query")}_{requese.get("city")}.html')

    except requests.exceptions.ConnectionError:
        print('[!] Проверь подключение !')


def main():
    pr=Figlet(font='slant')
    print(pr.renderText('IP INFO'))
    ip = input('Веди IP :')
    get_info_by_ip(ip=ip)
while True:
    if __name__ == '__main__':
        main()

