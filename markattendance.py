from selenium import webdriver
from getpass import getpass
import time
import smtplib
from datetime import datetime


def send_mail(alert_level=0):
	server = smtplib.SMTP("smtp.gmail.com",587)
	server.ehlo()
	server.starttls()
	server.login("am438@snu.edu.in",pd)
	msg="\r\n".join([
			"From: am438@snu.edu.in",
			"To: am438@snu.edu.in",
			"Subject: Attendance initiated",
			"",
			"Attendance"
				])

	server.sendmail("am438@snu.edu.in","am438@snu.edu.in",msg)
	server.quit()


user=input("Enter your Id")
pwd=getpass("Enter your password")
pd=getpass("Your email password:")


driver=webdriver.PhantomJS(executable_path="C:\Program Files\phantomjs.exe")

driver.get("https://markattendance.webapps.snu.edu.in/public/application/login/login")

def login():

	username=driver.find_element_by_id("login_user_name")
	password=driver.find_element_by_id("login_password")

	username.send_keys(user)
	password.send_keys(pwd)

	arrow= driver.find_element_by_class_name("btn")
	arrow.click()


time.sleep(5)

while(True):
	print(" %s Logging in..." %(datetime.now().time()))

	login()
	time.sleep(3)
	
	try:
	
		driver.find_element_by_class_name("btn-success").click()

	
		time.sleep(5)
	
		print("Attendance has been initiated.")

		try:

			send_mail()
			time.sleep(3)

		
			print("A mail has been sent confirming marked attendance.")
			break

		except:

			print("Error:Unable to send mail.")
			break

	except:
		print("Attendance not initiated yet")
	
		print(" %s Logging Out..." %(datetime.now().time()))
		
		driver.find_element_by_class_name("btn-danger").click()
	
		print("Sleeping for 15 secs...")

		time.sleep(15)



driver.quit()



















