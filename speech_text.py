import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Please speak something...")
    recognizer.adjust_for_ambient_noise(source) 
    try:
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        text = recognizer.recognize_google(audio, language="en-US")
        print("You said: ", text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.WaitTimeoutError:
        print("Listening timed out")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

    

    
