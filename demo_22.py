import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button

interval = 50 # ms, time between animation frames

fig, ax = plt.subplots(figsize=(6,6))
ax.set_title('Reduction ratio '+(str(int(-14)))+':1')
plt.subplots_adjust(left=0.15, bottom=0.35)

ax.set_aspect('equal')
plt.xlim(-1.4*40,1.4*40)
plt.ylim(-1.4*40,1.4*40)
#plt.grid()
t = np.linspace(0, 2*np.pi, 10000)
delta = 1


## draw pinA
num_pinsA = 61
pinsA = [ax.plot([], [], 'k-')[0] for n in range(num_pinsA)]
def draw_pinA_init():
    for p in pinsA:
        p.set_data([0], [0])
def pinA_update(e,n,n1,d,D, phis):
    for i in range(int(n)):    
        xd = (d/2*np.cos(t)+ D/2*np.cos(2*i*np.pi/n)) + e*np.cos(phis)
        yd = (d/2*np.sin(t)+ D/2*np.sin(2*i*np.pi/n)) + e*np.sin(phis)
        x = xd*np.cos(-phis/(n1+1)) - yd*np.sin(-phis/(n1+1)) 
        y = xd*np.sin(-phis/(n1+1)) + yd*np.cos(-phis/(n1+1)) 
        pinsA[i].set_data(x,y)

## draw pinB
num_pinsB = 61
pinsB = [ax.plot([], [], 'k-')[0] for n in range(num_pinsB)]
def draw_pinB_init():
    for p in pinsB:
        p.set_data([0], [0])
def pinB_update(e,n,d,D, phis):
    for i in range(int(n)):    
        xd = (d/2*np.cos(t)+ D/2*np.cos(2*i*np.pi/n)) + e*np.cos(phis)
        yd = (d/2*np.sin(t)+ D/2*np.sin(2*i*np.pi/n)) + e*np.sin(phis)
        x = xd*np.cos(-phis/(n+1)) - yd*np.sin(-phis/(n+1)) 
        y = xd*np.sin(-phis/(n+1)) + yd*np.cos(-phis/(n+1)) 
        pinsB[i].set_data(x,y)

## draw drive_pin
d0, = ax.plot([0],[0],'r-', lw=2)

def drive_pin_update(r):
    x = r*np.sin(t)
    y = r*np.cos(t)
    d0.set_data(x,y)


##inner pin:
inner_pin, = ax.plot([0],[0],'g-')
dot, = ax.plot([0],[0], 'go', ms=5)

def update_inner_pin(e,n,Rm, phi):
    x = (Rm+e)*np.cos(t)+e*np.cos(phi-phi/(n+1))
    y = (Rm+e)*np.sin(t)+e*np.sin(phi-phi/(n+1))
    inner_pin.set_data(x,y)
    
    x1 = (Rm+e)*np.cos(phi-phi/(n+1))+e*np.cos(phi-phi/(n+1))
    y1 = (Rm+e)*np.sin(phi-phi/(n+1))+e*np.sin(phi-phi/(n+1))
    dot.set_data(x1, y1)

##hypocycloidA:
hypocycloidA, = ax.plot([0],[0],'r-')
edotA, = ax.plot([0],[0], 'ro', ms=5)

