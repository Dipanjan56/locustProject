from locust import User, task, between


class MyUser(User):
    wait_time = between(1, 2)

    # this is taskDecorator with weightage i.e. probability of picking the task by user
    @task(2)
    def add_cart(self):
        print("I am adding to cart")

    @task(4)
    def view_product(self):
        print("I am viewing the product")


# Terminal -> locust -f locustScripts/basic_locust_01_taskDecorator_weight.py -u 1 -r 1 -t 15s --headless --only-summary