from flask import Flask

app = Flask(__name__)


# Controller
@app.route('/helloFlask')  # 街口名稱須為 string
def helloFlask():        # user 訪問此街口時做的事
    return '<h3>Hello Flask!</h3>'      # 回傳值須為 string, html型態

@app.route('/hello/<username>')  # username is a variable
def helloUser(username):         # catch the variable
    return 'Hello {}!!!??!'.format(username)

@app.route('/add/<x>/<y>')
def add(x, y):
    return '{}'.format(int(x)+int(y))  # xy is a string

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

