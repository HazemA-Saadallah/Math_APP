def to_dict(s):
    if s[0] != "-":
        newstr = "+" + s
    else:
        newstr = s
    calc_list = list()
    while len(newstr) != 0:
        for chr in newstr[1:]:
            if chr in ['×', '÷', '+', '-']:
                calc_list.append((newstr[0], newstr[1:newstr[1:].find(chr)+1]))
                newstr = newstr[newstr[1:].find(chr)+1:]
        calc_list.append((newstr[0], newstr[1:len(newstr)]))
        newstr = ''
    return calc_list


if __name__ == "__main__":
    print(to_dict("-5-969×56÷69/69+6993-43434/343+43434-43434-958+85"))
