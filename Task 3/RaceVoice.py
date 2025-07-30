from Verstappen import Verstappen
from Mostafa import Mostafa
from groq import Groq
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import os
from time import time
import GroqAPI

class RaceVoice:
    def __init__(self):
        self.max = Verstappen()
        self.mostafa = Mostafa()
        self.roundNo = 0
        self.maxTurn = True
        self.lastDamage = 0
        self.client = Groq(api_key=GroqAPI)
        self.sample_rate = 16000
        self.duration = 3
        self.channels = 1
    
    def record_audio(self):
        print("Speak your command now...")
        audio = sd.rec(
            int(self.duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=self.channels,
            dtype='int16'
        )
        sd.wait()
        return audio.flatten()

    def transcribe_with_groq(self, audio_data):
        temp_file = f"temp_cmd_{int(time())}.wav"
        wav.write(temp_file, self.sample_rate, audio_data)
        
        try:
            with open(temp_file, "rb") as audio_file:
                response = self.client.audio.transcriptions.create(
                    file=audio_file,
                    model="whisper-large-v3"
                )
            return response.text
        except Exception as e:
            print(f"Error in transcription: {e}")
            return None
        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)
            
    def get_voice_command(self):
        while True:
            audio = self.record_audio()
            command = self.transcribe_with_groq(audio)
            
            if not command:
                print("Sorry, I didn't catch that. Try again!")
                continue
                
            print(f"Recognized: {command}")
            command = command.lower().strip()
            
            if any(w in command for w in ["attack", "offense"]):
                if "1" in command or "one" in command:
                    return 'attack', 1
                elif "2" in command or "two" in command:
                    return 'attack', 2
                elif "3" in command or "three" in command:
                    return 'attack', 3
            elif any(w in command for w in ["defend", "defence"]):
                if "1" in command or "one" in command:
                    return 'defend', 1
                elif "2" in command or "two" in command:
                    return 'defend', 2
            
            print("Please say something like 'attack 2' or 'defend 1'")
    
    def start(self):

        while self.max._tireHealth > 0 and self.mostafa._tireHealth > 0:

            if self.maxTurn:
                print("It's Max's turn.")
                action, move = self.get_voice_command()
                
                if action == 'attack':
                    self.max._tireHealth = self.lastDamage
                    self.lastDamage = self.max.offence(move)
                    self.maxTurn = False
                else:
                    defence = self.max.defence(move)
                    self.max._tireHealth = (1 - defence) * self.lastDamage
                    self.maxTurn = False
            else:
                print("It's Mostafa's turn.")
                action, move = self.get_voice_command()
                
                if action == 'attack':
                    self.mostafa._tireHealth = self.lastDamage
                    self.lastDamage = self.mostafa.offence(move)
                    self.maxTurn = True
                else:
                    defence = self.mostafa.defence(move)
                    self.mostafa._tireHealth = (1 - defence) * self.lastDamage
                    self.maxTurn = True

            print(f"Round {self.roundNo + 1} complete.")
            self.roundNo += 1
            print(f"Max's fuel: {self.max._fuel}, tire health: {self.max._tireHealth}")
            print(f"Mostafa's fuel: {self.mostafa._fuel}, tire health: {self.mostafa._tireHealth}")
        
        if self.max._tireHealth <= 0:
            print("Mostafa wins!")
        elif self.mostafa._tireHealth <= 0:
            print("Max wins!")


myRace = RaceVoice()
myRace.start()    