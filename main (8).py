"""
write a function  called linear_serch_product that taks the list of products and a target product 
name as input.The function should perfome a linear search to find the target  product in the list and 
return a list of indices of all occurences of the product if found,or an empty list if the product is not
found.
"""


def linearSearchProduct(productlist ,targetProduct):
  indices = []

  for index,product in enumerate(productlist):
    if product == targetProduct:
      indices.append(index)

  return indices 


# Example usage
products =                         ["shoes"," boot","loafer", "shoes" ,"sandal","shoes"]
target = "shoes"
result= linearSearchProduct (products,target)
print(result)

