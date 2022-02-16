import requests
from tkinter import *


root = Tk()  # root interface for all the other UI components(the skeleton UI or the Container)
root.title("Metro Weather App")
root.iconbitmap(r"C:\Users\TAHIRUSALIFU\Desktop\MY PYTHON LEARNING\ImageViewer\flock_ico01.ico")
root.geometry("900x400")

root.configure(bg="#f595cf")
appLabel = Label(root, text="M E T R O  W E A T H E R   R E P O R T E R", fg="white", bg="green", font="akrobatbold 30")
appLabel.pack(expand=NO, fill=X)

def weatherShow():
    frame.forget()
    city = city_name.get()  #get city name
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=7114126667063ecc765ffd8c1830d0eb".format(city)
    try:
        res = requests.get(url)
        weather = res.json()
        weather_status = weather['weather'][0]['description']
        temperature = weather['main']['temp']
        humidity = weather['main']['humidity']
        wind_speed = weather['wind']['speed']

        #configure and then pack all weather info details
        frame.pack(padx=10, expand=NO, fill=X)
        cityLabel.configure(text="What does the weather look like at "+city+"?")
        cityLabel.pack(fill=X)
        weatherStatusLabel.configure(text="Weather status : "+weather_status, bg="#aef2ea")
        weatherStatusLabel.pack(fill=X)
        temperatureLabel.configure(text="Temperature : "+ str(temperature) + " Degrees Celcius", bg="#aef2ea")
        temperatureLabel.pack(fill=X)
        humidityLabel.configure(text="Humidity : " + str(humidity), bg="#aef2ea")
        humidityLabel.pack(fill=X)
        windLabel.configure(text="Wind speed : " + str(wind_speed) +" m/s", bg="#aef2ea")
        windLabel.pack(fill=X)

    except ConnectionError:
        weatherFail = "Oops! Sorry! Network problem encountered!"
        weatherStatusLabel.configure(text=weatherFail, fg="red", bg="#aef2ea")
        weatherStatusLabel.pack(fill=X)

    except Exception as e:
        weatherFail = "\nOops! Sorry! Some erro occured!" + str(e)
        weatherStatusLabel.configure(text=weatherFail, fg="red", bg="#aef2ea")
        weatherStatusLabel.pack(fill=X)


city_name_list = ["Kumasi", "Ashaiman", "Accra", "Kintampo", "Tamale", "Sekondi-Takoradi", "Sunyani", "Cape Coast", "Obuasi", "Teshie", "Tema", "Madina", "Koforidua", "Wa", "Techiman", "Ho", "Nungua", "Lashibi", "Dome", "Bawku", "Aflao", "Bolgatanta", "Suhum", "Yendi", "Nsawam", "Konongo", "Tafo", "Elmina", "Wenchi", "Axim", "Aburi", "Bechem", "Saltpond", "Akropong", "Kibi", "Bekwai", "Bechem", "Aboso", "Banda Ahenkro", "Mpraeso"]
city_name = StringVar(root)
city_name.set("Select the City")
cityOption = OptionMenu(root, city_name, *city_name_list)
cityOption.configure(width=len("Select the City"), bg="light blue")
cityOption.pack(padx=150, pady=10)

showWeather = Button(root, text="Display Weather Info", command=weatherShow, width=len("Display Weather Info"), bg="light blue")
showWeather.pack(pady=20)

#show weather info for city
frame = LabelFrame(root, text="Weather Information", relief='raised', padx=20, pady=20)
cityLabel = Label(frame, font="times 12 italic")
weatherStatusLabel = Label(frame, font=("times", 10, "bold"))
temperatureLabel = Label(frame, font=("times", 10, "bold"))
humidityLabel = Label(frame, font=("times", 10, "bold"))
windLabel = Label(frame, font=("times", 10, "bold"))

exitButton = Button(root, text="EXIT", width=20, bg="#f74d5b", fg="white", font="times 15 bold", command=root.destroy)
exitButton.pack(side=BOTTOM, pady=15)

root.mainloop()