from qiskit import QuantumCircuit

def circuit(n_qubits, n_layers, theta, w, x):

    qc = QuantumCircuit(n_qubits)
    
    for j in range(n_qubits):
        for i in range(n_layers):
            phi = theta[j][i] + w[j][i]*x

            qc.rz(phi[2], j)
            qc.ry(phi[0], j)
            qc.rz(phi[1], j)
    return qc