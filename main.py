import os

from flask import Flask, render_template



app = Flask(__name__)

sub_menu = [{"name": 'Одежда', "url": 'clothes'},
            {"name": 'Обувь', "url": 'shoes'},
            {"name": 'Куртка', "url": 'jacket'}, ]


@app.route('/')
def index(title='default'):
    title="Fushion clothes"
    return render_template('index.html', menu=sub_menu, title=title)


@app.route('/clothes/')
def clothes(title='default'):
    url =os.listdir('static/images/products/clothes')
    title='clothes'
    return render_template('clothes.html', menu=sub_menu, title=title, url=url)


@app.route('/shoes/')
def shoes(title='default'):
    url = os.listdir('static/images/products/shoes')
    title = 'shoes'
    return render_template('shoes.html', menu=sub_menu, title=title, url=url)


@app.route('/jacket/')
def jackets(title='default'):
    url = os.listdir('static/images/products/jacket')
    title = 'jacket'
    return render_template('jackets.html', menu=sub_menu, title=title, url=url)


if __name__ == '__main__':
    app.run(debug=True)
