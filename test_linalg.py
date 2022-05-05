from linalg import *
import numpy as np

def test_scal_prod():

    u = np.array([1,0,0])
    v = np.array([0,1,0])
    w = np.array([0,0,1])

    assert ScalProd(u,v) == ScalProd(v,w) == ScalProd(w, u) == 0
