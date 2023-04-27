import re

with open('C:/Users/etana/OneDrive/Documents/Forensic Investigations/log files/cowrie.log.2023-04-16', 'r', encoding='utf-8') as log_file:
    log_data = log_file.read()

usernames = re.findall(rb"b'(.*?)'", log_data.encode('utf-8'))
passwords = re.findall(rb"b'(.*?)'", log_data.encode('utf-8'))

with open('C:/Users/etana/OneDrive/Documents/Forensic Investigations/usernameandpasswords16.txt', 'w') as output_file:
    for username, password in zip(usernames, passwords):
        output_file.write(f"Username: {username.decode('utf-8')} Password: {password.decode('utf-8')}\n")
