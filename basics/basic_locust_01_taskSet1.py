from locust import User, task, between, TaskSet


class UserBehaviour(TaskSet):

    @task
    def add_cart(self):
        print("I am adding to cart")

    @task
    def view_product(self):
        print("I am viewing the product")


class MyUser(User):
    wait_time = between(1, 2)

    # defining another task class as list
    tasks = [UserBehaviour]

# Terminal -> locust -f basics/basic_locust_01_taskSet1.py -u 1 -r 1 -t 15s --headless --only-summary
