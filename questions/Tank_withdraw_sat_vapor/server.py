import random
import numpy as np
import pandas as pd

def generate(data):

    #df = pd.read_csv("clientFilesQuestion/SatVaporTable_Tscale_SI.csv")
    #l = len(df)
    #select = np.random.randint(47,l-1)
    #h1 = df["$h_g$ (kJ/kg)"].iloc[select] # kJ/kg enthalpy inlet
    #x = random.randint(10,40) #m3/s

    #h1 = round(random.uniform(200,300), 2) 
    #select2 = np.random.randint(15,35)
    #h2 = round(0.9*df["$h_g$ (kJ/kg)"].iloc[select2] + 0.1*df["$h_f$ (kJ/kg)"].iloc[select2], 1) # kJ/kg enthalpy outlet 2
    #h2= round(random.uniform(100,200))# J enthalpy inlet
    #h3 = df["$h_g$ (kJ/kg)"].iloc[select2+5] # kJ/kg enthalpy outlet 3

    #m1 = round(random.uniform(4,15), 2) # kg/s mass flow rate inlet  #random.randint(2,7)
    #m2=(x/100)*m1
    #m3=round(m1-m2,2)
    
    #Q=random.randint(40,70)*10
    
    

    # Generate physically reasonable range of input variables
    unit = random.choice([0,1])
    if unit == 1: 
        V = random.randint(35,85)/10 # Volume in ft^3
        x1 = random.randint(1,4)/100
        df = pd.read_csv("clientFilesQuestion/SatVaporTable_Pscale_English.csv")
        select1 = np.random.randint(17,29)
        select2 = random.randint(37,46)
        P1=df["$p$ (lbf/in$^2$)"].iloc[select1] 
        P2=df["$p$ (lbf/in$^2$)"].iloc[select2] 
        hg1=df["$h_g$ (Btu/lb)"].iloc[select1]
        hg2=df["$h_g$ (Btu/lb)"].iloc[select2]
        vg1=df["$v_g$ (ft$^3$/lb)"].iloc[select1]
        vg2=df["$v_g$ (ft$^3$/lb)"].iloc[select2]
        vf1=df["$v_f$ (ft$^3$/lb)"].iloc[select1]
        vf2=df["$v_f$ (ft$^3$/lb)"].iloc[select2]
        uf1=df["$u_f$ (Btu/lb)"].iloc[select1]
        ug1=df["$u_g$ (Btu/lb)"].iloc[select1]
        uf2=df["$u_f$ (Btu/lb)"].iloc[select2]
        ug2=df["$u_g$ (Btu/lb)"].iloc[select2]
        
        data['params']['Vunits'] = "ft"
        data['params']['Punits'] = "psi"
        data['params']['Qunits'] = "Btu"
    
    else: 
        V = random.randint(10,30)/100#random.randint(40,60) # Volume in ft^3
        x1 = random.randint(1,4)/100
        df = pd.read_csv("clientFilesQuestion/SatVaporTable_Pscale_SI.csv")
        l = len(df)
        select1 = np.random.randint(12,20) 
        select2 = random.randint(25,28) 
        P1=df["$p$ (bar)"].iloc[select1] 
        P2=df["$p$ (bar)"].iloc[select2] 
        hg1=df["$h_g$ (kJ/kg)"].iloc[select1]
        hg2=df["$h_g$ (kJ/kg)"].iloc[select2]
        vg1=df["$v_g$ (m$^3$/kg)"].iloc[select1]
        vg2=df["$v_g$ (m$^3$/kg)"].iloc[select2]
        vf1=df["$v_f$ (m$^3$/kg)"].iloc[select1]/1000
        vf2=df["$v_f$ (m$^3$/kg)"].iloc[select2]/1000
        uf1=df["$u_f$ (kJ/kg)"].iloc[select1]
        ug1=df["$u_g$ (kJ/kg)"].iloc[select1]
        uf2=df["$u_f$ (kJ/kg)"].iloc[select2]
        ug2=df["$u_g$ (kJ/kg)"].iloc[select2]
        
        data['params']['Vunits'] = "m"
        data['params']['Punits'] = "bar"
        data['params']['Qunits'] = "kJ"
        
    # Calculate answers
    #State 1
    v1=vf1+x1*(vg1-vf1)
    u1=uf1+x1*(ug1-uf1)
    m1=V/v1
    #State 2
    v2=v1
    x2=(v2-vf2)/(vg2-vf2)
    m2=m1
    u2=uf2+x2*(ug2-uf2)
    #state 3
    m3=V/vg2
    he=hg2
    u3=ug2
    
    #Answers
    Q1=m1*(u2-u1)
    Q2=(m3*u3)-(m2*u2)-he*(m3-m2)
    
    # Pass input quantities to question
    data['params']['V'] = V
    data['params']['p1'] = P1
    data['params']['p2'] = P2
    data['params']['x'] = round(x1*100,2)
    
    # Pass correct answers
    data['correct_answers']['answer1'] = Q1
    data['correct_answers']['answer2'] = Q2
