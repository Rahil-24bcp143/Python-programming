with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    for line in infile:
        for word in [' a ', ' the ', ' an ']:
            line = line.replace(word, ' ')
        outfile.write(line)
