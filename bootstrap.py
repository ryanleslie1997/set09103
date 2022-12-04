from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('base.html'), 200

@app.route('/home/')
def home():
    return render_template('inherits1.html'), 200

@app.route('/tourist/')
def tourist():
    return render_template('inherits2.html'), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
