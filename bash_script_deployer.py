#this prorgam will help me speed up the use of my Bash scripts for my IS577 class
import subprocess
print("Select option 1-3:")
option=int(input(" 1. search for usernames 2. list all invalid IP, 3. list all invalid username: "))

if option==1:
    subprocess.call('./username_ip_search')
elif option==2:
    subprocess.call('./invalid_ip')
elif option==3:
    subprocess.call('./invalid_username')
else:
    print("enter a valid option")
