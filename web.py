from flask import Flask, render_template, request
from googlefinance import getQuotes
app = Flask(__name__)

def get_stock_price(ticker):
    quotes = getQuotes(ticker)
    price = quotes[0]["LastTradePrice"]
    return "The price of {} is {}".format(ticker, price)

@app.route("/")
def index():
    name = request.values.get("name", "Stranger")
    greeting = "Hello, {}".format(name)
    return render_template("index.html", greeting=greeting)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/results")
def results():
    stock = request.values.get("stock")
    price = get_stock_price(stock)
    return render_template("results.html", price=price)   

# @app.route("/users/<username>")
# def profile():
#     user = get_user(username)
#     return  render_template("profile.html")

# debug=True makes it so changes will automatically load
app.run(debug=True)