# TDD is Test First Development - By Example

# Q. What is the opposite of TDD?
# A. Test Last Development - By Vague Notion

# 1. As a software engineer we get a business requirement like this one:
#       "Create an Adding Machine"
# 2. We immediately write a script to satisfy the requirement
# 3. We verify the script runs and adds numbers
# 4. We send the script to the QA department for testing

total = 0
number = 0
while number != "":
    number = input("Enter a number or blank line to get the total and quit.")
    if number != "":
        total += int(number)

print(f"{total}")
