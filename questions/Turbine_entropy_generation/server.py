import random
import numpy as np
import pandas as pd
import prairielearn as pl
import math

# This problem is tricky because Wdot, sigmadot variants only have one answer box, no intermediate step. 
# Also, Qdot is always negative for this problem, so heat is actully leaving the turbine, contrary to the diagram's arrow.

def generate(data):
    
    significant_digits = 4
    # Set problem units
    W=random.randint(10, 20)/10
    m=random.randint(110, 140)
    T_amb=27    #C

    df = pd.read_csv("clientFilesQuestion/SupHVaporTable_P20-100bar_SI.csv") 
    select1 = np.random.randint(1,21)
    p1 =df["$p$ (bar)"].iloc[select1]
    T1 =df["$T$ ($^{\circ}$C)"].iloc[select1]
    h1 = df["$h$ (kJ/kg)"].iloc[select1]
    s1 = df["$s$ (kJ/kg$\cdot$K)"].iloc[select1]

    df = pd.read_csv("clientFilesQuestion/SatVaporTable_Pscale_SI.csv")   
    select2 = np.random.randint(1,9)
    p2 = df["$p$ (bar)"].iloc[select2]
    h2 = df["$h_g$ (kJ/kg)"].iloc[select2]
    s2 = df["$s_g$ (kJ/kg$\cdot$K)"].iloc[select2]

    #Solution
    Q=(W*1000)-(m/60)*(h1-h2)
    sigma=(-Q/300)+(m/60)*(s2-s1)
    sigma=round(sigma, significant_digits - int(math.floor(math.log10(abs(sigma)))) - 1)

    Question=random.choice([0,1,2])
    if Question ==0:
        setup="producing power at a rate of " + str(W)+" MW"
        solve="$\\dot{\sigma}$"
        solveU="kW/K"
        ask="Determine the rate of entropy production, in kW/K"
        answer=sigma
    elif Question==1:
        setup="the rate of entropy generation is " + str(sigma)+" kW/K"
        solve="$\\dot{W}$"
        solveU="MW"
        ask="Determine the work done by the turbine, in MW"
        answer=W
    else: 
        setup="the rate of entropy generation is " + str(sigma)+" kW/K"
        solve="$\\dot{Q}$"
        solveU="kW"
        ask="Determine the rate of heat transfer, in kW"
        answer=Q
    
    
    data['params']['T1'] = T1
    data['params']['p1'] = p1/10
    data['params']['p2'] = p2*100
    data['params']['m'] = m
    data['params']['W'] = W
    
    data['params']['setup'] = setup
    data['params']['solve'] = solve
    data['params']['unit'] = solveU
    data['params']['ask'] = ask

    data['correct_answers']['ans'] = answer

  

