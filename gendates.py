#!/bin/python3
import datetime

message = [
    "#   ### ### #  # ### # # ### # # ### ### ### # # ###",
    "#   # # # # # #   #  # # # # # # #    #  #   # #  # ",
    "#   # # # # ##    #  ### ### # # ###  #  ###  #   # ",
    "#   # # # # # #   #  # # # # # # #    #  #   # #  # ",
    "### ### ### #  # ### # # # #  #  ###  #  ### # #  # ",
    "                                                    ",
    "                                                    "
]

if len(message) != 7:
    print("Message must be 7 rows")
    exit(1)

weeks = len(message[0])

for row in message:
    if len(row) != weeks:
        print("length of row differ, cannot continue.")
        exit()
        
print(len(message[1]))

for row in range(weeks):
    for col in range(7):
        if message[col][row] != " ":
            now = datetime.datetime.now()
            # calculate the date with the correct week.
            delta_weeks = row - weeks
            weekdate = now - datetime.timedelta(days=delta_weeks * -7)
            # calculate an ofset from that date with the correct weekday
            day_of_week = col
            delta_day =  day_of_week - weekdate.weekday();
            # calulate the correct date
            tgt = weekdate + datetime.timedelta(days=delta_day)
            
            # output the date several times to impove text contrast
            for i in range(10):
                print(tgt)

            
    
