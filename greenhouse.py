#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 19:37:28 2023

Create a GUI to display menu of options/buttons.
Create a visualtion of the data
Create a animated line graph of the co2 values over time.
pip3.10 install pandas  
python3.10 -m pip install matplotlib
@author: terrydennison
"""

import csv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import ttk
import tkinter


num = 0
us_data = ('/home/earl/Desktop/data_project/co2_data.csv')
doc_reader = pd.read_csv(us_data)

row_year = (doc_reader.loc[:]['Year'])
row_population = (doc_reader.loc[:]['Population'])
row_gdp = (doc_reader.loc[:]['GDP'])
row_co2 = (doc_reader.loc[:]['CO2'])
row_coal_co2 = (doc_reader.loc[:]['Coal CO2'])

# print(max(row_co2))

# plt.plot(row_year,row_co2)
# plt.show()

m_gui = Tk()
m_gui.geometry('1600x800')

gui_label = ttk.Label(master=m_gui, text='\tUSA Greenhouse Data \n\t(1800-2021)',
                      font=('Sans Serif', 23, 'bold')).grid(column=1, row=0, pady=30)

cat_vals=['Population', 'GDP', 'CO2', 'Coal CO2']
cat_var = StringVar()
cat_label = ttk.Label(master=m_gui, text="Category").grid(column=0, row=1)
cat_select = ttk.Combobox(master=m_gui, values=cat_vals, state='readonly', textvariable=cat_var).grid(column=0, row=2, padx=20)


vis_vals=[ 'Line', 'Bar', 'Pie']
vis_var = tkinter.StringVar()
vis_label = ttk.Label(master=m_gui, text="Visualize As:").grid(column=1, row=1)
vis_select = ttk.Combobox(master=m_gui, values=vis_vals, state='readonly', textvariable=vis_var).grid(column=1, row=2, padx=20)

scale_vals=['Per 10 years', 'Per 20 years', 'Per 30 years']
x_var = tkinter.StringVar()
x_label = ttk.Label(master=m_gui, text="Scale by Years").grid(column=2, row=1)
x_select = ttk.Combobox(master=m_gui, values=scale_vals, state='readonly', textvariable=x_var).grid(column=2, row=2,padx=20)
var= StringVar()
data_label = ttk.Label(master=m_gui, text='Data', font=(
    'Sans Serif', 20, 'bold', 'underline',)).grid(column=3, row=0)


high_box = ttk.Label(master=m_gui, text='High:', font=(
    'Sans Serif', 16, 'bold')).grid(column=2, row=4)
low_box = ttk.Label(master=m_gui, text='Low:', font=(
    'Sans Serif', 16, 'bold')).grid(column=2, row=5)


vis = ttk.Button(master=m_gui, text="Visualize", width=30,
                 command=lambda: [select_visual()]).grid(column=0, row=7)

def select_visual():

    fig = Figure(figsize=(3, 3), dpi=100)
    ax1 = fig.add_subplot(111)
    canvas = FigureCanvasTkAgg(fig, master=m_gui)

    # if cat_var.get() in cat_vals and vis_var.get() == 'Line':
    #     ax1.plot(row_year,row_population)
    #     canvas.get_tk_widget().grid(column=0, row=8)
    # if cat_var.get() in cat_vals and vis_var.get() in 'Bar':
    #     ax1.bar(row_year, row_population)
    #     canvas.get_tk_widget().grid(column=0, row=8)
    # if cat_var.get() in cat_vals and vis_var.get() in 'Pie':
    #     ax1.pie(x=row_co2,data=np.array(list(row_population[:])))
    #     canvas.get_tk_widget().grid(column=0, row=8)        

    if cat_var.get() == 'Population' and vis_var.get() == 'Line':
        ax1.plot(row_year,row_population)
        canvas.get_tk_widget().grid(column=0, row=8)
    if cat_var.get() == 'GDP' and vis_var.get() == 'Line':
        ax1.plot(row_year,row_gdp)
        canvas.get_tk_widget().grid(column=0, row=8)

    if cat_var.get() in cat_vals and vis_var.get() in 'Bar':
        ax1.bar(row_year, row_population)
        canvas.get_tk_widget().grid(column=0, row=8)
    if cat_var.get() in cat_vals and vis_var.get() in 'Pie':
        ax1.pie(x=row_co2,data=np.array(list(row_population[:])))
        canvas.get_tk_widget().grid(column=0, row=8)        

    print(str(cat_var.get()).strip("/';`"))
    


m_gui.mainloop()
