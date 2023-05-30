import matplotlib.pyplot as plt
from solar import Solar,Sun,Planet

solarsys = Solar(400, projection_2d=True)

sun = Sun(solarsys)
planets = []

n = int(input("How many planets do you want to add? "))

for i in range(n):
    m = int(input(f"Input planet {i+1}'s mass: "))
    px = int(input(f"Input planet {i+1}'s x-coordinate: "))
    py = int(input(f"Input planet {i+1}'s y-coordinate: "))
    pz = int(input(f"Input planet {i+1}'s z-coordinate: "))
    vx = int(input(f"Input planet {i+1}'s x-velocity: "))
    vy = int(input(f"Input planet {i+1}'s y-velocity: "))
    vz = int(input(f"Input planet {i+1}'s z-velocity: "))
    planets.append(Planet(solarsys,mass=m,position=(px,py,pz),velocity=(vx,vy,vz)))

print(planets)

while True:
    solarsys.calculate_all_body_interactions()
    solarsys.update_all()
    solarsys.draw_all()