# Settings for the hospital math model
# Ward 1 is ICU, Ward 2 is General Medicine

# How many beds and how long people stay
BEDS = [15, 60]
STAY = [12, 5]  # in days
DELTA = [1/s for s in STAY]  # People leaving the hospital

# How many people come in (keeps the total number of patients steady)
LAMBDA = [BEDS[i] / STAY[i] for i in range(2)]

# Meds and spreading rates
TAU = [0.8, 0.4]     # How much antibiotics they use (80% and 40%)
BETA = [0.15, 0.1]   # Spreading chance when a doctor touches a patient
ETA = [0.4, 0.4]     # Starting hand washing score (40%)
GAMMA = 1/45         # Body fighting off the bug naturally (about 1.5 months)

# Starting rules from the prompt
M_R = 0.05           # 5% of new guys already have the superbug
TRANSFER_RATE = 0.1  # 10% move from ICU to normal beds