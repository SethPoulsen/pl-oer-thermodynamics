import random
import numpy as np


def generate(data):

    # System Geometry
    gW= 350
    gH= 270
    sW=162 #system, assumed to be in center
    sH=100 #system
    inW=110
    inH=50
    length = 70
    data["params"]["gW"] = gW
    data["params"]["gH"] = gH
    data["params"]["sW"] = sW
    data["params"]["sH"] = sH
    data["params"]["sWpos"] = gW/2 # code assumes system is in the center of the grid
    data["params"]["sHpos"] = gH/2
    data["params"]["len"] = length

    # Flow arrows and directions
    Nflows = 4
    positions = np.linspace(0,11,12)
    positions = random.sample(positions.tolist(),Nflows)
    inout = np.random.randint(0,2,Nflows)
    x = np.empty(Nflows, dtype=float)
    y = np.empty(Nflows, dtype=float)
    th = np.empty(Nflows, dtype=float)
    tail = np.empty(Nflows)
    xoffset = np.zeros(Nflows, dtype=float)
    yoffset = np.zeros(Nflows, dtype=float)

    # Quantities
    valuesP = np.linspace(1,10,10)
    valuesN = -1*np.linspace(1,10,10)
    values = np.concatenate([valuesP,valuesP,valuesP])
    values = random.sample(values.tolist(),Nflows)

    # Make steady-state more likely
    ss = random.choice([0, 0, 1])
    if ss == 1:
        values[3] = -1*round((-1)**(1-inout[0])*values[0] + (-1)**(1-inout[1])*values[1] + (-1)**(1-inout[2])*values[2])
        if values[3] > 0:
            inout[3] = 1
        elif values[3] < 0:
            inout[3] = 0
        else:
            values[3] = random.randint(1,10) # don't worry about ss this time so there are no zero flows
        values[3] = abs(values[3])


    # Determine Arrow Positioning
    Deg = 2*np.pi/360 # conversion from degrees to radians
    for i in range(Nflows):
        if inout[i] == 1:
            tail[i] = False
        else:
            tail[i] = True
        if positions[i] == 0: #top of system
            x[i] = gW/2
            y[i] = gH/2-inH/2
            if inout[i] == 1: #in
                th[i] = 90
                yoffset[i] = -length
            else:
                th[i] = 270
                xoffset[i] = 5
        if positions[i] == 1: #bottom of system
            x[i] = gW/2
            y[i] = gH/2+inH/2
            if inout[i] == 1: #in
                th[i] = 270
                yoffset[i] = length
            else:
                th[i] = 90
        if positions[i] == 2: #left of system
            x[i] = gW/2-inW/2
            y[i] = gH/2
            if inout[i] == 1: #in
                th[i] = 0
                xoffset[i] = -length-20
            else:
                th[i] = 180
                xoffset[i] = -20
                yoffset[i] = 5
        if positions[i] == 3: #right of system
            x[i] = gW/2+inW/2
            y[i] = gH/2
            if inout[i] == 1: #in
                th[i] = 180
                xoffset[i] = length
            else:
                th[i] = 0
        if positions[i] == 4: #top left of system
            x[i] = gW/2-2/3*(inW/2)
            y[i] = gH/2-inH/2
            if inout[i] == 1: #in
                th[i] = 70
                xoffset[i] = 5-length*np.cos(th[i]*Deg)
                yoffset[i] = -10-length*np.sin(th[i]*Deg)
            else:
                th[i] = 70+180
                xoffset[i] = 5
                yoffset[i] = -10
        if positions[i] == 5: #top right of system
            x[i] = gW/2+2/3*(inW/2)
            y[i] = gH/2-inH/2
            if inout[i] == 1: #in
                th[i] = 110
                xoffset[i] = -length*np.cos(th[i]*Deg)
                yoffset[i] = -length*np.sin(th[i]*Deg)
            else:
                th[i] = 110+180
                xoffset[i] = 5
        if positions[i] == 6: #bottom left of system
            x[i] = gW/2-2/3*(inW/2)
            y[i] = gH/2+inH/2
            if inout[i] == 1: #in
                th[i] = 290
                xoffset[i] = -length*np.cos(th[i]*Deg)
                yoffset[i] = -length*np.sin(th[i]*Deg)
            else:
                th[i] = 290-180
        if positions[i] == 7: #bottom right of system
            x[i] = gW/2+2/3*(inW/2)
            y[i] = gH/2+inH/2
            if inout[i] == 1: #in
                th[i] = 250
                xoffset[i] = -length*np.cos(th[i]*Deg)
                yoffset[i] = -length*np.sin(th[i]*Deg)
            else:
                th[i] = 250-180
        if positions[i] == 8: #upper left of system
            x[i] = gW/2-inW/2
            y[i] = gH/2-(inH/2)
            if inout[i] == 1: #in
                th[i] = 20
                xoffset[i] = -20-length*np.cos(th[i]*Deg)
                yoffset[i] = -22-length*np.sin(th[i]*Deg)
            else:
                th[i] = 20+180
                xoffset[i] = -30
                yoffset[i] = -22
        if positions[i] == 9: #lower left of system
            x[i] = gW/2-inW/2
            y[i] = gH/2+(inH/2)
            if inout[i] == 1: #in
                th[i] = -20
                xoffset[i] = -20-length*np.cos(th[i]*Deg)
                yoffset[i] = -length*np.sin(th[i]*Deg)
            else:
                th[i] = -20+180
                xoffset[i] = -20
        if positions[i] == 10: #upper right of system
            x[i] = gW/2+inW/2
            y[i] = gH/2-(inH/2)
            if inout[i] == 1: #in
                th[i] = 160
                xoffset[i] = -length*np.cos(th[i]*Deg)
                yoffset[i] = -length*np.sin(th[i]*Deg)
            else:
                th[i] = 160+180
        if positions[i] == 11: #lower right of system
            x[i] = gW/2+inW/2
            y[i] = gH/2+(inH/2)
            if inout[i] == 1: #in
                th[i] = 200
                xoffset[i] = -length*np.cos(th[i]*Deg)
                yoffset[i] = -length*np.sin(th[i]*Deg)
            else:
                th[i] = 200+180

    data["params"]["x1"] = x[0]
    data["params"]["y1"] = y[0]
    data["params"]["th1"] = th[0]
    data["params"]["tail1"] = tail[0]
    data["params"]["xoff1"] = xoffset[0]
    data["params"]["yoff1"] = yoffset[0]
    data["params"]["x2"] = x[1]
    data["params"]["y2"] = y[1]
    data["params"]["th2"] = th[1]
    data["params"]["tail2"] = tail[1]
    data["params"]["xoff2"] = xoffset[1]
    data["params"]["yoff2"] = yoffset[1]
    data["params"]["x3"] = x[2]
    data["params"]["y3"] = y[2]
    data["params"]["th3"] = th[2]
    data["params"]["tail3"] = tail[2]
    data["params"]["xoff3"] = xoffset[2]
    data["params"]["yoff3"] = yoffset[2]
    data["params"]["x4"] = x[3]
    data["params"]["y4"] = y[3]
    data["params"]["th4"] = th[3]
    data["params"]["tail4"] = tail[3]
    data["params"]["xoff4"] = xoffset[3]
    data["params"]["yoff4"] = yoffset[3]

    data["params"]["val1"] = values[0]
    data["params"]["val2"] = values[1]
    data["params"]["val3"] = values[2]
    data["params"]["val4"] = values[3]

    # Transmit answers

    sum = 0
    for i in range(Nflows):
        sum = (-1)**(1-inout[i])*values[i] + sum
    data["correct_answers"]["ans"]=sum

    data["params"]["dec"] = False
    data["params"]["inc"] = False
    data["params"]["ss"] = False
    if sum < 0:
        data["params"]["dec"] = True
    elif sum > 0:
        data["params"]["inc"] = True
    elif sum == 0:
        data["params"]["ss"] = True

    return data

def grade(data):

    NumAns = data["submitted_answers"]["ans"]
    DropAns = data["submitted_answers"]["dir"]
    if (NumAns < 0):
        if DropAns == "decreased":
            data['partial_scores']['dir'] = {'score': 1, 'weight': 1}
        else:
            data['partial_scores']['dir'] = {'score': 0, 'weight': 1}
    elif NumAns > 0:
        if DropAns == "increased":
            data['partial_scores']['dir'] = {'score': 1, 'weight': 1}
        else:
            data['partial_scores']['dir'] = {'score': 0, 'weight': 1}
    elif NumAns == 0:
        if DropAns == "not changed":
            data['partial_scores']['dir'] = {'score': 1, 'weight': 1}
        else:
            data['partial_scores']['dir'] = {'score': 0, 'weight': 1}

    variables = ["ans", "dir"]
    score = 0
    for name in variables:
        score += data['partial_scores'][name]['score']
    data['score'] = score/len(variables)

    if data['partial_scores']['dir']['score'] == 0:
        data["feedback"]["IncorrectDir"] = "Direction of energy change must match with the calculated quantity."
    else:
        data["feedback"]["IncorrectDir"] = ""
