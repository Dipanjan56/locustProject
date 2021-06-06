from locust import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://demo.guru99.com/test/newtours/"

    @task
    def login_URL(self):
        print("I am logging into URL")


# Terminal -> locust -f basics/basic_locust_01_http_host.py -u 5 -r 1 -t 10s --headless --logfile logfiles/mylog.log --loglevel DEBUG
# u = number of users, r = spawn rate, t = runtime, --headless = headless mode,
# u = 5, r = 1 -> means every 1 sec, one user will be spawned and after 5 secs all the 5 users will be spawned
# t = 10s -> this script will run for 10 sec and will end after that
# logfile = file path -> to store log data in a file
# loglevel = DEBUG ->  it wont print any stats -> it will print only the error message or customized message


# Terminal -> locust -f basics/basic_locust_01_http_host.py -u 1 -r 1 --headless --only-summary
# only-summary = irrelevant request data will not be printed, only the print statements will be printed
