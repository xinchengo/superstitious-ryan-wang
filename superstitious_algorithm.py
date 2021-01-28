def get_stroke(c):
    if c == ' ':
        return 0
    strokes = []
    with open("strokes.txt", 'r') as fr:
        for line in fr:
            strokes.append(int(line.strip()))

    unicode_ = ord(c)

    if 13312 <= unicode_ <= 64045:
        return strokes[unicode_-13312]
    elif 131072 <= unicode_ <= 194998:
        return strokes[unicode_-80338]
    else:
        print("Invalid Character")


def calc(s1, s2):
    if(len(s1) < 4 and len(s2) < 4):
        while(len(s1) < 3):
            s1.insert(0, " ")
        while(len(s2) < 3):
            s2.insert(0, " ")
        stroke = []
        for i in s1:
            stroke.append(get_stroke(i))
        for i in s2:
            stroke.append(get_stroke(i))
        ans = ((1*stroke[0] + 4*stroke[1] + 6*stroke[2] +
                4*stroke[3] + 1*stroke[4]) % 10)*10 \
            + (1*stroke[1] + 4*stroke[2] + 6 *
               stroke[3] + 4*stroke[4] + 1*stroke[5]) % 10
    else:
        while(len(s1) < 4):
            s1.insert(0, " ")
        while(len(s2) < 4):
            s2.insert(0, " ")
        stroke = []
        for i in s1:
            stroke.append(get_stroke(i))
        for i in s2:
            stroke.append(get_stroke(i))
        ans = ((1*stroke[0] + 6*stroke[1] + 15*stroke[2] + 20 *
                stroke[3] + 15*stroke[4] + 6*stroke[5] + 1*stroke[6]) % 10)*10 \
            + (1*stroke[1] + 6*stroke[2] + 15*stroke[3] + 20 *
               stroke[4] + 15*stroke[5] + 6*stroke[6] + 1*stroke[7]) % 10
    return ans


if __name__ == "__main__":
    prompt = ">>> "
    print("Select what to do:")
    print("    1. calculate two names.")
    print("    2. calculate all the names in a file.")
    mode = input(prompt)
    if mode == "1":
        print("Enter the first name.")
        st1 = input(prompt)
        print("Enter the second name.")
        st2 = input(prompt)
        #print(st1+" "+st2)
        s1 = []
        s2 = []
        for i in st1:
            # print(i)
            s1.append(i)
        for i in st2:
            # print(i)
            s2.append(i)
        print(len(s1)+len(s2))
        print(str(calc(s1, s2)))
    elif mode == "2":
        print("Enter the filename you want to calculate.")
        print("Names should be separated in \\n.")
        fn = input(prompt)
        names = []
        with open(fn, 'r') as nm:
            for line in nm:
                names.append(line.strip())
        print("Enter the value n.")
        print("Only results larger than n will be displayed.")
        n = input(prompt)
        for i in names:
            for j in names:
                if calc(i, j) >= n:
                    print("The value of "+i+" and " +
                          j+" is "+str(calc(i, j))+".")
