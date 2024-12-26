import speech_recognition as sr
import pyttsx3
import requests
import datetime

engine = pyttsx3.init()
print("Assistant: Hello! I am your personal assistant. How can I help you today?")
engine.say("Hello! I am your personal assistant. How can I help you today?")
engine.runAndWait()

while True:
    recognizer = sr.Recognizer()
    text = ""

    with sr.Microphone() as source:
        print("Please speak something...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            text = recognizer.recognize_google(audio, language="en-US").lower()
            print("You said: ", text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
            engine.say("Google Speech Recognition could not understand the audio")
            engine.runAndWait()
        except sr.WaitTimeoutError:
            print("Listening timed out")
            engine.say("Listening timed out")
            engine.runAndWait()
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            engine.say("Could not request results from Google Speech Recognition service")
            engine.runAndWait()

    if text.strip():
        if "weather" in text:
            city = "mumbai"
            api_key = "0e7f2c72af6f4052f88792fedd3beb8e"
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather = data["weather"][0]["description"]
                temp = data["main"]["temp"]
                print(f"Assistant: the weather in {city} is {weather} with a temperature of {temp}°C")
                engine.say(f"The weather in {city} is {weather} with a temperature of {temp}°C")
            else:
                engine.say("Sorry, I could not fetch the weather")
                print("Sorry, I could not fetch the weather")

        elif "news" in text:
            api_key_news = "2819fef7ae32433491d1e07b8e9a65dc"
            url_news = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key_news}"
            response = requests.get(url_news)
            if response.status_code == 200:
                articles = response.json().get("articles", [])
                headlines = [article['title'] for article in articles[:5]]
                print("Here are the top 5 news headlines: ")
                for i, headline in enumerate(headlines, 1):
                    print(f"{i}. {headline}")
                engine.say("Here are the top 5 news headlines: " + ", ".join(headlines))

        elif "time" in text:
            time = datetime.datetime.now().strftime("%I:%M %p")
            print(time)
            engine.say(f"The current time is {time}")

        elif "exit" in text or "quit" in text:
            engine.say("Goodbye!")
            engine.runAndWait()
            break

    engine.runAndWait()
