import sys
try:
    print(a)
except:
    print(sys.exc_info())# print exact exception
    print(sys.exc_info()[0])# print 0th position exception
    print(sys.exc_info()[1])# print 1th position exception
