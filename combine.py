#Note, Do not inherit  Image class. Image class is not made to be inherited!
#you can just save the new image in self.img
from PIL import Image, ImageDraw, ImageFont
from weather import Weather
class Combine:
    def __init__(self,bg,weather):
        #save backgroud image in the class
        self.img=Image.open(bg)
        #making a drawer object
        self.drawer=ImageDraw.Draw(self.img)
        #save weather OBJECT in the class
        self.weather=weather
        # start comibinging function
        self.__combine()
    def __combine(self):
        #this function should combine bg with weather details
        
        #Gov Title
        fnt=ImageFont.truetype(font="./assets/fonts/ArchitectsDaughter.ttf",size=32)
        self.drawer.text((460,80),self.weather.data["govName"],font=fnt,fill="#ff00dd")
        #Date 
        fnt=ImageFont.truetype(font="./assets/fonts/ArchitectsDaughter.ttf",size=30)
        self.drawer.text((290,505),self.weather.data["date"],font=fnt,fill="#ffffff")
        #Day Temp
        fnt=ImageFont.truetype(font="./assets/fonts/Itim.ttf",size=70)
        self.drawer.text((90,220),self.weather.data["day"]["temp"],font=fnt,fill="#ff0000")
        #Day Icon
        day_icon=Image.open(f"./assets/img/icons/{self.weather.data['day']['icon']}.png")
        self.img.paste(day_icon,(232,185),day_icon)
        #this method source : 
        #https://stackoverflow.com/questions/5324647/how-to-merge-a-transparent-png-image-with-another-image-using-pil
        #########
        #Night Temp
        self.drawer.text((575,220),self.weather.data["night"]["temp"],font=fnt,fill="#0000ff")
        #Night Icon
        night_icon=Image.open(f"./assets/img/icons/{self.weather.data['night']['icon']}.png")
        self.img.paste(night_icon,(700,185),night_icon)
    def save(self,fp):
        self.img.save(fp)
    def show(self):
        self.img.show()
