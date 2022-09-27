def req1(a, b, c, d, e):
	return a or e
def req2(a, b, c, d, e):
	return b or c or d
def req3(a, b, c, d, e):
	return a or d or e
def req4(a, b, c, d, e):
	return c or e
def req5(a, b, c, d, e):
	return a or c
def req6(a, b, c, d, e):
	return b or d or e

def satisfyReqs(a, b, c, d, e):
	return req1(a, b, c, d, e) and \
		req2(a, b, c, d, e) and \
		req3(a, b, c, d, e) and \
		req4(a, b, c, d, e) and \
		req5(a, b, c, d, e) and \
		req6(a, b, c, d, e)

def buildModel(l):
    if len(l) < 5:
        buildModel(l+[False])
        buildModel(l+[True])
    else:
        print(l)

buildModel([])