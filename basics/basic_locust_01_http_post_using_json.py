from locust import HttpUser, SequentialTaskSet, task, between
import uuid
import json


class UserBehaviour(SequentialTaskSet):

    def __init__(self, parent):
        super().__init__(parent)
        self.token = ""
        self.randomid = ""
        self.request_id = ""

    def on_start(self):
        self.token = "984970da979ab78943c0d1c74317eb1e9bd5ba7d"
        # python function for generating random uuid : uuid.uuid4
        self.randomid = str(uuid.uuid4())
        resp = self.client.post("/rest/v1/projects", json={"name": "HelloProj2"},
                                headers={
                                    "Content-Type": "application/json",
                                    "X-Request-Id": self.randomid,
                                    "Authorization": "Bearer " + self.token
                                })
        json_response_dict = resp.json()
        print(json_response_dict)
        self.request_id = json_response_dict["id"]

    @task()
    def create_task(self):
        print("I am in task")
        print("request_id" + str(self.request_id))


class WebsiteUser(HttpUser):
    tasks = [UserBehaviour]
    host = "https://api.todoist.com"
    wait_time = between(5, 10)

# Terminal -> locust -f basics/basic_locust_01_http_post_using_json.py --headless --run-time=10 --logfile=logfiles/log.txt
