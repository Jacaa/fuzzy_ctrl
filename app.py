from flask import Flask, render_template, request, jsonify, make_response
from fuzzy import defuzzified_result 
import StringIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        params = request.get_json(force=True)
        plot, power = defuzzified_result(float(params['speed']), 
                                         float(params['distance']))
        img = StringIO.StringIO()
        img.write("<img class=\'plot\'src=\'data:image/png; base64," + plot + "\'>")
        resp = make_response(img.getvalue())
        return jsonify(img.getvalue(), power)
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
