"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import time

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""


def different_numbers_count(calls, texts):
    numbers = set()
    for each in calls:
        numbers.add(each[0])
        numbers.add(each[1])

    for each in texts:
        numbers.add(each[0])
        numbers.add(each[1])

    return len(numbers)


print(f"There are {different_numbers_count(calls, texts)}" +
      f" different telephone numbers in the records.")

# Time Complexity: O(n)
