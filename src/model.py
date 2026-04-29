import numpy as np

def amr_ode(y, t, params):
    # Unpack state variables (8 states)
    # PU=Uncolonized, PN=Non-Resistant, PR=Resistant, HC=Contaminated HCW
    PU1, PN1, PR1, HC1, PU2, PN2, PR2, HC2 = y
    
    # HCW constants (assuming fixed number of HCWs)
    HU1 = 5 - HC1
    HU2 = 15 - HC2
    
    # --- Ward 1: ICU Equations ---
    # Influx: Admissions (minus AMR) + Clearance
    # Outflux: Infection + Discharge + Transfer
    dPU1 = (LAMBDA[0] * (1-M_R)) + (GAMMA + params['tau1'])*PN1 + GAMMA*PR1 \
           - params['beta1']*HC1*PU1 - (DELTA[0] + params['nu'])*PU1
    
    dPN1 = 0 - (GAMMA + params['tau1'] + DELTA[0] + params['nu'])*PN1 # Simplified: PN enters as PU
    
    dPR1 = (LAMBDA[0] * M_R) + params['beta1']*HC1*PU1 \
           - (GAMMA + DELTA[0] + params['nu'])*PR1
           
    dHC1 = 0.1*(PN1 + PR1)*HU1 - params['eta1']*HC1
    
    # --- Ward 2: General Medicine ---
    # Note: Added 'params['nu']*PX1' terms representing transfers from ICU
    dPU2 = (LAMBDA[1] * (1-M_R)) + params['nu']*PU1 + (GAMMA + params['tau2'])*PN2 + GAMMA*PR2 \
           - params['beta2']*HC2*PU2 - DELTA[1]*PU2
           
    dPN2 = params['nu']*PN1 - (GAMMA + params['tau2'] + DELTA[1])*PN2
    
    dPR2 = (LAMBDA[1] * M_R) + params['nu']*PR1 + params['beta2']*HC2*PU2 \
           - (GAMMA + DELTA[1])*PR2
           
    dHC2 = 0.1*(PN2 + PR2)*HU2 - params['eta2']*HC2
    
    return [dPU1, dPN1, dPR1, dHC1, dPU2, dPN2, dPR2, dHC2]