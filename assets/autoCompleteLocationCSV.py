import findAddrFromLatLon

# Open the CSV file
file = open('toilet_location.csv', 'r')
out = open('toilet_location_autocomplete.csv', 'w')

# Not reading the header
header = file.readline()
out.write(header)

# Read the rest of the file while dont reach the end
while True:
    line = file.readline()

    if not line:
        break

    # Split the line into a list
    line_split = line.split(',')

    # If an adress is already in the file, skip it
    if line_split[1] != '':
        out.write(line)
        continue

    # Get the address from the lat and lon
    lat = line_split[2]
    lon = line_split[3]
    # Get the address
    addr = findAddrFromLatLon.findAddrFromLatLon(lat, lon)
    addr = addr.replace(',', ' ')
    print(addr)

    # Write the address in the file
    line_split[1] = addr
    line = ','.join(line_split)
    out.write(line)

file.close()
out.close()
