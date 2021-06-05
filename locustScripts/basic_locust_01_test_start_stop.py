from locust import HttpUser, task, between, events


# It will execute only once before all the users gets spawned[before on_start as well] [kind of before suite]
# this has to be written in module level i.e outside any class
@events.test_start.add_listener
def script_start(**kwargs):
    print("I am connecting to DB")


# It will execute only once after all the users gets de-spawned[after on_stop as well] [kind of after suite]
# this has to be written in module level i.e outside any class
@events.test_stop.add_listener
def script_stop(**kwargs):
    print("I am disconnecting from DB")


class MyUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://demo.guru99.com/test/newtours/"

    # it will execute only once per user before the execution of all repetitive tasks
    # this has to be written inside any class
    def on_start(self):
        print("I am logging into URL")

    @task
    def doing_work(self):
        print("I am doing my work")

    # it will execute only once per user after the execution of all repetitive tasks
    # this has to be written inside any class
    def on_stop(self):
        print("I am logging out")

# Terminal -> locust -f locustScripts/basic_locust_01_test_start_stop.py -u 2 -r 1 -t 5s --headless --only-summary
