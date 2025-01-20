from time import sleep

for i in range(21):
    spaces = " " * (20 - i)
    percentage = 5*i
    print(f"\r[{'='*i}{spaces}]{percentage}%", flush=True, end="")
    sleep(0.25)