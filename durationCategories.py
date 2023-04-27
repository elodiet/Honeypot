file_path = "C:/Users/etana/OneDrive/Documents/Forensic Investigations/duration.txt"

# Define category intervals
categories = [
    ("<1", 1),
    (">=1 - <5", 5),
    (">=5 - <10", 10),
    (">=10 - <15", 15),
    (">=15 - <20", 20),
    (">=20 - <25", 25),
    (">=25 - <30", 30),
    (">=30 - <35", 35),
    (">=35 - <40", 40),
    (">=40 - <45", 45),
    (">=45 - <50", 50),
    (">=50", None)
]

# Initialize counters for each category
counters = {category[0]: 0 for category in categories}

# Read file and count durations in each category
with open(file_path, "r") as file:
    durations = file.readlines()
    for duration in durations:
        duration = float(duration.strip())
        for category in categories:
            if category[1] is None or duration < category[1]:
                counters[category[0]] += 1
                break

# Print results
for category in categories:
    print(f"{category[0]}: {counters[category[0]]}")
