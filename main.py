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
    title='clothes'
    return render_template('clothes.html', menu=sub_menu, title=title)


@app.route('/shoes/')
def shoes(title='default'):
    title = 'shoes'
    return f"<h1>{title}</h1>"


@app.route('/jacket/')
def jackets(title='default'):
    title = 'jacket'
    return f"<h1>{title}</h1>"


if __name__ == '__main__':
    app.run(debug=True)
