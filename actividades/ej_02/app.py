# Aplicacion del servidor
from microdot import Microdot, send_file
from machine import Pin
led1 = Pin(32, Pin.OUT, value=0)
led2 = Pin(33, Pin.OUT, value=0)
led3 = Pin(25, Pin.OUT, value=0)

app = Microdot()

@app.route('/')
async def index(request):
    return send_file('index.html')

@app.route('/<dir>/<file>')
async def index(request, dir, file):
    return send_file("/{}/{}". format(dir, file))

@app.route('/led/toggle/<led>')
async def led_toggle(request, led):
    print(led)
    if led == "led1":
        led1.value(not led1.value())
        print('hola mundo') 
        
    elif led == "led2":
        led2.value(not led2.value())
        print('hola mundo')
        
    elif led == "led3":
        led3.value(not led3.value())
        print('hola mundo')

app.run(port=80)
