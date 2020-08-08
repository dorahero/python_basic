from flask import Flask, request, render_template
import poker as p
# jsonify 回傳json

app = Flask(__name__)

@app.route('/poker', methods=['GET', 'POST'])
def poker():
    request_method = request.method
    if request.method == 'GET':
        return render_template('pokercode.html')
    elif request.method == 'POST':
        players = request.form.get('players')
        cards = p.poker(int(players))
        return render_template('pokercode.html',
                               request_method=request_method,
                               players=players,
                               cards=cards)
        # 印 flask 一定要回傳string, 將 json 轉換為 string

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
