import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scienceplots
import csv

plt.style.use(['science','ieee'])

# Incompact3d: xlr, xhr, xh20
# Nek5000: np6, np8, nh20


#================================User-Defined Functions=====================================
def CSV_converter(filename):
    datContent=[['T','D1','D2']]
    # read flash.dat to a list of lists
    for i in open(filename).readlines():
        l = i.strip().split()
        r = []
        for j in l:
            r.append(j)
        datContent.append(r)

    filename.replace("dat", "csv")
    # write it as a new CSV file
    with open(filename, "w") as f:
        writer = csv.writer(f)
        writer.writerows(datContent)
#=======================================================================================


#===================================Plottting Drag Forces==============================                              

# importing files
xlr_drag = pd.read_csv("./xcompact3d/h16-lr/forces.dat")
xhr_drag = pd.read_csv("./xcompact3d/h16-hr/forces.dat")
xh20_drag = pd.read_csv("./xcompact3d/h20/forces.dat")

np6_drag = pd.read_csv("./nek5000/h16p6/data/forces.dat")
np8_drag = pd.read_csv("./nek5000/h16p8/data/forces.dat")
nh20_drag = pd.read_csv("./nek5000/h20/data/forces.dat")

plt.plot(xlr_drag["T"], xlr_drag.D1, color='k')
plt.plot(xhr_drag["T"], xhr_drag.D1, color='b')
plt.plot(xh20_drag["T"], xh20_drag.D1, color='r')
plt.plot(np6_drag['T'], np6_drag.D1+np6_drag.D2, color='g')
plt.plot(np8_drag['T'], np8_drag.D1+np8_drag.D2, color='maroon')
plt.plot(nh20_drag['T'], nh20_drag.D1+nh20_drag.D2, color='orange')
plt.axhline(1.6177, color='darkblue')
plt.text(25,1.4,"Kawaguti(1953)")
plt.xlabel("Time (s)")
plt.ylabel("Drag Coefficient ($C_D$)")
plt.title("Comparison of Drag coefficient")
plt.legend(["X3D-LR", "X3D-HR", "X3D-H20", "NEK-P6", "NEK-P8", "NEK-H20"])
plt.grid()
plt.xlim([1,60])
plt.ylim([1,5])
plt.savefig("drag.png")
plt.close()
#=======================================================================================

#=================================Steady State==========================================
xlr_ss = pd.read_csv("./xcompact3d/h16-lr/data/probe3.csv", header=0, names=['v','x','y','z'])
xhr_ss = pd.read_csv("./xcompact3d/h16-hr/data/probe3.csv", header=0, names=['v','x','y','z'])
xh20_ss = pd.read_csv("./xcompact3d/h20/data/probe3.csv", header=0, names=['v','x','y','z'])

np6_ss = pd.read_csv("./nek5000/h16p6/data/probe1dot5.csv", header=0, names=['t','x','y','z','v'])
np8_ss = pd.read_csv("./nek5000/h16p8/data/probe1dot5.csv", header=0, names=['t','x','y','z','v'])
nh20_ss = pd.read_csv("./nek5000/h20/data/probe1dot5.csv", header=0, names=['t','x','y','z','v'])

plt.plot(np.arange(0,39.75,0.75), xlr_ss.v, color='k')
plt.plot(np.arange(0,60,0.75), xhr_ss.v, color='b')
plt.plot(np.arange(0,30,0.75), xh20_ss.v, color='r')
plt.plot(np6_ss.t, np6_ss.v, color='g')
plt.plot(np8_ss.t, np8_ss.v, color='maroon')
plt.plot(np6_ss.t, nh20_ss.v, color='orange')
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity probe at $x=1.5 D$")
plt.legend(["X3D-LR", "X3D-HR", "X3D-H20", "NEK-P6", "NEK-P8", "NEK-H20"])
plt.grid()
plt.savefig("ss3.png")
plt.close()

xlr_ss = pd.read_csv("./xcompact3d/h16-lr/data/probe4dot5.csv", header=0, names=['v','x','y','z'])
xhr_ss = pd.read_csv("./xcompact3d/h16-hr/data/probe4dot5.csv", header=0, names=['v','x','y','z'])
xh20_ss = pd.read_csv("./xcompact3d/h20/data/probe4dot5.csv", header=0, names=['v','x','y','z'])

