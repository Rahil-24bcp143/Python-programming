
src = "src.txt"
tar = "tar.txt"

with open(src, 'r') as src, open(tar, 'w') as tgt:
    for line in src:
        tgt.write(line.upper())
