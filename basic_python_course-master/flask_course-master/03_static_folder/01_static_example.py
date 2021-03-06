from flask import Flask

# static_url_path: 街口 指引到 static_folder: 本機路徑 名稱可不同
app = Flask(__name__, static_url_path='/static', static_folder='./static')

@app.route('/hello_google')
def hello_google():
    outStr = """
    <link href="/static/css/mystyle.css" rel="stylesheet" type="text/css">
    <div>
        This is a book.
    </div>
    <div class="test">
        This is a book.
    </div>
    <div>
        <img src="/static/image/googlelogo.png">
    </div>
    """

    return outStr

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
