import numpy as np

def mat_cos_sim(vectors_1, vectors_2):
    assert vectors_1.shape[1] == vectors_2.shape[1]
    norms_1 = np.linalg.norm(vectors_1, axis=1).reshape(-1, 1)
    norms_2 = np.linalg.norm(vectors_2, axis=1).reshape(-1, 1)
    dot_products = np.dot(vectors_1, vectors_2.T)
    similarities = dot_products / (norms_1 * norms_2.T)
    return similarities
    
source_vecs = np.random.random((20, 50))
target_vecs = np.random.random((100, 50))

similarities = mat_cos_sim(source_vecs, target_vecs)
