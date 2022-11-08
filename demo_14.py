import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button

interval = 50 # ms, time between animation frames

fig, ax = plt.subplots(figsize=(6,6))
plt.subplots_adjust(left=0.15, bottom=0.35)

ax.set_aspect('equal')
plt.xlim(-1.2*40,1.2*40)
plt.ylim(-1.2*40,1.2*40)
#plt.grid()
t = np.linspace(0, 2*np.pi, 2000)
delta = 1


## draw pin
num_pins = 61
pins = [ax.plot([], [], 'g-')[0] for n in range(num_pins)]
ddot, = ax.plot([20],[0], 'go', ms=5)

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
            
        xd1 = (d/2*np.cos(phis)+ D/2) + e*np.cos(phis)
        yd1 = (d/2*np.sin(phis) ) + e*np.sin(phis)
        x1 = xd1*np.cos(-phis/(n+1)) - yd1*np.sin(-phis/(n+1)) 
        y1 = xd1*np.sin(-phis/(n+1)) + yd1*np.cos(-phis/(n+1)) 
        ddot.set_data(x1, y1)


## draw drive_pin
num_drive_pins = 61
drive_pins = [ax.plot([], [], 'k-')[0] for n in range(num_drive_pins)]

def drive_pin_init():
    for p in drive_pins:
        p.set_data([0], [0])

def drive_pin_update(r,n,D,phis):
    for i in range(int(n)):
        xd = r*np.sin(t) + D/2*np.cos(2*i*np.pi/n)
        yd = r*np.cos(t) + D/2*np.sin(2*i*np.pi/n)

        x = xd*np.cos(-phis/(n+1)) - yd*np.sin(-phis/(n+1)) 
        y = xd*np.sin(-phis/(n+1)) + yd*np.cos(-phis/(n+1)) 
        drive_pins[i].set_data(x,y)


## draw circle
m1, = ax.plot([0], [0],'r-')

def draw_circle(r):
    x = r*np.sin(t) 
    y = r*np.cos(t)
    m1.set_data(x,y)


##ehypocycloidA:
ehypocycloid, = ax.plot([0],[0],'r-')
edot, = ax.plot([0],[0], 'ro', ms=5)

def update_ehypocycloidA(e,n,D,d, phis):
    RD=D/2
    rd=d/2
    rc = (n-1)*(RD/n)
    rm = (RD/n)
    xa = (rc+rm)*np.cos(t)-e*np.cos((rc+rm)/rm*t)
    ya = (rc+rm)*np.sin(t)-e*np.sin((rc+rm)/rm*t)

    dxa = (rc+rm)*(-np.sin(t)+(e/rm)*np.sin((rc+rm)/rm*t))
    dya = (rc+rm)*(np.cos(t)-(e/rm)*np.cos((rc+rm)/rm*t))

    x = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.cos(-phis/(n-1) -phis/(n+1) + np.pi/(n-1))-(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.sin(-phis/(n-1) -phis/(n+1) + np.pi/(n-1))  
    y = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.sin(-phis/(n-1) -phis/(n+1) + np.pi/(n-1))+(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.cos(-phis/(n-1) -phis/(n+1)+ np.pi/(n-1)) 
    
    ehypocycloid.set_data(x,y)
    edot.set_data(x[0], y[0])


##ehypocycloidB:
ehypocycloidB, = ax.plot([0],[0],'b-')
edotB, = ax.plot([0],[0], 'bo', ms=5)

def update_ehypocycloidB(e,n,D,d, phis):
    RD=D/2
    rd=d/2
    rc = (n+1)*(RD/n)
    rm = (RD/n)
    xa = (rc-rm)*np.cos(t)+e*np.cos((rc-rm)/rm*t)
    ya = (rc-rm)*np.sin(t)-e*np.sin((rc-rm)/rm*t)

    dxa = (rc-rm)*(-np.sin(t)-(e/rm)*np.sin((rc-rm)/rm*t))
    dya = (rc-rm)*(np.cos(t)-(e/rm)*np.cos((rc-rm)/rm*t))

    x = (xa - rd/np.sqrt(dxa**2 + dya**2)*(-dya))
    y = (ya - rd/np.sqrt(dxa**2 + dya**2)*dxa)

    ehypocycloidB.set_data(x,y)
    edotB.set_data(x[0], y[0])


axcolor = 'lightgoldenrodyellow'

ax_fm = plt.axes([0.25, 0.21, 0.5, 0.02], facecolor=axcolor)
ax_Rd = plt.axes([0.25, 0.18, 0.5, 0.02], facecolor=axcolor)
ax_rd = plt.axes([0.25, 0.15, 0.5, 0.02], facecolor=axcolor)
ax_e = plt.axes([0.25, 0.12, 0.5, 0.02], facecolor=axcolor)
ax_N = plt.axes([0.25, 0.09, 0.5, 0.02], facecolor=axcolor)
ax_d = plt.axes([0.25, 0.06, 0.5, 0.02], facecolor=axcolor)
ax_D = plt.axes([0.25, 0.03, 0.5, 0.02], facecolor=axcolor)

sli_fm = Slider(ax_fm, 'fm', 10, 100, valinit=50, valstep=delta)
sli_Rd = Slider(ax_Rd, 'Rd', 1, 40, valinit=20, valstep=delta)
sli_rd = Slider(ax_rd, 'rd', 0.1, 10, valinit=1.5, valstep=delta/10)
sli_e = Slider(ax_e, 'e', 0.1, 10, valinit=2, valstep=delta/10)
sli_N = Slider(ax_N, 'N', 2, 40, valinit=10, valstep=delta)
sli_d = Slider(ax_d, 'd', 2, 20, valinit=10,valstep=delta)
sli_D = Slider(ax_D, 'D', 5, 100, valinit=80,valstep=delta)

def update(val):
    sfm = sli_Rd.val
    sRd = sli_Rd.val
    srd = sli_rd.val    
    se = sli_e.val
    sN = sli_N.val
    sd = sli_d.val
    sD = sli_D.val
    ax.set_xlim(-1.5*0.5*sD,1.5*0.5*sD)
    ax.set_ylim(-1.5*0.5*sD,1.5*0.5*sD)

sli_fm.on_changed(update)
sli_Rd.on_changed(update)
sli_rd.on_changed(update)
sli_e.on_changed(update)
sli_N.on_changed(update)
sli_d.on_changed(update)
sli_D.on_changed(update)

resetax = plt.axes([0.8, 0.0, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    sli_fm.reset()    
    sli_rd.reset()
    sli_Rd.reset()    
    sli_e.reset()
    sli_N.reset()
    sli_d.reset()
    sli_D.reset()

button.on_clicked(reset)

def animate(frame):
    sfm = sli_fm.val
    sRd = sli_Rd.val
    srd = sli_rd.val    
    se = sli_e.val
    sN = sli_N.val
    sd = sli_d.val
    sD = sli_D.val
    frame = frame+1
    phi = 2*np.pi*frame/sfm


    draw_pin_init()
    draw_circle(sRd)

    pin_update(se,sN,sd,sD, phi)

    drive_pin_init()
    drive_pin_update(srd,sN,sD,phi)

    update_ehypocycloidA(se,sN,sD,sd, phi)
    update_ehypocycloidB(se,sN,sD,sd, phi)

    fig.canvas.draw_idle()



ani = animation.FuncAnimation(fig, animate,frames=sli_fm.val*(sli_N.val-1), interval=interval)
dpi=100
plt.show()
