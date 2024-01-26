#import the function

from utils.voice_recognition import listen_and_recognize
from web_automation import perform_web_actions

def main():
    while True:
        try:
            #Listen from the commands
            command = listen_and_recognize()

            #Perform web actions based on the voice command
            perform_web_actions(command)

        except KeyboardInterrupt:
            print("Voice Assistance terminated.")
            break

if __name__ == "__main__":
    main()
