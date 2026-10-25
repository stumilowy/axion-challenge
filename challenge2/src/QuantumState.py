import numpy as np
import math
import random

class QuantumState:
    base_states = {
        '0': np.array([complex(1,0),complex(0,0)]),
        '1': np.array([complex(0,0),complex(1,0)]),
        'i': (1/math.sqrt(2))*np.array([complex(1,0),complex(0,1)]),
        '-i': (1/math.sqrt(2))*np.array([complex(1,0),complex(0,-1)]),
        '+': (1/math.sqrt(2))*np.array([complex(1,0),complex(1,0)]),
        '-': (1/math.sqrt(2))*np.array([complex(1,0),complex(-1,0)])
    }

    def __init__(self, state_list):
        if not all(c in self.base_states for c in state_list):
            raise ValueError("Ciąg musi składać się tylko z dozwolonych stanów (0, 1, i, -i, +, -)")

        self.n_qubits = len(state_list)
        if self.n_qubits == 0:
            raise ValueError("Ciąg stanów nie może być pusty.")

        state = self.base_states[state_list[0]].copy()

        for c in state_list[1:]:
            state = np.kron(state, self.base_states[c])

        self.state = state

    def measure(self, n: int):
        if self.n_qubits < n or n < 1:
            raise  ValueError(f"Pomiar możliwy tylko dla n z przedmiału [{1},{self.n_qubits}]")

        probs = self.get_probability()

        # licznie prawdopodobienstaw na 0 dla danageo qubitu
        prob_0 = 0
        move = self.n_qubits - n
        for i, p in enumerate(probs):
            if not ((i >> move) & 1):
                prob_0 += p
        # losowanie
        outcome = 0 if random.random() < prob_0 else 1
        # kolaps
        for i, p in enumerate(probs):
            qubit_state = 1 if (i >> move) & 1 else 0
            if qubit_state != outcome:
                self.state[i] = 0j


        # normalizacja
        A = math.sqrt(1/np.sum(np.abs(self.state) ** 2))
        self.state = A * self.state

        return outcome

    def get_probability(self):
        return np.abs(self.state) ** 2
