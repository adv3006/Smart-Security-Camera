import os
import time
import datetime

def check(hostname):
    try:
        print("Begin checking server status")
        while (True):
            print("Status: ", end = "")
            if (os.system("ping -c 1 " + hostname + " &> /dev/null") != 0):		# Test the single ping without any gibberish outputs
                print("Offline...at " + str(datetime.datetime.now()))
            else:
                print("Online")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nStop checking server status")

#check("192.168.43.248")