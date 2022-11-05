from flask import Flask, render_template  # From the module import the Flask Class.

app = Flask(__name__)     # Instantiate Flask into app (object)


@app.get("/")             # Flask decorator that maps routes to view functions
def index():                   # A view function is a function mapped to a route (flask)
    me = {                             # A python dictionary containing keys and values.
        "first_name": "Chaka",
        "last_name": "Robinson",
        "hobbies": "Fishing",
        "active": True,

    }
    return me                         # A return statement (required)

@app.get("/about")
def about_me():
    return render_template ("index.html")