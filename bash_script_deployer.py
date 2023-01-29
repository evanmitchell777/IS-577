import subprocess

option=int(input("Select option 1-3: 1. search for usernames 2. list all invalid IP, 3. list all invalid username: "))

if option==1:
    subprocess.call('./username_ip_search')
elif option==2:
    subprocess.call('./invalid_ip')
elif option==3:
    subprocess.call('./invalid_username')
else:
    print("enter a valid option")
