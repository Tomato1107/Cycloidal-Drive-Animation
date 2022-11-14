import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button

interval = 50 # ms, time between animation frames

fig, ax = plt.subplots(figsize=(6,6))
plt.subplots_adjust(left=0.15, bottom=0.35)

ax.set_aspect('equal')
plt.xlim(-1.6*40,1.6*40)
plt.ylim(-1.6*40,1.6*40)
#plt.grid()
t = np.linspace(0, 2*np.pi, 4096*2)
delta = 1


##inner pinD:
inner_pinD, = ax.plot([0],[0],'b-')
d0, = ax.plot([0],[0],'k-', lw=2)
dotD, = ax.plot([0],[0], 'bo', ms=5)

def update_inner_pinD(n1,D,Rm ,phi):
    RD=D/2
    n = (n1) * 2 +1
    rm = (RD/(n))   
    x0 = Rm*np.sin(t)
    y0 = Rm*np.cos(t)
    d0.set_data(x0,y0)

    x = (Rm+2*rm)*np.cos(t)+2*rm*np.cos(phi)
    y = (Rm+2*rm)*np.sin(t)+2*rm*np.sin(phi)
    inner_pinD.set_data(x,y)
    
    x1 = (Rm+2*rm)*np.cos(phi+np.pi)+2*rm*np.cos(phi)
    y1 = (Rm+2*rm)*np.sin(phi+np.pi)+2*rm*np.sin(phi)
    dotD.set_data(x1, y1)


##hypocycloidA:
num_hypocycloidA = 50
hypocycloidA = [ax.plot([0],[0],'b-')[0] for n in range(num_hypocycloidA)]
num_hypocycloidA1 = 50
hypocycloidA1 = [ax.plot([0],[0],'b-')[0] for n in range(num_hypocycloidA1)]

def hypocycloidA_init():
    for eh in hypocycloidA:
        eh.set_data([0], [0])
    for eh in hypocycloidA1:
        eh.set_data([0], [0])


def update_hypocycloidA(n1,D,phis):
    RD=D/2
    n = (n1) * 2 +1
    rc = (n-1)*(RD/(n))
    rm = (RD/(n))
     
    t1 = np.linspace(0, 2*np.pi/(n-1), 2000)
    t2 = np.linspace(-2*np.pi/(n-1), 0, 2000)

    for i in range(int((n-1)/2)):
        xa = (rc+rm)*np.cos(t1)-rm*np.cos((rc+rm)/rm*t1)
        ya = (rc+rm)*np.sin(t1)-rm*np.sin((rc+rm)/rm*t1)
        x = (xa )*np.cos(-phis/((n-1)/2) -np.pi/(n-1) - (4*i)*np.pi/(n-1))-(ya )*np.sin(-phis/((n-1)/2) -np.pi/(n-1) - (4*i)*np.pi/(n-1))  + 2*rm*np.cos(phis)
        y = (xa )*np.sin(-phis/((n-1)/2) -np.pi/(n-1) - (4*i)*np.pi/(n-1))+(ya )*np.cos(-phis/((n-1)/2) -np.pi/(n-1) - (4*i)*np.pi/(n-1))  + 2*rm*np.sin(phis)
        hypocycloidA[i].set_data(x,y)

        xa1 = (rc-rm)*np.cos(t2)+rm*np.cos((rc-rm)/rm*t2)
        ya1 = (rc-rm)*np.sin(t2)-rm*np.sin((rc-rm)/rm*t2) 
        x1 = (xa1 )*np.cos(-phis/((n-1)/2) -np.pi/(n-1) + (4*i)*np.pi/(n-1))-(ya1 )*np.sin(-phis/((n-1)/2) -np.pi/(n-1) + (4*i)*np.pi/(n-1))  + 2*rm*np.cos(phis)
        y1 = (xa1 )*np.sin(-phis/((n-1)/2) -np.pi/(n-1) + (4*i)*np.pi/(n-1))+(ya1 )*np.cos(-phis/((n-1)/2) -np.pi/(n-1) + (4*i)*np.pi/(n-1))  + 2*rm*np.sin(phis)    
        hypocycloidA1[i].set_data(x1,y1)


