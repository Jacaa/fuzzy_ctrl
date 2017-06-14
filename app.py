from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        service = request.form.get('service')
        food = request.form.get('food')
        return jsonify(service, food)
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
