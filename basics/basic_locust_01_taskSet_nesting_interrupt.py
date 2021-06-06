from locust import User, task, between, TaskSet


# default behaviour of nested TaskSet Class is: user will pick any one of the nested class randomly
# and user will never be able to exit out of that class, so rest of the classes will never get executed
# To solve this kind of problem we need to use self.interrupt
class UserBehaviour(TaskSet):

    @task(2)
    class Cart_Module(TaskSet):
        @task(4)
        def add_cart(self):
            print("I am adding to cart")

        @task(2)
        def delete_cart(self):
            print("I am deleting from cart")

        @task(1)
        def stop(self):
            print("I am stopping")
            self.interrupt()

    @task(4)
    class Product_Module(TaskSet):
        @task(4)
        def view_product(self):
            print("I am viewing the product")

        @task(2)
        def add_product(self):
            print("I am adding the product")

        @task(1)
        def stop(self):
            print("I am stopping")
            self.interrupt()


class MyUser(User):
    wait_time = between(1, 2)

    # defining another task class as list
    tasks = [UserBehaviour]

# Terminal -> locust -f basics/basic_locust_01_taskSet_nesting_interrupt.py -u 1 -r 1 -t 10s --headless --only-summary
