# Max number
list =[1048,1255,2125,1050,2506,1236,2010,1055]
maxnumber = list[0]
for x in list:
    if maxnumber < x :
        maxnumber = x
        print("MAX number in array is",maxnumber)

# Min number
list =[50,100,150,200,250,300,350,400]
minnumber = list[0]
for x in list:
    if minnumber > x :
        minnumber = x
        print("MIN number in array is",minnumber)
