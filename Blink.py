import time
import mraa

###### Programe Begins ####
print (mraa.getVersion())
Led = mraa.Gpio(4)
Led.dir(mraa.DIR_OUT)
Led.write(1)
value = 0
while 1:
        if value == 0:
                value = 1
        else:
                value = 0
        Led.write(value)
        print "LED "+str(value)
        time.sleep(1)
