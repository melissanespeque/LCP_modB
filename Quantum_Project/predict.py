from circuit_construction import *
from qiskit.quantum_info import Statevector, DensityMatrix, partial_trace, state_fidelity
from representatives import *

def predict(x, n_qubits, n_layers, n_classes, theta, w, alpha, reprs):
    
    predictions = []
    
    for xi in x:
        qc = circuit(n_qubits, n_layers, theta, w, xi)
        sv = Statevector(qc)
        dm = DensityMatrix(sv)
        
        # compute score for each class
        scores = np.zeros(n_classes)
        for c in range(n_classes):
            for q in range(n_qubits):
                other_qubits = [idx for idx in range(n_qubits) if idx != q]
                rho = partial_trace(dm, other_qubits)
                scores[c] += alpha[c, q] * state_fidelity(rho, DensityMatrix(reprs[c])).real
        
        predictions.append(np.argmax(scores))
    
    return np.array(predictions)