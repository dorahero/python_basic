from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/hello_post', methods=['GET', 'POST'])
def hello_post():
    request_method = request.method
    username = ''  # 首次造訪方式為 GET 若無此行會無 username 變數
    if request_method == 'POST':
        username = request.form.get('name')  # html 中 input 的名稱
    return render_template('hello_post.html',
                            request_method=request_method,
                            username=username)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
