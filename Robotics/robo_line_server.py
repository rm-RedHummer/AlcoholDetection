from flask import Flask, render_template,request, redirect, url_for
import serial
import time
app = Flask(__name__)
# initialize connection to Arduino
# if your arduino was running on a serial port other than '/dev/ttyACM0/'
# declare: a = Arduino(serial_port='/dev/ttyXXXX')
arduino = serial.Serial('COM4', 9600)
time.sleep(3)
# I declara ang nga  pins na gagamitin 
# pasimulan ang digital pin bilang output
print ('Arduino initialized')
# magkakaroon ng 2 different requests sa webpage
# GET = we just type in the url
# POST = some sort of form submission like a button
@app.route('/', methods = ['POST','GET'])
def definePage():
    # mga variables sa template page (templates/index.html)
    author = "Reymark"
    # kapag  post request sa webpage 
    if request.method == 'POST':
        # ka pag na click ang  turn on button
        if request.form['submit'] == 'Turn On': 
            print ('TURN ON')
            # pailawin ang LED on arduino
            arduino.write(b'A')
        # kapag na click ang turn off button
        elif request.form['submit'] == 'Turn Off': 
            print ('TURN OFF')
            # turn off LED on arduino
            arduino.write(b'B')
            
        else:
            pass
    
    # basahin ang  analog value galing sa photoresistor
    #readval = float(100);

    # ang default  page para ma display ang  template ng mga variables
    return render_template('index.html', author=author)
if __name__ == "__main__":
    # patakbuhin ang webpage
    # do 0.0.0.0 para maka log sa webpage
    # gamitin ang network kung saan naka konecta ang computer
    app.run(host='0.0.0.0')
