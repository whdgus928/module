def change(hour,minute,second,total):
    h=total//3600
    m=(total%3600)//60
    s=((total%3600)%60)
    hour+=h
    minute+=m
    second+=s
    while minute>60:
        hour+=1
        minute-=60
    while second>60:
        minute+=1
        second-=60
    return hour,minute,second