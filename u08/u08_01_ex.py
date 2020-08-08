from flask import Flask


app = Flask(__name__, static_url_path='/static1', static_folder='./static')

@app.route('/hello_google')
def hello_google():
    #  static_url_path = '/static1'
    outStr = """<img src="/static1/image/googlelogo.png">"""    # 街口路徑
    return outStr

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
