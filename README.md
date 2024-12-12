# quantum_gates

-> QFM Gate pour encoder des features classiques dans un circuit quantique. RZ pour les phases, CNOT pour l’entanglement. Rapide à tester sur du QML, modulable selon les données. Simplifie l'encodage des données classiques en états quantiques. Gère les phases (RZ) et les corrélations (CNOT), utile pour explorer des feature maps dans les algos de machine learning quantique. Encapsulation d’un encodage complexe dans une seule porte QFM. Réduit le temps de dev, facilite le prototypage en QML, et évite de réinventer les feature maps à chaque projet.

-> Generalized Entangler Gate pour créer une superposition uniforme sur tous les qubits. Pratique pour l’init state dans les algo quantiques type Grover. Juste un bloc Hadamard pour chaque qubit, simple et clean. Simplifie l'initiation des circuits avec une superposition uniforme.
