import itertools
import math
import matplotlib.pyplot as plt
from vectors import Vector

#? Class containing the solar system
class Solar:
    def __init__(self, size, projection_2d=False):
        self.size = size
        self.projection_2d = projection_2d
        self.bodies = []

        self.fig, self.ax = plt.subplots(
            1,
            1,
            subplot_kw = {'projection':'3d'},
            figsize = (self.size / 50, self.size / 50)
            
        )
        self.fig.tight_layout()
        if self.projection_2d:
            self.ax.view_init(10, 0)
        else:
            self.ax.view_init(0, 0)

    #* function to add a body/planet
    def add_body(self, body):
        self.bodies.append(body)

    #* function to update everything
    def update_all(self):
        self.bodies.sort(key=lambda item: item.position[0])
        for body in self.bodies:
            body.move()
            body.draw()
            body.draw_orbit()

    #* function to create graph
    def draw_all(self):
        #// setting limits to graph
        self.ax.set_xlim((-self.size / 2, self.size / 2))
        self.ax.set_ylim((-self.size / 2, self.size / 2))
        self.ax.set_zlim((-self.size / 2, self.size / 2))
        if self.projection_2d:
            self.ax.xaxis.set_ticklabels([])
            self.ax.yaxis.set_ticklabels([])
            self.ax.zaxis.set_ticklabels([])
        else:
            self.ax.axis(False)
        plt.pause(0.001)
        self.ax.clear()

    #* function to display physics
    def calculate_all_body_interactions(self):
        bodies_copy = self.bodies.copy()
        for idx, first in enumerate(bodies_copy):
            for second in bodies_copy[idx + 1:]:
                #// showing acceleration due to gravity
                first.accelerate_due_to_gravity(second)

#? Class containing the movements of planets
class SolarSystemBody:
    min_display_size = 4
    display_log_base = 2
    
    def __init__(
        self, solar_system, mass, position=(0, 0, 0), velocity=(0, 0, 0)):
        self.solar_system = solar_system
        self.mass = mass
        self.position = position
        self.velocity = Vector(*velocity)
        self.display_size = max(
            math.log(self.mass, self.display_log_base),
            self.min_display_size,
        )
        self.colour = "black"
        self.solar_system.add_body(self)
        
    #* function to make planets move
    def move(self):
        #// making the planets move
        self.position = (
            self.position[0] + self.velocity[0],
            self.position[1] + self.velocity[1],
            self.position[2] + self.velocity[2]
        )
    
    #* function to make orbital trace
    def draw_orbit(self):
        #// plotting the distance trace from the sun to individual planets
        self.solar_system.ax.plot(
            [self.position[0],self.velocity[0]],
            [self.position[1],self.velocity[1]],
            [self.position[2], self.velocity[2]], 
            color = (.5,.5,.5)
        )

    #* function to plot the planets
    def draw(self):
        #// plotting the planets
        self.solar_system.ax.plot(
            *self.position,
            markersize=self.display_size + self.position[0] / 30,
            marker="o",
            color=self.colour
        )
        #// plotting the shadows
        if self.solar_system.projection_2d:
            self.solar_system.ax.plot(
                self.position[0],
                self.position[1],
                -self.solar_system.size / 2,
                marker="o",
                markersize=self.display_size / 2,
                color=(.5, .5, .5),
            )

    #* function to simulate physics
    def accelerate_due_to_gravity(self, other):
        #// getting the distance of the planets with other planets/sun
        distance = Vector(*other.position) - Vector(*self.position)
        distance_mag = distance.get_magnitude()



        #// f = GM1M2/r^2
        #// G / Gravitational constant is not used because of the limitations of matplotlib
        force_mag = self.mass * other.mass / (distance_mag ** 2)
        force = distance.normalize() * force_mag

        reverse = 1

        for body in self, other:
            #// increasing the velocity when planets get close
            #// f = ma 
            #// a = f / m
            acceleration = force / body.mass
            body.velocity += acceleration * reverse
            #// changing the direction of the planet when completing a full rotation due to gravity
            reverse = -1

#? The sun class
class Sun(SolarSystemBody):
    def __init__(
        self, solar_system, mass= 10500, position=(0, 0, 0),velocity=(0, 0, 0)):
        super(Sun, self).__init__(solar_system, mass, position, velocity)
        self.colour = "yellow"

#? The planet class
class Planet(SolarSystemBody):
    #// iterating through the colors
    colors = itertools.cycle([(1, 0, 0), (0, 0, 1), (0, 1, 1)])

    def __init__(self, solar_system, mass=10, position=(0, 0, 0), velocity=(0, 0, 0)):
        super(Planet, self).__init__(solar_system, mass, position, velocity)
        self.colour = next(Planet.colors)