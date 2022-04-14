from tkinter import *
import tkinter 
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
import matplotlib.pyplot as plt

# https://stackoverflow.com/questions/63152444/how-do-i-create-a-live-graph-with-cpu-data-in-tkinter
def plot(): 
    plt.style.use("dark_background")

    
    fig = Figure(figsize = (5, 5), 
                 dpi = 100) 
  
    
    y = [i**2 for i in range(101)] 
  
    
    plot1 = fig.add_subplot(111) 

    plot1.plot(y) 
  
    frame = tkinter.Frame(window)
    frame.place(x=0, y=0)
    canvas = FigureCanvasTkAgg(fig, 
                               master = frame)   
    canvas.draw() 

    
    canvas.get_tk_widget().pack()
  
    
    #toolbar = NavigationToolbar2Tk(canvas, 
                                  # window) 
    #toolbar.update() 
  
      
window = Tk() 
  
window.title('Plotting in Tkinter') 
  
window.geometry("500x500") 
  
"""plot_button = Button(master = window,  
                     command = plot, 
                     height = 2,  
                     width = 10, 
                     text = "Plot") 
  
plot_button.pack() 
"""
plot() 
window.mainloop() 