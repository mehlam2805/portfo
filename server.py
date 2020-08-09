from flask import Flask, render_template, redirect, request
import csv
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/<string:page_name>')
def page(page_name):
    return render_template(page_name)


def write_to_csv(data):
	with open('database.csv',newline = '', mode = 'a') as database2:
		name = data['name']
		enquiry = data['enquiry']
		csv_writer = csv.writer(database2, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([name, enquiry])

def write_to_file(data):
	with open('data.txt', mode = 'a') as database:
		name = data['name']
		subject = data['subject']
		enquiry = data['enquiry']
		file = database.write(f'\n {name}, {subject}, {enquiry}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = dict(request.form)
		write_to_csv(data)
		return redirect('tankyou.html')
	else:
		return 'something went wrong'



