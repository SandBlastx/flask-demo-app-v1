from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    user_attrs = {}
    if request.method == 'POST':
        user_attrs = request.form.to_dict()
    elif request.args:
        user_attrs = request.args.to_dict()
    return render_template('index.html', user_attrs=user_attrs)


@app.route('/health')
def health():
    return {'status': 'healthy'}, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
