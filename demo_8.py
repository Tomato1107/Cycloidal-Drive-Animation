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

def pin_update(n,d,D):
    for i in range(int(n)):    
        x = (d/2*np.sin(t)+ D/2*np.cos(2*i*np.pi/n))
        y = (d/2*np.cos(t) + D/2*np.sin(2*i*np.pi/n))
        pins[i].set_data(x,y)


## draw drive_pin
d0, = ax.plot([0],[0],'k-', lw=2)

def drive_pin_update(r):
    x = r*np.sin(t)
    y = r*np.cos(t)
    d0.set_data(x,y)


##inner pin:
inner_pin, = ax.plot([0],[0],'r-')
dot, = ax.plot([0],[0], 'ro', ms=5)

def update_inner_pin(e,Rm, phi):
    x = (Rm+e)*np.cos(t)+e*np.cos(phi)
    y = (Rm+e)*np.sin(t)+e*np.sin(phi)
    inner_pin.set_data(x,y)
    
    x1 = (Rm+e)*np.cos(phi)+e*np.cos(phi)
    y1 = (Rm+e)*np.sin(phi)+e*np.sin(phi)
    dot.set_data(x1, y1)

##inner pinD:
inner_pinD, = ax.plot([0],[0],'b-')
dotD, = ax.plot([0],[0], 'bo', ms=5)

def update_inner_pinD(e,Rm, phi):
    x = (Rm+e)*np.cos(t)-e*np.cos(phi)
    y = (Rm+e)*np.sin(t)-e*np.sin(phi)
    inner_pinD.set_data(x,y)
    
    x1 = (Rm+e)*np.cos(phi+np.pi)-e*np.cos(phi)
    y1 = (Rm+e)*np.sin(phi+np.pi)-e*np.sin(phi)
    dotD.set_data(x1, y1)


##hypocycloidA:
hypocycloidA, = ax.plot([0],[0],'r-')
edotA, = ax.plot([0],[0], 'ro', ms=5)

def update_hypocycloidA(lamuda,e,n,D,d, phis):
    #lamuda = 0.9
    RD=D/2
    rd=d/2
    rc = (n-1)*(RD/n)
    rm = (RD/n)
    xa = (rc+rm)*np.cos(t)-e*lamuda*np.cos((rc+rm)/rm*t)-rd*(np.cos(t) - lamuda*np.cos((rc+rm)/rm*t))/np.sqrt(1 + lamuda**2 - 2*lamuda*np.cos(rc/rm*t)) 
    ya = (rc+rm)*np.sin(t)-e*lamuda*np.sin((rc+rm)/rm*t)-rd*(np.sin(t) - lamuda*np.sin((rc+rm)/rm*t))/np.sqrt(1 + lamuda**2 - 2*lamuda*np.cos(rc/rm*t)) 

    x = (xa )*np.cos(-phis/(n-1))-(ya )*np.sin(-phis/(n-1))  + e*np.cos(phis)
    y = (xa )*np.sin(-phis/(n-1))+(ya )*np.cos(-phis/(n-1))  + e*np.sin(phis)
    hypocycloidA.set_data(x,y)
    edotA.set_data(x[0], y[0])


##hypocycloidC:
hypocycloidC, = ax.plot([0],[0],'b-')

def update_hypocycloidC(lamuda,e,n,D,d, phis):
    #lamuda = 0.9
    RD=D/2
    rd=d/2
    rc = (n)*(RD/n)
    rm = (RD/n)
    xa = (rc+rm)*np.cos(t)-e*lamuda*np.cos((rc+rm)/rm*t)-rd*(np.cos(t) - lamuda*np.cos((rc+rm)/rm*t))/np.sqrt(1 + lamuda**2 - 2*lamuda*np.cos(rc/rm*t)) 
    ya = (rc+rm)*np.sin(t)-e*lamuda*np.sin((rc+rm)/rm*t)-rd*(np.sin(t) - lamuda*np.sin((rc+rm)/rm*t))/np.sqrt(1 + lamuda**2 - 2*lamuda*np.cos(rc/rm*t)) 

    hypocycloidC.set_data(xa,ya)


##hypocycloidB:
hypocycloidB, = ax.plot([0],[0],'b-')
edotB, = ax.plot([0],[0], 'bo', ms=5)

def update_hypocycloidB(lamuda,e,n,D,d, phis):
    #lamuda = 0.9
    RD=D/2
    rd=d/2
    rc = (n+1)*(RD/n)
    rm = (RD/n)
    xa = (rc-rm)*np.cos(t)+e*lamuda*np.cos((rc-rm)/rm*t)+rd*(np.cos(t) - lamuda*np.cos((rc-rm)/rm*t))/np.sqrt(1 + lamuda**2 - 2*lamuda*np.cos(rc/rm*t)) 
    ya = (rc-rm)*np.sin(t)-e*lamuda*np.sin((rc-rm)/rm*t)+rd*(np.sin(t) + lamuda*np.sin((rc-rm)/rm*t))/np.sqrt(1 + lamuda**2 - 2*lamuda*np.cos(rc/rm*t)) 

    x = (xa )*np.cos(phis/(n+1))-(ya )*np.sin(phis/(n+1))  - e*np.cos(phis)
    y = (xa )*np.sin(phis/(n+1))+(ya )*np.cos(phis/(n+1))  - e*np.sin(phis)
    hypocycloidB.set_data(x,y)
    edotB.set_data(x[0], y[0])


