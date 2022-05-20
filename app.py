from flask import Flask, render_template, jsonify, request
import whois
import datetime

app = Flask(__name__)
app.debug = True
app.config['TEMPLATE_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    url = request.form['url']
    w = whois.whois(url)
    w.expiration_date  # dates converted to datetime object
    datetime.datetime(2013, 6, 26, 0, 0)
    w.text
    return render_template('search.html', url=url, record=w)

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='127.0.0.1')