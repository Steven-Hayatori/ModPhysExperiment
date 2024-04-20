## Steven Linden
import numpy as np
import cmath

lambda_0 = 17.6 * (10**-3)
lambda_g = 21 * (10**-3)
rou_1 = 40
rou_2 = 32.5
d_1 = 90.8* (10**-3)
d_2 = 80.3* (10**-3)

lambda_c = 31.2 * (10**-3)
l = 1.1 * (10**-3)
k_g = 2*np.pi/lambda_g

bi_duan = ((1 - 1j*rou_1*cmath.tan(k_g*d_1))/(rou_1 - 1j*cmath.tan(k_g*d_1)))
bi_kai = ((1 - 1j*rou_2*cmath.tan(k_g*d_2))/(rou_2 - 1j*cmath.tan(k_g*d_2)))

bi_jie = cmath.sqrt(bi_duan*bi_kai)

gamma = (cmath.atan(cmath.sqrt(bi_kai/bi_duan)))/l

miu = - 1j*(lambda_g/(2*np.pi))*gamma*bi_jie
print(f'miu = {miu:.4g}')
epsilon = (lambda_0/(2*np.pi))**2 * (((2*np.pi/lambda_c)**2 - gamma**2)/miu)
print(f'epsilon = {epsilon:.4g}')