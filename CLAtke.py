"""
Illustration du cours Couche limite atmospherique dispense par Olivier THUAL
Toulouse INP-ENSEEIHT - Departement Hydraulique et méacinque des fluides
3eme annee option Sciences de l'eau et de l'environnement

Aurelien LINE 2018/11/11
"""

# -----------------------------------------------------------------------------
# Cas etudie : Ecoulement sur un massif montagneux
# Refroidissement d'une vallee la nuit ? 2750m -> 750m sur 40km
# (inspire de la Vallee d'Aure)
# 16h -> 7h
#  0.0km, alti : 2750m, temp : 6 -> 3
#  2.5km, alti : 1750m
# 10.0km, alti : 1500m
# 17.5km, alti : 1000m
# 22.5km, alti :  850m
# 40.0km, alti :  750m, temp : 18 -> 12
# -----------------------------------------------------------------------------

# bibliotheques ---------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

# parametres du probleme ------------------------------------------------------
thr =                           # temperature potentielle de reference
ug = 10 # 0 ?
thg =
tmax =
nt =
L = 40000                       # longueur
nx = 400
"""
l =                             # largeur
ny =
"""
H = 4000                        # hauteur maximale
nz = 100
z0 = 40                         # hauteur de rugosite

c1 = 1
c2 = 1
c3 = 1

# parametres physiques fixes --------------------------------------------------
g = 9.81                        # constante gravitationelle
k = 0.41                        # constante de VON KARMAN

# conditions aux limites ------------------------------------------------------
ub0 = 0
ubH = ug
thb0 = thr
thbH = thg
debdz0 = 0
debdzH = 0

# calculs preliminaires
z = np.linspace(0, H, nz)
dt = tmax/nt
dx = L/nx
"""
dy = l/ny
"""
dz = H/nz
us = k * ug / np.log(H/z0) # comprendre d'ou vient cette expression !
u0 = us / k * np.log(z/z0)      # profil de vitesse initial
thb = thb0 + (thg-thb0) * (z-z0) / (H-z0)
eb = us + 0 * z(1:nz)
