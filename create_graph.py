import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D


n = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

# 10 tests da bst - pior caso
t_n_bst = [537.37, 1018.88, 1395.45, 2238.63, 2594.51, 3038.43, 3680.26, 4109.18, 4670.38, 5011.3]
# 10 tests da avl - pior caso
t_n_avl = [7.82, 8.94, 9.6, 10.1, 10.36, 10.64, 10.82, 10.92, 11.22, 11.44]
# 10 tests da rbt - pior caso
t_n_rbt = [8.04, 9.29, 9.65, 10.06, 10.91, 11.17, 11.34, 11.67, 12.1, 12.05]

line1, = plt.plot(n, t_n_bst, 'go', label='bst', linestyle='--')
line2, = plt.plot(n, t_n_avl, 'bo', label='avl', linestyle='--')
line3, = plt.plot(n, t_n_rbt, 'ro', label='rbt', linestyle='--')

plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)})

plt.xlabel('n')
plt.ylabel('T(n)')
plt.show()
