import pygame
import time
import random

pygame.init()

print("""
      This is a program made for Husky to have our own pet 
      to get started wake up the Husky by typing the following words
      1) Wake up Husky
      2) wups
      3) hello Husky
      To Stop Say
      1) Goodbye
      2
      """)

# Load the sound file
pygame.mixer.music.load("Huskysound.mp3")



while True:
    owner_input = input("User: ").strip().lower()  # Remove leading and trailing whitespaces
    
    def Husky(data):
        if data.lower().strip() in ["quit", "q", "bye", "goodbye"]:
            pygame.mixer.music.load("crying.mp3")
            pygame.mixer.music.play()
            time.sleep(2)
            quit()
        else:
            # Generate a random number between 1 and 5
            num_barks = random.randint(2, 5)
            # Play the "Bhow Bhow" sound the number of times generated
            print("Husky:","Bhow " * num_barks)
            pygame.mixer.music.play()
    Husky(owner_input)
