# Pizza Restaurant Management System

## Introduction
This project manages a pizza restaurant that receives orders for pizzas with different toppings. The orders are processed through a pipeline of dough chef, topping chef, oven, and waiter to finally be served to the customers. The system logs the start and end time for each step of the pipeline and saves a report to a MongoDB that runs in a Docker container.

## Requirements
- Docker
- Python 3.x
- pymongo

## Installation
1. Clone the repository
2. Build the Docker image
    $ cd pizza-restaurant-management-system
    $ docker build -t pizza-restaurant-management-system .
3. Start the Docker container
4. $ docker run -p 27017:27017 -d --name pizza-restaurant-management-system pizza-restaurant-management-system

## Usage
1. Open a new terminal window
2. Start the MongoDB client
    $ docker exec -it pizza-restaurant-management-system mongo
3. Run the main program
    $ python main.py


   
