from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    # return "Hello world"
    return render_template('index.html')

@app.route('/explore')
def explore():
    return render_template('explore.html')

@app.route('/discounts')
def discounts():
    return render_template('discounts.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()