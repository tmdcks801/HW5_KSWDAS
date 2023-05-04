import csv

if __name__ == '__main__':

    f=open('q1.csv',encoding='ANSI')

    data=csv.reader(f)
    header=next(data)

    max=-999
    min=999
    av=0
    cnt=0

    for row in data:
        if row[2]=='' :
            row[2]=0
        else:
            row[2]=float(row[2])
            av+=row[2]
            cnt+=1
            if max<row[2]:
                max=row[2]
            if min>row[2]:
                min=row[2]
    print("Annual Temperature Report for Seoul in 2022")
    print("Average Temperature:",round(av/cnt,2))
    print("Average minimum Temperature:",min)
    print("Average maximum Temperature:",max)
