import csv


if __name__ == '__main__':

    f=open('q4.csv',encoding='ANSI')

    data=csv.reader(f)
    header=next(data)

    max_1=0
    min_1=99999999999
    max_2=0
    min_2=99999999999
    max_3=0
    min_3=99999999999
    max_4=0
    min_4=99999999999

    maxsta_1=""
    maxsta_2=""
    maxsta_3=""
    maxsta_4=""

    minsta_1=""
    minsta_1=""
    minsta_1=""
    maxsta_4=""
  

    for row in data:
        if row[1]!='' or row[-1]!='' or row[-2]!='' :
            if row[1]=='1호선':
                if max_1<float(row[-1])+float(row[-2]):
                    max_1=float(row[-1])+float(row[-2])
                    maxsta_1=row[3]
                if min_1>float(row[-1])+float(row[-2]):
                    min_1=float(row[-1])+float(row[-2])
                    minsta_1=row[3]
            elif row[1]=='2호선':
                if max_2<float(row[-1])+float(row[-2]):
                    max_2=float(row[-1])+float(row[-2])
                    maxsta_2=row[3]
                if min_2>float(row[-1])+float(row[-2]):
                    min_2=float(row[-1])+float(row[-2])
                    minsta_2=row[3]
            elif row[1]=='3호선':
                if max_3<float(row[-1])+float(row[-2]):
                    max_3=float(row[-1])+float(row[-2])
                    maxsta_3=row[3]
                if min_3>float(row[-1])+float(row[-2]):
                    min_3=float(row[-1])+float(row[-2])
                    minsta_3=row[3]
            elif row[1]=='4호선':
                if max_4<float(row[-1])+float(row[-2]):
                    max_4=float(row[-1])+float(row[-2])
                    maxsta_4=row[3]
                if min_4>float(row[-1])+float(row[-2]):
                    min_4=float(row[-1])+float(row[-2])
                    minsta_4=row[3]
                
    print("subway report for seoul on match 2023")
    print()
    print("Line1")
    print("busenist station:",maxsta_1,":",max_1)
    print("least used station:",minsta_1,":",min_1)

    print("Line2")
    print("busenist station:",maxsta_2,":",max_2)
    print("least used station:",minsta_2,":",min_2)

    print("Line3")
    print("busenist station:",maxsta_3,":",max_3)
    print("least used station:",minsta_3,":",min_3)

    print("Line4")
    print("busenist station:",maxsta_4,":",max_4)
    print("least used station:",minsta_4,":",min_4)


    f.close()
