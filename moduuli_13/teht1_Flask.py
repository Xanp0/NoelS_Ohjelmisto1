from flask import Flask, request
import json
import math

app = Flask(__name__)
@app.route('/alkuluku/<int:numero>')
def alkuluku(numero):
    #args = request.args
    onkoAlku = True

    for testaus in range(2, int(math.sqrt(numero))):
        if numero % testaus == 0:
            onkoAlku = False
            break

    if onkoAlku:
        vastaus = {'"Number:"' + numero + ', "isPrime:true"'}
    else:
        vastaus = {'"Number:"' + numero + ', "isPrime:false"'}
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
