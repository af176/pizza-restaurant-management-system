import time
import threading


class DoughChef(threading.Thread):
    def __init__(self, orders, lock):
        threading.Thread.__init__(self)
        self.orders = orders
        self.lock = lock

    def run(self):
        while True:
            with self.lock:
                if len(self.orders) == 0:
                    break
                order = self.orders.pop(0)
                order['dough_time'] = time.time()
                print(f"Dough chef started working on order {order['id']} at {order['dough_time']}")
                time.sleep(7)
                order['dough_end'] = time.time()
                print(f"Dough chef finished order {order['id']} at {order['dough_end']}")


class ToppingChef(threading.Thread):
    def __init__(self, orders, lock):
        threading.Thread.__init__(self)
        self.orders = orders
        self.lock = lock

    def run(self):
        while True:
            with self.lock:
                if len(self.orders) == 0:
                    break
                order = self.orders[0]
                if 'dough_end' not in order:
                    continue
                order['topping_time'] = time.time()
                print(f"Topping chef started working on order {order['id']} at {order['topping_time']}")
                time.sleep(4 * len(order['toppings']))
                order['topping_end'] = time.time()
                print(f"Topping chef finished order {order['id']} at {order['topping_end']}")
                self.orders.pop(0)


class Oven(threading.Thread):
    def __init__(self, orders, lock):
        threading.Thread.__init__(self)
        self.orders = orders
        self.lock = lock

    def run(self):
        while True:
            with self.lock:
                if len(self.orders) == 0:
                    break
                order = self.orders[0]
                if 'topping_end' not in order:
                    continue
                order['oven_time'] = time.time()
                print(f"Oven started cooking order {order['id']} at {order['oven_time']}")
                time.sleep(10)
                order['oven_end'] = time.time()
                print(f"Oven finished cooking order {order['id']} at {order['oven_end']}")
                self.orders.pop(0)


class Waiter(threading.Thread):
    def __init__(self, orders, lock):
        threading.Thread.__init__(self)
        self.orders = orders
        self.lock = lock

    def run(self):
        while True:
            with self.lock:
                if len(self.orders) == 0:
                    break
                order = self.orders[0]
                if 'oven_end' not in order:
                    continue
                order['waiter_time']
