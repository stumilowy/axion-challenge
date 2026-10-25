import math
from abc import ABC, abstractmethod

import numpy as np


class Gate(ABC):
    I = np.array([[1+0j,0j],
                  [0j,1+0j]])

    def __init__(self, qubits_indices, n_qubits):
        if n_qubits < 1:
            raise ValueError('Minimalnie 1 qubit')
        if len(qubits_indices) < 1:
            raise ValueError(f'Bramka musi być nałożona na przynajmniej 1 qubit')
        if not all(0 < q <= n_qubits for q in qubits_indices):
            raise ValueError(f'Dozwolone indeksy to od 1 do {n_qubits}')
        self.qubits_indices = qubits_indices
        self.n_qubits = n_qubits

    @property
    @abstractmethod
    def base_matrix(self):
        pass

    @abstractmethod
    def matrix(self):
        pass


class SingleQubitGate(Gate):
    @property
    @abstractmethod
    def base_matrix(self):
        pass

    def matrix(self):
        base_gate_matrix = self.base_matrix
        gated_qubits = [1 if i+1 in self.qubits_indices else 0 for i in range(self.n_qubits)]
        matrix = base_gate_matrix if gated_qubits[0] else self.I
        for q in gated_qubits[1:]:
            if q: matrix = np.kron(matrix,base_gate_matrix)
            else: matrix = np.kron(matrix,self.I)
        return matrix

class X(SingleQubitGate):
    def __init__(self, qubits_indices, n_qubits):
        super().__init__(qubits_indices,n_qubits)

    @property
    def base_matrix(self):
        return np.array([[0j,1+0j],
                         [1+0j,0j]])


class Y(SingleQubitGate):
    def __init__(self, qubits_indices, n_qubits):
        super().__init__(qubits_indices,n_qubits)

    @property
    def base_matrix(self):
        return np.array([[0j,-1j],
                         [1j,0j]])

class Z(SingleQubitGate):
    def __init__(self, qubits_indices, n_qubits):
        super().__init__(qubits_indices,n_qubits)

    @property
    def base_matrix(self):
        return np.array([[1+0j,    0j],
                         [  0j, -1+0j]])

class H(SingleQubitGate):
    a = 1 / math.sqrt(2)
    def __init__(self, qubits_indices, n_qubits):
        super().__init__(qubits_indices,n_qubits)

    @property
    def base_matrix(self):
        return self.a * np.array([[1+0j,  1+0j],
                                  [1+0j, -1+0j]])

class Ry(SingleQubitGate):
    def __init__(self, qubits_indices, n_qubits, the):
        self.the = the
        super().__init__(qubits_indices,n_qubits)

    @property
    def base_matrix(self):
        return np.array([[math.cos(self.the/2)+0j,  -math.sin(self.the/2)+0j],
                         [math.sin(self.the/2)+0j,   math.cos(self.the/2)+0j]])

# ta bramka jest zaimplementowana tylko dla przypadku dwóch qubitów
class CNOT(Gate):

    def __init__(self, first_control_second_target=True):
        self.first_control_second_target = first_control_second_target
        super().__init__([1,2],2)

    @property
    def base_matrix(self):
        if self.first_control_second_target:
            return np.array([[1 + 0j,     0j,     0j,     0j],
                             [0j    , 1 + 0j,     0j,     0j],
                             [0j    , 0j    ,     0j, 1 + 0j],
                             [0j    , 0j    , 1 + 0j,     0j]])
        else:
            return np.array([[1 + 0j,     0j,     0j,     0j],
                             [0j    ,     0j,     0j, 1 + 0j],
                             [0j    ,     0j, 1 + 0j,     0j],
                             [0j    , 1 + 0j,     0j,     0j]])


    def matrix(self):
        return self.base_matrix
