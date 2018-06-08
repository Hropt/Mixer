
#gets current weight
def getWeight():
    return 26
    #get weight


#tares the weight
def tare():
    return 1


def make_gt(size):
    if size == 1:
        #pour small size gin
        #pour small size tonic
        return 1
    elif size == 2:
        #pour medium size gin
        #pour medium size tonic
        return 2
    elif size == 3:
        #pour large size gin
        #pour large size tonic
        return 3

def make_cl(size):
    if size == 1:
        #pour small size rum
        #pour small size coke
        return 1
    elif size == 2:
        #pour medium size rum
        #pour medium size coke
        return 2
    elif size == 3:
        #pour large size rum
        #pour large size coke
        return 3

def make_jc(size):
    if size == 1:
        #pour small size jack
        #pour small size coke
        return 1
    elif size == 2:
        #pour medium size jack
        #pour medium size coke
        return 2
    elif size == 3:
        #pour large size jack
        #pour large size coke
        return 3


def make_drink(drink, size):
    tare()
    if drink == 1:
        make_gt(size)
        print("making: " + "gin & tonic " + str(size))
    elif drink == 2:
        make_cl(size)
        print("making: " + "cuba libre " + str(size))
    elif drink == 3:
        make_jc(size)
        print("making: " + "jack & coke " + str(size))