from locust import User, task, between


def add_cart(userClass):
    print("I am adding to cart")


def view_product(userClass):
    print("I am viewing the product")


class MyUser(User):
    wait_time = between(1, 2)

    # task Attributes :

    # defining tasks as list
    # tasks = [add_cart, view_product]

    # defining tasks as dictionary, giving them the weightage here only
    tasks = {add_cart: 6, view_product: 3}

# Terminal -> locust -f locustScripts/basic_locust_01_taskAttribute_weight.py -u 1 -r 1 -t 15s --headless --only-summary
