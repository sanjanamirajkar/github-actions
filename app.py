from flask import flask, render_template

app = flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/health')
def health():
    return 'Server is up and running'

if __name__ == "__main__":
    app.run(debug=True)
