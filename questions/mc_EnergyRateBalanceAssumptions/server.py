import random

def generate(data):

    # Create a list of question prompts and the corresponding answers
    scenarios = [
        {
            "question": "one-inlet/one-outlet and steady-state",
            "answer": "$0 = \dot{Q}-\dot{W} +\dot{m}(h_{\\text{in}} - h_{\\text{out}})$",
        },
        {
            "question": "one-inlet/one-outlet",
            "answer": "$dU/dt = \dot{Q}-\dot{W} +\dot{m}(h_{\\text{in}} - h_{\\text{out}})$",
        },
        {
            "question": "negligible heat transfer",
            "answer": "$dU/dt = -\dot{W} +\sum_{\\text{in}}\dot{m}_{\\text{in}}h_{\\text{in}} - \sum_{\\text{out}}\dot{m}_{\\text{out}}h_{\\text{out}}$",
        },
        {
            "question": "negligible heat transfer and steady-state",
            "answer": "$0 = -\dot{W} +\sum_{\\text{in}}\dot{m}_{\\text{in}}h_{\\text{in}} - \sum_{\\text{out}}\dot{m}_{\\text{out}}h_{\\text{out}}$",
        },
        {
            "question": "negligible work transfer and steady-state",
            "answer": "$0 = \dot{Q} +\sum_{\\text{in}}\dot{m}_{\\text{in}}h_{\\text{in}} - \sum_{\\text{out}}\dot{m}_{\\text{out}}h_{\\text{out}}$",
        },
        {
            "question": "negligible work transfer",
            "answer": "$dU/dt = \dot{Q} +\sum_{\\text{in}}\dot{m}_{\\text{in}}h_{\\text{in}} - \sum_{\\text{out}}\dot{m}_{\\text{out}}h_{\\text{out}}$",
        },
        {
            "question": "negligible heat transfer, one-inlet/one-outlet, and steady-state",
            "answer": "$0 = -\dot{W} +\dot{m}(h_{\\text{in}} - h_{\\text{out}})$",
        },
        {
            "question": "negligible heat transfer and one-inlet/one-outlet",
            "answer": "$dU/dt = -\dot{W} +\dot{m}(h_{\\text{in}} - h_{\\text{out}})$",
        },
        {
            "question": "negligible work transfer, one-inlet/one-outlet, and steady-state",
            "answer": "$0 = \dot{Q} +\dot{m}(h_{\\text{in}} - h_{\\text{out}})$",
        },
        {
            "question": "negligible work transfer and one-inlet/one-outlet",
            "answer": "$dU/dt = \dot{Q} +\dot{m}(h_{\\text{in}} - h_{\\text{out}})$",
        }
    ]

    # Randomize the order of the scenarios
    random.shuffle(scenarios)

    # First shuffled scenario is the one we will take as correct
    data['params']['question_prompt'] = scenarios[0]['question']
    data['params']['correct_answer'] = scenarios[0]['answer']

    # Next three shuffled scenarios are the distractors
    data['params']['wrong_answer1'] = scenarios[1]['answer']
    data['params']['wrong_answer2'] = scenarios[2]['answer']
    data['params']['wrong_answer3'] = scenarios[3]['answer']
