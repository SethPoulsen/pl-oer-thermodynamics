import random
import numpy as np
import pandas as pd
import prairielearn as pl

def generate(data):
    
    # SI or English units, find mdot or Wdot
    
    SIUnits = random.choice([0,1])
    givenW = random.choice([0,1])

    if SIUnits:
        df = pd.read_csv("clientFilesQuestion/IdealGasAir_Tscale_SI_A22_UTF8_all.csv")
        m = len(df)
        select = np.random.randint(0,m-3)
        T1 = df["$T$ (K)"].iloc[select] # K
        h1 = df["$h$ (kJ/kg)"].iloc[select] # kJ/kg
        delta = random.randint(1,3) # amount to skip in Tables
        T2 = df["$T$ (K)"].iloc[select+delta] # K
        h2 = df["$h$ (kJ/kg)"].iloc[select+delta] # kJ/kg
        P1 = 1 # Could fix to be isentropic using p_r if needed # Extra informatoin
        P2 = random.randint(2,7) # bar # Extra info
        
        mdot = round(random.uniform(1,10),1) # kg/s
        Wdot = round(mdot*(h1-h2),1) # kW since h in kJ/kg
        
        data['params']['TUnits'] = 'K'
        data['params']['PUnits'] = 'bar'
        mdotUnits = 'kg/s'
        WdotUnits = 'kW'
        table = 'A-22'

    else: #English
        df = pd.read_csv("clientFilesQuestion/IdealGasAir_Tscale_English_A22E_UTF8_All.csv")
        m = len(df)
        select = np.random.randint(0,m-3)
        T1 = df["$T$ ($^{\circ}$R)"].iloc[select] 
        h1 = df["$h$ (Btu/lb)"].iloc[select] 
        delta = random.randint(1,3)
        T2 = df["$T$ ($^{\circ}$R)"].iloc[select+delta] # K
        h2 = df["$h$ (Btu/lb)"].iloc[select+delta]
        P1 = 2000 # lbf/ft^2 # Extra information
        P2 = random.randint(2001,7000) # lbf/ft^2 # Extra info
        Wdot = -1*random.choice([1,2,4,8,9])*100000 # ft-lbf/s, negative b/c compressor
        mdot = round(Wdot/(h1-h2)/778.167,1) # Btu/s = 778.167 ft-lbf/s, 1 horsepower = 550 ft-lbf/s
        
        data['params']['TUnits'] = '$^{\circ}R$'
        data['params']['PUnits'] = 'lbf/ft$^2$'
        mdotUnits = 'lb/s'
        WdotUnits = 'ft-lbf/s'
        table = 'A-22E'
        
    if givenW:
        data['params']['solve'] = '$\dot{m}$'
        data['params']['units'] = mdotUnits
        data['correct_answers']['ans1'] = mdot
        if SIUnits: # ad hoc Casework for SI or English units -- English displaying x10^5
            qSetup = 'If the required power to the compressor, $\dot{W}$, is ' + str(Wdot) + " " + str(WdotUnits) + ', find the inlet mass flow rate $\dot{m}$ in ' + str(mdotUnits) + "." 
        else:
            qSetup = 'If the required power to the compressor, $\dot{W}$, is ' + str(Wdot) + '$\cdot$ ' + str(WdotUnits) + ', find the inlet mass flow rate $\dot{m}$ in ' + str(mdotUnits) + "." 
    else:
        data['params']['solve'] = '$\dot{W}$'
        data['params']['units'] = WdotUnits
        data['correct_answers']['ans1']  = Wdot
        qSetup = 'If the inlet mass flow rate to the compressor, $\dot{m}$, is ' + str(mdot) + ' ' + str(mdotUnits) + ', find the required power $\dot{W}$ in ' + str(WdotUnits) + "." 
        

    data['params']['T1'] = str(T1)
    data['params']['T2'] = str(T2)
    data['params']['P1'] = str(P1)
    data['params']['P2'] = str(P2)
    data['params']['table'] = table
    data['params']['question_setup'] = qSetup