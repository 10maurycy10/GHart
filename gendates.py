#!/bin/python3
import datetime

message = [
    "A     A AAAAA    A   AAA AAA AAA",
    "AA    A A   A    A    A  A   A  ",
    "A A   A A   A    A    A  A   A  ",
    "A  A  A A   A    A    A  AAA AAA",
    "A   A A A   A    A    A  A   A  ",
    "A    AA A   A    A    A  A   A  ",
    "A     A AAAAA    AAA AAA A   AAA"
]

if len(message) != 7:
    print("Message must be 7 rows")
    exit(1)

weeks = len(message[0])

for row in message:
    if len(row) != weeks:
        print("length of row differ, cannot continue.")
        exit()

end_date = datetime.datetime.fromisoformat(input("End date (ISO format): "))

start_date = end_date - datetime.timedelta(weeks=weeks)

print("start date is : " + start_date.isoformat())
print("end date is : " + end_date.isoformat())

chose = input("Continue? [Y/N]")
if chose != "Y" and chose != "y":
    exit(1)

f = open("dates", "w")

date_counts = 0
for row in range(weeks):
    for col in range(7):
        if message[col][row] != " ":
            # calculate the date with the correct week.
            delta_weeks = row - weeks
            weekdate = end_date - datetime.timedelta(days=delta_weeks * -7)
            # calculate an ofset from that date with the correct weekday
            day_of_week = col
            delta_day =  day_of_week - weekdate.weekday();
            # calulate the correct date
            # the -1 is to compensate for GH starting the chart on weekends
            tgt = weekdate + datetime.timedelta(days=delta_day - 1)
            
            if message[col][row] in "0123456789ABCDEF":
                count = "0123456789ABCDEF".index(message[col][row])
                for i in range(count):
                    date_counts = date_counts + 1
                    f.write(tgt.isoformat() + "\n")
            else:
                print("Warning '" + message[col][row] + "' is not in alphabet")

f.close()
print("Saved " + str(date_counts) + " dates to 'dates'")

            
    
