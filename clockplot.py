import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import datetime
from numpy import pi



a=[['18:33:44','18:59:06']]
d=[]

for x in a:
	mstart,mfinish=int(x[0][3:5]),int(x[1][3:5])
	hstart,hfinish=int(x[0][:2]),int(x[1][:2])
	if hstart!=hfinish:
		for mi in range(mstart,60):
			#print("{}:{}".format(hstart,mi))
			sec=(hstart*3600)+(mi*60)
			d.append((sec/(12*3600))*2*np.pi)




		for hr in range(hstart+1,hfinish):
			for mi in range(0,60):
				#print("{}:{}".format(hr,mi))
				sec=(hr*3600)+(mi*60)
				d.append((sec/(12*3600))*2*np.pi)

		for hr in range(hfinish,hfinish+1):
			for mi in range(0,mfinish+1):
				#print("{}:{}".format(hr,mi))
				sec=(hr*3600)+(mi*60)
				d.append((sec/(12*3600))*2*np.pi)
	else:
		for mi in range(mstart,mfinish+1):
			sec=(hstart*3600)+(mi*60)
			d.append((sec/(12*3600))*2*np.pi)



ax = plt.subplot(111, polar=True)
plt.setp(ax.get_yticklabels(), visible=False)
ax.set_xticks(np.linspace(0, 2*pi, 12, endpoint=False))
ax.set_xticklabels([12,1,2,3,4,5,6,7,8,9,10,11])
ax.set_theta_direction(-1)
ax.set_theta_offset(pi/2.0)    



ax.bar(d, np.full(len(d),1), width=0.00939, bottom=0.0, color='g',alpha=1 ,linewidth=0)
plt.ylim(0,1)
plt.grid(False)
plt.show()
