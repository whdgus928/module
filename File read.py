f=open('C:/Users/user/Downloads/메모.txt',mode='r',encoding='utf-8-sig')
line=None
num=[]
while line!=' ' :
    line=f.readline()
    if '동영상 시간 길이 추출 성공 :' in line:
        a,b=line.split('동영상 시간 길이 추출 성공 :')
        b = int(b.replace(" " , ""))
        num.append(b)
    if not line: break

print(sum(num))
f.close()
