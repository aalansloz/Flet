import time
from playsound import playsound

class Tiempo(object):
    hours=0
    minutes=0
    seconds=0
    def __init__(self,hours,minutes,seconds):
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds


def make_time():
    hours=int(input("¿Cuantas horas necesitas? "))
    minutes = int(input("¿Cuantos minutos necesitas? "))
    seconds= int(input("¿Cuantos segundos necesitas? "))
    return Tiempo(hours,minutes,seconds)

def iniciar_pomodoro():
    timer=Tiempo(0,25,0)
    while timer.minutes != 0:
        timer.minutes -= 1
        timer.seconds = 60
        for i in range(0,60):
            print("Minutos : " + str(timer.minutes) + " Segundos: " + str(timer.seconds))
            time.sleep(1)
            timer.seconds -= 1
    playsound('timesup.mp3')
