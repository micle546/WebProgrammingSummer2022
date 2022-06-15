from this import s
from flask import Flask

app = Flask(__name__)

@app.route("/")
def get_index():
    return "<p>test22 (╯°□°）╯︵ ǝƃɐdqǝʍ</p>"


