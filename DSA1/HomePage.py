from flask import Flask, render_template, request, redirect, url_for, session, flash
import Datas

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', x = Datas.x, y = Datas.y, z = Datas.CryptoData1_CC[0].head(1))

@app.route('/about')
def about():
    return render_template('about.html', x = Datas.x, z = Datas.CryptoData1_CC[0].head(1))

@app.route('/table')
@app.route('/datas')
def table():
    tables = []
    tableName = Datas.CryptoData1_UC_M_S
    tableName.insert(0, '')
    for dataframe in Datas.CryptoData1_CC:
        top_10_rows = dataframe.head(10)
        html_table = top_10_rows.to_html(index=False)
        tables.append(html_table)
    return render_template('datas.html', tables=tables, titles=tableName)

app.run(debug=True)