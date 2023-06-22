import random
import math

def generate(data):


     # Choose the question set up randomly


    #Define figure
    figname = "piston.png"
    data['params']['figname'] = figname


    # Define Pressure the atmosphere exerts
    pa = 101.5 # kPa


    # Define the Absolute Pressure of the air inside the cylinder
    pint = random.randint(105,200) # kPa


    # Define the area of the piston
    d = random.randint(10,25) # cm, diameter
    A = round(math.pi*d**2/4)

    #Define the direction of the piston movement
    direction = random.choice([0,1])
    heightchange = ['raised', 'lowered']
    data['params']['heightchange'] = heightchange[direction]
    heightfactor = [1,-1]
    data['params']['heightfactor']= heightfactor[direction]

    # Define the height of the piston
    Height = round(random.uniform(1,10.0), 1) # cm

    unit = random.choice([0,1])  # Change units or not
    if unit == 1: # convert all units to English engineering
        # Set problem units
        data['params']['Lunits'] = "in"
        data['params']['punits'] = "psi"
        data['params']['Eunits'] = "Btu"
        data['params']['Conversion'] = "1 Btu = 778.17 ft$\cdot$lbf. 1 ft = 12 in"

        # Convert and round English inputs
        pa = round(pa * 0.145038, 1) # psi atmospheric pressure
        pint = round(pint * 0.145038) # psi gas pressure
        A = round(5* A * 0.155) # in^2 cylinder area
        Height = round(5 * Height * 0.3937) # in height change

        # Pass values to data
        data['params']['pa'] = pa
        data['params']['pint'] = pint
        data['params']['A'] = A
        data['params']['height'] = Height

        #Solve for Work done by the gas (integrate pdV) on the vertical piston cylinder
        W = ( (pint * (12)**2) * (A * (1/12)**2) * (heightfactor[direction]) * (Height * (1/12)) ) * (1/778.17)

    else:
        # Set problem units
        data['params']['Lunits'] = "cm"
        data['params']['punits'] = "kPa"
        data['params']['Eunits'] = "J"
        data['params']['Conversion'] = ""

        # Pass values to data
        data['params']['pa'] = pa
        data['params']['pint'] = pint
        data['params']['A'] = A
        data['params']['height'] = Height

        #Solve for Work done by the gas (integrate pdV) on the vertical piston cylinder
        W = (pint * 1000) * (A * (1/100)**2) * (heightfactor[direction]) * (Height * (1/100))


    # Put the answer for work into data['correct_answers']
    data['correct_answers']['W'] = W
