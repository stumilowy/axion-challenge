from quantum_simulator import add_single_qubit_gate
from numpy import pi

class Circuit:
    gates = []

    def __init__(self, qubit_base_state):
        self.qubit_base_state = qubit_base_state

    def add_gates(self, gates, the = pi):
        self.gates.extend((gates,the))

    def process_gates(self):
        qubit = self.qubit_base_state.copy()
        for gate in self.gates:
            print(f"Processing qubit via gate {gate}...")
            qubit = add_single_qubit_gate(qubit,gate[0],gate[1])
        print()

    def display_circuit:

