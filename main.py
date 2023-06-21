import matplotlib.pyplot as plt
from tkinter import *

from solar import Solar,Sun,Planet

solarsys = Solar(400, projection_2d=False)

sun = Sun(solarsys)
planets = []

background= "#062c43"
fontcolor= "#ced7e0"

#? Class for user input window 
class Window():
    def __init__(self,win):
        self.win = win
        self.win.title("Solar System Simulator")
        self.win.config(bg=background)
        self.win.geometry("800x650")

        self.mass = 0
        self.x_pos = 0
        self.y_pos = 0
        self.z_pos = 0
        self.x_vel = 0
        self.y_vel = 0
        self.z_vel = 0

        #// label for title
        Label(self.win, text="Welcome to the best solar system simulation", font=("Roboto", 15), bg=background, fg = fontcolor).grid(row=0,column=0, columnspan=3)

        #// label for mass
        Label(self.win, text="Mass (mass of the planet in ...)", bg=background, fg = fontcolor).grid(row=1,column=0)
        self.mass_entry = Entry(self.win, width = 5)
        self.mass_entry.grid(row=1, column=1)
        Label(self.win, text="x 10^30 kg", bg=background, fg = fontcolor).grid(row=1,column=2)

        #// label for x-position
        Label(self.win, text="x-position (starting point of the planet from x-axis)", bg=background, fg = fontcolor).grid(row=2,column=0)
        self.xpos_entry = Entry(self.win, width = 5)
        self.xpos_entry.grid(row=2, column=1)
        
        #// label for y-position
        Label(self.win, text="y-position (starting point of the planet from y-axis)", bg=background, fg = fontcolor).grid(row=3,column=0)
        self.ypos_entry = Entry(self.win, width = 5)
        self.ypos_entry.grid(row=3, column=1)

        #// label for z-position
        Label(self.win, text="z-position (starting point of the planet from z-axis)", bg=background, fg = fontcolor).grid(row=4,column=0)
        self.zpos_entry = Entry(self.win, width = 5)
        self.zpos_entry.grid(row=4, column=1)

        #// label for x-velocity
        Label(self.win, text="x-velocity (the velocity the planet moving on x-axis)", bg=background, fg = fontcolor).grid(row=5,column=0)
        self.xvel_entry = Entry(self.win, width = 5)
        self.xvel_entry.grid(row=5, column=1)

        #// label for y-velocity
        Label(self.win, text="y-velocity (the velocity the planet moving on y-axis)", bg=background, fg = fontcolor).grid(row=6,column=0)
        self.yvel_entry = Entry(self.win, width = 5)
        self.yvel_entry.grid(row=6, column=1)

        #// label for z-velocity
        Label(self.win, text="z-velocity (the velocity the planet moving on z-axis)", bg=background, fg = fontcolor).grid(row=7,column=0)
        self.zvel_entry = Entry(self.win, width = 5)
        self.zvel_entry.grid(row=7, column=1)

        #// button to update the graph
        button1 = Button(self.win, text="Add planet", command = self.update_values, bg=background, fg = fontcolor)
        button1.grid(row=8, column=2)
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

        #// altering the graph with new user inputs and keep the planets rotating
        while True:
            solarsys.update_all()
            solarsys.draw_all()
            solarsys.calculate_all_body_interactions()

#? Driver function
def main():
    #// initializing tkinter

    win = Tk()
    #// making window for input
    gui = Window(win)
    #// looping the window
    gui.win.mainloop()

#? Calling the driver function
if __name__ == "__main__":
    main()