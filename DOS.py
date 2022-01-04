import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Plot_dos(file_name):
    # Plot_dos read in .dos file generate by QE calculation make a dos plot
    DOS=pd.read_fwf(file_name,index=False)
   # print(DOS.head())
    DOS.iloc[:,0]=np.arange(0.,40.01,0.01)
    plt.plot(DOS.iloc[:,0],DOS.iloc[:,1])
    plt.xlabel('E(eV)',fontsize=18)
    plt.ylabel('DOS(E)',fontsize=18)
    plt.title('Plot of Density of State(DOS) of Li2O2 Feher crystal',fontsize=30)
    plt.show()
    

