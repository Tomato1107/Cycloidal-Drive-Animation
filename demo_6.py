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
t = np.linspace(0, 2*np.pi, 400)
delta = 1


## draw pin
num_pins = 61
pins = [ax.plot([], [], 'g-')[0] for n in range(num_pins)]

def draw_pin_init():
    for p in pins:
        p.set_data([0], [0])

def pin_update3(n,e,d,D,phi):
    for i in range(int(n)):    
        x = (d/2*np.sin(t)+ D/2*np.cos(2*i*np.pi/n))*np.cos(-phi/(n)) - (d/2*np.cos(t) + D/2*np.sin(2*i*np.pi/n))*np.sin(-phi/(n)) + e*np.cos(phi) 
        y = (d/2*np.sin(t)+ D/2*np.cos(2*i*np.pi/n))*np.sin(-phi/(n)) + (d/2*np.cos(t) + D/2*np.sin(2*i*np.pi/n))*np.cos(-phi/(n)) + e*np.sin(phi) 
        pins[i].set_data(x,y)


## draw drive_pin
m1, = ax.plot([0], [0],'r-')
inner_pin, = ax.plot([0], [0],'k-')
dot, = ax.plot([0],[0], 'ko', ms=5)

def draw_circle(e,r,phis):
    x0 = r*np.sin(t) + 2*e*np.cos(phis)
    y0 = r*np.cos(t) + 2*e*np.sin(phis)
    m1.set_data(x0,y0)

    x = (r-2*e)*np.cos(t)
    y = (r-2*e)*np.sin(t)
    inner_pin.set_data(x,y)

    x1 = (r-2*e)*np.cos(phis)
    y1 = (r-2*e)*np.sin(phis)
    dot.set_data(x1, y1)


##ehypocycloidA:
ehypocycloidA, = ax.plot([0],[0],'r-')
edotA, = ax.plot([0],[0], 'ro', ms=5)

