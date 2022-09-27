import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

def Up(channel):
    print("Button UP pushed!")
def Down(channel):
    print("Button DOWN pushed!")
def Left(channel):
    print("Button LEFT pushed!")
def Right(channel):
    print("Button RIGHT pushed!")

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Pin 10 input pin and set initial value to be pulled low (off)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Pin 11 input pin and set initial value to be pulled low (off)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Pin 12 input pin and set initial value to be pulled low (off)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Pin 13 input pin and set initial value to be pulled low (off)

GPIO.add_event_detect(10,GPIO.RISING,callback=Up) # Setup event on pin 10 rising edge
message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.add_event_detect(11,GPIO.RISING,callback=Down) # Setup event on pin 10 rising edge
message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.add_event_detect(12,GPIO.RISING,callback=Left) # Setup event on pin 10 rising edge
message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.add_event_detect(13,GPIO.RISING,callback=Right) # Setup event on pin 10 rising edge
message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up

message = input("Press enter to quit\n\n") # Run until someone presses enter
