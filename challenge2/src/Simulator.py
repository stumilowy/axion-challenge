import copy
from collections import Counter

import numpy as np

from Circuit import Circuit
from Gates import CNOT


class Simulator:
    BAR_WIDTH = 30

    def __init__(self, circuit: Circuit):
        self.circuit = circuit
        self.result = None

    def run(self):
        self.result = self.circuit.run()
        return self.result

    def _get_result(self):
        if self.result is None:
            self.run()
        return self.result

    def _bitstring(self, i):
        return format(i, f'0{self.circuit.quantum_state.n_qubits}b')

    @staticmethod
    def _format_amplitude(a):
        if np.isclose(a.imag, 0):
            return f'{a.real:+.3f}'
        if np.isclose(a.real, 0):
            return f'{a.imag:+.3f}i'
        return f'({a.real:+.3f}{a.imag:+.3f}i)'

    def _bar(self, p):
        return '█' * round(p * self.BAR_WIDTH)

    def show_circuit(self):
        print('Obwód:')
        for step, gate in enumerate(self.circuit.gates, start=1):
            if isinstance(gate, CNOT):
                control, target = (1, 2) if gate.first_control_second_target else (2, 1)
                desc = f'control = q{control}, target = q{target}'
            else:
                desc = 'qubity: ' + ', '.join(f'q{q}' for q in gate.qubits_indices)
            print(f'  {step}. {type(gate).__name__:<5} {desc}')
        print()

    def show_state(self, title='Stan końcowy'):
        state = self._get_result().state
        terms = [f'{self._format_amplitude(a)}|{self._bitstring(i)}>'
                 for i, a in enumerate(state) if not np.isclose(a, 0)]
        print(f'{title}:')
        print('  |ψ> = ' + ' '.join(terms))
        print()

    def show_probabilities(self):
        probs = self._get_result().get_probability()
        print('Prawdopodobieństwa:')
        for i, p in enumerate(probs):
            print(f'  |{self._bitstring(i)}>  {p * 100:6.2f}%  {self._bar(p)}')
        print()

    def measure(self, qubit):
        # pomiar na wyniku symulacji - kolapsuje stan, kolejne show_* pokażą stan po pomiarze
        outcome = self._get_result().measure(qubit)
        print(f'>>> Pomiar q{qubit} = {outcome}')
        print()
        return outcome

    def sample(self, shots=1000):
        # pomiar na kopiach, żeby nie niszczyć wyniku symulacji
        result = self._get_result()
        counts = Counter()
        for _ in range(shots):
            qs = copy.deepcopy(result)
            outcome = ''.join(str(qs.measure(q)) for q in range(1, qs.n_qubits + 1))
            counts[outcome] += 1
        return counts

    def show_histogram(self, shots=1000):
        counts = self.sample(shots)
        print(f'Pomiary ({shots} shotów):')
        for outcome, count in sorted(counts.items()):
            print(f'  |{outcome}>  {count:>5}  {self._bar(count / shots)}')
        print()

    def summary(self, shots=1000):
        self.show_circuit()
        self.show_state()
        self.show_probabilities()
        self.show_histogram(shots)
