import sys
sys.path.append('/home/pi/Adafruit-Raspberry-Pi-Python-Code/Adafruit_CharLCD')
from Adafruit_CharLCD import Adafruit_CharLCD
lcd=Adafruit_CharLCD()     # instantiate Layar LCD
lcd.clear()
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)    # mengatur penomoran BCM GPIO
# Siapkan pin masukan
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# Siapkan keluaran LED
GPIO.setup(20, GPIO.OUT)
# Fungsi panggilan balik untuk dijalankan saat gerakan terdeteksi
def motionSensor(channel):
   lcd.clear()
   GPIO.output(20, GPIO.LOW)
   if GPIO.input(21):     # Benar = Naik
       global counter
       counter += 1
       lcd.message('Motion Detected\n{0}'.format(counter))
       GPIO.output(20, GPIO.HIGH)
# tambahkan pendengar acara di pin 21
GPIO.add_event_detect(21, GPIO.BOTH, callback=motionSensor, bouncetime=300) 
counter = 0
try:
   while True:
       sleep(1)         #tunggu 1 detik
finally:                   # jalankan saat keluar
   GPIO.cleanup()         # membersihkan
   print "All cleaned up."