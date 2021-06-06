from locust import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://demo.guru99.com/test/newtours/"

    def on_start(self):
        print("I am logging into URL")

    @task
    def doing_work(self):
        print("I am doing my work")

    def on_stop(self):
        print("I am logging out")

# Terminal -> locust -f locustScripts/Basics/basic_locust_01_on_start_stop.py -u 2 -r 1 -t 5s --headless --only-summary
