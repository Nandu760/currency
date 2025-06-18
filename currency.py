import os
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('currency.html', result='')

@app.route('/convert', methods=['POST'])
def convert():
    amount = float(request.form['amount'])
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']

    try:
        url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
        response = requests.get(url)
        data = response.json()
        converted_amount = data['result']
        result = f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"
    except Exception as e:
        result = "Error fetching data."
        print("Error:", e)

    return render_template('currency.html', result=result)
    
if __name__ == '__main__':
 port=int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0',port=port)
