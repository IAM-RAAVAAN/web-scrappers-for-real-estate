import schedule
import time
import os
import subprocess
os.chdir('/root/working')
print(os.getcwd())


def job():
    print("I'm working...")
    subprocess.check_output(
        'python3 99acers1_com_working.py', shell=True)
    return


schedule.every().day.at("18:13").do(job)

while True:
    schedule.run_pending()
    # time.sleep(60) # wait o
