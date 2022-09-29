def s(x1,x2,x3):
    return (x1 or x2 or x3)

def n(x1,x2,x3):
    return (not s(x1,x2,x3) or (x1^x2^x3 and not(x1 and x2 and x3)))

def ns(x1,x2,x3):
    return (x1^x2^x3 and not(x1 and x2 and x3))

def c(x1,x2,x3,y1,y2,y3):
    return (not(x1 and y1) and not (x2 and y2) and not (x3 and y3))

def isValid(a1,a2,a3,b1,b2,b3,c1,c2,c3,d1,d2,d3,e1,e2,e3,f1,f2,f3):
    if not (ns(a1,a2,a3) and ns(b1,b2,b3) and ns(c1,c2,c3) and ns(d1,d2,d3) and ns(e1,e2,e3) and ns(f1,f2,f3)):
        return False
    return (c(a1,a2,a3,b1,b2,b3) and c(a1,a2,a3,c1,c2,c3) and c(a1,a2,a3,e1,e2,e3) and c(d1,d2,d3,b1,b2,b3) and c(c1,c2,c3,e1,e2,e3) and c(c1,c2,c3,d1,d2,d3) and c(d1,d2,d3,f1,f2,f3) and c(e1,e2,e3,f1,f2,f3))
