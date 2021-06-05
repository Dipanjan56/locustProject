from locust import HttpUser, task, between, SequentialTaskSet


class UserBehavior(SequentialTaskSet):
    login_data = {"action": "process",
                  "userName": "qamile1@gmail.com",
                  "password": "qamile",
                  "login.x": "41",
                  "login.y": "12"
                  }

    @task
    def launch_URL(self):
        with self.client.get("/mercurycruise.php", name="launch_mercury", catch_response=True) as resp1:
            print("resp1" + resp1.text)
            if "Mercury Tours" in resp1:
                resp1.success()
            else:
                resp1.failure("failed to launch URL")

    @task
    def login(self, login_data=login_data):
        with self.client.post("/login.php", data=login_data, name="login_mercury") as resp2:
            print("resp2" + resp2.text)
            if "Find a Flight" in resp2:
                resp2.success("failed to login")
            else:
                resp2.failure()


class MyUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://newtours.demoaut.com"

    tasks = [UserBehavior]

# Terminal -> locust -f locustScripts/basic_locust_01_http_post_catchResponse.py -u 1 -r 1 --headless -t10s
