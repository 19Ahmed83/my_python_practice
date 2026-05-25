months = {
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
}

while True:
    date = input("Date: ")
    try:
        month, day, year = date.split("/")
        year = int(year)
        month = int(month)
        day = int(day)
        if day <= 31 and month <= 12:
            print(f"{year}-{month:02}-{day:02}")
            break
        else:
            continue
        

    except ValueError:
        print("Enter correct date please: ")
    

    try:
        if month in months:
            index = index.months(month) + 1
            print(f"{year}-{index:02}-{day:02}")
            break
        else:
            continue
    except ValueError:
        continue