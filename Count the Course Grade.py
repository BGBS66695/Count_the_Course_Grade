f = open('report.txt', 'w')

filename=input() #Input the file name
a=open(filename)
content1=a.read()
a.close()
content=content1.rstrip("\n")
lst=content.split('\n')
sub_lst1 = [item.split("\t") for item in lst]

result=[]
i=0
for _ in lst:
    last_three = sub_lst1[i][-3:]
    threenumber=[int(j) for j in last_three]
    result.append(sum(threenumber)/len(threenumber))
    i+=1

x=0 
for _ in lst:
    if result[x]>=90:
        f.write("{}\t{}\t{}\t{}\t{}\tA\n".format(sub_lst1[x][0], sub_lst1[x][1], sub_lst1[x][2], sub_lst1[x][3], sub_lst1[x][4]))
    elif 80<=result[x]<90:
        f.write("{}\t{}\t{}\t{}\t{}\tB\n".format(sub_lst1[x][0], sub_lst1[x][1], sub_lst1[x][2], sub_lst1[x][3], sub_lst1[x][4]))
    elif 70<=result[x]<80:
        f.write("{}\t{}\t{}\t{}\t{}\tC\n".format(sub_lst1[x][0], sub_lst1[x][1], sub_lst1[x][2], sub_lst1[x][3], sub_lst1[x][4]))
    elif 60<=result[x]<70:
        f.write("{}\t{}\t{}\t{}\t{}\tD\n".format(sub_lst1[x][0], sub_lst1[x][1], sub_lst1[x][2], sub_lst1[x][3], sub_lst1[x][4]))
    elif result[x]<60:
        f.write("{}\t{}\t{}\t{}\t{}\tF\n".format(sub_lst1[x][0], sub_lst1[x][1], sub_lst1[x][2], sub_lst1[x][3], sub_lst1[x][4]))
    x+=1

midt1=[]
y=0
for _ in lst:
    mid1 = sub_lst1[y][-3]
    midt1.append(int(mid1))
    y+=1

total=sum(midt1)
length=len(midt1)
average=total/length


midt2=[]
z=0
for _ in lst:
    mid2 = sub_lst1[z][-2]
    midt2.append(int(mid2))
    z+=1

total1=sum(midt2)
length1=len(midt2)
average1=total1/length1


midt3=[]
l=0
for _ in lst:
    mid3 = sub_lst1[l][-1]
    midt3.append(int(mid3))
    l+=1

total2=sum(midt3)
length2=len(midt3)
average2=total2/length2


f.write("\n")
avg1 = f'{average:.2f}'
avg2 = f'{average1:.2f}'
avg3 = f'{average2:.2f}'
f.write("Averages: midterm1 {}, midterm2 {}, final {}\n".format(avg1, avg2, avg3))

f.close()