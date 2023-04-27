import json

# Open the input file for reading and the output file for writing
with open('C:/Users/etana/OneDrive/Documents/Forensic Investigations/log files/cowrie.json.2023-04-11', 'r') as f_input, open('C:/Users/etana/OneDrive/Documents/Forensic Investigations/Timestamps/timestamps0411.txt', 'w') as f_output:
    # Initialize a list to store all the timestamps
    timestamps = []

    # Loop through each line in the input file
    for line in f_input:
        # Load the line as JSON
        data = json.loads(line)

        # Check if the event ID is "cowrie.session.connect"
        if data['eventid'] == 'cowrie.session.connect':
            # If it is, extract the timestamp and append it to the list
            timestamp = data['timestamp']
            timestamps.append(timestamp)

    # Sort the timestamps in chronological order
    timestamps.sort()

    # Write each timestamp to the output file
    for timestamp in timestamps:
        f_output.write(timestamp + '\n')
