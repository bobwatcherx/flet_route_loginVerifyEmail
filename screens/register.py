from flet import *
import random
import string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from myconnect import mycursor,mydb

def RegisterView(page):
	nametxt = TextField(label="email")
	passwordtxt = TextField(label="password")


	def send_verification_email(email, token):
	    subject = "Verifikasi Email"
	    body = "Klik link berikut untuk melakukan verifikasi email: http://localhost:5000/verify_email?token=" + token + "&email=" + email

	    message = MIMEMultipart()
	    message['From'] = "noreply@myapp.com"
	    message['To'] = email
	    message['Subject'] = subject
	    message.attach(MIMEText(body, 'plain'))

	    # koneksi ke SMTP server Mailtrap dan kirim email
	    with smtplib.SMTP('smtp.mailtrap.io', 2525) as smtp:
	        smtp.login("27b3da367addfa", "bc4d9ff24e96cb")
	        smtp.sendmail("noreply@myapp.com", email, message.as_string())

	def generate_token():
	    letters = string.ascii_letters
	    return ''.join(random.choice(letters) for i in range(10))


	def registerprocess(e):
		mycursor.execute("SELECT * FROM users WHERE email = %s", (nametxt.value,))
		result = mycursor.fetchone()
		if result:
			print("Email sudah terdaftar")
			return
		token = generate_token()
		sql = "INSERT INTO users (email, password, verification_token) VALUES (%s, %s, %s)"
		val = (nametxt.value, passwordtxt.value, token)
		mycursor.execute(sql, val)
		mydb.commit()
		send_verification_email(nametxt.value, token)
		print("Registrasi berhasil, silakan cek email untuk verifikasi")
		page.snack_bar = SnackBar(
			Text("Send Email Verification",size=30),
			bgcolor="blue"
			)
		page.snack_bar.open = True
		nametxt.value = ""
		passwordtxt.value = ""
		page.update()


	return Column(
		controls=[
			Text("you register ",size=30,weight="bold"),
			nametxt,
			passwordtxt,
			ElevatedButton("Register my account",
			bgcolor="blue",color="white",
			on_click=registerprocess
				),
			ElevatedButton("Login Now",
			bgcolor="orange",color="white",
			on_click=lambda e:page.go("/login")
				)
			]
		)
