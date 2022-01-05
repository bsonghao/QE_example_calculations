import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
import sys
import Bands as bd

# sym=bd.Symmetries('bandx.out')
# print(sym)
bd.bndplot('LiO2_bands.dat.gnu',2.818,'bandx.out',\
plt,label=[r'$\Gamma$', 'A','K',r'$\Gamma$','A','H','K',r'$\Gamma$','M','L','A'],\
compound="LiO2")