np6_ss = pd.read_csv("./nek5000/h16p6/data/probe3.csv", header=0, names=['t','x','y','z','v'])
np8_ss = pd.read_csv("./nek5000/h16p8/data/probe3.csv", header=0, names=['t','x','y','z','v'])
nh20_ss = pd.read_csv("./nek5000/h20/data/probe3.csv", header=0, names=['t','x','y','z','v'])

plt.plot(np.arange(0,39.75,0.75), xlr_ss.v, color='k')
plt.plot(np.arange(0,60,0.75), xhr_ss.v, color='b')
plt.plot(np.arange(0,30,0.75), xh20_ss.v, color='r')
plt.plot(np6_ss.t, np6_ss.v, color='g')
plt.plot(np8_ss.t, np8_ss.v, color='maroon')
plt.plot(nh20_ss.t, nh20_ss.v, color='orange')
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity probe at $x=3 D$")
plt.legend(["X3D-LR", "X3D-HR", "X3D-H20", "NEK-P6", "NEK-P8", "NEK-H20"])
plt.grid()
plt.savefig("ss4dot5.png")
plt.close()
#=======================================================================================================

#======================================Velocity Distribution============================================
ref_b = pd.read_csv("before.csv",names=['x','v'])
ref_a = pd.read_csv("wake.csv",names=['x','v'])
ref_a.x = ref_a.x*0.5
ref_b.x = ref_b.x*(-0.5)

xlr_xv = pd.read_csv("./xcompact3d/h16-lr/data/xvel.csv", header=0, names=['v1','v2','v3','x'])
xhr_xv = pd.read_csv("./xcompact3d/h16-hr/data/xvel.csv", header=0, names=['v1','v2','v3','x'])
xh20_xv = pd.read_csv("./xcompact3d/h20/data/xvel.csv", header=0, names=['v1','v2','v3','x'])

np6_xv = pd.read_csv("./nek5000/h16p6/data/xvel.csv", header=0, names=['v1','v2','v3','x'])
np8_xv = pd.read_csv("./nek5000/h16p8/data/xvel.csv", header=0, names=['v1','v2','v3','x'])
nh20_xv = pd.read_csv("./nek5000/h20/data/xvel.csv", header=0, names=['v1','v2','v3','x'])

plt.plot(xlr_xv.x-1.5, np.sqrt(xlr_xv.v1**2 + xlr_xv.v2**2 + xlr_xv.v3**2), color='k')
plt.plot(xhr_xv.x-1.5, np.sqrt(xhr_xv.v1**2 + xhr_xv.v2**2 + xhr_xv.v3**2), color='b')
plt.plot(xh20_xv.x-1.5, np.sqrt(xh20_xv.v1**2 + xh20_xv.v2**2 + xh20_xv.v3**2), color='r')
plt.plot(np6_xv.x-2, np.sqrt(np6_xv.v1**2 + np6_xv.v2**2 + np6_xv.v3**2), color='g')
plt.plot(np8_xv.x-2, np.sqrt(np8_xv.v1**2 + np8_xv.v2**2 + np8_xv.v3**2), color='maroon')
plt.plot(nh20_xv.x-2, np.sqrt(nh20_xv.v1**2 + nh20_xv.v2**2 + nh20_xv.v3**2), color='orange')
plt.plot(ref_b.x,ref_b.v, color='darkblue', linestyle=':')
plt.plot(ref_a.x,np.abs(ref_a.v), color='darkblue', linestyle=':')
plt.xlabel("$x$ (in Diameters)")
plt.ylabel("Velocity Magnitude (m/s)")
plt.title("Velocity Distribution along the x-axis")
plt.legend(["X3D-LR", "X3D-HR", "X3D-H20", "NEK-P6", "NEK-P8", "NEK-H20", "Kawaguti(1953)"])
plt.xlim([-2,7])
plt.grid()
plt.savefig("xv.png")
plt.close()