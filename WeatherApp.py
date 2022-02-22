#!/usr/bin/env python3

__version__: '2.0' # REV Date Feb 22nd, 2022: Added URL link for fail condition.

# NOTE: For this to work you must have the requests python module
# installed. Do this from command line or terminal:
# python -m pip install requests OR python3 -m pip install requests

# Import tkinter resources for making a textbox for the user
from tkinter import *
import webbrowser
from tkinter.constants import COMMAND, DISABLED
import tkinter as tk

# Import requests module and JSON module
import requests, json, time

# Import DateTime module so python knows the time
import datetime
# Define a function to call the current time and date, bind it, and format it
now = datetime.datetime.now()
TitleDate = now.strftime("%Y-%m-%d %H:%M:%S")

def Weather(n):
    # base URL for JSON weather data; we'll add to this as we go
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    # City name: change as needs be for your user
    CITY = n
    # API key; you can get one of these for free from with a quick google search :)
    API_KEY = "af3f11579680280547897fa6eb2352eb"
    # Updating the URL with our city and api
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    # Setting up the HTML request
    response = requests.get(URL)
    #Check that we get a hit and tell python what to display
    if response.status_code == 200:
        # Grab the JSON data
        data = response.json()
        # Grab the main Dictionary block
        main = data['main']
        # Extract the temperature data
        temperature = main['temp']
        # Extract the humidity
        humidity = main['humidity']
        # Extract the pressure
        pressure = main['pressure']
        # And get a little weather summary
        report = data['weather']

        # Use tkinter to define a textbox for our app
        app = tk.Tk()
        # Lets add a title
        app.title(f"Weather Report: {TitleDate}")
        # Set the dimensions of the Textbox 
        content=tk.Text(app, height=10, width=50)
        content.configure(bg='#49A', fg='white')

        # Add JSON data to the textbox in a human readable format
        content.insert(tk.INSERT, """{:-^30}
Temperature (Celcius): {:0.1f}
Humidity: {}
Pressure: {}
Description: {}""".format(CITY, temperature - 273.15, humidity, pressure, report[0]['description']))

        # Make sure no extra data can be written to the textbox
        content.config(state=DISABLED)
        # Publish everything we have just made to a visible textbox for the user
        content.pack()
        # Ensure that it continues to loop and display until they close it manually
        app.mainloop()

    else:
        # Show that the city chosen is wrong and they need to go look it up
        app = tk.Tk()
        # Lets add a title
        app.title(f"Weather Report: {TitleDate}")
        # Set the dimensions of the Textbox 
        content=tk.Text(app, height=10, width=50)
        content.configure(bg='red', fg='white')

        # Add JSON data to the textbox in a human readable format
        content.insert(tk.INSERT, """    
        
    
    
      Error: Wrong city. Check city name on:""")
        def callback(URL):
            webbrowser.open_new_tab(URL)
        link = Label(app, text="www.openweathermap.org",font=('Helveticabold', 15), cursor="hand2")
        content.pack()
        content.config(state=DISABLED)
        link.pack()
        link.bind("<Button-1>", lambda e:
        callback("https://openweathermap.org/"))
        # Ensure that it continues to loop and display until they close it manually
        app.mainloop()

def main():
    root = tk.Tk()
    root.title("ENTER CITY")
    root.geometry("200x100")
    def retrieve_input():
        inputValue = textBox.get("1.0", "end-1c")
        Weather(inputValue)
    textBox = Text(root, height=2, width=15)
    textBox.pack()

    Search = Button(root, height=1, width=10, text="Search", command=lambda: retrieve_input())
    Search.pack()

    tk.mainloop()


if __name__ == "__main__":
    main()
