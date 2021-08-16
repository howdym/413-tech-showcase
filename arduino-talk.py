import serial                                                              
import time     
import zoom_ops

ArduinoUnoSerial = serial.Serial('com5',9600, timeout=1)         
time.sleep(2)
while True:  
    recv = ArduinoUnoSerial.readline()                                                      
    if len(recv) != 0:      
        print(recv) 
        zoom_ops.do_all() 
        ArduinoUnoSerial.write(b'0')                            
