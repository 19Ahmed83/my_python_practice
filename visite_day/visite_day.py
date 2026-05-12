visit_day = {"Alice": "Apr 2", "Bob": "May 9", "Alex": "Oct 22"}

while True:
    print("Enter a name: (blanc to quit)")
    name = input().capitalize()
    if name == "":
        break
    if name in visit_day:
        print(visit_day[name] + " is the visit day of " + name)
    else:
        print("I do not have visit day information for " + name)
        print("What is their visit day? ")  
        v_day = input()
        visit_day = v_day  
        print("Visit day database updated")


