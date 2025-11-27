import random

def parse_state(text: str):
    parts = text.replace(",", " ").split()
    if len(parts) != 9:
        raise ValueError("Must contain 9 numbers.")
    nums = [int(x) for x in parts]
    if sorted(nums) != list(range(9)):
        raise ValueError("Numbers must be 0–8.")
    return nums

def count_inversions(state):
    arr = [x for x in state if x != 0]
    inv = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                inv += 1
    return inv

def is_solvable(state):
    return count_inversions(state) % 2 == 0

def generate_solvable_puzzle():
    state = list(range(9))
    while True:
        random.shuffle(state)
        if is_solvable(state):
            return state
