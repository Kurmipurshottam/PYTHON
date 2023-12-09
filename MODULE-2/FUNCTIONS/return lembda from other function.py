#returning lemda from other function
def double(x):
    return lambda r,z : r*x*z
fun=double(50)# it is for double function[50=x]
print(fun(5,2))# it is for the lembda[5=r,2=z]
