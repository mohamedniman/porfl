from flask import Flask, render_template, url_for, request, redirect
import csv
import smtplib
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

def write_to_csv(data):
	with open('database.csv', mode='a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database, delimiter = ',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])

def email_sender(data):
	email = EmailMessage()
	email['from'] = data["email"]
	email['to'] = 'mohamedniman9785@gmail.com'
	email['subject'] = data["subject"]
	email.set_content(data["message"])
	with smtplib.SMTP(hsot='smtp.gmail.com', port=587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.login('mysite@gmail.com','maamiza9785')
		smtp.send_message(email)
		smtpserver = smtplib.SMTP('smtp.gmail.com',587)
		return 0

@app.route('/submite_form', methods=['POST', 'GET'])
def submite_form():
   if request.method == 'POST':
	    try:
	        data = request.form.to_dict()
	        print(data)
	        write_to_csv(data)
	        #email_sender(data)
	        return redirect('/thankyou.html')
	    except:
	        return 'Something went wrong :('
   else:
        return 'Something went wrong. Try Agian'

