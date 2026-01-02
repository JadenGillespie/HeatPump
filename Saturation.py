import pandas as pd 
import matplotlib.pyplot as plt

###Constants 
WF = ["Ammonia","Propane","n-Butane","Isobutane","Dichlorodifluoromethane","Chlorodifluoromethane","R-134a"]
PATH = "/home/jaden-gillespie/Desktop/HeatPump/NIST_SAT"

def main () :
    print(prompt()) 
    return 0 


def prompt () : #select and return the selected substance 
    
    for i in range(len(WF)) : 
        print(i+1,WF[i])
    
    print() 
    return WF[int(input("Input the working fluid by Number: \n"))-1] 


def txt_opn (fluid) : #open and parse NIST data, return (x,y) 
    df = pd.read_table(PATH+fluid, delim_whitespace=True, header = 0)

if __name__ == "__main__" :
    print(main())
    