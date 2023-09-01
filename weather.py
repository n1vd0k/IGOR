import requests
s_city = "Barnaul,RU"
city_id = 0
appid = "2bc87d62c784d1e17b9d897dc7396738"
def weather():
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Barnaul,ru&APPID=2bc87d62c784d1e17b9d897dc7396738",
                     params={'id': city_id, 'units': 'metric', 'lang': 'en', 'APPID': appid})
        data = res.json()
        return "Today in Barnaul:"+ str(data['weather'][0]['description'])+", temp:" + str(data['main']['temp'])+", temp_min:" + str(data['main']['temp_min']) + ", temp_max:" + str(data['main']['temp_max'])
    except Exception as e:
        pass

