import subprocess

print("Select option 1-3:")
option=int(input(" 1. search for usernames 2. list all invalid IP, 3. list all invalid username: "))

while True:
    if option==1:
        filepath=input("enter filepath: ")
        username=input("enter username you want to search for: ")
        command=f"grep {username} {filepath} | awk '{{print $11}}' | sort | uniq -c | awk '{{ if ($2 ~ /^[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*$/) {{ print $2 \" \" $1 }} }}'"
        result= subprocess.run(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        output=result.stdout.decode()
        print(output)
        break
    elif option==2:
        filepath=input("enter filepath: ")
        command=f"grep 'invalid user' {filepath}  | awk '{{ match($0, /[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+/); ip = substr($0, RSTART, RLENGTH); print ip }}' | sort | uniq -c | sort -nr"
        result=subprocess.run(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        output=result.stdout.decode()
        print(output)
        break
    elif option==3:
        filepath=input("enter a filepath: ")
        command=f"grep 'Failed password' {filepath}  | awk '{{print $(NF-5)}}' |sort | uniq -c"
        result=subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output=result.stdout.decode()
        print(output)
        break
    else:
        print("enter a valid option")
        option=int(input(" 1. search for usernames 2. list all invalid IP, 3. list all invalid username: "))
