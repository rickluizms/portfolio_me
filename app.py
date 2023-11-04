from flask import Flask, render_template, request, send_file, make_response, send_from_directory, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/home', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/resume', methods=['GET'])
def resume():
    return render_template('resume.html')

@app.route('/projects', methods=['GET'])
def projects():
    return render_template('projects.html')

@app.route('/projects/dashboard', methods=['GET'])
def project_dashboard():
    return render_template('project-dashboard.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')



if __name__ == "__main__":
    app.run(debug=True)
    
# Subir em HEROKU