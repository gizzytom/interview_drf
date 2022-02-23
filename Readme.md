### ATM API

interview task

####Requirements:
`Python 3.8.0`

####Create your own virtual environment

```bash
python3 -m venv venv

```

####Install your requirements
`pip install -r requirements.txt`
or
`pip install django==3.2.10`
#
`pip install djangorestframework==3.11.1`Provides utilities on top of Django to create REST API's
#
`pip install drf-spectacular====0.21.2` For creating Documentation of our API

#### Make your migrations

In your terminal:

```
python manage.py makemigrations
python manage.py migrate
```

####Create a new superuser
`python manage.py createsuperuser`

you can skip email address and enter a simple password like '1234'

####Final checks
Start the development server and ensure everything is running without errors.
`python manage.py runserver`

####
create a few customers in django admin , go to 
http://127.0.0.1:8000/admin/ and enter your credentials, 
in "Accounts"
create a few test customers, make a note with the details[name,cardnumber,pin,balance]
you are the "bank employee" and can view, create, delete and change customer's details

####
acess swager API GUI to test the app
http://localhost:8000/docs/#/

example:
to "withdraw" the money from the card click on
POST /api/withdraw/
enter the number of the card , pin and the amount you want to withdraw
{
  "cardNumber": "3",
  "pin": "7777",
  "amount": "8"
}click on the blue button "execute"
scroll down for server response code and response body