def update_hypocycloidA(e,n,n1,D,d, phis):

    RD=D/2
    rd=d/2
    rc = (n-1)*(RD/n)
    rm = (RD/n)

    xa = (rc+rm)*np.cos(t)-e*np.cos((rc+rm)/rm*t)
    ya = (rc+rm)*np.sin(t)-e*np.sin((rc+rm)/rm*t)

    dxa = (rc+rm)*(-np.sin(t)+(e/rm)*np.sin((rc+rm)/rm*t))
    dya = (rc+rm)*(np.cos(t)-(e/rm)*np.cos((rc+rm)/rm*t))

    x = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.cos(-phis/(n-1) -phis/(n1+1) - np.pi/(n-1))-(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.sin(-phis/(n-1) -phis/(n1+1) - np.pi/(n-1))  
    y = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.sin(-phis/(n-1) -phis/(n1+1) - np.pi/(n-1))+(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.cos(-phis/(n-1) -phis/(n1+1)- np.pi/(n-1)) 

    x1 = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.cos(-phis/(n-1) -phis/(n1+1) )-(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.sin(-phis/(n-1) -phis/(n1+1) )  
    y1 = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.sin(-phis/(n-1) -phis/(n1+1) )+(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.cos(-phis/(n-1) -phis/(n1+1)) 
    
    hypocycloidA.set_data(x,y)
    edotA.set_data(x1[0], y1[0])


##hypocycloidC:
hypocycloidC, = ax.plot([0],[0],'g-')

def update_hypocycloidC(e,n,n1,D,d, phis):
    #lamuda = 0.9
    RD=D/2
    rd=d/2
    rc = (n)*(RD/n)
    rm = (RD/n)

    xa = (rc+rm)*np.cos(t)-e*np.cos((rc+rm)/rm*t)
    ya = (rc+rm)*np.sin(t)-e*np.sin((rc+rm)/rm*t)

    dxa = (rc+rm)*(-np.sin(t)+(e/rm)*np.sin((rc+rm)/rm*t))
    dya = (rc+rm)*(np.cos(t)-(e/rm)*np.cos((rc+rm)/rm*t))

    xd = xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya)  + e*np.cos(phis)
    yd = ya + rd/np.sqrt(dxa**2 + dya**2)*dxa + e*np.sin(phis)

    x = (xd )*np.cos(-phis/(n1+1))-(yd )*np.sin(-phis/(n1+1))
    y = (xd )*np.sin(-phis/(n1+1))+(yd )*np.cos(-phis/(n1+1)) 

    hypocycloidC.set_data(x,y)


##hypocycloidB:
hypocycloidB, = ax.plot([0],[0],'b-')
edotB, = ax.plot([0],[0], 'bo', ms=5)

def update_hypocycloidB(e,n,D,d, phis):
    RD=D/2
    rd=d/2
    rc = (n+1)*(RD/n)
    rm = (RD/n)

    xa = (rc-rm)*np.cos(t)+e*np.cos((rc-rm)/rm*t)
    ya = (rc-rm)*np.sin(t)-e*np.sin((rc-rm)/rm*t)

    dxa = (rc-rm)*(-np.sin(t)-(e/rm)*np.sin((rc-rm)/rm*t))
    dya = (rc-rm)*(np.cos(t)-(e/rm)*np.cos((rc-rm)/rm*t))

    x = xa - rd/np.sqrt(dxa**2 + dya**2)*(-dya)
    y = ya - rd/np.sqrt(dxa**2 + dya**2)*dxa

    hypocycloidB.set_data(x,y)
    edotB.set_data(x[0], y[0])


##hypocycloidD:
hypocycloidD, = ax.plot([0],[0],'g-')

def update_hypocycloidD(e,n,D,d, phis):

    RD=D/2
    rd=d/2
    rc = (n)*(RD/n)
    rm = (RD/n)

    xa = (rc-rm)*np.cos(t)+e*np.cos((rc-rm)/rm*t)
    ya = (rc-rm)*np.sin(t)-e*np.sin((rc-rm)/rm*t)

    dxa = (rc-rm)*(-np.sin(t)-(e/rm)*np.sin((rc-rm)/rm*t))
    dya = (rc-rm)*(np.cos(t)-(e/rm)*np.cos((rc-rm)/rm*t))

    xd = xa - rd/np.sqrt(dxa**2 + dya**2)*(-dya) + e*np.cos(phis)
    yd = ya - rd/np.sqrt(dxa**2 + dya**2)*dxa + e*np.sin(phis)

    x = (xd )*np.cos(-phis/(n+1))-(yd )*np.sin(-phis/(n+1)) 
    y = (xd )*np.sin(-phis/(n+1))+(yd )*np.cos(-phis/(n+1))  

    hypocycloidD.set_data(x,y)


axcolor = 'lightgoldenrodyellow'
ax_fm = plt.axes([0.25, 0.16, 0.5, 0.015], facecolor=axcolor)
ax_Rm = plt.axes([0.25, 0.14, 0.5, 0.015], facecolor=axcolor)
ax_e = plt.axes([0.25, 0.12, 0.5, 0.015], facecolor=axcolor)
ax_N1 = plt.axes([0.25, 0.10, 0.5, 0.015], facecolor=axcolor)
ax_N = plt.axes([0.25, 0.08, 0.5, 0.015], facecolor=axcolor)
ax_d = plt.axes([0.25, 0.06, 0.5, 0.015], facecolor=axcolor)
ax_D1 = plt.axes([0.25, 0.04, 0.5, 0.015], facecolor=axcolor)
ax_D = plt.axes([0.25, 0.02, 0.5, 0.015], facecolor=axcolor)

sli_fm = Slider(ax_fm, 'fm', 5, 100, valinit=30, valstep=delta)
sli_Rm = Slider(ax_Rm, 'Rm', 1, 50, valinit=20, valstep=delta)
sli_e = Slider(ax_e, 'e', 0.1, 10, valinit=1.2, valstep=delta/10)
sli_N1 = Slider(ax_N1, 'N2', 3, 40, valinit=35, valstep=delta)
sli_N = Slider(ax_N, 'N1', 3, 40, valinit=25, valstep=delta)
sli_d = Slider(ax_d, 'd', 2, 20, valinit=5,valstep=delta)
sli_D1 = Slider(ax_D1, 'D2', 5, 200, valinit=90,valstep=delta)
sli_D = Slider(ax_D, 'D1', 5, 200, valinit=70,valstep=delta)


def update(val):
    sfm = sli_Rm.val
    sRm = sli_Rm.val
    se = sli_e.val
    sN = sli_N.val
    sN1 = sli_N1.val
    sd = sli_d.val
    sD = sli_D.val
    sD1 = sli_D1.val
    if sD>sD1:
        ax.set_xlim(-1.2*0.5*sD,1.2*0.5*sD)
        ax.set_ylim(-1.2*0.5*sD,1.2*0.5*sD)
    if sD1>sD:
        ax.set_xlim(-1.2*0.5*sD1,1.2*0.5*sD1)
        ax.set_ylim(-1.2*0.5*sD1,1.2*0.5*sD1)
    ax.set_title('Reduction ratio '+(str(round(-(sN1*(sN-1))/(sN1+sN),2)))+':1')

sli_fm.on_changed(update)
sli_Rm.on_changed(update)
sli_e.on_changed(update)
sli_N.on_changed(update)
sli_N1.on_changed(update)
sli_d.on_changed(update)
sli_D.on_changed(update)
sli_D1.on_changed(update)

resetax = plt.axes([0.85, 0.01, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    sli_fm.reset()    
    sli_Rm.reset()
    sli_e.reset()
    sli_N.reset()
    sli_N1.reset()
    sli_d.reset()
    sli_D.reset()
    sli_D1.reset()

button.on_clicked(reset)

def animate(frame):
    sfm = sli_fm.val
    sRm = sli_Rm.val
    se = sli_e.val
    sN = sli_N.val
    sN1 = sli_N1.val
    sd = sli_d.val
    sD = sli_D.val
    sD1 = sli_D1.val
    frame = frame+1
    #phi = 0
    phi = 2*np.pi*frame/sfm

    draw_pinA_init()
    pinA_update(se,sN,sN1,sd,sD,phi)

    draw_pinB_init()
    pinB_update(se,sN1,sd,sD1,phi)

    update_inner_pin(se,sN1,sRm, phi)

    drive_pin_update(sRm)

    update_hypocycloidA(se,sN,sN1,sD,sd, phi)
    update_hypocycloidC(se,sN,sN1,sD,sd, phi)

    update_hypocycloidB(se,sN1,sD1,sd, phi)    
    update_hypocycloidD(se,sN1,sD1,sd, phi)
    fig.canvas.draw_idle()

ani = animation.FuncAnimation(fig, animate,frames=sli_fm.val*(sli_N.val-1), interval=interval)
dpi=100
plt.show()
