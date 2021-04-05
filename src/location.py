import math

class Location :
    def __init__(self, x, y) :
        self.x = x
        self.y = y

    # calculate euclidean distance of current location to other location
    # input
    #   Location : otherLocation
    # output : float
    def euclideanDist(self,otherLocation):
        return (math.sqrt((self.x-otherLocation.x)**2 + (self.y-otherLocation.y)**2))


if __name__ == '__main__':
    l1 = Location(1,1)
    l2 = Location(2,1)

    x = l1.euclideanDist(l2)

    print(x)