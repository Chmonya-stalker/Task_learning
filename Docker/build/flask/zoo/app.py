from flask import Flask, render_template
app = Flask(__name__)

@app.route('/zoo/')
def index():
    return render_template('index.html')
@app.route('/zoo/cat')
def cat():
    return render_template('animals/Cat.html')
@app.route('/zoo/pig')
def pig():
    return render_template('animals/Pig.html')
@app.route('/zoo/dog')
def dog():
    return render_template('animals/Dog.html')
@app.route('/zoo/duck')
def duck():
    return render_template('animals/Duck.html')
@app.route('/zoo/snake')
def snake():
    return render_template('animals/Snake.html')

if __name__ == '__main__':
    app.run()