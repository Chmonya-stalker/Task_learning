#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask import request
app = Flask(__name__)

@app.route('/zoo/', methods=['GET', 'POST'])
def form_example():
    animallist = ["Dogs", "Cat", "Pig", "Snake", "Duck"]
    soundlist = ["gav gav", "may may", "hry hry", "chhh chhh", "kra kra"]

    if request.method == 'POST':

        animal = request.form.get('animal')
        if animal is None:
            return 'You have not passed the required animal key'
        # Проверка поля "Животное"
        if len(animal) <= 0 or animal.isspace():
            return 'Invalid animal name format'
        else:
            animal = animal.strip()
            if not animal in animallist:
                return 'There is no such animal. You may have entered the wrong name'

        # Проверка поля "Имя"     
        name = request.form.get('name')
        if name is None:
            return 'You have not passed the required name key'
        if len(name) <= 0 or name.isspace():
            return 'Name Empty :('
        else:
            name = name.strip()

        # Проверка числа повторов 
        count = request.form.get('count')
        if count is None:
            return 'You have not passed the required count key'
        if len(count) <= 0 or count.isspace():
            return 'Count is empty.'
        else:
            try: 
                count = int(count)
                if count < 1:
                    return 'Count < 1'
            except:
                return 'Invalid Count format.'
           
        # Формирование звуков
        sound = ''
        for i in range(count):
            sound +=" " + soundlist[animallist.index(animal)]

        return '''
                  <h1>Привет! Я (сюда вставить эмоджи) {} !</h1>
                  <h1>Меня зовут {}</h1>
                  <h1>Я делаю {}</h1>
                  '''.format(animal, name, sound)
                  

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