import datetime

filename = datetime.datetime.now()
data = [""]

with open('AppLog.txt', 'a') as file1:
    for line in data:
        file1.write(filename.strftime("%Y-%m-%d %H:%M:%S"))  # Writes the date
        file1.write(line + '\n')  # write a line of data after date, followed by carriage return
