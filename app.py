from flask import Flask, render_template, request, send_file, make_response, send_from_directory, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)