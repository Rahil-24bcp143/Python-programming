
with open('file1.txt') as f1, open('file2.txt') as f2, open('merged.txt', 'w') as out:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

    for l1, l2 in zip(lines1, lines2):
        out.write(l1)
        out.write(l2)

    longer = lines1 if len(lines1) > len(lines2) else lines2
    for extra in longer[len(lines2):] if longer == lines1 else longer[len(lines1):]:
        out.write(extra)
