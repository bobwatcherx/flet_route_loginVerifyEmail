from flet import *
import random
import string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from myconnect import mycursor,mydb


def LoginView(page):
	nametxt = TextField(label="email")
	passwordtxt = TextField(label="password")


	def is_email_verified(email):
	    mycursor.execute("SELECT is_verified FROM users WHERE email = %s", (nametxt.value,))
	    result = mycursor.fetchone()
	    if result[0] == 1:
	        return True
	    else:
	        return False

	def loginprocess(e):
	    mycursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (nametxt.value, passwordtxt.value))
	    result = mycursor.fetchone()
	    if result is None:
	        print("Email atau password salah")
	        page.snack_bar = SnackBar(
	            Text("Wrong email password",size=30),
	            bgcolor="red"
	        )
	        page.snack_bar.open = True
	        page.update()
	    if not is_email_verified(nametxt.value):
	        print("Email belum terverifikasi")
	        page.snack_bar = SnackBar(
	            Text("your email is not verified",size=30),
	            bgcolor="red"
	        )
	        page.snack_bar.open = True
	        page.update()
	    if result :
	    	print(result)
	    	get_token = result[4]
	    	page.go("/dashboard")
	    	page.client_storage.set("login",get_token)
	    	print("Adalah",page.client_storage.get("login"))
	    	print("Anda sudah di dashboard") 
		    
	    page.update()   
	        


	return Column(
		controls=[
			Text("you login page",size=30,weight="bold"),
			nametxt,
			passwordtxt,
			ElevatedButton("login Now",
				bgcolor="green",color="white",
				on_click=loginprocess
				),
			ElevatedButton("masuk",
				bgcolor="green",color="white",
				on_click=lambda e:page.go("/dashboard")
				),
			Row([
			TextButton("no have account,register",
				on_click=lambda e:page.go("/register")
				)
				],alignment="center")
			]
		)
