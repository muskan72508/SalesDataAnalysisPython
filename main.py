# Question-1

# 1. *Reading Data*
#    - Load a text file named sales_data.txt containing columns Product, Region, and Sales.
#    - Print the first 5 rows of the file.


file=open("sales_data.txt",'r')
finalData=[]
index=0
while True:
    line=file.readline()
    if not line:
        break
    if(index==0):
        index=index+1
        continue
    else:
        index=index+1
        lineArr=line.split(",")


        if(len(lineArr)==3):
            columnNumber=index+1


            sales=lineArr[2]
            salesValue=0

            if(sales[len(sales)-1]=="\n"):
                salesValue=sales[0:len(sales)-1:1]
            else:
                salesValue=sales

            obj={}
            obj["product"]=lineArr[0]
            obj["region"]=lineArr[1]
            obj["sales"]=int(salesValue)

            finalData.append(obj)


# Stores final data after cleaning
# print(finalData)

# Looping thorugh all the data
# for data in finalData:
#     for key in data.keys():
#         print("Key is: ",key)
#         print("value is: ",data[key])




# 2. *Finding the Highest*
#    - Find the product with the highest sales.
#    - Find the region with the highest total sales.

# - Find the product with the highest sales.

sorted_data_sales = sorted(finalData, key=lambda x: x["sales"], reverse=True)

ansDict=sorted_data_sales[0]

print("Product with highest sales: ",ansDict["product"])


#  Find the region with the highest total sales.

regionDict={
    "North":0,
    "South":0,
    "East":0,
    "West":0
}

for data in finalData:
    for key in data.keys():
        if(key=="region"):
            regionName=data[key]
            regionDict[regionName]=regionDict[regionName]+data["sales"]

mx=-1
ans=""

for key in regionDict.keys():
    regionName=key
    salesValue=regionDict[key]

    if(salesValue>mx):
        ans=regionName
        mx=salesValue

print("Region with the highest total sales is: ",ans)

