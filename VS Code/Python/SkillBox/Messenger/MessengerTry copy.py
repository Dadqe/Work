# Links
from flask import Flask
import time

server = Flask('MiR Server')

@server.route('/')
def hello():
    return 'Hello, World!'

@server.route('/status')
def status():
    return {
        'status : True,
        'name' : server.name,
        'time' :
    time.strftime('%H : %M : %S %D', time.localtime())
    }
    
server.run()


# Результат запроса на http://127.0.0.1:5000/status -> {'name':'MiR Server','status':true,'time':09:19:59 03/05/21}