"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq9bvdvk4rjsvapv60-a.oregon-postgres.render.com",
        database="todo_l8vg",
        user="root",
        password="xAS55MDI8AQHqkkkOfPOtB6JCryMR914")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
