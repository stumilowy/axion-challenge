from Circuit import Circuit
from Gates import CNOT, X, H
from QuantumState import QuantumState

# indeksownie w tym programie zaczyna sie od 1
# chodzi o tworzenie gatów i na które qubity mają zostać nałożone
# oraz wyznaczenie który qubit w qubit state ma być zmierzony

qs = QuantumState(['0','0'])
circuit = Circuit(qs)
#x = X([1,2],qs.n_qubits)
h = H([1],qs.n_qubits)
cnot = CNOT()
circuit.add_gate(h)
circuit.add_gate(cnot)
qs_after_circuit = circuit.run()
qs_after_circuit.measure(1)





