#import
import speech_recognition as sr

#function for recognize and listen

def listen_and_recognize():
    #Create a recognizer object from the SpeechRecognition
    recognizer = sr.Recognizer()

    #Open Microphone
    with sr.Microphone() as source:
        print("Listening for a command....")

        #adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)

        #Capture audio from microphone
        audio = recognizer.listen(source)

    try:
        #Attempt to recognize the voicce
        command = recognizer.recognize_google(audio).lower()
        print(f"Recognized command: (command)")
        return command

    except sr.UnknownValueError:
        #Case when the speech recognition couldn't understand
        print("Could not UnderStand audio. Please try again.")
    except sr.RequestError as e:
        #Handle the case when there is an issue
        print(f"Could not request result from Google Web Speech API; {e}")
