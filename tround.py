def tround(number=float, toround=1):
    strnumber = str(number)
    bef = len(strnumber.split(".")[0])
    strnumber = strnumber.replace(".", "")
    btoround = toround + bef - 1
    if int(strnumber[btoround]) >= 5:
        strnumber = strnumber[:btoround-1] + str(int(strnumber[btoround-1]) + 1) + strnumber[btoround:]
        if toround != 1:
            strnumber = strnumber[:bef] + "." + strnumber[bef:]
            return strnumber[:btoround+1]
        else:
            return strnumber[:btoround]
    else:
        if toround != 1:
            strnumber = strnumber[:bef] + "." + strnumber[bef:]
            return strnumber[:btoround+1]
        else:
            return strnumber[:btoround]