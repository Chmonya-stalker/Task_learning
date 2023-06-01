#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask import request
import emoji
app = Flask(__name__)

#Создание маршрута для метода POST
@app.route('/', methods=['POST'])
def post_metod():

    # Работа с переменной 'animal'
    animal = request.form.get('animal')
    if animal is None:
        return 'You have not passed the required animal key'
    # Проверка поля "Животное"
    if len(animal) <= 0 or animal.isspace():
       return 'Invalid animal name format'
    else:
        animal = animal.strip()

    # Работа с переменной 'count'
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
    sound = request.form.get('sound')
    for i in range(count-1):
        sound +=" " + sound

    return '''
            <h1>Привет! Я {} {}!</h1>
            <h1>Я делаю {}</h1>
            '''.format(animal, emoji.emojize(f':{animal}:'), sound)

#Создание маршрута для метода GET
@app.route('/', methods=['GET'])
# Добавь маршрут для метода POST, что бы принимал json формата: {animal: foo, count: number, sound: bar}
def get_metod():
    return '''
      <form method="POST">
        <h1> Добро пожаловать в Зоопарк! </h1>
        <h2> Пожалуйста, напишите к какому животному Вы хотите схоодить.</h2>
            <div><label>Животное: <input type="text" name="animal"></label></div>
            <div><label>Какой вы хотите услышать звук от животного: <input type="text" name="sound"></label></div>
            <div><label>Сколько раз вы услышать его звук: <input type="number" name="count"></label></div>
            <input type="submit" value="К животному">
проверка как работает
        </form>'''
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
