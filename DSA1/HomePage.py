from flask import Flask, render_template, request, redirect, url_for, session, flash
import Datas

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', x = Datas.x, y = Datas.y, z = Datas.CryptoData1_CC[0].head(1))

@app.route('/about')
def about():
    return render_template('about.html', x = Datas.x, z = Datas.CryptoData1_CC[0].head(1))

@app.route('/tabletop10')
@app.route('/datastop10')
def tabletop10():
    route_name = 'Top 10 Values'
    tables = []
    for dataframe in Datas.CryptoData1_CC:
        top_10_rows = dataframe.head(10)
        html_table = top_10_rows.to_html(index=False)
        tables.append(html_table)
    return render_template('datas.html', tables=tables, route_name=route_name, titles=['', 'binance-coin', 'bitcoin', 'bitcoin-cash', 'bitcoin-sv', 'cardano', 'eos', 'ethereum', 'litecoin', 'stellar', 'tether', 'tezos', 'xrp'])

@app.route('/tablebottom10')
@app.route('/datasbottom10')
def tablebottom10():
    route_name = 'Last 10 Values'
    tables = []
    for dataframe in Datas.CryptoData1_CC:
        top_10_rows = dataframe.tail(10)
        html_table = top_10_rows.to_html(index=False)
        tables.append(html_table)
    return render_template('datas.html', tables=tables, route_name=route_name, titles=['', 'binance-coin', 'bitcoin', 'bitcoin-cash', 'bitcoin-sv', 'cardano', 'eos', 'ethereum', 'litecoin', 'stellar', 'tether', 'tezos', 'xrp'])

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

app.run(debug=True)