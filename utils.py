import qsharp
import numpy as np
from PhaseEstimation import run

def get_p_chapeau(proba, shots):
    return proba[1]/shots

def get_phi_chapeau(p_chapeau, oracles):
    return (2 / oracles) * (np.arcsin(np.sqrt(p_chapeau)) - (np.pi/4))

def get_precision(phi_chapeau, phi):
    return abs(phi_chapeau - phi)

def n_run(nShots, phi, oraclePower, nb_run):
    r = []
    for i in range(nb_run):
        my_run = run.simulate(nShots=nShots, phi=phi, oraclePower=oraclePower)
        r.append(get_precision(get_phi_chapeau(get_p_chapeau(my_run, nShots), oraclePower), phi))
    return np.mean(r)