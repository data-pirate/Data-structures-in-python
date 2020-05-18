"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in
lexicographic order with no duplicates.
"""


def identify_telemarketers(calls, texts):
    callers = set(number[0] for number in calls)
    recievers = set(number[1] for number in calls)
    text_senders = set(number[0] for number in texts)
    text_recievers = set(number[1] for number in texts)

    telemarketers = set()

    for each in callers:
        if (each not in recievers and
           each not in text_senders and
           each not in text_recievers):
            telemarketers.add(each)

    return telemarketers


print("These numbers could be telemarketers: ")
print(*sorted(identify_telemarketers(calls, texts)), sep='\n')
