# Generalized Entangler Gate: Creates a uniform superposition across all basis states by applying Hadamard gates to all qubits. 
# Useful for state initialization in quantum algorithms.

from qiskit import QuantumCircuit, Aer, execute
from qiskit.circuit import Gate
import numpy as np

def generalized_entangler_gate(n_qubits):
    qc = QuantumCircuit(n_qubits, name="G_Ent")

    for qubit in range(n_qubits):
        qc.h(qubit)
    
    entangler_gate = qc.to_gate()
    return entangler_gate

n_qubits = 3

qc = QuantumCircuit(n_qubits)
qc.append(generalized_entangler_gate(n_qubits), range(n_qubits))
qc.measure_all()

# Simuler le circuit
backend = Aer.get_backend('qasm_simulator')
result = execute(qc, backend=backend, shots=1024).result()

counts = result.get_counts()
print("Résultats de la mesure :")
print(counts)

backend_sv = Aer.get_backend('statevector_simulator')
result_sv = execute(qc.remove_final_measurements(inplace=False), backend=backend_sv).result()
statevector = result_sv.get_statevector()
print("\nVecteur d'état final :")
print(statevector)
