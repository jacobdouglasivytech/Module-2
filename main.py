#Jacob Douglas 
#GPA Calculator
#this program if gets students names and gpa and place them in appropiate list (Dean's List or the Honor Roll.)
while True:
  last_name = input("Enter students last name (or 'ZZZ' to stop): ")
  if last_name == "ZZZ":
    break
  else:
    first_name = input("Enter students first name: ")
    gpa = float(input("Enter students GPA: "))
    if gpa >= 3.5:
      print(first_name, last_name, "has made the Honor Roll list and the Dean's list.")
    elif gpa > 3.25:
      print(first_name, last_name, "has made the Honor Roll list.")
    else:
      print("Better luck next semester!")