
# interface for importing an excel file
import tkinter as tk
from tkinter import filedialog
import pandas as pd

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue')
canvas1.pack()

def getExcel ():
    global df
    
    import_file_path = filedialog.askopenfilename()
    df = pd.read_excel (import_file_path)
    print (df)
    
browseButton_Excel = tk.Button(text='Import Excel File', command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=browseButton_Excel)

root.mainloop()


# Import a file that has a variable name
import pandas as pd
from pandas import DataFrame
import tkinter as tk 
 
root= tk.Tk()
  
canvas1 = tk.Canvas(root, width = 300, height = 300) # create the canvas
canvas1.pack()
  
entry1 = tk.Entry (root) # create the entry box
canvas1.create_window(150, 100, window=entry1)
  
def insert_number(): # add a function/command to be called by the button (i.e., button1 below)
    global x1 # add 'global' before the variable x1, so that you can use that variable outside of the command/function if ever needed 
    x1 = str(entry1.get()) # store the data input by the user as a variable x1 
 
    PATH = r'C:\Users\Ron\Desktop\Import into Python\Sales_' + x1 + '.csv' #(use "r" before the path string to address special character, such as '\'). Don't forget to put the file name at the end of the path + '.csv'
    read_sales = pd.read_csv (PATH)   #read the csv file using the 'PATH' varibale 
    df = DataFrame(read_sales,columns=['Client Name','Country','Product','Purchase Price','Date'])  # assign column names
    print (df)
 
button1 = tk.Button (root, text='Input date to import file (ddmmyyyy) ',command=insert_number, bg='green', fg='white') # button to call the 'insert_number' command above 
canvas1.create_window(150, 140, window=button1)
  
root.mainloop()


# Export Pandas DataFrame to a CSV file using Tkinter
import tkinter as tk
from tkinter import filedialog
from pandas import DataFrame

cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
        'Price': [22000,25000,27000,35000]
        }

df = DataFrame(cars, columns= ['Brand', 'Price'])


root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

def exportCSV ():
    global df
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    df.to_csv (export_file_path, index = False, header=True)

saveAsButton_CSV = tk.Button(text='Export CSV', command=exportCSV, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=saveAsButton_CSV)

root.mainloop()





# GUI to import csv
import tkinter as tk
from tkinter import filedialog
import pandas as pd

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

def getCSV ():
    global df
    
    import_file_path = filedialog.askopenfilename()
    df = pd.read_csv (import_file_path)
    print (df)
    
browseButton_CSV = tk.Button(text="      Import CSV File     ", command=getCSV, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=browseButton_CSV)

root.mainloop()





###########################################################
# how to create a tkinter GUI with the following components
###########################################################
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
 
root= tk.Tk()

# Canvas screen, where you can place items, such as labels and buttons

canvas1 = tk.Canvas(root, width = 800, height = 300)
canvas1.pack()

# Labels to display text on top of the Canvas

label1 = tk.Label(root, text='Graphical User Interface')
label1.config(font=('Arial', 20))
canvas1.create_window(400, 50, window=label1)

# Entry Boxes to allow users type values (3 entry boxes)

entry1 = tk.Entry (root)
canvas1.create_window(400, 100, window=entry1) 
  
entry2 = tk.Entry (root)
canvas1.create_window(400, 120, window=entry2) 
          
entry3 = tk.Entry (root)
canvas1.create_window(400, 140, window=entry3) 

# Functions to display Bar and Pie charts

def create_charts():
    global x1
    global x2
    global x3
    global bar1
    global pie2
    x1 = float(entry1.get())
    x2 = float(entry2.get())
    x3 = float(entry3.get())

    figure1 = Figure(figsize=(4,3), dpi=100) 
    subplot1 = figure1.add_subplot(111) 
    xAxis = [float(x1),float(x2),float(x3)] 
    yAxis = [float(x1),float(x2),float(x3)] 
    subplot1.bar(xAxis,yAxis, color = 'lightsteelblue') 
    bar1 = FigureCanvasTkAgg(figure1, root) 
    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=0)
      
    figure2 = Figure(figsize=(4,3), dpi=100) 
    subplot2 = figure2.add_subplot(111) 
    labels2 = 'Label1', 'Label2', 'Label3' 
    pieSizes = [float(x1),float(x2),float(x3)]
    my_colors2 = ['lightblue','lightsteelblue','silver']
    explode2 = (0, 0.1, 0)  
    subplot2.pie(pieSizes, colors=my_colors2, explode=explode2, labels=labels2, autopct='%1.1f%%', shadow=True, startangle=90) 
    subplot2.axis('equal')  
    pie2 = FigureCanvasTkAgg(figure2, root)
    pie2.get_tk_widget().pack()

def clear_charts(): #  'clear_charts' function will be called when the user clicks on the second button (i.e., 'button2') to clear the charts from the GUI
    bar1.get_tk_widget().pack_forget()
    pie2.get_tk_widget().pack_forget()

# Buttons to trigger the functions and exit the application
            
button1 = tk.Button (root, text=' Create Charts ',command=create_charts, bg='palegreen2', font=('Arial', 11, 'bold')) 
canvas1.create_window(400, 180, window=button1)

button2 = tk.Button (root, text='  Clear Charts  ', command=clear_charts, bg='lightskyblue2', font=('Arial', 11, 'bold'))
canvas1.create_window(400, 220, window=button2)

button3 = tk.Button (root, text='Exit Application', command=root.destroy, bg='lightsteelblue2', font=('Arial', 11, 'bold'))
canvas1.create_window(400, 260, window=button3)
 
root.mainloop()




#################################################
# How to Place Matplotlib Charts on a Tkinter GUI
#################################################


import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

data1 = {'Country': ['US','CA','GER','UK','FR'],
         'GDP_Per_Capita': [45000,42000,52000,49000,47000]
        }
df1 = DataFrame(data1,columns=['Country','GDP_Per_Capita'])


data2 = {'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
         'Unemployment_Rate': [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
        }
df2 = DataFrame(data2,columns=['Year','Unemployment_Rate'])


data3 = {'Interest_Rate': [5,5.5,6,5.5,5.25,6.5,7,8,7.5,8.5],
         'Stock_Index_Price': [1500,1520,1525,1523,1515,1540,1545,1560,1555,1565]
        }  
df3 = DataFrame(data3,columns=['Interest_Rate','Stock_Index_Price'])
 

root= tk.Tk() 
  
figure1 = plt.Figure(figsize=(6,5), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df1 = df1[['Country','GDP_Per_Capita']].groupby('Country').sum()
df1.plot(kind='bar', legend=True, ax=ax1)
ax1.set_title('Country Vs. GDP Per Capita')

figure2 = plt.Figure(figsize=(5,4), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df2 = df2[['Year','Unemployment_Rate']].groupby('Year').sum()
df2.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
ax2.set_title('Year Vs. Unemployment Rate')

figure3 = plt.Figure(figsize=(5,4), dpi=100)
ax3 = figure3.add_subplot(111)
ax3.scatter(df3['Interest_Rate'],df3['Stock_Index_Price'], color = 'g')
scatter3 = FigureCanvasTkAgg(figure3, root) 
scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax3.legend(['Stock_Index_Price']) 
ax3.set_xlabel('Interest Rate')
ax3.set_title('Interest Rate Vs. Stock Index Price')

root.mainloop()

