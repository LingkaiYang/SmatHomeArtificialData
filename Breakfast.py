# import
import numpy as np
import pandas as pd

# code to generate artifical data for "Breakfast"
ninhabitants = 10

# eat food 
n_samples1, n_samples2, n_samples3 = 250*ninhabitants, 90*ninhabitants, 25*ninhabitants

alpha1, scale1 = 60, 10 
s1 = np.random.gamma(alpha1, scale1, n_samples1)
alpha2, scale2 = 60, 20 
s2 = np.random.gamma(alpha2, scale2, n_samples2)
alpha3, scale3 = 120, 20 
s3 = np.random.gamma(alpha3, scale3, n_samples3)
data1 = np.concatenate((s1.reshape(-1,1),s2.reshape(-1,1),s3.reshape(-1,1)), axis=0)
params_usetoiletR = np.array([[alpha1,scale1,alpha1*scale1],[alpha2,scale2,alpha2*scale2],[alpha3,scale3,alpha3*scale3]])

# wash dishes
n_samples1, n_samples2 = 300*ninhabitants, 65*ninhabitants

alpha1, scale1 = 10, 30  
s1 = np.random.gamma(alpha1, scale1, n_samples1)
alpha2, scale2 = 30, 20 
s2 = np.random.gamma(alpha2, scale2, n_samples2)
data2 = np.concatenate((s1.reshape(-1,1),s2.reshape(-1,1)), axis=0)
params_washhandsR = np.array([[alpha1,scale1,alpha1*scale1], [alpha2,scale2,alpha2*scale2]])
