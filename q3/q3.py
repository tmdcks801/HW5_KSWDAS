import csv


if __name__ == '__main__':

    f=open('q3.csv',encoding='ANSI')

    data=csv.reader(f)
    header=next(data)

    dic={}



    for row in data:
        if row[1]!='' or row[-1]!='' or row[-2]!='' :
            if row[1]=='1호선' or row[1]=='2호선' or row[1]=='3호선' or row[1]=='4호선' or row[1]=='5호선' or row[1]=='6호선' or row[1]=='7호선' or row[1]=='8호선' or row[1]=='9호선':
                if row[1] not in dic:
                    dic[row[1]]=float(row[-1])+float(row[-2])
                else:
                    dic[row[1]]=dic.get(row[1], 0)+float(row[-1])+float(row[-2])

    dic_1=sorted(dic.items(), key=lambda x: x[1], reverse=True)

    print("subway report for seoul on match 2023")
    print("1st busenist line:",dic_1[0][0],":",dic_1[0][1])
    print("2st busenist line:",dic_1[1][0],":",dic_1[1][1])
    print("1st least used line:",dic_1[-1][0],":",dic_1[-1][1])
    print("2st least used line:",dic_1[-2][0],":",dic_1[-2][1])
    f.close()
