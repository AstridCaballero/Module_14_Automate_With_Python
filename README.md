![img.png](img.png)
## Module 14 - Automation with Python

### Chapter 15 - Website Monitoring 3: Restart Application and Reboot Server

Notes from chapter 15 were taken in notes app in freestyle, and it includes a mix of screenshots of TWN bootcamp as well as
screenshots of my own work on the terminal and browser. I used AI and I have added that research to my notes.

Notes have been exported into pdf format to be able to get the screenshots (avoiding retaking screenshots which is time-consuming)

You can find original notes for
- Chapter 15 [here](Module%2014%20-%20chapter%2015_notes.pdf).

### Description Module 14 - chapter 13  to 15: Website Monitoring and recovery
This DEMO was developed over three chapters and here are their correspondent links:
https://github.com/AstridCaballero/Module_14_Automate_With_Python/tree/Module_14/Automate_Python_chapter-13
https://github.com/AstridCaballero/Module_14_Automate_With_Python/tree/Module_14/Automate_Python_chapter-14 
https://github.com/AstridCaballero/Module_14_Automate_With_Python/tree/Module_14/Automate_Python_chapter-15


We wrote a python script to monitor a website app (nginx) to check if the app and the server running it are responsive. 

The python script makes an http request to the app if it gets nothing back then the server is in trouble. If it gets a response back and the status of that response is not 200 then the app is in trouble.

In both cases we notify somebody (usually ‘support’ team) via email so they are aware and we restart the app and/or the server accordingly.

### Chapter 13

- Create a Linode server
    - Ssh into the server
        - Install docker for ubuntu
        - Start a nginx conatiner on port 8080 and open port 8080 via the server’s firewall
- Create and write a Python automation script -> call it ‘monitor-website.py’ 
    - create a function called ‘monitor_application’ in there:
        - Install library ‘requests’ -> so python can make http request to the website app
        - Import ‘request’ library into the python script
        - Use .get() call to reach the app and store the http response from it in a var called ‘response’
        - Check the attribute ‘status_code’ from the ‘response’ object
            - If ‘status_code’ equals 200 -> we print that all is good
            - Else -> service is down, print that app is down and notify via email
               ### - Chapter 14
                - Notify via email to somebody that service is down (usually ‘support’ team) for that
                    - Import library ‘smtplib’ (it is python in-built library)
                    - Write logic to send an email inside a ‘with’ statement as we will connect to an email provider and this is a resource we can’t control -> if there is an issue on the email provider’s side then ‘with’ deals with the issue and cleans up the resources for us (alternative to try/finally). Inside the ‘with’ statement:
                        - Create a var called ‘smtp’ that opens a plain-text TCP connection with the email provider so we need to pass:
                            - Host -> name of email provider, in our case is gmail
                            - Port -> port of the email provider for gmail	-> smtplib.SMTP("smtp.gmail.com", 587)
                        - Upgrade the plain-text TCP connection to a TLS-encryted which is secure using .starttls() -> from now on the code we add inside the ‘with’ statement is encrypted instead of plain-text
                        - Identify python with the email provider via ehlo()
                        - Login to the email account via .login() and pass two arguments:
                            - Email address -> I used Pycharm editor to create an env var and store this value there. Then using the OS library (which I imported) I fetch the env var and store it in global var called ‘EMAIL_ADDRESS’
                            - Password -> this one is a password created by the email provider granted the account has a MFA. I created one and I used it here. -> I used Pycharm editor to create an env var and store this value there. Then using the OS library I fetch the env var and store it in global var called ‘EMAIL_PASSWORD’	-> smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                        - Create message -> contains email subject and email message, I call it ‘message’
                        - Send message using .sendmail() and passing three arguments to it:
                            - Sender email -> ‘EMAIL_ADDRESS’
                            - Recipient email -> ‘EMAIL_ADDRESS’
                            - Message -> ‘message’
        - Take care of edge cases
            - Wrap the logic in a try/except block -> If .get() fails then it throws an exception and we want to catch it (defensive programming). 
                - Try -> will call .get() and validate the response with if/else statements
                - Except -> will catch the exception and also
                    - Send a notification via email following the same process as we did under the ‘else’ statement’. 
    - Refactor
	    To avoid code duplication we refactor the code and extract the logic of sending an email from the ‘else’ statement and 
            create a new function called ‘send_notification’ that takes one parameter ‘mail_msg’. 
				We use this function in:
                    - the ‘else’ statement and 
                    - here inside the except block.
    - ### Chapter 15
    - Write logic to restart container when there is a response and the status_code is not 200 in a function called ‘restart_container’ 
        - Python needs to ssh into the Linode server and for that it needs library ‘Paramiko’
            - Install library Paramiko
            - Import library paramiko
        - Create an ssh client using paramiko library and call it ‘ssh’
        - Add host key to the ‘ssh’ client
        - Make the ssh connection using .connect() and pass same arguments as we do when we ssh manually
            - Linode server’s IP address
            - Server’s username
            - File with credentials to auth, in my case is id_ed25519
            - Execute a command to start the docker container that already exists in the Linode server (I start it manually at the beginning of the DEMO) so I have its ID and for this
            DEMO we hardcode it. The command returns a tuple of three objects stdin, stdout, stderr so we stored them in variables to see their contents -> stdin, stdout, stderr = ssh.exec_command("docker start 52527a5428e8")
            - Print stdout
            - Close the ssh connection
    - Write logic to reboot server when there is not a response in a function called ‘estart_server_and_container’
        - Python needs to connect to Linode account to create a Linode client, for this we use a library called ‘linode-api4’
            - Install ‘linode-api4’
            - Import ‘‘linode_api4’
        - Create Linode client and pass a Linode token as argument so python can auth with linode
            - Create linode token in linode console
            - Use Pycharm editor to create an environment variable storing the linode token
        - Connect to a resource in this case the Linode server using .load() and pass:
            - Object type -> Instance (a server/droplet is of type instance)
            - instance ID
        - Reboot the server -> it is a OS restart, disk is untouched using reboot()
        - Run the nginx container -> the rebooted server has the container image as the disk is untouched but it is not running. To do this we need:
            - Make sure the server is up and running by writing the logic to restart the container inside a while loop that checks if the server has ‘status’ equal to ‘running’ if that is the case then we can proceed. Once the ‘status’ is ‘runninng’ then
                - Wait for extra 5 seconds using the library ‘time’ and the function sleep() to make sure the server is ready -> I still had timing issues and this fixed it
                - Call the restart_container() function
                - Break from the while loop -> otherwise it will run for ever.
    - Add a scheduler using library ‘schedule’ so python can monitor the website regularly, for that 
        - Create a to do list that has the information of the jobs that need to be run, in our case we want to call monitor_application() -> schedule.every(5).minutes.do(monitor_application)
        - Check todo list to see if there is a pending job to run -> schedule.run_pending()
            - It needs to be wrapped by a while loop so python can do the monitoring for ever.

### Improvement	
- Add time.sleep(1) inside the while loop that calls schedule.run_pending() so we don’t call it millions of times per second hitting the CPU core at 100% unnecessarily. Instead we monitor the app once per second.


I learnt how to send email notifications, how to ssh into a server, how to reboot a Linode server and restart an app using python and the libraries that I need. I also learnt how schedulers work.
