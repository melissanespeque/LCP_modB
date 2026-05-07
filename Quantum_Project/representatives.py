import numpy as np

def representatives(n_classes, qubits_lab):

    reprs = np.zeros((n_classes, 2**qubits_lab), dtype = 'complex')
    if qubits_lab == 1:
        if n_classes == 0:
            raise ValueError('Nonsense classifier')
        if n_classes == 1:
            raise ValueError('Nonsense classifier')
        if n_classes == 2:
            reprs[0] = np.array([1, 0])
            reprs[1] = np.array([0, 1])
        if n_classes == 3:
            reprs[0] = np.array([1, 0])
            reprs[1] = np.array([1 / 2, np.sqrt(3) / 2])
            reprs[2] = np.array([1 / 2, -np.sqrt(3) / 2])
        if n_classes == 4:
            reprs[0] = np.array([1, 0])
            reprs[1] = np.array([1 / np.sqrt(3), np.sqrt(2 / 3)])
            reprs[2] = np.array([1 / np.sqrt(3), np.exp(1j * 2 * np.pi / 3) * np.sqrt(2 / 3)])
            reprs[3] = np.array([1 / np.sqrt(3), np.exp(-1j * 2 * np.pi / 3) * np.sqrt(2 / 3)])
        if n_classes == 6:
            reprs[0] = np.array([1, 0])
            reprs[1] = np.array([0, 1])
            reprs[2] = 1 / np.sqrt(2) * np.array([1, 1])
            reprs[3] = 1 / np.sqrt(2) * np.array([1, -1])
            reprs[4] = 1 / np.sqrt(2) * np.array([1, 1j])
            reprs[5] = 1 / np.sqrt(2) * np.array([1, -1j])
        if qubits_lab == 2:
            if n_classes == 0:
                raise ValueError('Nonsense classifier')
            if n_classes == 1:
                raise ValueError('Nonsense classifier')
            if n_classes == 2:
                reprs[0] = np.array([1, 0, 0, 0])
                reprs[1] = np.array([0, 0, 0, 1])
            if n_classes == 3:
                reprs[0] = np.array([1, 0, 0, 0])
                reprs[1] = np.array([0, 1, 0, 0])
                reprs[2] = np.array([0, 0, 1, 0])
            if n_classes == 4:
                reprs[0] = np.array([1, 0, 0, 0])
                reprs[1] = np.array([0, 1, 0, 0])
                reprs[2] = np.array([0, 0, 1, 0])
                reprs[3] = np.array([0, 0, 0, 1])
            
    return reprs

def get_Y(n_classes, true_class, reprs): 
    
    psi_true = reprs[true_class] 
    Y = np.zeros(n_classes)
    
    for c in range(n_classes):
        overlap = np.dot(np.conj(psi_true), reprs[c])  
        Y[c] = np.abs(overlap) ** 2
    
    return Y