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
        resp_get=self.client.get("/mercurycruise.php", name="launch_mercury")
        print(resp_get.text)

    @task
    def login(self, login_data=login_data):
        resp_post=self.client.post("/login.php", data=login_data, name="login_mercury")
        print(resp_post.text)


class MyUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://newtours.demoaut.com"

    tasks = [UserBehavior]

# Terminal -> locust -f locustScripts/basic_locust_01_http_post_assignment.py  -u 1 -r 1
