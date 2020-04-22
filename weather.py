govs_dic = {
    "Ajloun": 221874,
    "Madaba": 224575,
    "Irbid": 224033,
    "Jerash": 224190,
    "Mafraq": 222143,
    "Amman": 221790,
    "Zarqa": 222674,
    "As-salt": 221989,
    "Karak": 222081,
    "At-tfilah": 222569,
    "Maan": 224521,
    "Aqaba": 221898,
    "JUST": 224034
}
import requests
import json
class Weather:
    def __init__(self,token,govName):
        options={
            "apikey":token,
            "metric":True
        }
        self.res=requests.get(f"http://dataservice.accuweather.com/forecasts/v1/daily/1day/{govs_dic[govName]}", params=options)
        #If an error happend, print status code and exit
        if self.res.status_code !=200:
            print("ERROR ON WEATHER")
            print ("STATUS CODE:",self.res.status_code)        
            return
        self.responseObj=json.loads(self.res.text)
        #storing data in better looking dictionary
        self.data={
            "day":{
                "temp":str(self.responseObj["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"]),
                "icon":self.responseObj["DailyForecasts"][0]["Day"]["Icon"]
            },
            "night":{
                "temp":str(self.responseObj["DailyForecasts"][0]["Temperature"]["Minimum"]["Value"]),
                "icon":self.responseObj["DailyForecasts"][0]["Night"]["Icon"]
            },
            "date":self.responseObj["DailyForecasts"][0]["Date"],
            "govName":govName
        }
        json.dump(self.responseObj,open("./outputs/weather.json","w") )
