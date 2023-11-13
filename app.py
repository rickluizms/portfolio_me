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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')



# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
#
#              V I E W S - P R O J E C T S - D A S H B O A R D S
#
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 

@app.route('/projects/dashboard1', methods=['GET'])
def project_dashboard1():
    return render_template('projects/dashboards/dashboard1.html')

@app.route('/projects/dashboard2', methods=['GET'])
def project_dashboard2():
    return render_template('projects/dashboards/dashboard2.html')

@app.route('/projects/dashboard3', methods=['GET'])
def project_dashboard3():
    return render_template('projects/dashboards/dashboard3.html')

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
#
#              V I E W S - P R O J E C T S - D A T A  S C I E N C E
#
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 

@app.route('/projects/data1', methods=['GET'])
def project_data1():
    return render_template('projects/data-science/data1.html')

@app.route('/projects/data2', methods=['GET'])
def project_data2():
    return render_template('projects/data-science/data2.html')

@app.route('/projects/data3', methods=['GET'])
def project_data3():
    return render_template('projects/data-science/data3.html')

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
#
#              V I E W S - P R O J E C T S - B A C K  E N D
#
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 

@app.route('/projects/backend1', methods=['GET'])
def project_backend1():
    return render_template('projects/back-end/backend1.html')

@app.route('/projects/backend2', methods=['GET'])
def project_backend2():
    return render_template('projects/back-end/backend2.html')

@app.route('/projects/backend3', methods=['GET'])
def project_backend3():
    return render_template('projects/back-end/backend3.html')

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
#
#              V I E W S - P R O J E C T S - F R O N T  E N D
#
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 

@app.route('/projects/frontend1', methods=['GET'])
def project_frontend1():
    return render_template('projects/front-end/frontend1.html')

@app.route('/projects/frontend2', methods=['GET'])
def project_frontend2():
    return render_template('projects/front-end/frontend2.html')

@app.route('/projects/frontend3', methods=['GET'])
def project_frontend3():
    return render_template('projects/front-end/frontend3.html')

if __name__ == "__main__":
    app.run(debug=True)
