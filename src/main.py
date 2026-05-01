import os
import sys

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from constants import *
from model import amr_ode

# Time plan: run for 1 full year (365 days)
t = np.linspace(0, 365, 365)

# Pack our starting numbers into a dictionary
params = {
    'tau1': TAU[0], 'tau2': TAU[1],
    'beta1': BETA[0], 'beta2': BETA[1],
    'eta1': ETA[0], 'eta2': ETA[1],
    'nu': TRANSFER_RATE * DELTA[0]
}

# Start with mostly clean patients and just a few superbug ones
# The list is: [PU1, PN1, PR1, HC1, PU2, PN2, PR2, HC2]
y0 = [14, 0, 1, 0, 58, 0, 2, 0]

# ==========================================
# PART 1: The Baseline (Original Situation)
# ==========================================
# Let the math run!
sol = odeint(amr_ode, y0, t, args=(params,))

# Draw the baseline picture
plt.figure(figsize=(10, 5))
plt.plot(t, sol[:, 2], 'r-', label='Superbug Patients (ICU)')
plt.plot(t, sol[:, 6], 'b-', label='Superbug Patients (Normal Ward)')
plt.title('Baseline: Superbug Spread Over 12 Months')
plt.xlabel('Days')
plt.ylabel('Number of Patients')
plt.legend()
plt.grid(True, alpha=0.3)

# Save the picture to the right folder
save_dir = 'results/plots'
os.makedirs(save_dir, exist_ok=True) 
plt.savefig(f'{save_dir}/baseline_dynamics.png', dpi=300)
plt.show()  # <--- NOTE: You must close the pop-up window to see the next chart!


# ==========================================
# PART 2: Sensitivity Analysis (Hand Washing)
# ==========================================
# What if doctors wash their hands more? Let's test 20%, 40%, 60%, 80%
plt.figure(figsize=(10, 5))
hand_washing_scores = [0.2, 0.4, 0.6, 0.8]

# Loop through each score to see what happens
for score in hand_washing_scores:
    # Copy the original settings so we don't mess them up
    test_params = params.copy()
    
    # Change the hand washing score (eta) for both wards
    test_params['eta1'] = score
    test_params['eta2'] = score
    
    # Run the math again with the new score
    test_sol = odeint(amr_ode, y0, t, args=(test_params,))
    
    # Draw a line for this specific score (we only look at ICU to keep it clean)
    plt.plot(t, test_sol[:, 2], label=f'Hand Washing: {int(score*100)}%')

# Add titles and labels for the second picture
plt.title('What if doctors wash hands more? (ICU Superbug Patients)')
plt.xlabel('Days')
plt.ylabel('Number of Patients in ICU')
plt.legend()
plt.grid(True, alpha=0.3)

# Save the new picture
plt.savefig(f'{save_dir}/sensitivity_hand_washing.png', dpi=300)
plt.show()

# --- Quick check to make sure the math isn't crazy ---
total_pop_icu = sol[-1, 0:3].sum()
print(f"Quick Check: Total people in ICU at the end = {total_pop_icu:.2f} (Should be around 15)")