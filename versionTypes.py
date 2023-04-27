import json

versions = []
with open('C:/Users/etana/OneDrive/Documents/Forensic Investigations/log files/cowrie.json.2023-04-16', 'r') as f:
    for line in f:
        data = json.loads(line)
        if 'cowrie.client.version' in data['eventid']:
            version = data['version']
            versions.append(version)

# Write the versions to a new file
with open('C:/Users/etana/OneDrive/Documents/Forensic Investigations/Version/versions.txt', 'a', encoding='utf-8') as f:
    f.write('\n'.join(versions))

