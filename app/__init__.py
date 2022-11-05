from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello, world Again</h1>"



@app.route("/products")
def products():
    product_list = ["Juice", "Berries", "Sandwhiches"]