import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

for profile in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', profile, 'key=clear']).decode('utf-8').split('\n')
        password = [b.split(":")[1][1:-1] for b in results if "Key Content" in b][0]
        print("{:<30} | {:<}".format(profile, password))
    except IndexError:
        print("{:<30} | {:<}".format(profile, ""))
