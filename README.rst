=====================
Django Pickled Model
=====================

Django pickled model provides you a model with dynamic data types.
a field can store any value in any type.

You can store Integer, Boolean, String and any other data type just using a single field.
so there is no need to define extra fields and make your model dirty.


Quick start
-----------

1. Add "pickles" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'pickles',
    ]

2. Include the pickles URLconf in your project urls.py like this::

    path('pickles/', include('pickles.api.urls')),

3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create dynamic-type data (you'll need the Admin app enabled).

5. You can get a list of your pickles by calling the API URL.

How it works
------------
Admin panel is where you can create your objects.
currently supported data types are:

- STRING
- INTEGER
- FLOAT
- LIST
- DICTIONARY
- BOOLEAN

Now let's describe each field in admin creation form.

**name**

the key name for your value. considering the schema {name: value}, the name you enter will be replaced.

**value**

value is the field that you can enter any data based on the **value data type** that you choose.

- for **STR** the value will be like: "my string value"
- for **INTEGER** the value will be like: 1
- for **FLOAT** the value will be like: 1.5
- for **LIST** the value will be like: [1,2,3]
- for **DICTIONARY** the value will be like: {"key": "value"}
- for **BOOLEAN** the value will be like: True


**value data type**

this is the field that you must choose your value data type.


