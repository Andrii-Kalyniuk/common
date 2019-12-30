# Simple project with authorization
This application works according to such algorithm:
To see the main page you must be logged in. For this
you must send post request on auth url with arguments 
login and password, they are both required. If you do 
everything right your user will be added to users dict, 
which means that you are registered. After this step you 
can not yet view the main page content, for this you have 
to send post request on login url with arguments login and
password, they are both required. Finally, I can 
congratulate and inform you that you can already view 
the content of the main page, but hurry up session will 
expire in 20 minutes and you will be logged out from app. 
You can also logout by yourself just send get request on logout url.
## Steps to see how it works

* Do POST http://127.0.0.1:5000/auth?login=Nick&password=12345
* DO POST http://127.0.0.1:5000/login?login=Nick&password=12345
* DO GET http://127.0.0.1:5000/main