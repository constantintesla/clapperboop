import winsound
import random
def beep(frequency,duration):
    winsound.Beep(frequency, duration)




i = 1
while i < 19:
    freq = random.randrange(200, 700)
    lent = random.randrange(50, 150)
    print(freq,lent)
    beep(freq,lent)

    i += 1


