# Question-1

# 1. *Reading Data*
#    - Load a text file named sales_data.txt containing columns Product, Region, and Sales.
#    - Print the first 5 rows of the file.



file=open("sales_data.txt",'r')

finalDataLList=[]
index=0
while True:
    line=file.readline()
    if not line:
        break
    if(index==0):
        index=index+1
        continue


    # A,North,450
    dataList=line.split(",")


    if(len(dataList)==3):
        productName=dataList[0]
        regionName=dataList[1]
        salesValue=dataList[2]

        if(salesValue[len(salesValue)-1]=="\n"):
            newSalesValue=salesValue[0:len(salesValue)-1]
        else:
            newSalesValue=salesValue
        obj={
            "Index":index,
            "Product":productName,
            "Region":regionName,
            "Sales":int(newSalesValue)
        }
        finalDataLList.append(obj)
        index=index+1


print(finalDataLList)


# 2. *Finding the Highest*
#    - Find the product with the highest sales.
#    - Find the region with the highest total sales.

# - Find the product with the highest sales.


def getMyKey(argDict):
    return argDict["Sales"]
sortedList=sorted(finalDataLList,key=getMyKey,reverse=True)

ansDict=sortedList[0]
print("Product with highest sales is: ",ansDict["Product"])

#  Find the region with the highest total sales

regionSalesDict={}

for valDict in finalDataLList:
    # {'Index': 1, 'Product': 'A', 'Region': 'North', 'Sales': 450}
    region=valDict.get("Region")

    if(regionSalesDict.get(region)):
        key=region
        value=regionSalesDict.get(region)+valDict.get("Sales")
        regionSalesDict[key]=value
    else:
        key=region
        value=valDict.get("Sales")
        regionSalesDict[key]=value

regionSalesList=regionSalesDict.items()

def getMyKey(argTup):
    return argTup[1]

regionSalesListSorted=sorted(regionSalesList,key=getMyKey,reverse=True)
regionValueTup=regionSalesListSorted[0]
regionValue=regionValueTup[0]

print("The region with the highest total sales: ",regionValue)





# 3. *Finding the Lowest*



#    - Identify the product with the lowest sales.

def getmykey(newdct):
    return newdct["Sales"]
salessortedList = sorted(finalDataLList, key = getmykey)

print("Product with lowest sales is: ",salessortedList[0]["Product"])



#    -  the region with the lowest total sales.

newsales = {}
for salesDict in finalDataLList:
    region=salesDict.get("Region")
    sales=salesDict.get("Sales")

    if(newsales.get(region)):
        existSales=newsales.get(region)
        newsalesVal=existSales+sales
        key=region
        value=newsalesVal
        newsales[key]=value
    else:
        key=region
        value=sales
        newsales[key]=value

newsalesList=newsales.items()

def getmykey(argTup):
    return argTup[1]

newsalesListSorted=sorted(newsalesList,key=getmykey)

newsalesListSortedTup=newsalesListSorted[0]
newsalesListSortedTupVal=newsalesListSortedTup[0]

print("The region with the lowest total sales: ",newsalesListSortedTupVal)





# 4. *Calculating Sums*

#    - Calculate the total sales for all products combined.

totalSum=0
for valDict in finalDataLList:
    sales=valDict.get("Sales")
    totalSum=totalSum+sales


print("Total sales for all products combined: ",totalSum)

#    - Calculate the total sales for each region.

ansDict={}
for valDict in finalDataLList:
    region=valDict.get("Region")
    sale=valDict.get("Sales")

    if(ansDict.get(region)):
        key=region
        value=ansDict.get(region)+sale
        ansDict[key]=value

    else:
        key=region
        value=sale
        ansDict[key]=value

print("The total sales for each region: ",ansDict)



# 5. *Calculating Averages*
#    - Find the average sales for all products.

numberOfProducts=len(finalDataLList)

print("The average sales for all products. ",totalSum/numberOfProducts)

#    - Find the average sales per region.

ansDict={}

for valDict in finalDataLList:
    region=valDict.get("Region")
    sale=valDict.get("Sales")

    if(ansDict.get(region)):
        tempDict=ansDict.get(region)
        count=tempDict["count"]+1
        sumVal=tempDict["totalSum"]+sale
        average=sumVal/count
        key=region
        value={
            "count":count,
            "totalSum":sumVal,
            "average":average
        }
        ansDict[key]=value

    else:
        count=1
        sumVal=sale
        average=sumVal/count
        key=region
        value={
            "count":count,
            "totalSum":sumVal,
            "average":average
        }
        ansDict[key]=value


print("The average sales per region: ",ansDict)



# 6. *Looping Through Data*


#    - Print all products where sales are greater than 500.

productNameList=[]
for valDict in finalDataLList:
    productName=valDict.get("Product")
    sales=valDict.get("Sales")

    if sales>500:
        productNameList.append(productName)

print("All products where sales are greater than 500: ",productNameList)

#    - Count how many products have sales less than 200.

count=0
for valDict in finalDataLList:
    sales=valDict.get("Sales")

    if sales<200:
        count=count+1

print("Count of products have sales less than 200.",count)



# 8. *Combining Operations*

#    - Which product had the highest sales in each region?




nortList=[]
southList=[]
eastList=[]
westList=[]
for valDict in finalDataLList:

    productName=valDict.get("Product")
    region=valDict.get("Region")
    sales=valDict.get("Sales")

    if(region=="North"):
        nortList.append((sales,productName))
    if(region=="South"):
        southList.append((sales,productName))
    if(region=="East"):
        eastList.append((sales,productName))
    if(region=="West"):
        westList.append((sales,productName))


nortListSorted=sorted(nortList,reverse=True)
southList=sorted(southList,reverse=True)
eastList=sorted(eastList,reverse=True)
westList=sorted(westList,reverse=True)


ansObj={
    "North":nortListSorted[0][1],
    "South":southList[0][1],
    "East":eastList[0][1],
    "West":westList[0][1]
}
print("Product had the highest sales in each region: ",ansObj)