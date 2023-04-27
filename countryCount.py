from collections import Counter

# read in the countries from the input file
with open('C:/Users/etana/OneDrive/Documents/Forensic Investigations/ipaddresses-logfiles/countries.txt', 'r') as f:
    countries = [line.strip() for line in f.readlines()]

# count the occurrences of each country
counts = Counter(countries)

# write the results to the output file
with open('C:/Users/etana/OneDrive/Documents/Forensic Investigations/ipaddresses-logfiles/country_counts.txt', 'w') as f:
    for country, count in counts.items():
        f.write(f"{country}: {count}\n")
