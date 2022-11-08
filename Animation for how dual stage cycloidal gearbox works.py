import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button

fig, ax = plt.subplots(figsize=(6,6))
plt.subplots_adjust(left=0.15, bottom=0.35)

ax.set_aspect('equal')
plt.xlim(-1.2*40,1.2*40)
plt.ylim(-1.2*40,1.2*40)
#plt.grid()
t = np.linspace(0, 2*np.pi, 4000)
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


## draw 2nd output pin
num_output_pins = 61
output_pins = [ax.plot([], [], 'g-')[0] for n in range(num_output_pins)]

def draw_output_pin_init():
    for p in output_pins:
        p.set_data([0], [0])

def output_pin_update(n1,n2,d,D,phi):
    for i in range(int(n1)):   
        '''
           Z1 /_/_/_/    Z4 ________
                ___       __|__    |
           Z2    |         ___     |
              ___|__________|  Z3  | 
              |  |         _|_     |
              | _|_                |
         in __|                    |___ out
 
         j= 1/(1-((Z1/Z2)*(Z3/Z4))

        ''' 

        if n1!=n2:
            j=1/(1-n2/(n2-1)*(n1-1)/n1)
            x = (d/2*np.sin(t)+ D/2*np.cos(2*i*np.pi/n1))*np.cos(phi/j+np.pi/n1) - (d/2*np.cos(t) + D/2*np.sin(2*i*np.pi/n1))*np.sin(phi/j+np.pi/n1)
            y = (d/2*np.sin(t)+ D/2*np.cos(2*i*np.pi/n1))*np.sin(phi/j+np.pi/n1) + (d/2*np.cos(t) + D/2*np.sin(2*i*np.pi/n1))*np.cos(phi/j+np.pi/n1)
        if n1==n2:          
            x = (d/2*np.sin(t)+ D/2*np.cos(2*i*np.pi/n1))*np.cos(np.pi/n1) - (d/2*np.cos(t) + D/2*np.sin(2*i*np.pi/n1))*np.sin(np.pi/n1)
            y = (d/2*np.sin(t)+ D/2*np.cos(2*i*np.pi/n1))*np.sin(np.pi/n1) + (d/2*np.cos(t) + D/2*np.sin(2*i*np.pi/n1))*np.cos(np.pi/n1)       
        output_pins[i].set_data(x, y)
 

## draw drive_pin
d0, = ax.plot([0],[0],'k-', lw=2)

def drive_pin_update(r):
    x = r*np.sin(t)
    y = r*np.cos(t)
    d0.set_data(x,y)


##inner pinB:
inner_pinB, = ax.plot([0],[0],'b-')
dotB, = ax.plot([0],[0], 'bo', ms=5)

def update_inner_pinB(e,Rm, phi):
    x = (Rm+e)*np.cos(t)-e*np.cos(phi)
    y = (Rm+e)*np.sin(t)-e*np.sin(phi)
    inner_pinB.set_data(x,y)
    
    x1 = (Rm+e)*np.cos(phi+np.pi)-e*np.cos(phi)
    y1 = (Rm+e)*np.sin(phi+np.pi)-e*np.sin(phi)
    dotB.set_data(x1, y1)


##ehypocycloidA:
ehypocycloidA, = ax.plot([0],[0],'r-')
edotA, = ax.plot([0],[0], 'ro', ms=5)

