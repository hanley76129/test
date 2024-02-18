from flask import Flask, render_template, request
from time import sleep
from cats import Cats
import random

app = Flask(__name__, template_folder='template',static_folder='static')

# @app.route('/')
# def loading():
#     h = '/home'
#     return render_template('loading.html', h=h)


@app.route('/')
def home():
    Snow = Cats("Snowflake", "I love cats", "/static/img/snow.png")
    Andy = Cats("Andy", "Dreams of sleeping on the campus of MIT some day. Spends his time watching kat-pop purr-formances!", "/static/img/andy.png")
    Brendan = Cats("Brandon", "I love cats", "/static/img/brenden.png")
    Jordan = Cats("Jordan", "I love cats", "/static/img/jordan.png")
    Nick = Cats("Nickoles", "Nickoles is short for Nick. The type of cat to go in McDonalds asking for a hashmap.", "/static/img/nick.png")
    return render_template('index.html', s = Snow, a = Andy, b = Brendan, j = Jordan, n = Nick)
   


if (__name__ == "__main__"):
    app.run(host='0.0.0.0', port=8080)

