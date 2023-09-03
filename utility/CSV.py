import csv

read=csv.reader(open("C:\\Users\\Lenovo\\PycharmProjects\\Python_POM_Framework\\TestData\\testdata.csv","r"))
dataList = []

for d in read:
    dataList.append(d)
print(dataList)
print(len(dataList))
print(dataList[0])
print(dataList[1])
