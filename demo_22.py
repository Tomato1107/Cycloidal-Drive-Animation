import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button

interval = 50 # ms, time between animation frames

fig, ax = plt.subplots(figsize=(6,6))
plt.subplots_adjust(left=0.15, bottom=0.35)

ax.set_aspect('equal')
plt.xlim(-1.4*40,1.4*40)
plt.ylim(-1.4*40,1.4*40)
#plt.grid()
t = np.linspace(0, 2*np.pi, 10000)
delta = 1


## draw pin
num_pins = 61
pins = [ax.plot([], [], 'k-')[0] for n in range(num_pins)]
def draw_pin_init():
    for p in pins:
        p.set_data([0], [0])
def pin_update(e,n,d,D, phis):
    for i in range(int(n)):    
        xd = (d/2*np.cos(t)+ D/2*np.cos(2*i*np.pi/n)) + e*np.cos(phis)
        yd = (d/2*np.sin(t)+ D/2*np.sin(2*i*np.pi/n)) + e*np.sin(phis)
        x = xd*np.cos(-phis/(n+1)) - yd*np.sin(-phis/(n+1)) 
        y = xd*np.sin(-phis/(n+1)) + yd*np.cos(-phis/(n+1)) 
        pins[i].set_data(x,y)



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

def update_hypocycloidA(e,n,D,d, phis):

    RD=D/2
    rd=d/2
    rc = (n-1)*(RD/n)
    rm = (RD/n)

    xa = (rc+rm)*np.cos(t)-e*np.cos((rc+rm)/rm*t)
    ya = (rc+rm)*np.sin(t)-e*np.sin((rc+rm)/rm*t)

    dxa = (rc+rm)*(-np.sin(t)+(e/rm)*np.sin((rc+rm)/rm*t))
    dya = (rc+rm)*(np.cos(t)-(e/rm)*np.cos((rc+rm)/rm*t))

    x = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.cos(-phis/(n-1) -phis/(n+1) - np.pi/(n-1))-(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.sin(-phis/(n-1) -phis/(n+1) - np.pi/(n-1))  
    y = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.sin(-phis/(n-1) -phis/(n+1) - np.pi/(n-1))+(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.cos(-phis/(n-1) -phis/(n+1)- np.pi/(n-1)) 

    x1 = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.cos(-phis/(n-1) -phis/(n+1) )-(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.sin(-phis/(n-1) -phis/(n+1) )  
    y1 = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.sin(-phis/(n-1) -phis/(n+1) )+(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.cos(-phis/(n-1) -phis/(n+1)) 
    
    hypocycloidA.set_data(x,y)
    edotA.set_data(x1[0], y1[0])


##hypocycloidC:
hypocycloidC, = ax.plot([0],[0],'g-')

def update_hypocycloidC(e,n,D,d, phis):
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

    x = (xd )*np.cos(-phis/(n+1))-(yd )*np.sin(-phis/(n+1))
    y = (xd )*np.sin(-phis/(n+1))+(yd )*np.cos(-phis/(n+1)) 

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
ax_fm = plt.axes([0.25, 0.12, 0.5, 0.015], facecolor=axcolor)
ax_Rm = plt.axes([0.25, 0.10, 0.5, 0.015], facecolor=axcolor)
ax_e = plt.axes([0.25, 0.08, 0.5, 0.015], facecolor=axcolor)
ax_N = plt.axes([0.25, 0.06, 0.5, 0.015], facecolor=axcolor)
ax_d = plt.axes([0.25, 0.04, 0.5, 0.015], facecolor=axcolor)
ax_D = plt.axes([0.25, 0.02, 0.5, 0.015], facecolor=axcolor)

sli_fm = Slider(ax_fm, 'fm', 10, 100, valinit=30, valstep=delta)
sli_Rm = Slider(ax_Rm, 'Rm', 1, 50, valinit=20, valstep=delta)
sli_e = Slider(ax_e, 'e', 0.1, 10, valinit=2.0, valstep=delta/10)
sli_N = Slider(ax_N, 'N', 3, 40, valinit=17, valstep=delta)
sli_d = Slider(ax_d, 'd', 2, 20, valinit=10,valstep=delta)
sli_D = Slider(ax_D, 'D', 5, 100, valinit=80,valstep=delta)

def update(val):
    sfm = sli_Rm.val
    sRm = sli_Rm.val
    se = sli_e.val
    sN = sli_N.val
    sd = sli_d.val
    sD = sli_D.val
    ax.set_xlim(-1.4*0.5*sD,1.4*0.5*sD)
    ax.set_ylim(-1.4*0.5*sD,1.4*0.5*sD)

sli_fm.on_changed(update)
sli_Rm.on_changed(update)
sli_e.on_changed(update)
sli_N.on_changed(update)
sli_d.on_changed(update)
sli_D.on_changed(update)

resetax = plt.axes([0.85, 0.01, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    sli_fm.reset()    
    sli_Rm.reset()
    sli_e.reset()
    sli_N.reset()
    sli_d.reset()
    sli_D.reset()

button.on_clicked(reset)

def animate(frame):
    sfm = sli_fm.val
    sRm = sli_Rm.val
    se = sli_e.val
    sN = sli_N.val
    sd = sli_d.val
    sD = sli_D.val
    frame = frame+1
    #phi = 0
    phi = 2*np.pi*frame/sfm

    draw_pin_init()

    pin_update(se,sN,sd,sD,phi)
    update_inner_pin(se,sN,sRm, phi)

    drive_pin_update(sRm)

    update_hypocycloidA(se,sN,sD,sd, phi)
    update_hypocycloidC(se,sN,sD,sd, phi)

    update_hypocycloidB(se,sN,sD,sd, phi)    
    update_hypocycloidD(se,sN,sD,sd, phi)
    fig.canvas.draw_idle()

ani = animation.FuncAnimation(fig, animate,frames=sli_fm.val*(sli_N.val-1), interval=interval)
dpi=100
plt.show()
