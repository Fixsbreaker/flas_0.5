from flask import Flask

app = Flask(__name__)


@app.route('/')
def func():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def return_sample_page():
    line = ["Человечество вырастает из детства.",
            "Человечеству мала одна планета.",
            "Мы сделаем обитаемыми безжизненные пока планеты.",
            "И начнем с Марса!",
            "Присоединяйся!"]
    return "</br>".join(line)


@app.route('/image_mars')
def image():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1 style="
                        color: red;
                    ">Жди нас, Марс!</h1>
                    <img src='/static/image/mars.jpg' height=350px'>
                    <p>Вот она какая, красная планета</p>
                  </body>
                </html>"""

@app.route('/promotion_image')
def bootstrap():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1 style="
                        color: red;
                    ">Жди нас, Марс!</h1>
                    <img src='/static/image/mars.jpg' height=350px'>
                    <div class="alert alert-secondary" role="alert">
                        Человечество вырастает из детства
                    </div>
                    <div class="alert alert-success" role="alert">
                        Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                        Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                        И начнём с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                        Присоединяйся
                    </div>
                  </body>
                </html>"""




if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')