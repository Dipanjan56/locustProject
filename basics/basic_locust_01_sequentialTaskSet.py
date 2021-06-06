from locust import User, task, between, SequentialTaskSet


# SequentialTaskSet will execute all the tasks written sequentially
class UserBehaviour(SequentialTaskSet):

    def on_start(self):
        print("I will login")

    @task
    def flight_finder(self):
        print("I will find flight by entering criteria")

    @task
    def select_flight(self):
        print("select flight")

    @task
    def book_flight(self):
        print("book flight")

    def on_stop(self):
        print("I will log out")


class MyUser(User):
    wait_time = between(1, 2)

    # defining another task class as list
    tasks = [UserBehaviour]

# Terminal -> locust -f basics/basic_locust_01_sequentialTaskSet.py -u 1 -r 1 -t 10s --headless --only-summary
