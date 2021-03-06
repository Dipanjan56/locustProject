from locust import HttpUser, SequentialTaskSet, task, between

formdata1 = {
    "tripType": "roundtrip",
    "passCount": "1",
    "fromPort": "Acapulco",
    "fromMonth": "10",
    "fromDay": "24",
    "toPort": "Acapulco",
    "toMonth": "10",
    "toDay": "24",
    "servClass": "Coach",
    "airline": "No" "Preference",
    "findFlights.x": "43",
    "findFlights.y": "11"
}
formdata2 = {
    "fromPort": "Acapulco",
    "toPort": "Acapulco",
    "passCount": "1",
    "toDay": "24",
    "toMonth": "10",
    "fromDay": "24",
    "fromMonth": "10",
    "servClass": "Coach",
    "outFlight": "Blue Skies Airlines$360$270$5:03",
    "inFlight": "Blue Skies Airlines$630$27012:23",
    "reserveFlights.x": "57",
    "reserveFlights.y": "7"
}

formdata3 = {
    "outFlightName": "Blue Skies Airlines",
    "outFlightNumber": "360",
    "outFlightPrice": "270",
    "outFlightTime": "5:03",
    "inFlightName": "Blue Skies Airlines",
    "inFlightNumber": "630",
    "inFlightPrice": "270",
    "inFlightTime": "12:23",
    "fromPort": "Acapulco",
    "toPort": "Acapulco",
    "passCount": "1",
    "toDay": "24",
    "toMonth": "10",
    "fromDay": "24",
    "fromMonth": "10",
    "servClass": "Coach",
    "subtotal": "540",
    "taxes": "44",
    "passFirst0": "qa",
    "passLast0": "mile",
    "pass.0.meal": "",
    "creditCard": "AX",
    "creditnumber": "12234567",
    "cc_exp_dt_mn": "None",
    "cc_exp_dt_yr": "None",
    "cc_frst_name": "qa",
    "cc_mid_name": "",
    "cc_last_name": "mile",
    "billAddress1": "test1,test2",
    "billAddress2": "",
    "billCity": "sss",
    "billState": "Hawaii",
    "billZip": "0000000",
    "billCountry": "215",
    "delAddress1": "1325 Borregas Ave",
    "delAddress2": "",
    "delCity": "Sunnyvale",
    "delState": "CA",
    "delZip": "94089",
    "delCountry": "215",
    "buyFlights.x": "81",
    "buyFlights.y": "10",
}


class UserBehaviour(SequentialTaskSet):

    def on_start(self):
        with self.client.post("/login.php", name="login", data={"action": "process", "userName": "qamile1@gmail.com",
                                                                "password": "qamile", "login.x": "41", "login.y": "12"},
                              catch_response=True) as resp:

            if ("Find a Flight") in resp.text:
                resp.success()
            else:
                resp.failure("failed to login")

    @task()
    def find_flight(self):
        print("add post request to search flight")
        print("verify with catch response that flight search is successful")
        # Select a Flight
        with self.client.post("/mercuryreservation2.php", data=formdata1, name="Find_Flight",
                              catch_response=True) as res_1:
            if ("Select a Flight") in res_1.text:
                res_1.success()
            else:
                res_1.failure("find flight failed" + res_1.text)

    @task()
    def select_flight(self):
        print("add post request to select flight")
        print("verify with catch response that select flight is successful")
        # Book a Flight
        with self.client.post("/mercurypurchase.php", data=formdata2, name="Select_Flight",
                              catch_response=True) as res_2:
            if ("Book a Flight") in res_2.text:
                res_2.success()
            else:
                res_2.failure("select flight failed" + res_2.text)

    @task()
    def book_flight(self):
        print("add post request to book flight")
        print("verify with catch response that flight book is successful")
        print("once success criteria is met, you can change criteria to wrong wordings to see fail criteria is working")
        # Flight Confirmation
        with self.client.post("/mercurypurchase2.php", data=formdata3, name="Book_Flight",
                              catch_response=True) as res_3:
            if ("Flight Confirmation") in res_3.text:
                res_3.success()
            else:
                res_3.failure("book flight failed" + res_3.text)


class MyUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://demo.guru99.com/test/newtours"
    tasks = [UserBehaviour]

# To achieve master slave configuration, lets create 3 terminal session and name those as Master, Worker_1, Worker_2
# Master Terminal -> locust -f basics/basic_locust_01_master_slave.py --master
# when we hit this command, then we have to launch locust web interface and there we can see one additional tab called "Workers"

# Worker_1 and Worker_2 Terminal [Option 1] -> locust -f basics/basic_locust_01_master_slave.py --worker
# For this option, it means master is in the localhost

# Worker_1 or Worker_2 Terminal [Option 2] -> locust -f basics/basic_locust_01_master_slave.py --worker --master-host host_ip --master-port port_number
# We will choose this option when master host is in different than workers
# default port which master listens is 5557[then we dont need to mention prt number], but in case it does differntly
# then we need to provide the port number as well

# For the above scenario, Both the workers are independent of each other and can pick any user from csv
# It might be the case that both teh worker can pick the same user from csv
# Also we do some configuration so that workers should convey their state to each other [need to research]

# for headless mode ->
# Master Terminal -> locust -f basics/basic_locust_01_master_slave.py --master --headless -u 4 -r 2
# If we need to wait for the workers to up and running first and then only start the test, then
# Master Terminal -> locust -f basics/basic_locust_01_master_slave.py --master --expect-workers=2 --headless -u 4 -r 2
