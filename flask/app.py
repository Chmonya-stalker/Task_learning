#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask import request
import emoji
app = Flask(__name__)

# Функция для проверок всех условий для взодящих значений
def check_and_output(animal,sound,count):

    if len(animal) <= 0 or animal.isspace():
        return 'Invalid animal name format'
    else:
            animal = animal.strip().lower()

    if len(count) <= 0 or count.isspace():
        return 'Wrong number format'
    else:
        try: 
            count = int(count)
            if count < 1:
                return 'The number cannot be less than 1'
        except:
            return 'Invalid Count format.'

    if len(sound) <= 0 or sound.isspace():
        return 'Invalid sound format'
    sound =(sound + " ") * count

    # Проверка существования животного и эмоджи #
    emoji_animal = emoji.emojize(f':{animal}:')
    if emoji_animal == f':{animal}:':
        return 'There is no such animal. Check the title'

    return '''
        <h1>Привет! Я {} {}!</h1>
        <h1>Я делаю {}</h1>
        '''.format(animal, emoji_animal, sound)

# Создание маршрута для JSON #
@app.route('/json/', methods=['POST'])
def json_metod():

    request_data = request.get_json()

    if ('animal' in request_data) and ('sound' in request_data) and ('count' in request_data):
        animal = request_data['animal']
        sound = request_data['sound']
        count = request_data['count']

    else:
        return 'Одно из обязательных полей пропущено!'

    return check_and_output(animal,sound,count)


# Создание маршрута для метода POST #
@app.route('/', methods=['POST'])
def post_metod():

    animal = request.form.get('animal')
    sound = request.form.get('sound')
    count = request.form.get('count')
    if (animal is None) or (sound is None) or (count is None):
        return 'Одно из обязательных полей пропущено!'

    return check_and_output(animal,sound,count)

# Создание маршрута для метода GET #
@app.route('/', methods=['GET'])
def get_metod():
    return '''
      <form method="POST">
        <h1> Добро пожаловать в Зоопарк! </h1>
        <h2> Пожалуйста, напишите к какому животному Вы хотите схоодить.</h2>
            <div><label>Животное: <input type="text" name="animal"></label></div>
            <div><label>Какой вы хотите услышать звук от животного: <input type="text" name="sound"></label></div>
            <div><label>Сколько раз вы услышать его звук: <input type="number" name="count"></label></div>
            <input type="submit" value="К животному">
        </form>'''

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)