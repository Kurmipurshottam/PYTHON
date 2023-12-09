# 31] How will you create a dictionary using tuples in python?
tuple1=(7,75,21,111)
tuple2=('raj','purshottam','smit','nikhil')
print("tuple1 = ",tuple1)
print("tuple2 = ",tuple2)
# Create a dictionary by zipping the two tuples
res = dict(zip(tuple1, tuple2))
# Print the resulting dictionary
print("creating dictionary using tuple1 and tuple2 = ", res)
