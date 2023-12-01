from time import sleep
from datetime import date, datetime
from subprocess import call

# URL and year
URL = "https://adventofcode.com"
YEAR = 2023

# Loads the session cookie from a text file
with open("session.txt") as f:
    SESSION = f.readline()

def setup_day():
    # Get current day and the day's URL
    day = date.today().day
    day_url = f"{URL}/{YEAR}/day/{day}"


    # Opens today's challenge in the default browser
    call(f'explorer {day_url}', shell=True)

    # Creates the directory and opens it with vscode
    call(f'mkdir day-{day}', shell=True)
    call(f'code .\\day-{day}', shell=True)

    # Creates python files from template, and test input file
    call(f'copy template.py .\\day-{day}\\1.py', shell=True)
    call(f'copy template.py .\\day-{day}\\2.py', shell=True)
    call(f'copy NUL .\\day-{day}\\test.txt', shell=True)

    # Gets the input data
    call(f'curl --cookie "session={SESSION}"  {day_url}/input > day-{day}/input.txt', shell=True)

if __name__ == '__main__':
    waiting = True
    while waiting:
        now = datetime.now()
        h, m, s = now.hour, now.minute, (now.second - 3) % 60

        print(f"  -  Waiting... {h:0>2d}:{m:0>2d}:{s:0>2d}", end="\r")

        if h == 5 and m == 0 and s == 0:
            print("Attempting setup...\t\t")
            setup_day()
            waiting = False
        
        sleep(1)
        