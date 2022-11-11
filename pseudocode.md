# Backend Bistro Pseudocode

For this project, we will be creating a simple Python/Django API to serve as the backend for our previously created React Restaurant frontend app. 


Create the models, views, and database for an API that provides READ operations for a user’s restaurant items in a PostgresQL database.

---

## Requirements

1. Store the following data in your PostgreSQL database and implement models for READ only operations for the following data:
    - Menu Items
        - Title
        - Description
        - Price
        - Spicy Level
        - FK to Category
        - FK to Cuisine
    - Category (Appetizer, Dessert, Main Dish, etc.)
    - Cuisine (American, Thai, etc.)

<br/>

1. Create views to send JSON data back to a GET request for a list of all menu items with the category and cuisine labels nested in the data.

1. Create routes to use the views created in the previous step.
            
1. Change the URL in the React Restaurant Code to the Gitpod url of your running backend code only. (NOTE: We shouldn’t be writing any React code for basic requirements)

- - - 

## Database Table Structure

![database-tables](./pseudo_img/dbdiagram.png)
##### items table many to one relationship to cuisine and category table

Django python framework will allow us to create models/classes that will handle and write sql to our databases. Using Postgres for our DB with python library psycopg2. Sql will be generated "handwaved" using Django.

Djando uses Models/ python classes that allow us to write db tables using python without writing out any sql. 

After a table(s) is generated/ migrated into our Postgres db.

We will use Django's views file to write how we want to display/ or send data when it is called.

A build in feature of Django is we can added data to our DB using a pre-built front-end that comes with admin privileges. Ex; We can set whats called a superuser with a username and password. Once a superuser is setup a user can then login as an admin and preform (C.R.U.D) on our DB.

---

## Requirement 1.

### Table item

Using the image provided. Our db table structure will end up looking like this.  A `item` will represent a dish/ food item, each item will need an `id` that increments every time an new item is added. `title` will be a string/ varchar data type. Same for `description`. `price` will be a float or decimal value to allow for accurate pricing of an item/dish.  `spice_level` is numeric ranging from a value of 1-5 in spiciness. 

`cuisine_id` will be a foreign key that is linked to *cuisine table's id*

`category_id` will be a foreign key that is linked to *category table's id*

Django automatically adds '_id' to any foreign key that is added to a table's column.

---

### Table cuisine

Contains a `id` incremented, and a `title` text/ varchar/ string

---

### Table category

Contains a `id` incremented, and a `title` text/ varchar/ string

---
### Relationship status

- `item` many to one `cuisine`
- `item` many to one `category`

---

## Models

<br/>
Some model classes will need to be created in order to create the tables we need in our database that contain the right columns and data types.

```
from django.db import models
```

### cuisine
```
class cuisine(models.Model):
    title = models.CharField(max_length=30)
```

### category
```
class category(models.Model):
    title = models.CharField(max_length=30)
```

### items
```
class item(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    spice_level = models.IntegerField()
    cuisine = models.ForeignKey(cuisine,on_delete=models.PROTECT)
    category = models.ForeignKey(category,on_delete=models.PROTECT)

```

---









