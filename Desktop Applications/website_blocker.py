# This program blocks access to websites

import time
from datetime import datetime as dt


hosts_path = "/etc/hosts" # for Ubuntu and macOS
hosts_path_w = "C:\Windows\System32\drivers\etc\hosts" #for Windows


redirect = "127.0.0.1" # when blocks website, redirects to local
website_list = ["www.facebook.com", "facebook.com"] # Here You put all websites you want to be blocked

# Time when site are blocked
start_hour = 8 # work day beginning
end_hour = 17 # work day end


while True:
    # if it work day time
    if dt(dt.now().year, dt.now().month, dt.now().day, 20) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 23):
        with open(hosts_path, 'r+') as file:
            content=file.read()

            # add website address to be blocked
            for website in website_list:
                if website not in content:
                    file.write(redirect + " " + website + "\n")

    # not work day time
    else:
        with open(hosts_path, 'r+') as file:
            content=file.readlines()

            # if in file hosts are some website address, then delete it
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()

    time.sleep(300) # Each 5 minutes script are working, to check what time is it