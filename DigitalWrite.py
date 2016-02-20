import time
import mraa

###### Programe Begins ####
print (mraa.getVersion())  #Print mraa version for reference

# Initiate Digital Pin 4 with direction out
Led = mraa.Gpio(4)    
Led.dir(mraa.DIR_OUT)

value = 0
while 1:
        if value == 0:
                value = 1
        else:
                value = 0
        Led.write(value)   #Set voltage at digital pin to HIGH/LOW
        print "LED "+str(value)
        time.sleep(1)
