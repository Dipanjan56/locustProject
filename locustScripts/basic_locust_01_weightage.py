from locust import HttpUser, task, between


class MyWebUser(HttpUser):
    wait_time = between(1, 2)
    weight = 3 # will increase the probability of executing this task 3 times more than the other tasks
    host = "http://newtours.demoaut.com/"

    @task
    def login_URL(self):
        print("I am logging into web URL")


class MyMobileUser(HttpUser):
    wait_time = between(1, 2)
    weight = 1
    host = "http://newtours.demoaut.com/"

    @task
    def login_URL(self):
        print("I am logging into mobile URL")
