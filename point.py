class Point:
    # all classes need to ahve an init method
    # all classes inherit from somehwhere
    # if there is explicit inherit, everything is inherited from the base class: object
    def __init__(self, x, y):
        """
        Init method that initializes the point with X and Y
        :param x: X coordinate value
        :param y: Y coordinate vlaue
        :return:
        """
        self.x = x
        self.y = y

    def __str__(self):
        # this is adding how the python should print an object, its defining the print o/w it will print the ID
        """
        How to print this point?
        :return:
        """
        return f"<x={self.x}, y={self.y}>"

    def __repr__(self):
        """
        How to print if in a list?
        :return:
        """
        return self.__str__()

    def distance_org(self):
        '''
        Return the distance from origin of the point instance
        :return:
        '''
        return ((self.x ** 2 + self.y ** 2) ** 0.5)

    def __gt__(self, other):
        '''
        How to compare 2 points? we define it here
        :param other:
        :return:
        '''
        my_size = self.distance_org()
        their_size = other.distance_org()
        return my_size > their_size

    def __eq__(self, other):
        '''
        how to compare with ==?
        :param other:
        :return:
        '''
        return self.distance_org() == other.distance_org()


if __name__ == "__main__":  # this is to import only the class
    # nothing happens to a function, unless you call it
    # when you use the class after creating it, we instantiate it
    # class is a mold, each time i create a point which certain characteristics, eg: when creating a blue lambo in class car, you are creating an instance. Class is the blueprint and the instance is the thing we are using.

    a = Point(2, 3)  # instantiate by calling the name of the class and parameters in brackets

    print(a.x)
    print(a.y)

    b = Point(7, 9)
    print(b.x)
    print(b.y)
    # every point with x and y values is an instance of the class
    # class is constructor that allows you to create points

    # add 5 random points into a list!
    # dana chatgpt code
    import random

    points = []
    for i in range(5):
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        points.append(Point(x, y))

    # profs
    for _ in range(5):
        points.append(Point(random.randint(0, 100), random.randint(0, 100)))

    for point in points:
        print(point)  # here it cal point.__str

    print(points)  # here it iterates and calls point.__repr
    a = Point(3, 4)  # we expect 5 as diastance to origin
    b = Point(12, 5)  # we expect 13 as distance to origin
    c = Point(5, 12)
    print(a > b)  # need to define how __gt__ works!

    print(a.distance_org(), b.distance_org())
    print(a.distance_org() > b.distance_org())
    # a > b this is the magic, this translates to: a.__gt__(b)
    # You can prove this by adding a break point in the __gt__ function, so if the code stops while running it =, this means that the __gt__ works
    # just by defining greater than, we have also taken care of equal to and less than but not less than or equal to, for which we need to create the equal part
    print(a > b)
    print(a < b)
    print(b == c)
    points.sort()
    print(f"the biggest point is: {points[-1]} and the smallest point is: {points[0]}")
