from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pag1')
def pag1():
    return render_template('pag1.html')


@app.route('/pag2')
def pag2():
    return render_template('pag2.html')


@app.route('/pag3')
def pag3():
    return render_template('pag3.html')


@app.route('/pag4')
def pag4():
    return render_template('pag4.html')


@app.route('/pag5')
def pag5():
    return render_template('pag5.html')


@app.route('/pag6')
def pag6():
    return render_template('pag6.html')


if __name__ == "__main__": 
    app.run(debug=True)
