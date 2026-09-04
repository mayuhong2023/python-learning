with open("access.log") as f:
    for line in f:
        line=line.strip()
        if not line:
            continue
        print(line)
