from flask import Flask, jsonify, render_template, request
import convert


app = Flask(__name__)


@app.route('/_add_numbers')
def add_numbers():
    data = request.args.get('a')
    result_ = convert.convert(data)
    return jsonify(result=result_)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
