#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask import request
app = Flask(__name__)

@app.route('/zoo/', methods=['GET', 'POST'])
def form_example():
    animallist = ["Dogs", "Cat", "Pig", "Snake", "Duck "]
    soundlist = ["gav gav", "may may", "hry hry", "chhh chhh", "kra kra"]
    if request.method == 'POST':
        animal = request.form.get('animal')
        if len(animal) < 0  or not animal in animallist:
            return 'There is no such animal. You may have entered the wrong name'

        name = request.form.get('name')
        if len(name) < 0:
            return 'Name Empty :('
        sound = animallist.index(animal)

        count = int(request.form.get('count'))
        if  len(animal) < 0 or not isinstance(count, int) or count < 1:
           return ' You entered the number of repetitions incorrectly.'

        return '''
                  <h1>Привет! Я (сюда вставить эмоджи) {} !</h1>
                  <h1>Меня зовут {}</h1>'''.format(animal, name)
                  

    return '''
           <form method="POST">
           <h1> Добро пожаловать в Зоопарк! </h1>
           <h2> Пожалуйста, напишите какое животное хотите услышать</h2>
           <ul>
                <li>Dogs</li>
                <li>Cat</li>
                <li>Pig</li>
                <li>Snake</li>
                <li>Duck</li>
            </ul>
               <div><label>Животное: <input type="text" name="animal"></label></div>
               <div><label>Какое вы хотите ему дать имя: <input type="text" name="name"></label></div>
               <div><label>Сколько раз вы хотите услышать его: <input type="number" name="count"></label></div>
               <input type="submit" value="К животному">
           </form>'''

if __name__ == '__main__':
    app.run()

#soundlist[animallist.index(animal)]
#for i in range(count):