def update_ehypocycloidA(e,n1,n2,D,d, phis):
    RD=D/2
    rd=d/2
    rc = (n1-1)*(RD/n1)
    rm = (RD/n1)
    xa = (rc+rm)*np.cos(t)-e*np.cos((rc+rm)/rm*t)
    ya = (rc+rm)*np.sin(t)-e*np.sin((rc+rm)/rm*t)

    dxa = (rc+rm)*(-np.sin(t)+(e/rm)*np.sin((rc+rm)/rm*t))
    dya = (rc+rm)*(np.cos(t)-(e/rm)*np.cos((rc+rm)/rm*t))

    x = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.cos(-phis/(n2-1)) - (ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.sin(-phis/(n2-1)) - e*np.cos(phis)
    y = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.sin(-phis/(n2-1)) + (ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.cos(-phis/(n2-1))  - e*np.sin(phis)
    ehypocycloidA.set_data(x,y)

    edotA.set_data(x[0], y[0])


##ehypocycloidB:
ehypocycloidB, = ax.plot([0],[0],'b-')
edotB, = ax.plot([0],[0], 'bo', ms=5)

def update_ehypocycloidB(e,n,D,d, phis):
    RD=D/2
    rd=d/2
    rc = (n-1)*(RD/n)
    rm = (RD/n)
    xa = (rc+rm)*np.cos(t)+e*np.cos((rc+rm)/rm*t)
    ya = (rc+rm)*np.sin(t)+e*np.sin((rc+rm)/rm*t)

    dxa = (rc+rm)*(-np.sin(t)-(e/rm)*np.sin((rc+rm)/rm*t))
    dya = (rc+rm)*(np.cos(t)+(e/rm)*np.cos((rc+rm)/rm*t))

    x = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.cos(-phis/(n-1))-(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.sin(-phis/(n-1))  - e*np.cos(phis)
    y = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.sin(-phis/(n-1))+(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.cos(-phis/(n-1))  - e*np.sin(phis)
    ehypocycloidB.set_data(x,y)
    edotB.set_data(x[0], y[0])


axcolor = 'lightgoldenrodyellow'

ax_fm = plt.axes([0.25, 0.16, 0.5, 0.015], facecolor=axcolor)
ax_Rm = plt.axes([0.25, 0.14, 0.5, 0.015], facecolor=axcolor)
ax_e = plt.axes([0.25, 0.12, 0.5, 0.015], facecolor=axcolor)
ax_N1 = plt.axes([0.25, 0.10, 0.5, 0.015], facecolor=axcolor)
ax_N = plt.axes([0.25, 0.08, 0.5, 0.015], facecolor=axcolor)
ax_d = plt.axes([0.25, 0.06, 0.5, 0.015], facecolor=axcolor)
ax_D1 = plt.axes([0.25, 0.04, 0.5, 0.015], facecolor=axcolor)
ax_D = plt.axes([0.25, 0.02, 0.5, 0.015], facecolor=axcolor)

sli_fm = Slider(ax_fm, 'fm', 5, 100, valinit=10, valstep=delta)
sli_Rm = Slider(ax_Rm, 'Rm', 1, 10, valinit=5, valstep=delta)
sli_e = Slider(ax_e, 'e', 0.1, 10, valinit=1.5, valstep=delta/10)
sli_N1 = Slider(ax_N1, 'N2', 3, 40, valinit=16, valstep=delta)
sli_N = Slider(ax_N, 'N1', 3, 40, valinit=15, valstep=delta)
sli_d = Slider(ax_d, 'd', 2, 20, valinit=5,valstep=delta)
sli_D1 = Slider(ax_D1, 'D2', 5, 100, valinit=80,valstep=delta)
sli_D = Slider(ax_D, 'D1', 5, 100, valinit=60,valstep=delta)

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


sli_fm.on_changed(update)
sli_Rm.on_changed(update)
sli_e.on_changed(update)
sli_N.on_changed(update)
sli_N1.on_changed(update)
sli_d.on_changed(update)
sli_D.on_changed(update)
sli_D1.on_changed(update)

resetax = plt.axes([0.8, 0.0, 0.1, 0.04])
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
    phi = 2*np.pi*frame/sfm


    draw_pin_init()
    draw_output_pin_init()

    pin_update(sN,sd,sD)
    output_pin_update(sN1,sN,sd,sD1,phi)

    update_inner_pinB(se,sRm, phi)

    drive_pin_update(sRm)

    update_ehypocycloidA(se,sN1,sN,sD1,sd, phi)
    update_ehypocycloidB(se,sN,sD,sd, phi)

    fig.canvas.draw_idle()



ani = animation.FuncAnimation(fig, animate,frames=sli_fm.val*(sli_N.val-1), interval=50)
dpi=100
plt.show()
