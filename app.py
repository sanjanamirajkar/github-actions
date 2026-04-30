from flask import flask, render_template


app = flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/health')
def health():
    return 'Server is up and running'


app.run(debug=True, host='0.0.0.0', port=80)
