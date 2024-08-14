import win32com.client as wincl
import speech_recognition as sr
import webbrowser
import os
import datetime
import requests
import google.generativeai as genai
from config import WEATHER_API_KEY
from config import NEWS_API_KEY
from config import gemini_api_key

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
# wipas68713@maxturns.com 1-9
NEWS_BASE_URL = 'https://newsapi.org/v2/top-headlines'


def say(text):
    speaker = wincl.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 0.6
        audio = r.listen(source)
    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return "Sorry, I did not understand that."
    except sr.RequestError:
        print("Could not request results; check your network connection.")
        return ""
    return query


def ai(prompt):
    genai.configure(api_key=gemini_api_key)

    title = f"gemini response from prompt: {prompt} \n >>>>>>>>>>>>>>>>>>>>>>>\n\n"
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(
        history=[]
    )

    response = chat_session.send_message(prompt)

    print(response.text)
    title += response.text
    if not os.path.exists("gemini"):
        os.mkdir("gemini")

    with open(f"gemini/{''.join(prompt.split('intelligence')[1:])}.txt", "w") as f:
        f.write(title)


def get_news(category):
    url = f"{NEWS_BASE_URL}?category={category}&apiKey={NEWS_API_KEY}&language=en"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])
        if articles:
            return "\n".join(
                [f"Title: {a['title']}\nDescription: {a.get('description', 'No description')}" for a in articles[:5]])
        return "No news articles found."
    return "Error fetching news."


def get_weather(city_name):
    url = f"{BASE_URL}?q={city_name}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        temperature = main['temp']
        humidity = main['humidity']
        description = weather['description']
        weather_info = (f"City: {city_name}\n"
                        f"Temperature: {temperature}°C\n"
                        f"Humidity: {humidity}%\n"
                        f"Weather Description: {description.capitalize()}")
        return weather_info
    else:
        return "Error fetching weather data. Please check the city name or API key."


applications = {
    "vs code": "C:/Program Files/Microsoft VS Code/Code.exe",
    "chrome": "C:/Program Files/Google/Chrome/Application/chrome.exe",
    "brave": "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe",
    "notepad": "C:/Windows/System32/notepad.exe",
    "calculator": "C:/Windows/System32/calc.exe",
    "edge": "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
}

sites = [
            ["Google", "https://www.google.com"],
            ["YouTube", "https://www.youtube.com"],
            ["Facebook", "https://www.facebook.com"],
            ["Instagram", "https://www.instagram.com"],
            ["WhatsApp", "https://www.whatsapp.com"],
            ["Amazon India", "https://www.amazon.in"],
            ["Cricbuzz", "https://www.cricbuzz.com"],
            ["Wikipedia", "https://www.wikipedia.org"],
            ["Flipkart", "https://www.flipkart.com"],
            ["Times of India", "https://www.timesofindia.com"],
            ["Quora", "https://www.quora.com"],
            ["Twitter", "https://www.twitter.com"],
            ["LinkedIn", "https://www.linkedin.com"],
            ["NDTV", "https://www.ndtv.com"],
            ["Hindustan Times", "https://www.hindustantimes.com"],
            ["Live Hindustan", "https://www.livehindustan.com"],
            ["Indian Express", "https://www.indianexpress.com"],
            ["MoneyControl", "https://www.moneycontrol.com"],
            ["ESPN CricInfo", "https://www.espncricinfo.com"],
            ["Hotstar", "https://www.hotstar.com"],
            ["News18", "https://www.news18.com"],
            ["JioCinema", "https://www.jiocinema.com"],
            ["YouTube Music", "https://music.youtube.com"],
            ["ChatGPT", "https://www.chatgpt.com"],
            ["Stack Overflow", "https://stackoverflow.com"],
            ["GitHub", "https://github.com"],
        ]


if __name__ == '__main__':
    say("jarvis this side, sir")

    while True:
        query = takeCommand()
        say(query)

        for site in sites:
            if f"open {site[0]} site".lower() in query.lower():
                say(f"Opening {site[0]} sir....")
                webbrowser.open(site[1])
        # todo: add more musics
        music = [
            ["comethru", r"C:\Users\HP\Music\comethru.mp3"],
            ["eenie meenie", r"C:\Users\HP\Music\Eenie Meenie.mp3"],
            ["love me", r"C:\Users\HP\Music\Love Me.mp3"],
            ["perfect by one direction", r"C:\Users\HP\Music\Perfect by One Direction.mp3"],
            ["senorita", r"C:\Users\HP\Music\Senorita.mp3"],
            ["snap", r"C:\Users\HP\Music\SNAP.mp3"],
            ["titanium", r"C:\Users\HP\Music\titanium.mp3"]
        ]

        for song in music:
            if f"play {song[0]}".lower() in query.lower():
                say(f"Playing {song[0]}")
                os.startfile(song[1])

        if "time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"sir the time is {strfTime}")

        for app_name, app_path in applications.items():
            if f"open {app_name}".lower() in query.lower():
                os.startfile(app_path)
                say(f"Opening {app_name}")

        if "news" in query.lower():
            say('''What type of news are you interested in? (e.g., business, entertainment, general, health,
             science, sports, technology)''')
            category_query = takeCommand().lower()
            valid_categories = ["business", "entertainment", "general", "health", "science", "sports", "technology"]

            if category_query in valid_categories:
                news_info = get_news(category_query)
                say(f"Here is the latest news in {category_query}: {news_info}")
                print(news_info)
            else:
                say('''Invalid category. Please choose from business, entertainment, general, health,
                 science, sports, technology.''')

        if "weather in" in query.lower():
            # Extract the city name from the query
            city = query.lower().split("weather in")[-1].strip()
            weather_info = get_weather(city)
            print(weather_info)
            say(weather_info)

        if "using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        if "exit" in query.lower() or "stop" in query.lower():
            say("have a good day sir")
            break
