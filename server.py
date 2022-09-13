from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key="b'\xdb\xa1q\x87\x13Lh\xbd\xcc\x18Q\xf3\x14Ti\x91'"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def create_user():
    session['username'] = request.form['name']
    session['userlocation'] = request.form['location']
    session['userlanguage'] = request.form['language']
    session['usercomment'] = request.form['comment']
    return redirect('/result')

@app.route("/result")
def show_user():
    return render_template('result.html')

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)