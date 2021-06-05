from locust import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://demo.guru99.com/test/newtours"
    login_data = {"action": "process",
                  "userName": "qamile1@gmail.com",
                  "password": "qamile",
                  "login.x": "41",
                  "login.y": "12"
                  }

    @task
    def launch_URL(self):
        self.client.get("/index.php", name="launch_newtours")

    @task
    def login(self, login_data=login_data):
        self.client.post("/login.php", data=login_data, name="login_newtours")

# Terminal -> locust -f locustScripts/basic_locust_01_http_post.py
