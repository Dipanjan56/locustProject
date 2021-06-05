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
        resp=self.client.get("/index.php", name="launch_newtours")
        print(resp.text)
        print(resp.status_code)
        print(resp.headers)

    @task
    def login(self, login_data=login_data):
        resp=self.client.post("/login.php", data=login_data, name="login_newtours")
        print(resp.text)
        print(resp.status_code)
        print(resp.headers)


class MyUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://demo.guru99.com/test/newtours"

    tasks = [UserBehavior]

# Terminal -> locust -f locustScripts/basic_locust_01_http_post_assignment.py  -u 1 -r 1
