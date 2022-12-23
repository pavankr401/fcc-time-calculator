def add_time(start, duration, day = ""):
    start_time, am_pm = start.split()
    start_hh, start_mm = start_time.split(":")
    duration_hh, duration_mm = duration.split(":")
    daysLater = 0
    before_am_pm = am_pm
    days_of_week = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    
    total_mm = int(start_mm) + int(duration_mm)
    total_hh = int(start_hh) + int(duration_hh) + total_mm // 60
    total_mm = total_mm % 60
    
    am_pm = check_am_pm(total_hh, am_pm)
    daysLater = giveDelay(before_am_pm, am_pm, daysLater, total_hh)
    
    total_hh = total_hh % 12
    if(total_hh == 0): total_hh = 12
    
    if(day != ""):
        day = day.lower()
        ind = days_of_week.index(day)
        ind = (ind + daysLater) % 7
        day = days_of_week[ind]
    
    return(resFormat(total_hh, total_mm, am_pm, daysLater, day))


def check_am_pm(total_hh, am_pm):
    if( (total_hh // 12) % 2 == 1 and am_pm == 'AM'): am_pm = 'PM'
    elif( (total_hh // 12) % 2 == 1 and am_pm == 'PM'): am_pm = 'AM'
    
    return am_pm

def giveDelay(before_am_pm, am_pm, daysLater, total_hh):
    if(before_am_pm == 'PM' and am_pm == 'AM'): daysLater = 1
    daysLater += total_hh // 24
    
    return daysLater

def numFormat(num):
    if(num < 10):
        num = "0" + str(num)
    else:
        num = str(num)
    
    return num

def resFormat(hh, mm, am_pm, daysLater, day):
    mm = numFormat(mm)
    hh = str(hh)
    
    if(daysLater == 0 and day == ""):
        format = hh + ":" + mm + " " + am_pm
    elif(daysLater == 0 and day != ""):
        day = day[0].upper() + day[1:]
        format = hh + ":" + mm + " " + am_pm + ", " + day
    elif(daysLater == 1 and day != ""):
        day = day[0].upper() + day[1:]
        format = hh + ":" + mm + " " + am_pm + ", " + day + " (next day)"
    elif(daysLater == 1 and day == ""):
        format = hh + ":" + mm + " " + am_pm + " (next day)"
    elif(daysLater > 1 and day != ""):
        day = day[0].upper() + day[1:]
        daysLater = str(daysLater)
        format = hh + ":" + mm + " " + am_pm + ", " + day + " (" + daysLater + " days later" + ")"
    elif(daysLater > 1 and day == ""):
        daysLater = str(daysLater)
        format = hh + ":" + mm + " " + am_pm + " (" + daysLater + " days later" + ")"
    
    return format

# print(add_time("11:59 PM", "24:05"))