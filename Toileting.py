# import
import numpy as np
import pandas as pd

# code to generate artifical data for "Toileting"
# ===================== 'use toilet' samples, three patterns
n_samples1, n_samples2, n_samples3 = 8000, 1600, 400

alpha1, scale1 = 3, 20 # mean and standard deviation
s1 = np.random.gamma(alpha1, scale1, n_samples1)
alpha2, scale2 = 50, 6 # mean and standard deviation
s2 = np.random.gamma(alpha2, scale2, n_samples2)
alpha3, scale3 = 200, 3 # mean and standard deviation
s3 = np.random.gamma(alpha3, scale3, n_samples3)
data1 = np.concatenate((s1.reshape(-1,1),s2.reshape(-1,1),s3.reshape(-1,1)), axis=0)
params_usetoiletR = np.array([[alpha1,scale1,alpha1*scale1],[alpha2,scale2,alpha2*scale2],[alpha3,scale3,alpha3*scale3]])

# ============================= 'wash hands', two patterns, 20 seconds and 40 seconds
n_samples1, n_samples2 = 7000, 3000 

alpha1, scale1 = 20, 1 # mean and standard deviation
s1 = np.random.gamma(alpha1, scale1, n_samples1)
alpha2, scale2 = 40, 1 # mean and standard deviation
s2 = np.random.gamma(alpha2, scale2, n_samples2)
data2 = np.concatenate((s1.reshape(-1,1),s2.reshape(-1,1)), axis=0)
params_washhandsR = np.array([[alpha1,scale1,alpha1*scale1], [alpha2,scale2,alpha2*scale2]])