WF = ["Ammonia","Propane","n-Butane","Isobutane","Dichlorodifluoromethane","Chlorodifluoromethane","R-134a"]

path = "/home/jaden-gillespie/Desktop/HeatPump/NIST_SAT"




def main () :
    print(prompt()) 
    return 0 


def prompt () : #select and return the selected substance 
    
    for i in range(len(WF)) : 
        print(i+1,WF[i])
    
    print() 
    return WF[int(input("Input the working fluid by Number: \n"))-1] 


def txt_opn (fluid) : #open and parse NIST data, return (x,y) 
    data = open(path+fluid+".txt", "r")
    return 0

if __name__ == "__main__" :
    print(main())
    