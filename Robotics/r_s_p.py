import serial
import time
import struct
arduino = serial.Serial('COM4', 9600)
num = 180
clock = 0

while True:
	time.sleep(.05)
	arduino.write(struct.pack('>B',num))
	clock = clock + 1
	if clock == 50:
		break;


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