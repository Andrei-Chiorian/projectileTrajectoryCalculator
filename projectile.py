import math

GRAVITATIONAL_ACCELERATION = 9.81
PROJECTILE = "∙"
x_axis_tick = "T"
y_axis_tick = "⊣"


class Projectile:
    """This class represents a projectile in physics. It is used to calculate the displacement,
    the coordinates of the trajectory, and other properties of the projectile.

    :param speed: The speed of the projectile in m/s.
    :param height: The height of the projectile in m.
    :param angle: The angle of elevation of the projectile in degrees.
    """

    __slots__ = ('__speed', '__height', '__angle')

    def __init__(self, speed, height, angle):
        """This method initializes an instance of the Projectile class.

        :param speed: The speed of the projectile in m/s.
        :param height: The height of the projectile in m.
        :param angle: The angle of elevation of the projectile in degrees.
        """
        self.__speed = speed
        self.__height = height
        self.__angle = math.radians(angle)

    def __str__(self):
        """This method returns a string representation of the Projectile object.

        :return: A string representation of the Projectile object.
        """
        return f'''
Projectile details:
speed: {self.speed} m/s
height: {self.height} m
angle: {self.angle}°
displacement: {round(self.__calculate_displacement(), 1)} m
'''

    def __calculate_displacement(self):
        """This method calculates the displacement of the projectile.

        :return: The displacement of the projectile in m.
        """
        horizontal_component = self.__speed * math.cos(self.__angle)
        vertical_component = self.__speed * math.sin(self.__angle)
        squared_component = vertical_component ** 2
        gh_component = 2 * GRAVITATIONAL_ACCELERATION * self.__height
        sqrt_component = math.sqrt(squared_component + gh_component)

        return horizontal_component * (vertical_component + sqrt_component) / GRAVITATIONAL_ACCELERATION

    def __calculate_y_coordinate(self, x):
        """This method calculates the y-coordinate of the projectile at a given x-coordinate.

        :param x: The x-coordinate of the projectile.
        :return: The y-coordinate of the projectile at the given x-coordinate.
        """
        height_component = self.__height
        angle_component = math.tan(self.__angle) * x
        acceleration_component = GRAVITATIONAL_ACCELERATION * x ** 2 / (
                2 * self.__speed ** 2 * math.cos(self.__angle) ** 2)
        y_coordinate = height_component + angle_component - acceleration_component

        return y_coordinate

    def calculate_all_coordinates(self):
        """This method calculates all the coordinates of the projectile.

        :return: A list of all the coordinates of the projectile.
        """
        return [
            (x, self.__calculate_y_coordinate(x))
            for x in range(math.ceil(self.__calculate_displacement()))
        ]

    @property
    def height(self):
        """This method returns the height of the projectile.

        :return: The height of the projectile in m.
        """
        return self.__height

    @property
    def angle(self):
        """This method returns the angle of elevation of the projectile.

        :return: The angle of elevation of the projectile in degrees.
        """
        return round(math.degrees(self.__angle))

    @property
    def speed(self):
        """This method returns the speed of the projectile.

        :return: The speed of the projectile in m/s.
        """
        return self.__speed

    @height.setter
    def height(self, n):
        """This method sets the height of the projectile.

        :param n: The new height of the projectile in m.
        """
        self.__height = n

    @angle.setter
    def angle(self, n):
        """This method sets the angle of elevation of the projectile.

        :param n: The new angle of elevation of the projectile in degrees.
        """
        self.__angle = math.radians(n)

    @speed.setter
    def speed(self, s):
        """This method sets the speed of the projectile.

        :param s: The new speed of the projectile in m/s.
        """
        self.__speed = s

    def __repr__(self):
        """This method returns a string representation of the Projectile object.

        :return: A string representation of the Projectile object.
        """
        return f'{self.__class__}({self.speed}, {self.height}, {self.angle})'


class Graph:
    __slots__ = '__coordinates'

    def __init__(self, coord):
        """
        This method initializes an instance of the Graph class.

        :param coord: A list of coordinates of the form (x, y) representing the points on the trajectory.
        """
        self.__coordinates = coord

    def __repr__(self):
        return f"Graph({self.__coordinates})"

    def create_coordinates_table(self):
        """
        This method creates a table of coordinates of the projectile.

        :return: A string representing a table of coordinates of the projectile.
        """
        table = '\n  x      y\n'
        for x, y in self.__coordinates:
            table += f'{x:>3}{y:>7.2f}\n'

        return table

    def create_trajectory(self):
        """
        This method creates a visual representation of the trajectory of the projectile.

        :return: A string representing the visual representation of the trajectory of the projectile.
        """
        rounded_coords = [(round(x), round(y)) for x, y in self.__coordinates]

        x_max = max(rounded_coords, key=lambda i: i[0])[0]
        y_max = max(rounded_coords, key=lambda j: j[1])[1]

        matrix_list = [[" " for _ in range(x_max + 1)] for _ in range(y_max + 1)]

        for x, y in rounded_coords:
            matrix_list[-1 - y][x] = PROJECTILE

        matrix = ["".join(line) for line in matrix_list]

        matrix_axes = [y_axis_tick + row for row in matrix]
        matrix_axes.append(" " + x_axis_tick * (len(matrix[0])))

        graph = "\n" + "\n".join(matrix_axes) + "\n"

        return graph


def projectile_helper(speed, height, angle):
    """
    This function is a helper for creating a Projectile object, calculating its coordinates,
    and creating a Graph object for visualizing its trajectory.

    :param speed: The speed of the projectile in m/s.
    :param height: The height of the projectile in m.
    :param angle: The angle of elevation of the projectile in degrees.
    """
    # Create a Projectile object with the given speed, height, and angle
    ball = Projectile(speed, height, angle)
    # Print the Projectile object's representation
    print(ball)
    # Calculate the coordinates of the projectile's trajectory
    coordinates = ball.calculate_all_coordinates()
    # Create a Graph object from the coordinates
    graph = Graph(coordinates)
    # Print the table of coordinates
    print(graph.create_coordinates_table())
    # Print the visual representation of the trajectory
    print(graph.create_trajectory())
