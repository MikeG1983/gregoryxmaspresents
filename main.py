import random
import pprint

households = []

households.append({
    "name": "John, Emily & Edward",
    "disallowed_recipients": ["John", "Emily"]
})

households.append({
    "name": "Ruth & Maddie (and cats)",
    "disallowed_recipients": ["Ruth"]
})

households.append({
    "name": "Mike & Martyna",
    "disallowed_recipients": ["Mike", "Martyna"]
})

households.append({
    "name": "Lynn & Stela",
    "disallowed_recipients": ["Lynn"]
})

households.append({
    "name": "Alex, Harriet & Rufus",
    "disallowed_recipients": ["Alex", "Harriet", "Rufus"]
})

present_recipients = ["John", "Emily", "Ruth", "Mike", "Martyna", "Lynn", "Alex", "Rufus", "Lawrence", "Carol",
                      "Harriet"]



random.shuffle(households)
random.shuffle(present_recipients)
present_assignments = {}


def assign_allowed_recipient(current_household, present_recipients, present_assignments):
    for recipient in present_recipients:
        if recipient not in current_household["disallowed_recipients"]:
            present_assignments[current_household["name"]].append(recipient)
            present_recipients.remove(recipient)
            return
    return


# Add each household to our final result (with an empty list of present recipients)
for household in households:
    present_assignments[household["name"]] = []

household_index = 0

while len(present_recipients) > 0:  # Loop through each present recipient
    current_household = households[household_index % (len(households))]
    assign_allowed_recipient(current_household, present_recipients, present_assignments)

    household_index += 1  # add 1 so we go to the next household

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(present_assignments)