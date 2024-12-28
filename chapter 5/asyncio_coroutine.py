import asyncio
import time
from random import randint


def start_state():
    print('start state called\n')
    input_value = randint(0,1)
    time.sleep(1)
    if input_value == 0:
        result = yield from state2(input_value)
    else:
        result = yield from state1(input_value)
    print('Resume of Transition : \n start state calling' + result)

def state1(transition_value):
    output_value = 'State 1 with trasnition value = %s\n' % transition_value
    input_value = randint(0,1)
    time.sleep(1)

    print('...evaluating...')
    if input_value == 0:
        result = yield from state3(input_value)
    else:
        result = yield from state2(input_value)

    return output_value + 'State 1 calling %s' % result

def state2(transition_value):
    output_value = 'state 2 with transition value = %s\n' % transition_value
    input_value = randint(0,1)
    time.sleep(1)
    print('....evaluating....')
    if input_value == 0:
        result = yield from state1(input_value)
    else:
        result = yield from state3(input_value)
    
    return output_value + 'state 2 calling %s' % result

def state3(transition_value):
    output_value = 'State 3 with transition value = %s\n' % transition_value
    input_value = randint(0,1)
    time.sleep(1)

    print('....evaluating....')




    
