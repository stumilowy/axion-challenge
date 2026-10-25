import copy

from QuantumState import QuantumState
from Gates import Gate
import numpy as np

class Circuit:

    def __init__(self, quantum_state: QuantumState):
        self.quantum_state = copy.deepcopy(quantum_state)
        self.gates = []

    def add_gate(self, gate: Gate):
        if gate.n_qubits != self.quantum_state.n_qubits:
            raise ValueError('Liczba kubitów bramki nie zgadza się z liczbą kubitów w stanie kwantowym')
        self.gates.append(gate)

    def _process_gate(self, gate, qs):
        # print(gate.matrix())
        # print(self.quantum_state.state)
        qs.state = np.dot(gate.matrix(), qs.state)

    def run(self):
        qs_c = copy.deepcopy(self.quantum_state)
        for gate in self.gates:
            print(qs_c.get_probability())
            self._process_gate(gate,qs_c)
        print(qs_c.get_probability())
        return qs_c




