API Students
========================================

About this Repository
-----------------

This is an example of an API created in  Rest Framework
You can use a software like a PostMan or Insominia or use the Rest Framework page to see how the API Works: 

Look the Rest Page: 
<img src="/docs/img/rest_page.png" alt="REST Page"/>
   
The API Returns, for example, in GET Method: 

<img src="/docs/img/get_method.png" alt="GET Method"/>

Table of Contents
-----------------

Getting Started
---------------

These instructions will get you a copy of the project up and running on
your local machine.


Installing
----------
You'll need on version of Python, installed on your device, you can get one <a href="https://www.python.org/downloads/">Here.</a>


Get the package from source:
~~~~~~~~~~~

Use Git to get the latest development version from our git
repository:

.. code:: bash

    git clone https://github.com/lhggomes/API.git

You'll need a Git client. The command line program is fine, but if you
prefer graphical interface, you can install e.g. git-gui on Linux.

~~~~~~~~~~~

Then install all needed packages: 

~~~~~~~~~~~
pip install -r requirements.txt
~~~~~~~~~~~
Create a SuperUser in Database, doing: 
~~~~~~~~~~~
python manage.py createsuperuser 
~~~~~~~~~~~

Run all migrations: 

~~~~~~~~~~~
python manage.py makemigrations 
python manage.py migrate
~~~~~~~~~~~



Built With
----------

- Django
- Python 3.8
- Rest Framework

Versioning
----------

We use `Git<http:www.github.com/lhhgomes>`__ for versioning. For the
versions available, see the `tags on this
repository <https://github.com/lhggomes/field-hospital.git>`__.

Authors
-------

-  **Lucas Henrique Silva Gomes** -

License
-------

This is free and unencumbered public domain software. For more
information, see http://unlicense.org/ or the accompanying
`UNLICENSE <UNLICENSE>`__ file.
