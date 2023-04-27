# list of input file names
input_files = ['C:/Users/etana/OneDrive/Documents/Forensic Investigations/ipaddresses-logfiles/ipaddressoutput0410', 'C:/Users/etana/OneDrive/Documents/Forensic Investigations/ipaddresses-logfiles/ipaddressoutput0411', 'C:/Users/etana/OneDrive/Documents/Forensic Investigations/ipaddresses-logfiles/ipaddressoutput0412', 'C:/Users/etana/OneDrive/Documents/Forensic Investigations/ipaddresses-logfiles/ipaddressoutput0413', 'C:/Users/etana/OneDrive/Documents/Forensic Investigations/ipaddresses-logfiles/ipaddressoutput0414', 'C:/Users/etana/OneDrive/Documents/Forensic Investigations/ipaddresses-logfiles/ipaddressoutput0415', 'C:/Users/etana/OneDrive/Documents/Forensic Investigations/ipaddresses-logfiles/ipaddressoutput0416']

# set to store unique IP addresses
unique_ips = set()

# loop through each input file and add unique IPs to set
for file_name in input_files:
    with open(file_name, 'r') as file:
        for line in file:
            ip = line.strip()
            if ip not in unique_ips:
                unique_ips.add(ip)

# write unique IPs to output file
with open('C:/Users/etana/OneDrive/Documents/Forensic Investigations/ipaddresses-logfiles/ipaddresses', 'a') as output_file:
    for ip in unique_ips:
        output_file.write(ip + '\n')
