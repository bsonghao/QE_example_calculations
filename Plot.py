import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
import sys
import Bands as bd

#sym=bd.Symmetries('bandx.out')
#print(sym)
bd.bndplot('Li2O2_bands.dat.gnu',8.02155,'bandx.out',plt,label=[r'$\Gamma$', 'A','K',r'$\Gamma$','A','H','K',r'$\Gamma$','M','L','A'])
