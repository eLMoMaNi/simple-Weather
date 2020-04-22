from weather import Weather
from combine import Combine
from flask import Flask
from flask import send_file
myApp=Flask(__name__)

@myApp.route("/")
def welcome():
    return send_file("gg.html",mimetype="html")

@myApp.route("/<gove>")
def imageGet(gove):
    print(gove)
    token="5H1CKkBf9eGbAiuLrygVg4XCZ4O0BRYx"
    weather=Weather(token,gove)

    bg="./assets/img/bg.png"
    weatherImage=Combine(bg,weather)

    weatherImage.save(f"./outputs/{gove}.png")
    return send_file (f"./outputs/{gove}.png",mimetype="image/png")


myApp.run()
