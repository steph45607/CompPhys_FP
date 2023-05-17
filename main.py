import matplotlib.pyplot as plt
from solar import Solar,SolarSystemBody,Sun,Planet

solarsys = Solar(400, projection_2d=True)

sun = Sun(solarsys)
planets = (
    Planet(
        solarsys,
        position=(150, 50, 0),
        velocity=(0, 5, 5),
    ),
    Planet(
        solarsys,
        mass=20,
        position=(100, -50, 150),
        velocity=(5, 0, 0)
    )
)
while True:
    solarsys.calculate_all_body_interactions()
    solarsys.update_all()
    solarsys.draw_all()