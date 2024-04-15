import urllib
from flask import jsonify
import requests
import os
from os.path import expanduser
from utils.csv_writer import *

class DataFetcher(object):
    """Fetches the data from the generated URL"""

    def __init__(self,RequestGenerator_obj, location):
        self.RequestGenerator_obj=RequestGenerator_obj
        self.location=location
        self.json_data=''

    def getData(self):
        """Fetches JSON data"""

        try:
            self.json_data=self.RequestGenerator_obj.request.json()
        except:
            print('There is a problem in your connection.')

        if self.json_data: #If data is fetched
            try:
                """Currently the following features are only addded:
                    1.Temperature
                    2.Humidity
                    3.Pressure
                    4.Wind Speed
                    5.Visibility
                """
                print('Temperature of %s is %i C'%(self.location,self.json_data['main']['temp']-273.15))
                print('Humidity : {}'.format(self.json_data['main']['humidity']))
                print('Pressure : {}'.format(self.json_data['main']['pressure']))
                print('Wind Speed : {}'.format(self.json_data['wind']['speed']))
                print('Visibility : {}'.format(self.json_data['visibility']))
            except KeyError:
                pass
            finally:
                print('-'*15)

    def exportData(self):
        """Exports fetched data into a CSV file"""

        try:
            self.CSVWriter_obj=CSVWriter() #Create an object of CSVWriter class
            self.CSVWriter_obj.write_data(Location=self.location,Temperature=self.json_data['main']['temp']-273.15,Humidity=self.json_data['main']['humidity'])
            print('Data transferred to CSV, path is -> '+filepath)
        except:
            print('Could not save the data into CSV format.Please try again.')

class WeatherApp(object):
    """Deals with the main flow of the program"""

    def __init__(self):
        self.URLGenerator_obj=None
        self.RequestGenerator_obj=None
        self.DataFetcher_obj=None
        self._key=None
        self.location=None

class WeatherData:
    
    def __init__(self, values) -> None:
        self.Location = values[0]
        


def get_weather_data():
    header = {
        'User-Agent': 'YFF prosjekt',
        'From': 'chrisandrebredesen@gmail.con'  # This is another valid field
    }
    lokasjon = input("Your location: ").lower()
    url = ""
    match lokasjon:
        case "oslo":
            url = "https://api.met.no/weatherapi/nowcast/2.0/complete?lat=59.9333&lon=10.7166"
        case "trondheim":
            url =  ""
    response = requests.get(url=url, headers=header)
    
    return response.json()

#def parce_data(mye_tull):
      