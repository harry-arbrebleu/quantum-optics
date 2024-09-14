import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import math
import pickle

rows = 5
cols = 5
n = rows * cols
q, p, tau = sp.symbols('q p tau')
i = sp.I
h = [(sp.pi ** (-1 / 4)) * sp.exp(- q ** 2 / 2)]
w = list()
# w = [
#     sp.exp(-p**2 - q**2)/sp.pi,
#     (4*p**2 + 4*q**2 - 2)*sp.exp(-p**2 - q**2)/(2*sp.pi),
#     (8*p**4 + 16*p**2*q**2 - 16*p**2 + 8*q**4 - 16*q**2 + 4)*sp.exp(-p**2 - q**2)/(2*sp.pi),
#     (16*p**6 + 48*p**4*q**2 - 72*p**4 + 48*p**2*q**4 - 144*p**2*q**2 + 72*p**2 + 16*q**6 - 72*q**4 + 72*q**2 - 12)*sp.exp(-p**2 - q**2)/(2*sp.pi),
#     (32*p**8 + 128*p**6*q**2 - 256*p**6 + 192*p**4*q**4 - 768*p**4*q**2 + 576*p**4 + 128*p**2*q**6 - 768*p**2*q**4 + 1152*p**2*q**2 - 384*p**2 + 32*q**8 - 256*q**6 + 576*q**4 - 384*q**2 + 48)*sp.exp(-p**2 - q**2)/(2*sp.pi),
#     (64*p**10 + 320*p**8*q**2 - 800*p**8 + 640*p**6*q**4 - 3200*p**6*q**2 + 3200*p**6 + 640*p**4*q**6 - 4800*p**4*q**4 + 9600*p**4*q**2 - 4800*p**4 + 320*p**2*q**8 - 3200*p**2*q**6 + 9600*p**2*q**4 - 9600*p**2*q**2 + 2400*p**2 + 64*q**10 - 800*q**8 + 3200*q**6 - 4800*q**4 + 2400*q**2 - 240)*sp.exp(-p**2 - q**2)/(2*sp.pi),
#     (128*p**12 + 768*p**10*q**2 - 2304*p**10 + 1920*p**8*q**4 - 11520*p**8*q**2 + 14400*p**8 + 2560*p**6*q**6 - 23040*p**6*q**4 + 57600*p**6*q**2 - 38400*p**6 + 1920*p**4*q**8 - 23040*p**4*q**6 + 86400*p**4*q**4 - 115200*p**4*q**2 + 43200*p**4 + 768*p**2*q**10 - 11520*p**2*q**8 + 57600*p**2*q**6 - 115200*p**2*q**4 + 86400*p**2*q**2 - 17280*p**2 + 128*q**12 - 2304*q**10 + 14400*q**8 - 38400*q**6 + 43200*q**4 - 17280*q**2 + 1440)*sp.exp(-p**2 - q**2)/(2*sp.pi),
#     (256*p**14 + 1792*p**12*q**2 - 6272*p**12 + 5376*p**10*q**4 - 37632*p**10*q**2 + 56448*p**10 + 8960*p**8*q**6 - 94080*p**8*q**4 + 282240*p**8*q**2 - 235200*p**8 + 8960*p**6*q**8 - 125440*p**6*q**6 + 564480*p**6*q**4 - 940800*p**6*q**2 + 470400*p**6 + 5376*p**4*q**10 - 94080*p**4*q**8 + 564480*p**4*q**6 - 1411200*p**4*q**4 + 1411200*p**4*q**2 - 423360*p**4 + 1792*p**2*q**12 - 37632*p**2*q**10 + 282240*p**2*q**8 - 940800*p**2*q**6 + 1411200*p**2*q**4 - 846720*p**2*q**2 + 141120*p**2 + 256*q**14 - 6272*q**12 + 56448*q**10 - 235200*q**8 + 470400*q**6 - 423360*q**4 + 141120*q**2 - 10080)*sp.exp(-p**2 - q**2)/(2*sp.pi),
#     (512*p**16 + 4096*p**14*q**2 - 16384*p**14 + 14336*p**12*q**4 - 114688*p**12*q**2 + 200704*p**12 + 28672*p**10*q**6 - 344064*p**10*q**4 + 1204224*p**10*q**2 - 1204224*p**10 + 35840*p**8*q**8 - 573440*p**8*q**6 + 3010560*p**8*q**4 - 6021120*p**8*q**2 + 3763200*p**8 + 28672*p**6*q**10 - 573440*p**6*q**8 + 4014080*p**6*q**6 - 12042240*p**6*q**4 + 15052800*p**6*q**2 - 6021120*p**6 + 14336*p**4*q**12 - 344064*p**4*q**10 + 3010560*p**4*q**8 - 12042240*p**4*q**6 + 22579200*p**4*q**4 - 18063360*p**4*q**2 + 4515840*p**4 + 4096*p**2*q**14 - 114688*p**2*q**12 + 1204224*p**2*q**10 - 6021120*p**2*q**8 + 15052800*p**2*q**6 - 18063360*p**2*q**4 + 9031680*p**2*q**2 - 1290240*p**2 + 512*q**16 - 16384*q**14 + 200704*q**12 - 1204224*q**10 + 3763200*q**8 - 6021120*q**6 + 4515840*q**4 - 1290240*q**2 + 80640)*sp.exp(-p**2 - q**2)/(2*sp.pi),
#     (1024*p**18 + 9216*p**16*q**2 - 41472*p**16 + 36864*p**14*q**4 - 331776*p**14*q**2 + 663552*p**14 + 86016*p**12*q**6 - 1161216*p**12*q**4 + 4644864*p**12*q**2 - 5419008*p**12 + 129024*p**10*q**8 - 2322432*p**10*q**6 + 13934592*p**10*q**4 - 32514048*p**10*q**2 + 24385536*p**10 + 129024*p**8*q**10 - 2903040*p**8*q**8 + 23224320*p**8*q**6 - 81285120*p**8*q**4 + 121927680*p**8*q**2 - 60963840*p**8 + 86016*p**6*q**12 - 2322432*p**6*q**10 + 23224320*p**6*q**8 - 108380160*p**6*q**6 + 243855360*p**6*q**4 - 243855360*p**6*q**2 + 81285120*p**6 + 36864*p**4*q**14 - 1161216*p**4*q**12 + 13934592*p**4*q**10 - 81285120*p**4*q**8 + 243855360*p**4*q**6 - 365783040*p**4*q**4 + 243855360*p**4*q**2 - 52254720*p**4 + 9216*p**2*q**16 - 331776*p**2*q**14 + 4644864*p**2*q**12 - 32514048*p**2*q**10 + 121927680*p**2*q**8 - 243855360*p**2*q**6 + 243855360*p**2*q**4 - 104509440*p**2*q**2 + 13063680*p**2 + 1024*q**18 - 41472*q**16 + 663552*q**14 - 5419008*q**12 + 24385536*q**10 - 60963840*q**8 + 81285120*q**6 - 52254720*q**4 + 13063680*q**2 - 725760)*sp.exp(-p**2 - q**2)/(2*sp.pi),
#     (2048*p**20 + 20480*p**18*q**2 - 102400*p**18 + 92160*p**16*q**4 - 921600*p**16*q**2 + 2073600*p**16 + 245760*p**14*q**6 - 3686400*p**14*q**4 + 16588800*p**14*q**2 - 22118400*p**14 + 430080*p**12*q**8 - 8601600*p**12*q**6 + 58060800*p**12*q**4 - 154828800*p**12*q**2 + 135475200*p**12 + 516096*p**10*q**10 - 12902400*p**10*q**8 + 116121600*p**10*q**6 - 464486400*p**10*q**4 + 812851200*p**10*q**2 - 487710720*p**10 + 430080*p**8*q**12 - 12902400*p**8*q**10 + 145152000*p**8*q**8 - 774144000*p**8*q**6 + 2032128000*p**8*q**4 - 2438553600*p**8*q**2 + 1016064000*p**8 + 245760*p**6*q**14 - 8601600*p**6*q**12 + 116121600*p**6*q**10 - 774144000*p**6*q**8 + 2709504000*p**6*q**6 - 4877107200*p**6*q**4 + 4064256000*p**6*q**2 - 1161216000*p**6 + 92160*p**4*q**16 - 3686400*p**4*q**14 + 58060800*p**4*q**12 - 464486400*p**4*q**10 + 2032128000*p**4*q**8 - 4877107200*p**4*q**6 + 6096384000*p**4*q**4 - 3483648000*p**4*q**2 + 653184000*p**4 + 20480*p**2*q**18 - 921600*p**2*q**16 + 16588800*p**2*q**14 - 154828800*p**2*q**12 + 812851200*p**2*q**10 - 2438553600*p**2*q**8 + 4064256000*p**2*q**6 - 3483648000*p**2*q**4 + 1306368000*p**2*q**2 - 145152000*p**2 + 2048*q**20 - 102400*q**18 + 2073600*q**16 - 22118400*q**14 + 135475200*q**12 - 487710720*q**10 + 1016064000*q**8 - 1161216000*q**6 + 653184000*q**4 - 145152000*q**2 + 7257600)*sp.exp(-p**2 - q**2)/(2*sp.pi),
#     (4096*p**22 + 45056*p**20*q**2 - 247808*p**20 + 225280*p**18*q**4 - 2478080*p**18*q**2 + 6195200*p**18 + 675840*p**16*q**6 - 11151360*p**16*q**4 + 55756800*p**16*q**2 - 83635200*p**16 + 1351680*p**14*q**8 - 29736960*p**14*q**6 + 223027200*p**14*q**4 - 669081600*p**14*q**2 + 669081600*p**14 + 1892352*p**12*q**10 - 52039680*p**12*q**8 + 520396800*p**12*q**6 - 2341785600*p**12*q**4 + 4683571200*p**12*q**2 - 3278499840*p**12 + 1892352*p**10*q**12 - 62447616*p**10*q**10 + 780595200*p**10*q**8 - 4683571200*p**10*q**6 + 14050713600*p**10*q**4 - 19670999040*p**10*q**2 + 9835499520*p**10 + 1351680*p**8*q**14 - 52039680*p**8*q**12 + 780595200*p**8*q**10 - 5854464000*p**8*q**8 + 23417856000*p**8*q**6 - 49177497600*p**8*q**4 + 49177497600*p**8*q**2 - 17563392000*p**8 + 675840*p**6*q**16 - 29736960*p**6*q**14 + 520396800*p**6*q**12 - 4683571200*p**6*q**10 + 23417856000*p**6*q**8 - 65569996800*p**6*q**6 + 98354995200*p**6*q**4 - 70253568000*p**6*q**2 + 17563392000*p**6 + 225280*p**4*q**18 - 11151360*p**4*q**16 + 223027200*p**4*q**14 - 2341785600*p**4*q**12 + 14050713600*p**4*q**10 - 49177497600*p**4*q**8 + 98354995200*p**4*q**6 - 105380352000*p**4*q**4 + 52690176000*p**4*q**2 - 8781696000*p**4 + 45056*p**2*q**20 - 2478080*p**2*q**18 + 55756800*p**2*q**16 - 669081600*p**2*q**14 + 4683571200*p**2*q**12 - 19670999040*p**2*q**10 + 49177497600*p**2*q**8 - 70253568000*p**2*q**6 + 52690176000*p**2*q**4 - 17563392000*p**2*q**2 + 1756339200*p**2 + 4096*q**22 - 247808*q**20 + 6195200*q**18 - 83635200*q**16 + 669081600*q**14 - 3278499840*q**12 + 9835499520*q**10 - 17563392000*q**8 + 17563392000*q**6 - 8781696000*q**4 + 1756339200*q**2 - 79833600)*sp.exp(-p**2 - q**2)/(2*sp.pi)
#     ]
for s in range(n):
    # print(s)
    wnew = sp.exp(-i * p * tau) * h[s].subs(q, q - tau / 2) * h[s].subs(q, q + tau / 2)
    func = (1 / (2 * sp.pi)) * sp.integrate(wnew, (tau, -sp.oo, sp.oo)).simplify()
    w.append(func)
    nw = (1 / sp.sqrt(2)) * (q * h[s] - sp.diff(h[s]))
    h.append(nw)
    print(func)
fig = plt.figure(figsize=(15, 10))
plt.rcParams['font.size'] = 14
plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'serif'
with open('w.pkl', 'wb') as f:
    pickle.dump(w, f)
with open('h.pkl', 'wb') as f:
    pickle.dump(h, f)

for s in range(n):
    print(s)
    row = s // cols
    col = s % cols
    ax = fig.add_subplot(rows, cols, s + 1, projection='3d')
    w_numeric = sp.lambdify([q, p], w[s], "numpy")
    q_vals = np.linspace(-1.5, 1.5, 1000)
    p_vals = np.linspace(-1.5, 1.5, 1000)
    Q, P = np.meshgrid(q_vals, p_vals)
    ax.plot_surface(Q, P, w_numeric(Q, P), cmap="coolwarm")
    ax.set_xlabel(r'$q$')
    ax.set_ylabel(r'$p$')
    # t = "W_{" + str(s) + "}(q, p)"
    # ax.set_zlabel(fr"${t}$")
    ax.set_title(fr"$|{s}\rangle$")
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, wspace=0.3, hspace=0.3)
plt.savefig('./image/wigner_plots.pdf')
plt.show()