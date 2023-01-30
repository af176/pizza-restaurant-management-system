import os
import time
from typing import List
from pymongo import MongoClient

from conf import orders
from dotenv import load_dotenv


def manage_pizza_restaurant(orders: List[dict]):
    load_dotenv()

    DB_URL = os.getenv("DB_URL", "mongodb://localhost:27017/")
    DB_NAME = os.getenv("DB_NAME", "pizza_restaurant")
    REPORT_COLLECTION = os.getenv("REPORT_COLLECTION", "reports")

    start_time = time.time()
    client = MongoClient(DB_URL)
    db = client[(DB_NAME)]
    reports_collection = db[REPORT_COLLECTION]

    for order in orders:
        order_start_time = time.time()

        # Dough preparation
        dough_start_time = time.time()
        print(f"Order {order['id']} dough preparation started at time {dough_start_time - start_time}")
        time.sleep(order['dough_time'])
        dough_end_time = time.time()
        print(f"Order {order['id']} dough preparation finished at time {dough_end_time - start_time}")

        # Topping preparation
        topping_start_time = time.time()
        print(f"Order {order['id']} topping preparation started at time {topping_start_time - start_time}")
        time.sleep(sum([topping["time"] for topping in order["toppings"]]))
        topping_end_time = time.time()
        print(f"Order {order['id']} topping preparation finished at time {topping_end_time - start_time}")

        # Cooking
        cooking_start_time = time.time()
        print(f"Order {order['id']} cooking started at time {cooking_start_time - start_time}")
        time.sleep(order['cook_time'])
        cooking_end_time = time.time()
        print(f"Order {order['id']} cooking finished at time {cooking_end_time - start_time}")

        # Serving
        serving_start_time = time.time()
        print(f"Order {order['id']} serving started at time {serving_start_time - start_time}")
        time.sleep(order['serve_time'])
        serving_end_time = time.time()
        print(f"Order {order['id']} serving finished at time {serving_end_time - start_time}")

        order_end_time = time.time()
        order_prep_time = order_end_time - order_start_time

        # Save report to MongoDB
        report = {
            "order_id": order['id'],
            "prep_time": order_prep_time,
        }
        reports_collection.insert_one(report)

    total_prep_time = time.time() - start_time
    print(f"Total preparation time: {total_prep_time} seconds")

    # Fetch reports from MongoDB
    reports = list(reports_collection.find({}))
    for report in reports:
        print(f"Order {report['order_id']} preparation time: {report['prep_time']} seconds")


if __name__ == '__main__':
    manage_pizza_restaurant(orders)

