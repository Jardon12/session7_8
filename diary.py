import datetime
now = datetime.datetime.now()
today = now.strftime("%d/%m/%y %H:%M")
print(today)
fp = open("my diary.txt", "a")
while True:
    entry = input ("What are you doing now (type quit to exit)")
    if entry == "quit":
        break
    fp.write(f"{today} {entry}\n")
fp.close()