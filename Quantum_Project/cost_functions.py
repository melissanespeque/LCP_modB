from pack_unpack_params import *
from circuit_construction import *
from qiskit.quantum_info import Statevector, DensityMatrix, partial_trace, state_fidelity
from representatives import *

def weighted_cost_function(params, n_qubits,n_layers, n_classes, x, y, reprs):

    wcf_qc = 0

    theta, w, alpha = unpack_params(params, n_qubits, n_layers, n_classes)
    qc = [circuit(n_qubits, n_layers, theta, w, xi) for xi in x]

    for i in range(len(qc)):
        sv = Statevector(qc[i])

        dm = DensityMatrix(sv)
        true_class = y[i]
        Y = get_Y(n_classes, true_class, reprs)   

        F_all = np.zeros((n_classes, n_qubits))
        for c in range(n_classes):
            
            for q in range(n_qubits):
                other_qubits = [idx for idx in range(n_qubits) if idx != q]
                rho=partial_trace(dm, other_qubits) 

                F_all[c,q] = state_fidelity(rho, DensityMatrix(reprs[c])).real
        
        for c in range(n_classes):
            summ = np.sum(alpha[c] * F_all[c, :]) 
            wcf_qc += (summ - Y[c]) ** 2 
            

    return 0.5*wcf_qc

