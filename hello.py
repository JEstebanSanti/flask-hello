from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
@app.route("/")
def hello_world():
        try:      
            number1 = float(request.form.get("numero1"))
            number2 = float(request.form.get("numero2"))
            suma = number1+number2
            resta = number1-number2
            division = number1/number2
            multiplicacion = number1 * number2
        except:
              number1 = ''
              number2 = ''
              suma = ''
              resta = ''
              division = ''
              multiplicacion = ''
        return render_template('holamundo.html', n1 = number1, n2= number2, resta = resta, suma = suma, division = division, multiplicacion = multiplicacion)
    
