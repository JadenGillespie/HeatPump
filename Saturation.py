import pandas as pd 
import matplotlib.pyplot as plt

###Constants 
WF = [
      "Ammonia",
      "Propane",
      "n-Butane",
      "Isobutane",
      "Dichlorodifluoromethane",
      "Chlorodifluoromethane",
      "R-134a",
      "QUIT"
      ]

PATH = "/home/jaden-gillespie/Desktop/HeatPump/NIST_SAT/"
PATH_PLT = "/home/jaden-gillespie/Desktop/HeatPump/Plots/"

HEADERS = [
    "Temperature (C)",
    "Pressure (MPa)",
    "Density (l, kg/m3)",
    "Volume (l, m3/kg)",
    "Internal Energy (l, kJ/mol)",
    "Enthalpy (l, kJ/mol)",
    "Entropy (l, J/mol*K)",
    "Cv (l, J/mol*K)",
    "Cp (l, J/mol*K)",
    "Sound Speed (l, m/s)",
    "Joule-Thomson (l, K/MPa)",
    "Viscosity (l, uPa*s)",
    "Thermal Conductivity (l, W/m*K)",
    "Surface Tension (N/m)",
    "Density (v, kg/m3)",
    "Volume (v, m3/kg)",
    "Internal Energy (v, kJ/mol)",
    "Enthalpy (v, kJ/mol)",
    "Entropy (v, J/mol*K)",
    "Cv (v, J/mol*K)",
    "Cp (v, J/mol*K)",
    "Sound Speed (v, m/s)",
    "Joule-Thomson (v, K/MPa)",
    "Viscosity (v, uPa*s)",
    "Thermal Conductivity (v, W/m*K)"
]

TEMP = 0
ENTR_L = 6
ENTR_V = 18



def main () :
    while (True) :
        working_fluid = prompt()
        if working_fluid == "QUIT" :
            break 
        sat_data = txt_opn(working_fluid) 
        TS_Plot(sat_data, working_fluid) 
        print()
        print()
        
    rec_TS()    

    return 0 

def prompt () : #select and return the selected substance 
    
    for i in range(len(WF)) : 
        print(i+1,WF[i])
    print() 
    return WF[int(input("Input the working fluid by Number: \n"))-1] 


def txt_opn (fluid) : #open and parse NIST data, return (x,y) 
    data = pd.read_table(PATH+fluid+".txt", sep='\s+', header = None, skiprows=1) #messy headers removed
    data.columns = HEADERS
    return data 

def TS_Plot (data, fluid) : 
    
    if fluid == WF[0] :
        color = 'blue' 
    elif fluid == WF[1]:
        color = 'green'
    elif fluid == WF[2]: 
        color = 'red' 
    elif fluid == WF[3]:
        color = 'cyan' 
    elif fluid == WF[4] :
        color = 'magenta' 
    elif fluid == WF[5]:
        color = 'yellow' 
    elif fluid == WF[6] :
        color = 'orange'
    
    plt.plot(data[HEADERS[ENTR_L]], data[HEADERS[TEMP]], label = fluid, color = color)
    plt.plot(data[HEADERS[ENTR_V]], data[HEADERS[TEMP]], color=color)
    plt.title("T-S of "+fluid) 
    plt.xlabel("Entropy (J/mol*K)")
    plt.ylabel(HEADERS[TEMP]) 
    plt.grid(True) 
    plt.legend()
    plt.savefig(PATH_PLT+"T-S of "+fluid)
    plt.show()

def rec_TS () : 
    
    for i in range(len(WF)-1) : 
        
        fluid = WF[i]
        data = txt_opn(fluid)
        
        if fluid == WF[0] :
            color = 'blue' 
        elif fluid == WF[1]:
            color = 'green'
        elif fluid == WF[2]: 
            color = 'red' 
        elif fluid == WF[3]:
            color = 'cyan' 
        elif fluid == WF[4] :
            color = 'magenta' 
        elif fluid == WF[5]:
            color = 'yellow' 
        elif fluid == WF[6] :
            color = 'orange'
    
        plt.plot(data[HEADERS[ENTR_L]], data[HEADERS[TEMP]], label = fluid, color = color)
        plt.plot(data[HEADERS[ENTR_V]], data[HEADERS[TEMP]], color=color)
        plt.title("T-S of Fluids") 
        plt.xlabel("Entropy (J/mol*K)")
        plt.ylabel(HEADERS[TEMP]) 
        plt.grid(True) 
        plt.legend()
        
    plt.savefig(PATH_PLT+"T-S")
    plt.show()     
    
if __name__ == "__main__" :
    print(main()) 
    
