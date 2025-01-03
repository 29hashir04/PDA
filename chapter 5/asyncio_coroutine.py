import asyncio
from random import randint

async def start_state():
    print('Start state called\n')
    input_value = randint(0, 1)
    await asyncio.sleep(1)  # Use asyncio.sleep for non-blocking delay
    if input_value == 0:
        result = await state2(input_value)
    else:
        result = await state1(input_value)
    print('Resume of Transition:\nStart state calling ' + result)

async def state1(transition_value):
    output_value = f'State 1 with transition value = {transition_value}\n'
    input_value = randint(0, 1)
    await asyncio.sleep(1)  # Use asyncio.sleep for non-blocking delay

    print('...evaluating...')
    if input_value == 0:
        result = await state3(input_value)
    else:
        result = await state2(input_value)

    return output_value + f'State 1 calling {result}'

async def state2(transition_value):
    output_value = f'State 2 with transition value = {transition_value}\n'
    input_value = randint(0, 1)
    await asyncio.sleep(1)  # Use asyncio.sleep for non-blocking delay
    print('....evaluating....')
    if input_value == 0:
        result = await state1(input_value)
    else:
        result = await state3(input_value)

    return output_value + f'State 2 calling {result}'

async def state3(transition_value):
    output_value = f'State 3 with transition value = {transition_value}\n'
    input_value = randint(0, 1)
    await asyncio.sleep(1)  # Use asyncio.sleep for non-blocking delay

    print('....evaluating....')
    if input_value == 0:
        result = await state1(input_value)
    else:
        result = await end_state(input_value)

    return output_value + f'State 3 calling {result}'

async def end_state(transition_value):
    output_value = f'End State with transition value = {transition_value}\n'
    print('....Stop Computation....')

    return output_value

if __name__ == '__main__':
    print('Finite State Machine simulation with asyncio coroutine')
    asyncio.run(start_state())  # Modern method to run the asyncio event loop