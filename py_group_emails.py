try:
    fhand = open('mbox-short.txt')
except:
    print('Bad File')
    exit()
hist = dict()
listd = list()
print(listd)
for line in fhand:

    listd.append(line)
    # Check to see if the line starts with From
    # Check if the does not only have From and email
    if line.startswith('From') and len(line.split()) > 2:
        day = line.split()[2]
        # If day is not in the hist dictionary
        if day not in hist:
            hist[day] = 1
        # Else increment it
        else:
            hist[day] += 1

# Sort the histogram by days of the week
keys = hist.keys()
keys = sorted(keys)
print(keys)

for key in keys:
    print(key, ':', hist[key])

# Group emails
print('Grouped emails')

for line in listd:
    if line.startswith('From') and len(line.split()) > 2:
        print('\n\t********', line.strip(), '********\n')
    else:
        print(line.strip())
