import time
import mraa

###### Programe Begins ####
print (mraa.getVersion())  #Print mraa version for reference

# Initiate Digital Pin 8 with direction in
Button = mraa.Gpio(8)
Button.dir(mraa.DIR_IN)

while 1:
        # Read voltage at Digital Pin
        value = Button.read()
        if value == 1:
                print "Button State: ON"
        else:
                print "Button State: OFF"
        time.sleep(.25)
