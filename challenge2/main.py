from math import pi

from Circuit import Circuit
from Gates import CNOT, X, Y, Z, H, Ry
from QuantumState import QuantumState
from Simulator import Simulator

# indeksownie w tym programie zaczyna sie od 1
# chodzi o tworzenie gatów i na które qubity mają zostać nałożone
# oraz wyznaczenie który qubit w qubit state ma być zmierzony

# stany jednoqubitowe
KET_0 = QuantumState(['0'])
KET_1 = QuantumState(['1'])
KET_PLUS = QuantumState(['+'])
KET_MINUS = QuantumState(['-'])
KET_I = QuantumState(['i'])
KET_MINUS_I = QuantumState(['-i'])

# stany dwuqubitowe
KET_00 = QuantumState(['0', '0'])
KET_01 = QuantumState(['0', '1'])
KET_10 = QuantumState(['1', '0'])
KET_11 = QuantumState(['1', '1'])
KET_PLUS_0 = QuantumState(['+', '0'])
KET_PLUS_MINUS = QuantumState(['+', '-'])


def print_header(title):
    print('=' * 50)
    print(title)
    print('=' * 50)


def build_circuit(quantum_state, gates):
    circuit = Circuit(quantum_state)
    for gate in gates:
        circuit.add_gate(gate)
    return circuit


def simulate(title, quantum_state, gates):
    print_header(title)
    Simulator(build_circuit(quantum_state, gates)).summary()


# jeden qubit
simulate('X|0> = |1>', KET_0, [X([1], 1)])
simulate('Y|0> = i|1>', KET_0, [Y([1], 1)])
simulate('Z|+> = |->', KET_PLUS, [Z([1], 1)])
simulate('H|0> = |+>', KET_0, [H([1], 1)])
simulate('H|-> = |1>', KET_MINUS, [H([1], 1)])
simulate('HZH|0> = X|0> = |1>', KET_0, [H([1], 1), Z([1], 1), H([1], 1)])
simulate('Z|i> = |-i>', KET_I, [Z([1], 1)])
simulate('Ry(pi/3)|0>, P(1) = 25%', KET_0, [Ry([1], 1, pi / 3)])

# dwa qubity
simulate('X na obu qubitach: |00> -> |11>', KET_00, [X([1, 2], 2)])
simulate('H na obu qubitach: |00> -> równa superpozycja', KET_00, [H([1, 2], 2)])
simulate('CNOT: |10> -> |11>', KET_10, [CNOT()])
simulate('CNOT odwrócony: |01> -> |11>', KET_01, [CNOT(first_control_second_target=False)])
simulate('Bell Φ+: H(1), CNOT na |00>', KET_00, [H([1], 2), CNOT()])
simulate('Bell Ψ+: H(1), CNOT na |01>', KET_01, [H([1], 2), CNOT()])
simulate('Bell Φ-: H(1), CNOT na |10>', KET_10, [H([1], 2), CNOT()])
simulate('Bell Ψ-: H(1), CNOT na |11>', KET_11, [H([1], 2), CNOT()])
simulate('CNOT na |+0> = Bell Φ+', KET_PLUS_0, [CNOT()])
