# Zoo и Speedtest

## Intro
Данный проект создавался с целью изучения таких областей как:
1. Docker (dockerfile и docker-compose)
2. HTTP методы
3. Python (фреймворк Flask в частности)
4. Web server Nginx
5. Github actions

## About it
Имеются 3 основных приложения реализованных через Docker:
1. [Speedtest](/speedtest/)
2. [Zoopark](/flask/)
3. [Revers](/revers/)

Также в проекте применяется [Github actions](/.github/workflows/):
1.  Публикация образа zoopark в Docker Hub
2.  Проверка кода по средствам CodeQL

## Project Logic
1. Стартует [Docker-compose](/docker-compose) файл:  
  - Первым запускается Revers. На этом же шаге выполняется маппинг 80-го порта из вашей машины к 80-тому Revers. Через него мы будем взаимодействовать с другими приложениями.  
  - Приложение Zoopark располагается на Docker Hub и образ для проекта берется оттуда.
2. Для перехода к speedtest, нам необходимо попасть на http://localhost/speed/
3. Для перехода к zoopark, нам необходимо попасть на http://localhost/zoo/


## P.S
Выражаю благодарность человеку, который нашел мне чем заняться.  
Заниматься подобным - безумно интересно.  
**_AnnoX4uk_**, Thanks a lot!)
