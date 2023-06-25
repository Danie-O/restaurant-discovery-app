from flask import Flask, render_template, request
from flask_mail import Mail, Message
# from bs4 import beautifulsoup
import config


app = Flask(__name__)
app.config.update(
    MAIL_SERVER="smtp.gmail.com",
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME=config.EMAIL,
    MAIL_PASSWORD=config.PASSWORD,
)
mail = Mail(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/explore')
def explore():
    return render_template('explore.html')


@app.route('/discounts')
def discounts():
    return render_template('discounts.html')


@app.route('/contact', methods=["GET"])
def contact():
    return render_template('contact.html', success=False)


@app.route("/subscribe_for_newsletter/", methods=["POST"])
def subscribe_for_newsletter():
    try:
        location = request.form['city']
        # TODO: use beautiful soup/ API to scrape top 10 discount deals for the day
        # TODO: store subscribed user details in db to enable sending of periodic emails
        discount = discounts[:10]
        name = request.form['name']
        msg = Message("Welcome to FoodXplorer!", 
                      sender="foodxplorer@gmail.com",
                      recipients=[request.form['email']]
            )
        msg.html = "Hello {}".format(request.form['name']) + \
                    " We are super excited to connect you with your favorite restaurants in your neighborhood. \
                      Find below some hot discount deals in your city today, and look forward to more of this evry Friday!(TGIF) \
                      \
                      This week's discounts:" + discounts
        mail.send(msg)

        return render_template('contact.html', success=True, error=False)
    except:
        return render_template('contact.html', success=False, error=True)

    


if __name__ == '__main__':
    app.run(debug=True)