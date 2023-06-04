import matplotlib.pyplot as plt
from tkinter import *

from solar import Solar,Sun,Planet

solarsys = Solar(400, projection_2d=True)

sun = Sun(solarsys)
planets = []

class Window():
    def __init__(self,win):
        self.win = win
        self.win.title("Solar System Simulator")
        self.win.geometry("900x900")

        self.mass = 0
        self.x_pos = 0
        self.y_pos = 0
        self.z_pos = 0
        self.x_vel = 0
        self.y_vel = 0
        self.z_vel = 0

        Label(self.win, text="Mass").grid(row=0,column=0)
        self.mass_entry = Entry(self.win, width = 5)
        self.mass_entry.grid(row=0, column=1)

        Label(self.win, text="x-position").grid(row=1,column=0)
        self.xpos_entry = Entry(self.win, width = 5)
        self.xpos_entry.grid(row=1, column=1)
        
        Label(self.win, text="y-position").grid(row=2,column=0)
        self.ypos_entry = Entry(self.win, width = 5)
        self.ypos_entry.grid(row=2, column=1)

        Label(self.win, text="z-position").grid(row=3,column=0)
        self.zpos_entry = Entry(self.win, width = 5)
        self.zpos_entry.grid(row=3, column=1)

        Label(self.win, text="x-velocity").grid(row=4,column=0)
        self.xvel_entry = Entry(self.win, width = 5)
        self.xvel_entry.grid(row=4, column=1)

        Label(self.win, text="y-velocity").grid(row=5,column=0)
        self.yvel_entry = Entry(self.win, width = 5)
        self.yvel_entry.grid(row=5, column=1)

        Label(self.win, text="z-velocity").grid(row=6,column=0)
        self.zvel_entry = Entry(self.win, width = 5)
        self.zvel_entry.grid(row=6, column=1)

        button1 = Button(self.win, text="update", command = self.update_values)
        button1.grid(row=7, column=0)
        self.win.bind("<Return>", self.update_values)
        pass

    def update_values(self, event=None):
        self.mass = float(self.mass_entry.get())
        self.x_pos = float(self.xpos_entry.get())
        self.y_pos = float(self.ypos_entry.get())
        self.z_pos = float(self.zpos_entry.get())
        self.x_vel = float(self.xvel_entry.get())
        self.y_vel = float(self.yvel_entry.get())
        self.z_vel = float(self.zvel_entry.get())

        #// appending user input into the solar system sim
        planets.append(Planet(solarsys,mass=self.mass, position=(self.x_pos, self.y_pos, self.z_pos),velocity=(self.x_vel,self.y_vel,self.z_vel)))

        while True:
            solarsys.update_all()
            solarsys.draw_all()
            solarsys.calculate_all_body_interactions()

def main():
    win = Tk()
    gui = Window(win)
    gui.win.mainloop()

main()