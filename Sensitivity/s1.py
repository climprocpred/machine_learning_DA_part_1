import numpy as np
from Experiment import *
import pickle

np.random.seed(0)
F = 8
N = 40
nens = 100
gamma = 1
loc = 5
x0 = F*np.ones(N)
x0[0] = F+.01
dt = 0.05
T = 2000
experiment = Experiment(x0,N,F,dt,nens=nens,loc=loc,gamma=gamma)
experiment.getTrue(T)
r = experiment.xx.std()*.2
experiment.ystd = r
experiment.Makeobs()
experiment.Assimilate()
with open('s1.pickle','wb') as f:
    pickle.dump(experiment,f)