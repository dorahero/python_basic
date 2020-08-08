from flask import Flask, request

app = Flask(__name__)

@app.route('/hello_post', methods=['GET', 'POST'])
def hello_post():
    request_method = request.method
    outStr = ''
    if request_method == 'GET':
        outStr = """
        <body>
            <form action="hello_post" method="POST">
                <input type="textbox" name="name">
                <button type="submit">SUBMIT</button>
            </form>
        </body>
        """
        return outStr
    elif request_method == 'POST':
        outStr = """
        <body>
            <form action="hello_post" method="POST">
                <input type="textbox" name="name">
                <button type="submit">SUBMIT</button>
            </form>
        """
        # get input which name is "name"
        name = request.form.get('name')
        outStr += """
            <div>
                Hello {}
            </div>
        </body>
        """.format(name)
        return outStr

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

# debug =True 可以直接更改程式存檔及同步更新網頁

