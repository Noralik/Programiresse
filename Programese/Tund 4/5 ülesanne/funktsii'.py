# def hello(name):
#     print("Hello,",name)
# hello("Johny")
# hello("silverhand")

def in_out (xmin,xmax,ymax,x,y):
    if (xmin<=x<=xmax and ymin<=y<=ymax):
        print ("The point is inside")
    else:
        print ("The point is outside")
in_out(7, -9, 22, -8)