from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def root():
    return render_template('home.html'), 200

@app.route('/tourist/', methods=['GET', 'POST'])
def tourist():
    return render_template('tourist.html'), 200

@app.route('/hospitality/', methods=['GET', 'POST'])
def hospitality():
    return render_template('hospitality.html'), 200

@app.route('/history/', methods=['GET', 'POST'])
def history():
    return render_template('history.html'), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
