### MPESA Online Payment STK Push Django App


This is an opensource mpesa django wrapper app for web push notification payment.
This only supports stk push payment at the moment

Built by: https://www.techtenant.co.ke

This is a safaricom (Daraja) wrapper

![alt text][logo]

[logo]: https://developer.safaricom.co.ke/sites/all/themes/apigee_responsive_custom/logo.png "Daraja"

For Django 

(Download The app and use in your djangoProject)


...or clone the project from github.



#### Instruction and Usage
The following are the instruction for theusage of the app.

##### Libraries

Install the following libraries using pip install 


```pip install -r requirements.txt

```
Add 'rest_framework' and 'mpesaApp' to your INSTALLED_APPS setting.



## Creating Migrations
With the app installed, the first thing you need to do is create a migration for it. You can do this with the following command:

```python
python3 manage.py makemigrations mpesaApp

python3 manage.py migrate mpesaApp

```
Go to the admin panel and fill all the details from daraja sandbox or live details.



## Compatibility

* python 3 and Django 2.1 and above


## License

Copyright is free for personal and commercial use. 

Copyright is licensed under a [Open Source Initiative - BSD License][] license.




* **Author**: [Oroni Brian][]
* **Source Code**: [Github][]

	
[Oroni Brian]: https://github.com/oronibrian
[Github]: https://github.com/oronibrian/django-mpesa.git
[Open Source Initiative - BSD License]: http://opensource.org/licenses/bsd-license.php