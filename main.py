import time
import datetime
import pygame

def getdate():
    return datetime.datetime.now()

def reminder(mp3, stop_word, file):
    pygame.init()
    pygame.display.set_mode((100,100))
    pygame.mixer.music.load(mp3)
    pygame.mixer.music.play(0)
    while (True):
        if (input("Enter done if over: ")== stop_word):
            pygame.mixer.music.stop()
            with open(file,'a') as f:
                f.write("\n"+ str(getdate())+ " : "+ stop_word)
                print("Data Recorded successfully")
            break
        else:
            clock = pygame.time.Clock()
            clock.tick(10)
            while pygame.mixer.music.get_busy():
                pygame.event.poll()
                clock.tick(10)

def Time_limit(currenttime):
    if currenttime > '09:00:00' and currenttime < '23:00:01':
        return True
    else:
        print("\t\t\t\tOut of office time")
        return False

print("\t\t\t\tWelcome to Healthy Programmer System ")
print("\t\t\t\tI will keep your eyes and your body healthy")

water_level = 18

water_reminder = 1200 #20 min
eyes_reminder = 1800 #30 min
physical_reminder = 2700 #45 min

currenttime = time.strftime('%H:%M:%S')
previous_water_time = time.time()
previous_eyeexercise_time = time.time()
previous_physicalexercise_time = time.time()

while(Time_limit(currenttime)):
    if water_level > 0:
        if (time.time() - previous_water_time) > water_reminder:  # water after every 20 minutes
            print("Time to drink water")
            while True :
                reminder('water.mp3', 'done', 'water.txt')
                previous_water_time = time.time()
                water_level -= 1
                break
        if time.time() - previous_eyeexercise_time > eyes_reminder :
             print("Time to do eye exercise")
             while True :
                 reminder('eyes.mp3', 'done', 'eyes.txt')
                 previous_eyeexercise_time = time.time()
                 break
        if time.time() - previous_physicalexercise_time > physical_reminder :
             print("Time to do Physical exercise")
             while True :
                 reminder('physical.mp3', 'done', 'physical.txt')
                 previous_physicalexercise_time = time.time()
                 break
print("\t\t\t\tThank You for using me.")