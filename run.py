with open("input.txt", "r") as i:
    lines = i.read().split(", ")
    l_s = set(lines)
    with open("excludelist", "w+") as o:
        s = str(l_s).replace("'", "").replace("{", "").replace("}", "").replace("\\n", "")
        o.write(s)
