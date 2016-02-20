import mraa
import time

#### Define Procedure to detect PosEdge
#### at a Digital Input Pin
def DetectNegEdge(Pin) :
  while 1:
    if Pin.read() == 1:
      time.sleep(0.05)
      if Pin.read() == 0:
          return

##### Programe begins #######

### Led Initilization ###############
# Set direction of D4 pin to out ####
Led = mraa.Gpio(4)
Led.dir(mraa.DIR_OUT)

### Button Initialization ###########
# Set direction of D8 pin to in #####
Button = mraa.Gpio(8)
Button.dir(mraa.DIR_IN)

### Toggle LED for each Neg Edge triggered by Button
Led_state = 0
Led.write(Led_state)
while 1:
  DetectNegEdge(Button)
  if Led_state==0:
    Led_state = 1
  else
    Led_state = 0
  Led.write(Led_state)

  
