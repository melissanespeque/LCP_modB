import numpy as np

def pack_params(theta, w, alpha):

    params = np.concatenate([theta.ravel(), w.ravel() ,alpha.ravel()])

    return params

def unpack_params(params, n_qubits, n_layers, n_classes):

    theta_size = n_qubits*n_layers*3
    w_size = n_qubits*n_layers*3

    theta = params[:theta_size].reshape(n_qubits, n_layers, 3)
    w = params[theta_size:theta_size+w_size].reshape(n_qubits, n_layers, 3)
    alpha = params[theta_size+w_size: ].reshape(n_classes, n_qubits)

    return theta, w, alpha
