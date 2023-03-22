from requests_html import HTMLSession

#s = HTMLSession()

def weather_query():

    weather_list = []

    try:
        s = HTMLSession()
        query = 'kouvola'
        weather_list.append(query)
        url = f'https://www.google.com/search?q=weather+{query}'

        r = s.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'})

        temp = r.html.find('span#wob_tm', first=True).text
        weather_list.append(temp)
        unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
        weather_list.append(unit)
        humidity = r.html.find('div.UQt4rd', first=True).find('span#wob_hm', first =True).text
        weather_list.append(humidity)
        #weather = {
         #   'query': query,
          #  'temp': temp,
           # 'unit': unit,
            #'humidity': humidity
           
            #}
        #weather_list.append(weather)

        #print(query, "temperature", temp, unit,"relative humidity", humidity)
        #print((weather_list))
        #return query, temp, unit, humidity
        return weather_list
    except Exception as e:
        print('newsscrape failed.')
        print(e)

#print(weather_query())
weather_query()