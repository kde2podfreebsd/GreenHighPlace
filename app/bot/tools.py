import requests
import os


from dotenv import load_dotenv


config = load_dotenv()
API_KEY = os.getenv("YandexGeoToken")

def get_address(lat, lon, language):
    try:
        lang = ""
        if language == "RU":
            lang = "ru_RU"
        elif language == "EN":
            lang = "en_US"
        URL = f"https://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}" \
              f"&geocode={lat},{lon}&format=json&sco=latlong&kind=house&results=1&lang={lang}"
        result = requests.get(URL).json()
        print(result)
        # print(result['response'])

        return result['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text']
    except Exception as e:
        return None


# print(get_address(7.879702, 98.372309, language='EN'))


