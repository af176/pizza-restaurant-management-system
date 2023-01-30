import time
from typing import List
from pymongo import MongoClient

orders = [{"id": 1, "dough_time": 7, "toppings": [{"id": 1, "time": 4}, {"id": 2, "time": 4}, ],
           "cook_time": 10,
           "serve_time": 5,
           },
          {
              "id": 2,
              "dough_time": 7,
              "toppings": [
                  {"id": 3, "time": 4},
                  {"id": 4, "time": 4},
              ],
              "cook_time": 10,
              "serve_time": 5,
          }
          ]


def manage_pizza_restaurant(orders: List[dict]):
    start_time = time.time()
    client = MongoClient("mongodb://localhost:27017/")
    db = client["pizza_restaurant"]
    reports_collection = db["reports"]

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
