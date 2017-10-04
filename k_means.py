import numpy as np
KMeansFit = lambda X, centers, max_itr, k: [[np.mean(X[np.argmin([np.linalg.norm(X - m_r, axis=1) for m_r in centers], axis=0) == r], axis=0) for r in range(k)] for itr in range(max_itr)]