##hypocycloidD:
hypocycloidD, = ax.plot([0],[0],'r-')

def update_hypocycloidD(lamuda,e,n,D,d, phis):
    #lamuda = 0.9
    RD=D/2
    rd=d/2
    rc = (n)*(RD/n)
    rm = (RD/n)
    xa = (rc-rm)*np.cos(t)+e*lamuda*np.cos((rc-rm)/rm*t)+rd*(np.cos(t) - lamuda*np.cos((rc-rm)/rm*t))/np.sqrt(1 + lamuda**2 - 2*lamuda*np.cos(rc/rm*t)) 
    ya = (rc-rm)*np.sin(t)-e*lamuda*np.sin((rc-rm)/rm*t)+rd*(np.sin(t) + lamuda*np.sin((rc-rm)/rm*t))/np.sqrt(1 + lamuda**2 - 2*lamuda*np.cos(rc/rm*t)) 

    hypocycloidD.set_data(xa,ya)


axcolor = 'lightgoldenrodyellow'
ax_la = plt.axes([0.25, 0.14, 0.5, 0.015], facecolor=axcolor)
ax_fm = plt.axes([0.25, 0.12, 0.5, 0.015], facecolor=axcolor)
ax_Rm = plt.axes([0.25, 0.10, 0.5, 0.015], facecolor=axcolor)
ax_e = plt.axes([0.25, 0.08, 0.5, 0.015], facecolor=axcolor)
ax_N = plt.axes([0.25, 0.06, 0.5, 0.015], facecolor=axcolor)
ax_d = plt.axes([0.25, 0.04, 0.5, 0.015], facecolor=axcolor)
ax_D = plt.axes([0.25, 0.02, 0.5, 0.015], facecolor=axcolor)

sli_la = Slider(ax_la, 'la', 0.8, 0.98, valinit=0.95, valstep=delta/100)
sli_fm = Slider(ax_fm, 'fm', 10, 100, valinit=50, valstep=delta)
sli_Rm = Slider(ax_Rm, 'Rm', 1, 10, valinit=5, valstep=delta)
sli_e = Slider(ax_e, 'e', 0.1, 10, valinit=2.5, valstep=delta/10)
sli_N = Slider(ax_N, 'N', 3, 40, valinit=16, valstep=delta)
sli_d = Slider(ax_d, 'd', 2, 20, valinit=10,valstep=delta)
sli_D = Slider(ax_D, 'D', 5, 100, valinit=80,valstep=delta)

def update(val):
    sla = sli_la.val
    sfm = sli_Rm.val
    sRm = sli_Rm.val
    se = sli_e.val
    sN = sli_N.val
    sd = sli_d.val
    sD = sli_D.val
    ax.set_xlim(-1.4*0.5*sD,1.4*0.5*sD)
    ax.set_ylim(-1.4*0.5*sD,1.4*0.5*sD)


sli_la.on_changed(update)
sli_fm.on_changed(update)
sli_Rm.on_changed(update)
sli_e.on_changed(update)
sli_N.on_changed(update)
sli_d.on_changed(update)
sli_D.on_changed(update)

resetax = plt.axes([0.85, 0.01, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    sli_la.reset() 
    sli_fm.reset()    
    sli_Rm.reset()
    sli_e.reset()
    sli_N.reset()
    sli_d.reset()
    sli_D.reset()

button.on_clicked(reset)

def animate(frame):
    sla = sli_la.val
    sfm = sli_fm.val
    sRm = sli_Rm.val
    se = sli_e.val
    sN = sli_N.val
    sd = sli_d.val
    sD = sli_D.val
    frame = frame+1
    phi = 2*np.pi*frame/sfm

    draw_pin_init()

    pin_update(sN,sd,sD)
    update_inner_pin(se,sRm, phi)
    update_inner_pinD(se,sRm, phi)

    drive_pin_update(sRm)

    update_hypocycloidA(sla,se,sN,sD,sd, phi)
    update_hypocycloidC(sla,se,sN,sD,sd, phi)

    update_hypocycloidB(sla,se,sN,sD,sd, phi)    
    update_hypocycloidD(sla,se,sN,sD,sd, phi)
    fig.canvas.draw_idle()

ani = animation.FuncAnimation(fig, animate,frames=sli_fm.val*(sli_N.val-1), interval=interval)
dpi=100
plt.show()
