import numpy as np

def params_construction(n_qubits, n_layers, n_classes):
    
    theta = np.random.uniform(0, 2*np.pi, (n_qubits, n_layers, 3))
    w = np.random.uniform(0, 1, (n_qubits, n_layers, 3))
    alpha = np.random.uniform(0, 1, (n_classes, n_qubits))
    
    return theta, w, alpha