def update_ehypocycloidA(e,n,D,d, phis):
    RD=D/2
    rd=d/2
    rc = (n-1)*(RD/n)
    rm = (RD/n)
    xa = (rc+rm)*np.cos(t)-e*np.cos((rc+rm)/rm*t)
    ya = (rc+rm)*np.sin(t)-e*np.sin((rc+rm)/rm*t)

    dxa = (rc+rm)*(-np.sin(t)+(e/rm)*np.sin((rc+rm)/rm*t))
    dya = (rc+rm)*(np.cos(t)-(e/rm)*np.cos((rc+rm)/rm*t))

    x = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.cos(-2*phis/(n-1))-(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.sin(-2*phis/(n-1))  + 2*e*np.cos(phis) 
    y = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.sin(-2*phis/(n-1))+(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.cos(-2*phis/(n-1))  + 2*e*np.sin(phis)
    ehypocycloidA.set_data(x,y)    

    edotA.set_data(x[0], y[0])


##ehypocycloidE:
ehypocycloidE, = ax.plot([0],[0],'r-')

def update_ehypocycloidE(e,n,D,d, phis):
    RD=D/2
    rd=d/2
    rc = (n-1)*(RD/n)
    rm = (RD/n)
    xa = (rc+rm)*np.cos(t)-e*np.cos((rc+rm)/rm*t)
    ya = (rc+rm)*np.sin(t)-e*np.sin((rc+rm)/rm*t)

    dxa = (rc+rm)*(-np.sin(t)+(e/rm)*np.sin((rc+rm)/rm*t))
    dya = (rc+rm)*(np.cos(t)-(e/rm)*np.cos((rc+rm)/rm*t))

    x = (xa - rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.cos(-2*phis/(n-1))-(ya - rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.sin(-2*phis/(n-1))  + 2*e*np.cos(phis) 
    y = (xa - rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.sin(-2*phis/(n-1))+(ya - rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.cos(-2*phis/(n-1))  + 2*e*np.sin(phis)
    ehypocycloidE.set_data(x,y)    


##ehypocycloidD:
ehypocycloidD, = ax.plot([0],[0],'b-')
edotD, = ax.plot([0],[0], 'bo', ms=5)

def update_ehypocycloidD(e,n,D,d, phis):
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

    ehypocycloidD.set_data(x,y)
    edotD.set_data(x[0], y[0])


##ehypocycloidF:
ehypocycloidF, = ax.plot([0],[0],'b-')

def update_ehypocycloidF(e,n,D,d, phis):
    RD=D/2
    rd=d/2
    rc = (n+1)*(RD/n)
    rm = (RD/n)
    xa = (rc-rm)*np.cos(t)+e*np.cos((rc-rm)/rm*t)
    ya = (rc-rm)*np.sin(t)-e*np.sin((rc-rm)/rm*t)

    dxa = (rc-rm)*(-np.sin(t)-(e/rm)*np.sin((rc-rm)/rm*t))
    dya = (rc-rm)*(np.cos(t)-(e/rm)*np.cos((rc-rm)/rm*t))

    x = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))
    y = (ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)

    ehypocycloidF.set_data(x,y)

axcolor = 'lightgoldenrodyellow'

ax_fm = plt.axes([0.25, 0.18, 0.5, 0.02], facecolor=axcolor)
ax_Rd = plt.axes([0.25, 0.15, 0.5, 0.02], facecolor=axcolor)
ax_e = plt.axes([0.25, 0.12, 0.5, 0.02], facecolor=axcolor)
ax_N = plt.axes([0.25, 0.09, 0.5, 0.02], facecolor=axcolor)
ax_d = plt.axes([0.25, 0.06, 0.5, 0.02], facecolor=axcolor)
ax_D = plt.axes([0.25, 0.03, 0.5, 0.02], facecolor=axcolor)

sli_fm = Slider(ax_fm, 'fm', 10, 100, valinit=50, valstep=delta)
sli_Rd = Slider(ax_Rd, 'Rd', 1, 40, valinit=10, valstep=delta)
sli_e = Slider(ax_e, 'e', 0.1, 10, valinit=1.4, valstep=delta/10)
sli_N = Slider(ax_N, 'N', 3, 40, valinit=10, valstep=delta)
sli_d = Slider(ax_d, 'd', 2, 20, valinit=10,valstep=delta)
sli_D = Slider(ax_D, 'D', 5, 100, valinit=80,valstep=delta)


def update(val):
    sfm = sli_fm.val
    sRd = sli_Rd.val
    se = sli_e.val
    sN = sli_N.val
    sd = sli_d.val
    sD = sli_D.val
    ax.set_xlim(-1.4*0.5*sD,1.4*0.5*sD)
    ax.set_ylim(-1.4*0.5*sD,1.4*0.5*sD)

sli_fm.on_changed(update)
sli_Rd.on_changed(update)
sli_e.on_changed(update)
sli_N.on_changed(update)
sli_d.on_changed(update)
sli_D.on_changed(update)

resetax = plt.axes([0.85, 0.01, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    sli_fm.reset()    
    sli_Rd.reset()    
    sli_e.reset()
    sli_N.reset()
    sli_d.reset()
    sli_D.reset()

button.on_clicked(reset)

def animate(frame):
    sfm = sli_fm.val
    sRd = sli_Rd.val
    se = sli_e.val
    sN = sli_N.val
    sd = sli_d.val
    sD = sli_D.val
    frame = frame+1
    phi = 2*np.pi*frame/sfm

    draw_pin_init()
    pin_update3(sN,se,sd,sD,phi)

    draw_circle(se,sRd,phi)
  
    update_ehypocycloidA(se,sN,sD,sd, phi)
    update_ehypocycloidE(se,sN,sD,sd, phi)
    update_ehypocycloidD(se,sN,sD,sd, phi)
    update_ehypocycloidF(se,sN,sD,sd, phi)
    fig.canvas.draw_idle()

ani = animation.FuncAnimation(fig, animate,frames=sli_fm.val*(sli_N.val-1), interval=interval)
dpi=100
plt.show()