##hypocycloidB:
num_hypocycloidB = 50
hypocycloidB = [ax.plot([0],[0],'g-')[0] for n in range(num_hypocycloidB)]
num_hypocycloidB1 = 50
hypocycloidB1 = [ax.plot([0],[0],'g-')[0] for n in range(num_hypocycloidB1)]
def hypocycloidB_init():
    for eh in hypocycloidB:
        eh.set_data([0], [0])
    for eh in hypocycloidB1:
        eh.set_data([0], [0])

def update_hypocycloidB(n1,D, phis):
    RD=D/2
    n = (n1) * 2 +1
    rc = (n+1)*(RD/(n))
    rm = (RD/(n))

    t1 = np.linspace(-2*np.pi/(n+1), 0, 2000)
    t2 = np.linspace(0, 2*np.pi/(n+1), 2000)

    for i in range(int((n+1)/2)):    
        xa = (rc+rm)*np.cos(t1)-rm*np.cos((rc+rm)/rm*t1)
        ya = (rc+rm)*np.sin(t1)-rm*np.sin((rc+rm)/rm*t1)
        x = (xa )*np.cos( np.pi/(n+1) - (4*i)*np.pi/(n+1))-(ya )*np.sin( np.pi/(n+1) - (4*i)*np.pi/(n+1))  
        y = (xa )*np.sin( np.pi/(n+1) - (4*i)*np.pi/(n+1))+(ya )*np.cos( np.pi/(n+1) - (4*i)*np.pi/(n+1))    
        hypocycloidB[i].set_data(x,y)    

        xa1 = (rc-rm)*np.cos(t2)+rm*np.cos((rc-rm)/rm*t2)
        ya1 = (rc-rm)*np.sin(t2)-rm*np.sin((rc-rm)/rm*t2)
        x1 = (xa1 )*np.cos( np.pi/(n+1) - (4*i)*np.pi/(n+1))-(ya1 )*np.sin( np.pi/(n+1) - (4*i)*np.pi/(n+1))  
        y1 = (xa1 )*np.sin( np.pi/(n+1) - (4*i)*np.pi/(n+1))+(ya1 )*np.cos( np.pi/(n+1) - (4*i)*np.pi/(n+1))   
        hypocycloidB1[i].set_data(x1,y1)

axcolor = 'lightgoldenrodyellow'

ax_fm = plt.axes([0.25, 0.08, 0.5, 0.015], facecolor=axcolor)
ax_Rm = plt.axes([0.25, 0.06, 0.5, 0.015], facecolor=axcolor)
ax_N = plt.axes([0.25, 0.04, 0.5, 0.015], facecolor=axcolor)
ax_D = plt.axes([0.25, 0.02, 0.5, 0.015], facecolor=axcolor)


sli_fm = Slider(ax_fm, 'fm', 10, 100, valinit=50, valstep=delta)
sli_Rm = Slider(ax_Rm, 'Rm', 1, 10, valinit=5, valstep=delta)
sli_N = Slider(ax_N, 'N', 3, 40, valinit=16, valstep=delta)
sli_D = Slider(ax_D, 'D', 5, 100, valinit=80,valstep=delta)

def update(val):
    sfm = sli_Rm.val
    sRm = sli_Rm.val
    sN = sli_N.val
    sD = sli_D.val
    ax.set_xlim(-1.6*0.5*sD,1.6*0.5*sD)
    ax.set_ylim(-1.6*0.5*sD,1.6*0.5*sD)

sli_fm.on_changed(update)
sli_Rm.on_changed(update)
sli_N.on_changed(update)
sli_D.on_changed(update)

resetax = plt.axes([0.85, 0.01, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    sli_fm.reset()    
    sli_Rm.reset()
    sli_N.reset()
    sli_D.reset()

button.on_clicked(reset)

def animate(frame):
    sfm = sli_fm.val
    sRm = sli_Rm.val
    sN = sli_N.val
    sD = sli_D.val
    frame = frame+1
    phi = 2*np.pi*frame/sfm

    update_inner_pinD(sN,sD,sRm ,phi)

    hypocycloidA_init()
    update_hypocycloidA(sN,sD, phi)

    hypocycloidB_init()
    update_hypocycloidB(sN,sD, phi)
    fig.canvas.draw_idle()



ani = animation.FuncAnimation(fig, animate,frames=sli_fm.val*(sli_N.val-1), interval=interval)
dpi=100
plt.show()
