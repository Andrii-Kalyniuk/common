import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_rectangle_perimeter(self):
        """
        Returns rectangle perimeter
        :return: number
        """
        perimeter = (self.width + self.height) * 2
        return perimeter

    def get_rectangle_square(self):
        """
        Returns rectangle square
        :return: number
        """
        square = self.width * self.height
        return square

    def get_sum_of_corners(self, number_of_corners):
        """
        Returns sum of corners due to the argument passed in
        one corner is 90 degrees, so if user put 2 in arguments
        that means that we need to count sum of 2 corners
        raise an error if user try to count sum of more than 4 corners
        :param number_of_corners:
        :return:
        """
        if number_of_corners > 4:
            raise ValueError("Rectangle has only 4 corners")

        sum_of_corners = 0
        for i in range(number_of_corners):
            sum_of_corners += 90

        return sum_of_corners

    def get_rectangle_diagonal(self):
        """
        Get the rectangle diagonal due to rhe Pifagor formula c^2 = a^2 + b^2
        where a, b are height and width respectively
        :return:
        """
        diagonal = math.sqrt(math.pow(self.height, 2) + math.pow(self.width, 2))
        return diagonal

    def get_radius_of_circumscribed_circle(self):
        """
        Radius equal half of rectangle diagonal
        :return:
        """
        diagonal = self.get_rectangle_diagonal()
        radius = diagonal / 2
        return radius

    def get_radius_of_inscribed_circle(self):
        """
        Get radius of inscribed circle in rectangle
        due to the formula:      d
                              -------
                                2√2
        where d is diagonal of the rectangle
        :return:
        """
        if self.width != self.height:
            assert ValueError("Can't inscribed circle in rectangle with such width and height")
        diagonal = self.get_rectangle_diagonal()
        radius = diagonal / 2 * math.sqrt(2)
        return radius
