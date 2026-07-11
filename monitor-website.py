import requests
import smtplib
import os
import paramiko

EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

def send_notification(email_msg):
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = f"Subject: SITE DOWN\n{email_msg}"
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)


try:
    response = requests.get("http://172-236-15-151.ip.linodeusercontent.com:8080/")
    if response.status_code == 200:
        print("Application is running successfully!")
    else:
        print("Application Down. Fix it!")
        # send notification email to support
        msg = f"Application returned {response.status_code}"
        send_notification(msg)

        # restart the application
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect("172.236.15.151", username="root", key_filename="/Users/astrid/.ssh/id_ed25519")
        stdin, stdout, stderr = ssh.exec_command("docker start 52527a5428e8")
        print(stdout.readlines())
        ssh.close()
        print("Application restarted")
        
except Exception as ex:
    print(f"Connection error happended: {ex}")
    # send notification email to support
    msg = "Application not accessible at all."
    send_notification(msg)
