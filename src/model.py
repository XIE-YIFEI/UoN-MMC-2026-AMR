import numpy as np
from constants import *

def amr_ode(y, t, params):
    # Unpack the 8 groups of people
    # PU = Clean, PN = Normal bug, PR = Superbug, HC = Dirty hands
    PU1, PN1, PR1, HC1, PU2, PN2, PR2, HC2 = y
    
    # Healthcare workers (assuming we have a fixed number of them)
    HU1 = 5 - HC1
    HU2 = 15 - HC2
    
    # --- Ward 1: ICU Math ---
    # People coming in + clearing the bug
    # Minus people getting sick + leaving + moving to ward 2
    dPU1 = (LAMBDA[0] * (1-M_R)) + (GAMMA + params['tau1'])*PN1 + GAMMA*PR1 \
           - params['beta1']*HC1*PU1 - (DELTA[0] + params['nu'])*PU1
    
    # Normal bugs (keeping it simple: they turn into clean patients)
    dPN1 = 0 - (GAMMA + params['tau1'] + DELTA[0] + params['nu'])*PN1
    
    # Superbug patients
    dPR1 = (LAMBDA[0] * M_R) + params['beta1']*HC1*PU1 \
           - (GAMMA + DELTA[0] + params['nu'])*PR1
           
    # Doctors getting dirty hands
    dHC1 = 0.1*(PN1 + PR1)*HU1 - params['eta1']*HC1
    
    # --- Ward 2: General Medicine Math ---
    # Note: We add the guys moving from the ICU here
    dPU2 = (LAMBDA[1] * (1-M_R)) + params['nu']*PU1 + (GAMMA + params['tau2'])*PN2 + GAMMA*PR2 \
           - params['beta2']*HC2*PU2 - DELTA[1]*PU2
           
    dPN2 = params['nu']*PN1 - (GAMMA + params['tau2'] + DELTA[1])*PN2
    
    dPR2 = (LAMBDA[1] * M_R) + params['nu']*PR1 + params['beta2']*HC2*PU2 \
           - (GAMMA + DELTA[1])*PR2
           
    dHC2 = 0.1*(PN2 + PR2)*HU2 - params['eta2']*HC2
    
    # Send all the math back
    return [dPU1, dPN1, dPR1, dHC1, dPU2, dPN2, dPR2, dHC2]