from flask import Flask, request, jsonify
import poker as p
# jsonify 回傳json

app = Flask(__name__)

@app.route('/poker', methods=['GET', 'POST'])
def poker():
    if request.method == 'GET':
        # 將結果回傳給 /poker 以 POST 方式
        outStr = """
        <html>
            <head>
                <title>poker</title>
            </head>
            <body>
                <h1>How many players?</h1>
                <form action="/poker" method="post">  
                    <input type="textbox" name="players">
                    <button type="submit">Submit</button>
                </form>
            </body>
        </html>
        """
        return outStr
    elif request.method == 'POST':
        players = request.form.get('players')
        cards = p.poker(int(players))
        return jsonify(cards)
        # 印 flask 一定要回傳string, 將 json 轉換為 string

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


