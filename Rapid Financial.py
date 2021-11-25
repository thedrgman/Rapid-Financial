import csv
data = []

print ("Welcome to Rapid Financial\n")
print ("Please confirm your identity with the following 3 questions to see your account history\n")

with open('customerData.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)
i = 0
t = 0
x = 0

while i != 3 or x == 1:
    name = input("Name: \n")
    while t <= len(data):
        if name in data[t]["Name"]:
            print("Found Name in system")
            i += 1
            break
        else:
            t += 1
    gender = input("Gender: male or female \n").lower()
    if gender in data[t]["Gender"]:
        print("Correct second confirmation")
        i += 1
    else:
        print("Incorrect response, try again")
        x = 1

    email = input("Email : \n")
    if email in data[t]["Email"]:
        print ("Identity Confirmed")
        i += 1
    else:
        print("Unable to confirm Identity")
        x = 1
    print("Spent Past 30 Days " + data[t]["Spent Past 30 Days"])
    print("Spent Past 6 Months " + data[t]["Spent Past 6 Months"])
    print("Spent Past 12 Months " + data[t]["Spent Past 12 Months"])