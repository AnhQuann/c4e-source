from flask import Flask, render_template
app = Flask(__name__)


@app.route('/<float:x>')
def index(x):
    return str(x)

if __name__ == '__main__':
  app.run(debug=True)
