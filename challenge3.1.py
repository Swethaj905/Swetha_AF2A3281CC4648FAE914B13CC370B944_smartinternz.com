def linearSearchProduct(productList
,targetProduct):
    indices=[]
    for index,product in enumerate(productList):
         if product==targetProduct:
             indices.append(index)
    return indices
products=["pen","pencil","eraser","pen","note","pen"]
target="pen"
target2="paper"
result=linearSearchProduct(products,target)
print(result)