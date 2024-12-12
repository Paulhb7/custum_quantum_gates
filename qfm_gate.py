from qiskit import QuantumCircuit, Aer, execute
from qiskit.circuit import Parameter
import numpy as np

def QFM_gate(x, name="QFM"):
    """
    porte QFM (Quantum Feature Map Gate) qui encode un vecteur x dans
    un circuit quantique.

    Paramètres :
    ------------
    x : array-like
        Vecteur de features classiques (float ou double).
    name : str
        Nom de la porte.

    Retourne :
    ----------
    Une instruction (porte) UnitaryGate correspondant à l’encodage de x!
    """
    x = np.array(x)
    d = len(x)
    
    # On va choisir le nombre de qubits pour encoder d features. Pour le max de simplicité, 
    # supposons n_qubits = d (1 feature par qubit).
    n_qubits = d

    qc = QuantumCircuit(n_qubits, name=name)
    
    # Initialisation : on peut commencer par placer tous les qubits dans un état |+>
    # pour pouvoir appliquer des phases. (ça reste optionnel)
    for qubit in range(n_qubits):
        qc.h(qubit)

    # Appliquer une rotation RZ sur chaque qubit proportionnelle à x_j
    # Par exemple, RZ(x_j)
    for i, val in enumerate(x):
        qc.rz(val, i)

    # Ajouter quelques CNOT pour entremêler les qubits, 
    # créant des corrélations entre les features
    # Par exemple on peut relier en chaîne les qubits
    for i in range(n_qubits - 1):
        qc.cx(i, i+1)

    # Retourner la porte unitaire correspondante
    qfm_gate = qc.to_gate()
    return qfm_gate

# Exemple
if __name__ == "__main__":
    # Vecteur de features
    data = [0.5, 1.0, -0.7]

    # Créer un circuit et appliquer la QFM Gate
    qc = QuantumCircuit(len(data))
    qfm = QFM_gate(data)
    qc.append(qfm, range(len(data)))

    # Simuler l’état final
    backend = Aer.get_backend('statevector_simulator')
    result = execute(qc, backend=backend).result()
    statevector = result.get_statevector(qc)
    print("État quantique final encodant les features:", data)
    print(statevector)
