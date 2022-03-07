import requests
from pyfiglet import Figlet
import folium
from os import sep

def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        data = {
            '[IP]': response.get('query'),
            '[Int Prov]': response.get('isp'),
            '[Organization]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon')
        }

        for k, v in data.items():
            print(f'{k}: {v}' )

        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save('maps'+sep+f"{response.get('query')}_{response.get('city')}.html")
    except requests.exceptions.ConnectionError:
        print('! please check your connection !')


def main():
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('HACK WORLD'))
    ip = input('Enter your ip address ---> ')
    get_info_by_ip(ip=ip)


if __name__ == '__main__':
    main()