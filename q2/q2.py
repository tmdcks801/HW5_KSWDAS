import csv

if __name__ == '__main__':

    f=open('q2.csv',encoding='ANSI')

    data=csv.reader(f)
    header=next(data)

    max=-999
    min=999
    max_date=""
    min_date=""
    n=0
    for row in data:
        if row[-1]=='' or row[-2]=='':
            row[-1]=0
            row[-2]=0
        else:
            row[-1]=float(row[-1])
            row[-2]=float(row[-2])
            n=row[-1]-row[-2]
            if(n>max):
                max=n
                max_date=row[0]
            if(n<min):
                min=n
                min_date=row[0]
    f.close()

    print("Annual Temperature Report for Seoul in 2022")
    print("Day with the Largest Tempeture vatiation:",max_date)
    print("Maximum Tempetature difference:",max)
    print("Day with the smallest Tempeture vatiation:",min_date)
    print("Minimum Tempetature difference:",round(min,2))
