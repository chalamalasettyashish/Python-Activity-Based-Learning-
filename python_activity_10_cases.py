"""Python Activity-Based Learning: 10 selected case-study programs.
Each section is a separate beginner-friendly program. Copy one section at a time to run it.
"""

#============================================================================
# CASE 12: Attendance Recovery Computation
#============================================================================
conducted = int(input("Classes conducted: "))
attended = int(input("Classes attended: "))
target = float(input("Required attendance (%): "))

if conducted <= 0 or attended < 0 or attended > conducted or not 0 <= target <= 100:
    print("Invalid input")
else:
    current = attended / conducted * 100
    extra = 0

    while (attended + extra) / (conducted + extra) * 100 < target:
        extra += 1

    print(f"Current attendance: {current:.2f}%")
    print(f"Extra classes to attend: {extra}")

#============================================================================
# CASE 13: ATM Transaction Sequence Simulation
#============================================================================
balance = float(input("Opening balance: "))
n = int(input("Number of transactions: "))
successful = 0
rejected = 0

if balance < 0 or n < 0:
    print("Invalid input")
else:
    for i in range(n):
        kind = input(f"Transaction {i + 1} (D for deposit, W for withdrawal): ").upper()
        amount = float(input("Amount: "))

        if amount <= 0:
            print("Rejected: amount must be positive")
            rejected += 1
        elif kind == "D":
            balance += amount
            successful += 1
            print("Deposit accepted")
        elif kind == "W" and amount <= balance:
            balance -= amount
            successful += 1
            print("Withdrawal accepted")
        else:
            print("Rejected: invalid type or insufficient balance")
            rejected += 1

    print(f"Final balance: Rs. {balance:.2f}")
    print(f"Successful transactions: {successful}")
    print(f"Rejected transactions: {rejected}")

#============================================================================
# CASE 14: Warehouse Inventory Reconciliation
#============================================================================
products = [
    ("Pen", 100, 40, 70, 65, 80),
    ("Notebook", 50, 30, 20, 60, 70),
    ("Pencil", 80, 10, 25, 65, 50)
]

print("Product | Expected | Actual | Difference | Replenish")
for name, opening, received, dispatched, actual, target in products:
    expected = opening + received - dispatched
    difference = actual - expected
    replenish = max(0, target - actual)
    print(f"{name:8} | {expected:8} | {actual:6} | {difference:10} | {replenish:9}")

#============================================================================
# CASE 17: Student Performance Trend Analysis
#============================================================================
subjects = ["Python", "Maths", "English"]
marks = [
    [55, 62, 70],
    [68, 60, 58],
    [35, 38, 39]
]
minimum_mark = 40

print("Subject  First  Latest  Change  Trend  Note")
for i in range(len(subjects)):
    first = marks[i][0]
    latest = marks[i][-1]
    change = latest - first

    if change > 0:
        trend = "Improved"
    elif change < 0:
        trend = "Declined"
    else:
        trend = "No change"

    note = "Needs attention" if latest < minimum_mark else "OK"
    print(f"{subjects[i]:8} {first:5} {latest:7} {change:7}  {trend:9} {note}")

#============================================================================
# CASE 23: Student Timetable Conflict Detection
#============================================================================
# Each tuple: (course, room, start_hour, end_hour)
schedule = [
    ("Python", "Lab-1", 9, 11),
    ("Maths", "Room-2", 10, 12),
    ("Web Design", "Lab-1", 10, 12),
    ("English", "Room-3", 12, 13)
]

found = False
for i in range(len(schedule)):
    course1, room1, start1, end1 = schedule[i]
    for j in range(i + 1, len(schedule)):
        course2, room2, start2, end2 = schedule[j]
        if room1 == room2 and start1 < end2 and start2 < end1:
            print(f"Conflict: {course1} and {course2} in {room1}")
            found = True

if not found:
    print("No room conflicts found")

#============================================================================
# CASE 26: Nested Loop Examination Seating Generator
#============================================================================
rows = 3
seats_per_row = 4
reserved = [(1, 3), (2, 2), (3, 4)]

for row in range(1, rows + 1):
    print(f"Row {row}: ", end="")
    for seat in range(1, seats_per_row + 1):
        if (row, seat) in reserved:
            print("RES", end="  ")
        else:
            print(f"S{seat}", end="   ")
    print()

#============================================================================
# CASE 29: Password Policy Validation Engine
#============================================================================
password = input("Enter a sample password: ")
errors = []

if len(password) < 8:
    errors.append("Use at least 8 characters")
if not any(ch.isupper() for ch in password):
    errors.append("Add an uppercase letter")
if not any(ch.islower() for ch in password):
    errors.append("Add a lowercase letter")
if not any(ch.isdigit() for ch in password):
    errors.append("Add a digit")
if not any(not ch.isalnum() for ch in password):
    errors.append("Add a special character")

if errors:
    print("Password does not meet the rules:")
    for error in errors:
        print("-", error)
else:
    print("Password meets all basic rules")

#============================================================================
# CASE 35: Text Compression Using Character Runs
#============================================================================
text = input("Enter text: ")

if text == "":
    print("Empty string")
else:
    encoded = ""
    current = text[0]
    count = 1

    for ch in text[1:]:
        if ch == current:
            count += 1
        else:
            encoded += current + str(count)
            current = ch
            count = 1

    encoded += current + str(count)
    print("Encoded text:", encoded)
    print("Original length:", len(text))
    print("Encoded length:", len(encoded))

    if len(encoded) < len(text):
        print("Encoding reduces the length")
    else:
        print("Encoding does not reduce the length")

#============================================================================
# CASE 39: Multi-Stage Examination Eligibility System
#============================================================================
attendance = float(input("Attendance percentage: "))
lab_done = input("All labs completed? (yes/no): ").lower()
internal_marks = float(input("Internal marks out of 100: "))
fees_paid = input("Fees cleared? (yes/no): ").lower()

reasons = []

if attendance < 75:
    reasons.append("Attendance is below 75%")
if lab_done != "yes":
    reasons.append("Laboratory work is incomplete")
if internal_marks < 40:
    reasons.append("Internal marks are below 40")
if fees_paid != "yes":
    reasons.append("Fees are not cleared")

if not reasons:
    print("Result: Eligible for final examination")
else:
    print("Result: Not eligible for final examination")
    print("Requirements not met:")
    for reason in reasons:
        print("-", reason)

#============================================================================
# CASE 42: Student Marks Matrix Analysis
#============================================================================
students = ["Anu", "Bala", "Charan"]
subjects = ["Python", "Maths", "English"]
marks = [
    [85, 78, 90],
    [72, 88, 75],
    [60, 65, 70]
]

totals = []
print("Student results:")
for i in range(len(students)):
    total = sum(marks[i])
    average = total / len(subjects)
    totals.append(total)
    print(f"{students[i]}: Total = {total}, Average = {average:.2f}")

print("\nSubject averages:")
for j in range(len(subjects)):
    subject_total = 0
    for i in range(len(students)):
        subject_total += marks[i][j]
    average = subject_total / len(students)
    print(f"{subjects[j]}: {average:.2f}")

top_index = totals.index(max(totals))
print(f"Top performer: {students[top_index]} ({totals[top_index]} marks)")

for j in range(len(subjects)):
    subject_average = sum(marks[i][j] for i in range(len(students))) / len(students)
    if subject_average < 50:
        print(f"Low average subject: {subjects[j]}")

