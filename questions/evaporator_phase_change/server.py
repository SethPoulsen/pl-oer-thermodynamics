import random
import numpy as np
import math
import pandas as pd
import prairielearn as pl

def generate(data):
    
    significant_digits = 4
    dfstate3 = pd.read_csv("clientFilesQuestion/SatVaporTable_Pscale_SI_R22.csv")
    selected_columns1 = ["$p$ (bar)","$T$ ($^{\circ}$C)","$h_f$ (kJ/kg)","$h_g$ (kJ/kg)"]
    whichP_R22 = random.choice([0,1,2,3])
    pR22_rows = [22,24,26,27]
    pR22tables = ["clientFilesQuestion/SupHVaporTable_P5bar_R22_SI.csv","clientFilesQuestion/SupHVaporTable_P5p5bar_R22_SI.csv","clientFilesQuestion/SupHVaporTable_P6bar_R22_SI.csv","clientFilesQuestion/SupHVaporTable_P7bar_R22_SI.csv","clientFilesQuestion/SupHVaporTable_P8bar_R22_SI.csv","clientFilesQuestion/SupHVaporTable_P9bar_R22_SI.csv"]
    dfstate4 = pd.read_csv(pR22tables[whichP_R22])
    selected_columns2 = ["$T$ ($^{\circ}$C)","$h$ (kJ/kg)"]
    
    # R22 State 3
    p3 = dfstate3["$p$ (bar)"].iloc[pR22_rows[whichP_R22]]
    hf3 = dfstate3["$h_f$ (kJ/kg)"].iloc[pR22_rows[whichP_R22]]
    hg3 = dfstate3["$h_g$ (kJ/kg)"].iloc[pR22_rows[whichP_R22]]
    x3 = random.choice([0.1,0.15,0.16,0.17,0.18,0.2,0.22,0.3])
    h3 = hf3 + x3*(hg3-hf3)
    
    #R22 State 4
    pos_T4_1 = 1 #Evaporator inlet pressure
    pos_T4_2 = 4 #Evaporator inlet pressure
    selecT4 = np.random.randint(pos_T4_1,pos_T4_2)
    T4 = dfstate4["$T$ ($^{\circ}$C)"].iloc[selecT4]
    h4 = dfstate4["$h$ (kJ/kg)"].iloc[selecT4]
    p4 = p3
    
    #Air State 1
    cp = 1 #kJ/kg-K
    AV1 = np.random.randint(30,40) #m3/min
    T1 = np.random.randint(24,35)
    p1 = random.choice([1,1.1,1.2,1.3]) #bar
    R = 8.314/28.97 #kJ/kg-K
    mair1 = (p1*(10**5)*(AV1))/((R*10**3)*(T1+273.15)) #kg/min
    mair1 = round(mair1, significant_digits - int(math.floor(math.log10(abs(mair1)))) - 1)
    
    #Air State 2
    T2 = T1 - np.random.randint(9,13)
    p2 = (p1 - 0.1)
    p2 = round(p2, significant_digits - int(math.floor(math.log10(abs(p2)))) - 1)
    
    #Refrigerant flow rate
    mR22 = mair1*((cp*(T1-T2))/(h4-h3)) #kg/min
    mR22 = round(mR22, significant_digits - int(math.floor(math.log10(abs(mR22)))) - 1)
    
    # Heat transfer
    QR22 = mR22*(h4-h3) #kg/min
    QR22 = round(QR22, significant_digits - int(math.floor(math.log10(abs(QR22)))) - 1)
    # Scenario
    scenarios = [
    # mR22
      {
          "unknown" : "mass flow rate $\dot{m}_{R22}$",
          "ques1"   : "\dot{m}_{R22}",
          "label"   : "kg/min",
          "ans1"    : mR22,
          
          "given1symbol" : "p_1",
          "given1value" : p1,
          "given1units" : "bar",
          
          "given2symbol" : "T_1",
          "given2value" : T1,
          "given2units" : "$^{\circ}$C",
          
          "given3symbol" : "AV_1",
          "given3value" : AV1,
          "given3units" : "m$^3$/min",
          
          "given4symbol" : "T_2",
          "given4value" : T2,
          "given4units" : "$^{\circ}$C",
          
          "given5symbol" : "p_2",
          "given5value" : p2,
          "given5units" : "bar",
          
          "given6symbol" : "p_3",
          "given6value" : p3,
          "given6units" : "bar",
          
          "given7symbol" : "x_3",
          "given7value" : x3,
          "given7units" : "",
          
          "given8symbol" : "p_4",
          "given8value" : p4,
          "given8units" : "bar",
          
          "given9symbol" : "T_4",
          "given9value" : T4,
          "given9units" : "$^{\circ}$C",
      },
    # T2
      {
          "unknown" : "temperature $T_2$",
          "ques1"   : "T_2",
          "label"   : "$^{\circ}$C",
          "ans1"    : T2,
          
          "given1symbol" : "p_1",
          "given1value" : p1,
          "given1units" : "bar",
          
          "given2symbol" : "T_1",
          "given2value" : T1,
          "given2units" : "$^{\circ}$C",
          
          "given3symbol" : "AV_1",
          "given3value" : AV1,
          "given3units" : "m$^3$/min",
          
          "given4symbol" : "\dot{m}_{R22}",
          "given4value" : mR22,
          "given4units" : "kg/min",
          
          "given5symbol" : "p_2",
          "given5value" : p2,
          "given5units" : "bar",
          
          "given6symbol" : "p_3",
          "given6value" : p3,
          "given6units" : "bar",
          
          "given7symbol" : "x_3",
          "given7value" : x3,
          "given7units" : "",
          
          "given8symbol" : "p_4",
          "given8value" : p4,
          "given8units" : "bar",
          
          "given9symbol" : "T_4",
          "given9value" : T4,
          "given9units" : "$^{\circ}$C",
      },
    # x3
      {
          "unknown" : "quality $x_3$",
          "ques1"   : "x_3",
          "label"   : "",
          "ans1"    : x3,
          
          "given1symbol" : "p_1",
          "given1value" : p1,
          "given1units" : "bar",
          
          "given2symbol" : "T_1",
          "given2value" : T1,
          "given2units" : "$^{\circ}$C",
          
          "given3symbol" : "AV_1",
          "given3value" : AV1,
          "given3units" : "m$^3$/min",
          
          "given4symbol" : "\dot{m}_{R22}",
          "given4value" : mR22,
          "given4units" : "kg/min",
          
          "given5symbol" : "p_2",
          "given5value" : p2,
          "given5units" : "bar",
          
          "given6symbol" : "p_3",
          "given6value" : p3,
          "given6units" : "bar",
          
          "given7symbol" : "T_2",
          "given7value" : T2,
          "given7units" : "$^{\circ}$C",
          
          "given8symbol" : "p_4",
          "given8value" : p4,
          "given8units" : "bar",
          
          "given9symbol" : "T_4",
          "given9value" : T4,
          "given9units" : "$^{\circ}$C",
      },
    # T4
      {
          "unknown" : "temperature $T_4$",
          "ques1"   : "T_4",
          "label"   : "$^{\circ}$C",
          "ans1"    : T4,
          
          "given1symbol" : "p_1",
          "given1value" : p1,
          "given1units" : "bar",
          
          "given2symbol" : "T_1",
          "given2value" : T1,
          "given2units" : "$^{\circ}$C",
          
          "given3symbol" : "AV_1",
          "given3value" : AV1,
          "given3units" : "m$^3$/min",
          
          "given4symbol" : "\dot{m}_{R22}",
          "given4value" : mR22,
          "given4units" : "kg/min",
          
          "given5symbol" : "p_2",
          "given5value" : p2,
          "given5units" : "bar",
          
          "given6symbol" : "p_3",
          "given6value" : p3,
          "given6units" : "bar",
          
          "given7symbol" : "T_2",
          "given7value" : T2,
          "given7units" : "$^{\circ}$C",
          
          "given8symbol" : "p_4",
          "given8value" : p4,
          "given8units" : "bar",
          
          "given9symbol" : "x_3",
          "given9value" : x3,
          "given9units" : "",
      },
    # AV1
      {
          "unknown" : "volume flow rate $AV_1$",
          "ques1"   : "AV_1",
          "label"   : "m$^3$/min",
          "ans1"    : AV1,
          
          "given1symbol" : "p_1",
          "given1value" : p1,
          "given1units" : "bar",
          
          "given2symbol" : "T_1",
          "given2value" : T1,
          "given2units" : "$^{\circ}$C",
          
          "given3symbol" : "T_4",
          "given3value" : T4,
          "given3units" : "$^{\circ}$C",
          
          "given4symbol" : "\dot{m}_{R22}",
          "given4value" : mR22,
          "given4units" : "kg/min",
          
          "given5symbol" : "p_2",
          "given5value" : p2,
          "given5units" : "bar",
          
          "given6symbol" : "p_3",
          "given6value" : p3,
          "given6units" : "bar",
          
          "given7symbol" : "T_2",
          "given7value" : T2,
          "given7units" : "$^{\circ}$C",
          
          "given8symbol" : "p_4",
          "given8value" : p4,
          "given8units" : "bar",
          
          "given9symbol" : "x_3",
          "given9value" : x3,
          "given9units" : "",
      },
    # mair1
      {
          "unknown" : "mass flow rate $\dot{m}_{air1}$",
          "ques1"   : "\dot{m}_{air1}",
          "label"   : "kg/min",
          "ans1"    : mair1,
          
          "given1symbol" : "p_1",
          "given1value" : p1,
          "given1units" : "bar",
          
          "given2symbol" : "T_1",
          "given2value" : T1,
          "given2units" : "$^{\circ}$C",
          
          "given3symbol" : "T_4",
          "given3value" : T4,
          "given3units" : "$^{\circ}$C",
          
          "given4symbol" : "\dot{m}_{R22}",
          "given4value" : mR22,
          "given4units" : "kg/min",
          
          "given5symbol" : "p_2",
          "given5value" : p2,
          "given5units" : "bar",
          
          "given6symbol" : "p_3",
          "given6value" : p3,
          "given6units" : "bar",
          
          "given7symbol" : "T_2",
          "given7value" : T2,
          "given7units" : "$^{\circ}$C",
          
          "given8symbol" : "p_4",
          "given8value" : p4,
          "given8units" : "bar",
          
          "given9symbol" : "x_3",
          "given9value" : x3,
          "given9units" : "",
      }
      ]
    
    random.shuffle(scenarios)
    
    #Given conditions
    data['params']['givensymbol1'] = scenarios[0]['given1symbol']
    data['params']['givenvalue1'] = scenarios[0]['given1value']
    data['params']['givenunits1'] = scenarios[0]['given1units']
    
    data['params']['givensymbol2'] = scenarios[0]['given2symbol']
    data['params']['givenvalue2'] = scenarios[0]['given2value']
    data['params']['givenunits2'] = scenarios[0]['given2units']

    data['params']['givensymbol3'] = scenarios[0]['given3symbol']
    data['params']['givenvalue3'] = scenarios[0]['given3value']
    data['params']['givenunits3'] = scenarios[0]['given3units']
    
    data['params']['givensymbol4'] = scenarios[0]['given4symbol']
    data['params']['givenvalue4'] = scenarios[0]['given4value']
    data['params']['givenunits4'] = scenarios[0]['given4units']

    data['params']['givensymbol5'] = scenarios[0]['given5symbol']
    data['params']['givenvalue5'] = scenarios[0]['given5value']
    data['params']['givenunits5'] = scenarios[0]['given5units']
    
    data['params']['givensymbol6'] = scenarios[0]['given6symbol']
    data['params']['givenvalue6'] = scenarios[0]['given6value']
    data['params']['givenunits6'] = scenarios[0]['given6units']
    
    data['params']['givensymbol7'] = scenarios[0]['given7symbol']
    data['params']['givenvalue7'] = scenarios[0]['given7value']
    data['params']['givenunits7'] = scenarios[0]['given7units']
    
    data['params']['givensymbol8'] = scenarios[0]['given8symbol']
    data['params']['givenvalue8'] = scenarios[0]['given8value']
    data['params']['givenunits8'] = scenarios[0]['given8units']
    
    data['params']['givensymbol9'] = scenarios[0]['given9symbol']
    data['params']['givenvalue9'] = scenarios[0]['given9value']
    data['params']['givenunits9'] = scenarios[0]['given9units']
    
    data['params']['TUnits'] = '$^{\circ}$C'
    data['params']['pUnits'] = 'bar'
    data['params']['mdotUnits'] = 'kg/s'
    data['params']['QdotUnits'] = 'MW'
    data['params']['unknown1'] = scenarios[0]['unknown']
    data['params']['label1'] = scenarios[0]['label']
    data['params']['ques1']  = scenarios[0]['ques1']
    data['correct_answers']['ans1']  = scenarios[0]['ans1']
    
    data['params']['unknown2'] = "heat transferred to refrigerant $\dot{Q}_{R22}$"
    data['params']['label2'] = "kJ/min"
    data['params']['ques2']  = "\dot{Q}_{R22}"
    data['correct_answers']['ans2']  = QR22
    
    
    #data['correct_answers']['Qsteam']  = Qsteam
    