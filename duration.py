import json

input_file = input("Enter the name of the input file: ")
output_file = input("Enter the name of the output file: ")

with open(input_file, 'r') as f:
    lines = f.readlines()

durations = []
for line in lines:
    data = json.loads(line)
    if data['eventid'] == 'cowrie.session.closed':
        durations.append(data['duration'])

with open(output_file, 'a') as f:
    for duration in durations:
        f.write(str(duration) + '\n')

print(f"Duration times written to {output_file}")
