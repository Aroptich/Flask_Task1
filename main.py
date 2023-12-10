from flask import Flask, render_template


app = Flask(__name__)

sub_menu = [{"name": 'Одежда', "url": 'clothes'},
            {"name": 'Обувь', "url": 'shoes'},
            {"name": 'Куртка', "url": 'jacket'},]

@app.route('/')
def index():
    return render_template('index.html', menu=sub_menu)

@app.route('/clothes/')
def clothes():
    return "<h1>clothes</h1>"

@app.route('/shoes/')
def shoes():
    return "<h1>shoes</h1>"

@app.route('/jacket/')
def jackets():
    return "<h1>jackets</h1>"
if __name__ == '__main__':
    app.run(debug=True)