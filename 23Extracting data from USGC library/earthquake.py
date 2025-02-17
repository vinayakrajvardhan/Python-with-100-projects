import requests
import pandas
import pprint


def getdata(startdate,enddate):
    url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson'
    param = {
        'format':'geojson',
        'startdate':startdate,
        'enddate':enddate
    }
    response = requests.get(url,params=param)
    data = response.json()
    return data

data = getdata('2024-03-07','2025-02-01')
# print(data)
pprint.pprint(data)


