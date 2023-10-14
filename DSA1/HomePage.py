from flask import Flask, render_template, request, redirect, url_for, session, flash
import Datas

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', x = Datas.x, y = Datas.y, z = Datas.CryptoData1_CC[0].head(1))

@app.route('/about')
def about():
    return render_template('about.html', x = Datas.x)

app.run(debug=True)