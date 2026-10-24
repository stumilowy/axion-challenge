
import numpy as np

import cmath
import math
import random

PI = np.pi
# alfa = complex(3/5,0)
# beta = complex(4/5,0)
alfa = complex(1,0)
beta = complex(0,0)
ket_zero = np.array([1,0])
ket_one = np.array([0,1])
ket_zero_zero = np.array([1,0,0,0])
ket_zero_one = np.array([0,1,0,0])
ket_one_zero = np.array([0,0,1,0])
ket_one_one = np.array([0,0,0,1])
qubit_state = np.array([alfa,beta])

X_gate = np.array([ [0,1],
                    [1,0]])
print(2*X_gate)

single_qubit_gates = {
    'X': np.array([ [0,1],
                    [1,0]]),
    'Z': np.array([ [1,0],
                    [0,-1]]),
    'H': (1/math.sqrt(2))*np.array([[1, 1],
                                    [1, -1]]),
}

cnot = np.array([[1,0,0,0],
                 [0,1,0,0],
                 [0,0,0,1],
                 [0,0,1,0]])

def Ry_gate(the):
    return np.array([[np.cos(the/2), -np.sin(the/2)],
                     [np.sin(the/2),  np.cos(the/2)]])

def add_single_qubit_gate(qubit, gate_name : str, the: float = 0) -> np.ndarray:
    if gate_name not in single_qubit_gates.keys() and gate_name != 'Ry':
        raise Exception('Gate not valid')

    if gate_name == 'Ry': gate = Ry_gate(the)
    else:  gate = single_qubit_gates[gate_name]
    return np.dot(gate,qubit)


def get_probability(qubit_state : np.ndarray) -> tuple[int,int]:
    zero_chance = abs(qubit_state[0])**2
    one_chance = abs(qubit_state[1])**2
    if not math.isclose(zero_chance+one_chance,1.0):
        print(f"illegal state: {zero_chance} + {one_chance} = {zero_chance + one_chance}")
    return zero_chance, one_chance

def display_probability(qubit_state : np.ndarray):
    zero_chance, one_chance = get_probability(qubit_state)
    print(f'Zero chance = {zero_chance*100:.2f}%\nOne chance = {one_chance*100:.2f}%')

def measure(qubit_state):
    zero_chance = abs(qubit_state[0])**2
    one_chance = abs(qubit_state[1])**2
    result = random.choices([0,1],weights=[zero_chance,one_chance])[0]
    print(result)

def cnot_gate(two_qubit_state):
    return np.dot(cnot,two_qubit_state)

display_probability(qubit_state)
qubit_state = add_single_qubit_gate(qubit_state, 'Ry', the=PI/3)
display_probability(qubit_state)

print(np.dot(cnot,np.kron(ket_one,ket_zero)))
print(np.kron(ket_one,ket_zero))




