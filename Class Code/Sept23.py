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

def satisfyCourseReqs(a, b, c, d, e):
	return req1(a, b, c, d, e) and \
		req2(a, b, c, d, e) and \
		req3(a, b, c, d, e) and \
		req4(a, b, c, d, e) and \
		req5(a, b, c, d, e) and \
		req6(a, b, c, d, e)

def satisfyScheduleReqs(a, b, c, d, e):
    return not(c and e)

def satisfyReqs(a, b, c, d, e):
    return satisfyCourseReqs(a, b, c, d, e) and satisfyScheduleReqs(a, b, c, d, e)

def buildModel(model):
    if len(model) < 5:
        buildModel(model+[False])
        buildModel(model+[True])
    else:
        if(satisfyReqs(*model)):
            print(model)

buildModel([])