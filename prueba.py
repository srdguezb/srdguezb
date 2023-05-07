# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 11:18:23 2022

@author: srdguezb
"""

#%%
import numpy as np
import matplotlib.pylab as pl

#%%
Vmin = 0
Vmax = 5
Vpp = Vmax - Vmin
Vmedia = (Vmax+Vmin) / 2
T = 2
nbits = 2
LSB = (Vmax - Vmin) / (2**nbits -1)

t = np.linspace(0, T, 100)
f = Vmedia + Vpp/2 * np.sin(2*np.pi*t/T)
error = np.zeros(np.shape(t))
fdigital = np.zeros(np.shape(t))

fig1,ax1 = pl.subplots(num=1, figsize=(3,3), dpi=200,
                     clear='True', facecolor='w', edgecolor='k')
l1 = ax1.plot(t, f, c='b', lw=.5, ls='-',
             marker='o', ms=0, markevery=1, label = 'seno vs t')
ax1.grid(True)
ax1.grid(which='minor', alpha=0.2)
ax1.grid(which='major', alpha=0.5)
ax1.legend(loc=(.5, .7), fontsize=10, ncol=1,  handletextpad=0.1,
          columnspacing=1.0, frameon=False)
ax1.set_xlabel('tiempo', color='blue')


#%% Forma 1: Desde la definición

marcas = np.zeros(2**nbits)
marcas[0] = Vmin
marcas[1:2**nbits] = marcas[0] + LSB * np.arange(1, 2**nbits)
rangos = np.zeros((2**nbits,2))
rangos[0,0], rangos[0,1] = Vmin, Vmin+LSB/2
rangos[1:2**nbits-1,1] = rangos[0,1] + LSB * np.arange(1, 2**nbits-1)
rangos[2**nbits-1,1] = Vmax
rangos[1:2**nbits,0] = rangos[0:2**nbits-1,1]

fig2,ax2 = pl.subplots(num=2, figsize=(2,2), dpi=200,
                     clear='True', facecolor='w', edgecolor='k')
l2 = ax2.plot((rangos[:,0], rangos[:,1]), (marcas, marcas), c='b', lw=1.5, ls='-',
             marker='o', ms=0, markevery=1, label = 'rangos')
ax2.grid(True)
ax2.grid(which='minor', alpha=0.2)
ax2.grid(which='major', alpha=0.5)
ax2.set_xlabel('Voltaje analógico', color='blue')
ax2.set_ylabel('Marca asignada', color='blue')


for i,valor in enumerate(f):
    intervalo = 0
    encontrado = False
    while not(encontrado):
        if valor >= rangos[intervalo,0] and valor <= rangos[intervalo,1]:
            encontrado = True
        else:
            intervalo +=1
    error[i] = valor - marcas[intervalo]
    fdigital[i] = marcas[intervalo]

fig3,ax3 = pl.subplots(2,1, sharex=True, num=3, figsize=(2,2), dpi=200,
                     clear='True', facecolor='w', edgecolor='k')

l301 = ax3[0].plot(t, f, c='b', lw=1.5, ls='-',
             marker='o', ms=0, markevery=1)
l302 = ax3[0].plot(t, fdigital, c='r', lw=0.5, ls='-',
             marker='o', ms=0, markevery=1)

ax3[0].grid(True)
ax3[0].grid(which='minor', alpha=0.2)
ax3[0].grid(which='major', alpha=0.5)
ax3[0].set_ylabel('seno', color='blue')

l31 = ax3[1].plot(t, error, c='b', lw=1.5, ls='-',
             marker='o', ms=0, markevery=1)
ax3[1].grid(True)
ax3[1].grid(which='minor', alpha=0.2)
ax3[1].grid(which='major', alpha=0.5)
ax3[1].set_ylabel('error', color='blue')


#%% Forma 2: La sencilla
intervalos2 = np.round((f+np.abs(Vmin))/LSB)
intervalos2 = intervalos2.astype(int)
fdigital2 = marcas[intervalos2]
error2 = f - fdigital2

fig4,ax4 = pl.subplots(2,1, sharex=True, num=4, figsize=(3,3), dpi=300,
                     clear='True', facecolor='w', edgecolor='k')

l401 = ax4[0].plot(t, f, c='b', lw=1.5, ls='-',
             marker='o', ms=0, markevery=1)
l402 = ax4[0].plot(t, fdigital2, c='k', lw=1.5, ls='-',
             marker='o', ms=0, markevery=1)

ax4[0].grid(True)
ax4[0].grid(which='minor', alpha=0.2)
ax4[0].grid(which='major', alpha=0.5)
ax4[0].set_ylabel('seno', color='blue')

l41 = ax4[1].plot(t, error2, c='k', lw=1.5, ls='-',
             marker='o', ms=0, markevery=1)
ax4[1].grid(True)
ax4[1].grid(which='minor', alpha=0.2)
ax4[1].grid(which='major', alpha=0.5)
ax4[1].set_ylabel('error2', color='blue')

# %%
