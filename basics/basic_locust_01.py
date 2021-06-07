from locust import User, task, between
import locust.stats

# if we do this then we dont need to worry in command line for the interval part
locust.stats.CSV_STATS_INTERVAL_SEC = 2


class MyUser(User):
    wait_time = between(1, 2)

    @task
    def login_URL(self):
        print("I am logging into URL")

# Terminal -> locust -f basics/basic_locust_01.py
# Advanded:
# Terminal -> locust -f basics/basic_locust_01.py -u 5 -r 1 -t 10s --headless --logfile logfiles/mylog.log --loglevel DEBUG
# u = number of users, r = spawn rate, t = runtime, --headless = headless mode,
# u = 5, r = 1 -> means every 1 sec, one user will be spawned and after 5 secs all the 5 users will be spawned : Linear Model
# t = 10s -> this script will run for 10 sec and will end after that
# logfile = file path -> to store log data in a file
# loglevel = DEBUG ->  it wont print any stats -> it will print only the error message or customized message
# headless = it will run without an UI


# Terminal -> locust -f basics/basic_locust_01_http_host.py -u 1 -r 1 --headless --only-summary
# only-summary = irrelevant request data will not be printed, only the print statements will be printed


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


# If we want to download data when we are running in headless mode ->
# Terminal -> locust -f basics/basic_locust_01.py -u 5 -r 1 -t 10s --headless --csv=reportdata/myData
# here above it means it will download the data after completion of the run i.e. 10 sec
# now if we run this: locust -f basics/basic_locust_01.py -u 5 -r 1 --headless --csv=reportdata/myData -t2s --run-time 10s
# this means it will periodically download data in csv format in the interval of 2s and the run will complete after 10s
# Also we can do this with the above code at line number 5, without using '-t2s --run-time 10s' in cmd
