import json

# Open the file and read its contents
with open('C:/Users/etana/OneDrive/Documents/Forensic Investigations/log files/cowrie.json.2023-04-16', 'r') as f:
    file_contents = f.read()

# Split the contents of the file into individual lines
lines = file_contents.splitlines()

# Initialize a counter for the number of login successes
login_success_count = 0

# Loop over the lines and check for the presence of cowrie.login.success
for line in lines:
    try:
        event = json.loads(line)
        if event['eventid'] == 'cowrie.login.success':
            login_success_count += 1
    except json.JSONDecodeError:
        pass

# Print the number of login successes
print(f"Number of login successes: {login_success_count}")
