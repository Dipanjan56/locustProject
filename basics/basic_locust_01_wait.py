from locust import HttpUser, task, between, constant, constant_pacing
from datetime import datetime


class MyUser(HttpUser):
    # # 'between' will wait randomly between 1 to 3 sec
    # wait_time = between(1, 3)

    # # 'constant' will wait fro 3 sec every time
    # wait_time = constant(3)

    # 'constant_pacing' wait time is adjusted according to the task time
    # i.e. if user take some time then it will deduct hat time from constant pacing time and wait for the remaining time
    # formula : constant_pacing_time = task1_time + wait_time = task2_time+wait_time
    # hence, wait_time = (constant_pacing_time-task1time) or (constant_pacing_time-task2time)
    # now lets say, user take more than constant_pacing time i.e task_time > constant_pacing_time
    # then wait_time = 0, i.e. user won't wait for anytime and immediately starts the next task
    wait_time = constant_pacing(5)
    host = "http://demo.guru99.com/test/newtours/"

    @task
    def login_URL(self):
        print(datetime.now())
