from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, make_response
from flask import session

app = Flask(__name__)
app.secret_key = "12lk34nml1k23n4lolkj2ndASJP3DMIU9As9simoiasndff032dmpokifmo"


@app.route("/")
@app.route("/home")
def get_index():
    if 'username' in session:
        username = session['username']
    else:
        return redirect(url_for('get_login'))
    return render_template('home.html', name=username)
    #return "<p>test22 (╯°□°）╯︵ ǝƃɐdqǝʍ</p>"

@app.route("/other")
def get_other():
    if 'username' in session:
        username = session['username']
        return render_template('other.html', name=username)
    return redirect(url_for('get_login'))

@app.route("/login", methods=['GET'])
def get_login():
    if 'username' in session:
        username = session['username']
    else:
        return render_template('login.html')
    return redirect(url_for('get_index'))

@app.route("/login", methods=['POST'])
def post_login():
    username = request.form.get("username", None)
    if username != None and username !='':
        session['username'] = username
        return redirect(url_for('get_index'))
    else:
        return redirect(url_for('get_login'))
    
    

@app.route("/logout", methods=['GET'])
def get_logout():
    response = make_response(redirect(url_for('get_login')))
    response.delete_cookie("username")
    session.pop('username', None)
    return response