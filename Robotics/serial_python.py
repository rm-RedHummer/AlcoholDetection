import serial
import time
arduino = serial.Serial('COM4', 9600)
while True:
	time.sleep(.1)
	num = 45
	command = (''.join(str(num))).encode()
	arduino.write(command)
	#print (str(command))


'''
Performs a pinMode() operation on pin_number
        Internally sends b'M{mode}{pin_number} where mode could be:
        - I for INPUT
        - O for OUTPUT
        - P for INPUT_PULLUP MO13
        """
        command = (''.join(('M',mode,str(pin_number)))).encode()
        #print 'set_pin_mode =',command,(''.join(('M',mode,str(pin_number))))
        self.conn.write(command)
'''