import datetime

filename = datetime.datetime.now()                            # Not sure why you called date filename, but so be it
data = ["first line", "second line", "third line"]            # Made up data

with open('new_results.txt', 'w') as file1:                    # Python recommends using file context manager rather than direct open/close
    for line in data:                                          # Loop over the data lines
        file1.write(filename.strftime("%Y_%m_%d-%H_%M_%S: "))  # Writes the date
        file1.write(line + '\n')                               # write a line of data after date, followed by carriage return