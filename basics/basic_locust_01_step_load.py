
import math
from locust import HttpUser, TaskSet, task, constant
from locust import LoadTestShape


class UserTasks(TaskSet):
    @task
    def get_root(self):
        self.client.get("/")


class WebsiteUser(HttpUser):
    wait_time = constant(0.5)
    tasks = [UserTasks]


class StepLoadShape(LoadTestShape):
    """
    A step load shape
    Keyword arguments:
        step_time -- Time between steps
        step_load -- User increase amount at each step
        spawn_rate -- Users to stop/start per second at every step
        time_limit -- Time limit in seconds
    """

    step_time = 30
    step_load = 10
    spawn_rate = 10
    time_limit = 600

    def tick(self):
        run_time = self.get_run_time()

        if run_time > self.time_limit:
            return None

        current_step = math.floor(run_time / self.step_time) + 1
        return (current_step * self.step_load, self.spawn_rate)


# Note:

# Locust default model:
# Liner Model : user ramps up linearly means if we give -u 10 -r 2 then for every second two user will be spawned
# and executes the script and after 5 sec all teh 10 users get spawned

# Step Load Model : user does not get spawned linearly, user count gets ramped up after a certain time
# lets say, 2 user will be spawned and will execute for 4 sec and then another 2 user will be spawned and execute for 2 sec and so on
# but the total number of users after they all got ramped up is same as the linear model
# for this we have to give this parameter -> --step-load [deprecated in locust 1.3]
# Terminal -> locust -f basics/basic_locust_01.py -u 4 -r 1 -t 10s --step-load [deprecated in locust 1.3]
# Latest: for this we need to use LoadTestShapeClass : https://docs.locust.io/en/stable/generating-custom-load-shape.html
