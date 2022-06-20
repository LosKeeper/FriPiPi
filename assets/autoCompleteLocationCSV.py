import findAddrFromLatLon

# Open the CSV file
file = open('toilet_location.csv', 'r+')

# Not reading the header
header = file.readline()

# Read the rest of the file while dont reach the end
while True:
    line = file.readline()

    if not line:
        break

    # Split the line into a list
    line = line.split(',')

    # If an adress is already in the file, skip it
    if line[1] != '':
        continue

    # Get the address from the lat and lon
    lat = line[2]
    lon = line[3]
    # Get the address
    addr = findAddrFromLatLon.findAddrFromLatLon(lat, lon)
    addr = addr.replace(',', ' ')

    # Write the address in the file at the same line
    file.seek(0)
    file.write(line[0] + ',' + addr + ',' + line[2] + ',' + line[3] + '\n')
