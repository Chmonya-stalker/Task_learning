from flask import Flask, render_template
from flask import request
app = Flask(__name__)

#@app.route('/zoo/', methods=['GET'])
#def index():
#    return render_template('index.html')
#@app.route('/zoo/cat')
#def cat():
#    return render_template('animals/Cat.html')
#@app.route('/zoo/pig')
#def pig():
#    return render_template('animals/Pig.html')
#@app.route('/zoo/dog')
#def dog():
#    return render_template('animals/Dog.html')
#@app.route('/zoo/duck')
#def duck():
#    return render_template('animals/Duck.html')
#@app.route('/zoo/snake')
#def snake():
#    return render_template('animals/Snake.html')

@app.route('/zoo/test', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        animal = request.form.get('animal')
        sound = request.form.get('sound')
        count = request.form.get('count')
        return '''
                  <h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language, framework)
    return '''
           <form method="POST">
           <h1> Добро пожаловать в Зоопарк! </h1>
               <div><label>Language: <input type="text" name="language"></label></div>
               <div><label>Framework: <input type="text" name="framework"></label></div>
               <input type="submit" value="Submit">
           </form>'''

if __name__ == '__main__':
    app.run()