from flask import Flask, render_template, url_for, request
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<username>/')
def info(username=None):
    return render_template('info.html', name=username)

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

#.app.route('favicon.ico)
#...def favicon():
# return 'thjfkakdsfn'
        
def write_to_csv(data):
    with open('database.csv', mode='a') as database:
        email = data["Email"]
        username = data["Username"]
        password = data["Password"]
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([username,email,password])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return 'You have successfully submitted your form. Thank you for your cooperation.'