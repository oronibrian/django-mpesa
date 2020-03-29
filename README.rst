============
Django mpesa
============

Django mpesa is a simple re-usable  of Django's application for mpesa STK push payment, that can be easily intergrated to any django powered site.

Quick start
-----------

1. Add "myblog" to INSTALLED_APPS:

  INSTALLED_APPS = {

    'mpesaApp'

  }

2. Include the myblog URLconf in urls.py:
    path('payment/', include('mpesaApp.urls')),

3. Run `python manage.py migrate` to create DJango mpesa's models.

4. Run the development server and access http://127.0.0.1:8000/admin/ to
    manage setup and add all your payment details.

5. Access http://127.0.0.1:8000/payment/ to view a json result of payment.