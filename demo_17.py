import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button

interval = 50 # ms, time between animation frames

fig, ax = plt.subplots(figsize=(6,6))
plt.subplots_adjust(left=0.15, bottom=0.35)

ax.set_aspect('equal')
plt.xlim(-1.4*50,1.4*50)
plt.ylim(-1.4*50,1.4*50)
#plt.grid()
t = np.linspace(0, 2*np.pi, 2000)

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

##inner pin:
inner_pin, = ax.plot([0],[0],'r-')
d0, = ax.plot([0],[0],'k-')
dot, = ax.plot([0],[0], 'ko', ms=5)

def update_inner_pin(e,Rm, phi):
    x = (Rm+e)*np.cos(t)+e*np.cos(phi)
    y = (Rm+e)*np.sin(t)+e*np.sin(phi)
    inner_pin.set_data(x,y)


    x1 = (Rm)*np.cos(t)*np.cos(phi) - (Rm)*np.sin(t)*np.sin(phi)
    y1 = (Rm)*np.cos(t)*np.sin(phi) + (Rm)*np.sin(t)*np.cos(phi)
    #self.line.set_data([0,x1],[0,y1])
    d0.set_data(x1, y1)
    dot.set_data(x1[0], y1[0])

## draw inner_pin
num_inner_pins = 10
inner_pins = [ax.plot([], [], 'g-')[0] for n in range(num_inner_pins)]

def draw_inner_pin_init():
    for p in inner_pins:
        p.set_data([0], [0])

def inner_pin_update(n,N,rd,Rd,phi):
    num = (N-2)/2
    for i in range(int(n)):    
        x = (rd*np.sin(t)+ Rd*np.cos(2*i*np.pi/n))*np.cos(-phi/(num)) - (rd*np.cos(t) + Rd*np.sin(2*i*np.pi/n))*np.sin(-phi/(num))
        y = (rd*np.sin(t)+ Rd*np.cos(2*i*np.pi/n))*np.sin(-phi/(num)) + (rd*np.cos(t) + Rd*np.sin(2*i*np.pi/n))*np.cos(-phi/(num))
        inner_pins[i].set_data(x,y)

#inner circle:
num_inner_circles = 10
inner_circles = [ax.plot([], [], 'r-')[0] for n in range(num_inner_circles)]

def draw_inner_circle_init():
    for circle in inner_circles:
        circle.set_data([0], [0])

def update_inner_circle(e,n,N,rd,Rd, phi):
    num = (N-2)/2
    for i in range(int(n)):
        x = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.cos(-phi/(num)) - ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.sin(-phi/(num)) + e*np.cos(phi)
        y = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.sin(-phi/(num)) + ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.cos(-phi/(num)) + e*np.sin(phi)
        inner_circles[i].set_data(x,y)

##ehypocycloidA:
num_ehypocycloidA = 50
ehypocycloidA = [ax.plot([0],[0],'r-')[0] for n in range(num_ehypocycloidA)]

def ehypocycloidA_init():
    for eh in ehypocycloidA:
        eh.set_data([0], [0])

edotA, = ax.plot([0],[0], 'ro', ms=5)
def update_ehypocycloidA(e,n,D,d, phis):

    RD=D/2
    rd=d/2
    num = (n-2)/2
    t1 = np.linspace(-np.pi/(2*num), np.pi/(2*num), 2000)
    rc = (num)*(RD/(num+1))
    rm = (RD/(num+1))
    for i in range(int(2*num)):

        xa1 = (rc+rm)*np.cos(t1)-e*np.cos((rc+rm)/rm*t1)
        ya1 = (rc+rm)*np.sin(t1)-e*np.sin((rc+rm)/rm*t1)

        dxa1 = (rc+rm)*(-np.sin(t1)+(e/rm)*np.sin((rc+rm)/rm*t1))
        dya1 = (rc+rm)*(np.cos(t1)-(e/rm)*np.cos((rc+rm)/rm*t1))
        
        xd1 = (xa1 + rd/np.sqrt(dxa1**2 + dya1**2)*(-dya1))
        yd1 = (ya1 + rd/np.sqrt(dxa1**2 + dya1**2)*dxa1)
 
        x = xd1*np.cos((i)*np.pi/(num) - phis/(num))-yd1*np.sin((i)*np.pi/(num) - phis/(num)) + e*np.cos(phis)
        y = xd1*np.sin((i)*np.pi/(num) - phis/(num))+yd1*np.cos((i)*np.pi/(num) - phis/(num)) + e*np.sin(phis)
        if i == 0:
            edotA.set_data(x[0], y[0])
        ehypocycloidA[i].set_data(x,y)

axcolor = 'lightgoldenrodyellow'

ax_fm = plt.axes([0.25, 0.27, 0.5, 0.02], facecolor=axcolor)
ax_Rm = plt.axes([0.25, 0.24, 0.5, 0.02], facecolor=axcolor)
ax_n = plt.axes([0.25, 0.21, 0.5, 0.02], facecolor=axcolor)
ax_Rd = plt.axes([0.25, 0.18, 0.5, 0.02], facecolor=axcolor)
ax_rd = plt.axes([0.25, 0.15, 0.5, 0.02], facecolor=axcolor)
ax_e = plt.axes([0.25, 0.12, 0.5, 0.02], facecolor=axcolor)
ax_N = plt.axes([0.25, 0.09, 0.5, 0.02], facecolor=axcolor)
ax_d = plt.axes([0.25, 0.06, 0.5, 0.02], facecolor=axcolor)
ax_D = plt.axes([0.25, 0.03, 0.5, 0.02], facecolor=axcolor)

sli_fm = Slider(ax_fm, 'fm', 10, 80, valinit=20, valstep=delta)
sli_Rm = Slider(ax_Rm, 'Rm', 1, 20, valinit=5, valstep=delta)
sli_n = Slider(ax_n, 'n', 3, 10, valinit=6, valstep=delta)
sli_Rd = Slider(ax_Rd, 'Rd', 1, 40, valinit=12, valstep=delta)
sli_rd = Slider(ax_rd, 'rd', 0.1, 10, valinit=1.5, valstep=delta/10)
sli_e = Slider(ax_e, 'e', 0.1, 10, valinit=1.2, valstep=delta/10)
sli_N = Slider(ax_N, 'N', 2, 40, valinit=18, valstep=2*delta)
sli_d = Slider(ax_d, 'd', 2, 20, valinit=5,valstep=delta)
sli_D = Slider(ax_D, 'D', 5, 100, valinit=45,valstep=delta)

def update(val):
    sfm = sli_Rd.val
    sRm = sli_Rm.val
    sRd = sli_Rd.val
    sn = sli_n.val
    srd = sli_rd.val    
    se = sli_e.val
    sN = sli_N.val
    sd = sli_d.val
    sD = sli_D.val
    ax.set_xlim(-1.4*0.5*sD,1.4*0.5*sD)
    ax.set_ylim(-1.4*0.5*sD,1.4*0.5*sD)



sli_fm.on_changed(update)
sli_Rm.on_changed(update)
sli_Rd.on_changed(update)
sli_n.on_changed(update)
sli_rd.on_changed(update)
sli_e.on_changed(update)
sli_N.on_changed(update)
sli_d.on_changed(update)
sli_D.on_changed(update)

resetax = plt.axes([0.8, 0.0, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    sli_fm.reset()    
    sli_Rm.reset()
    sli_n.reset()
    sli_rd.reset()
    sli_Rd.reset()    
    sli_e.reset()
    sli_N.reset()
    sli_d.reset()
    sli_D.reset()

button.on_clicked(reset)

def animate(frame):
    sfm = sli_fm.val
    sRm = sli_Rm.val
    sRd = sli_Rd.val
    sn = sli_n.val
    srd = sli_rd.val    
    se = sli_e.val
    sN = sli_N.val
    sd = sli_d.val
    sD = sli_D.val
    frame = frame+1
    phi = 2*np.pi*frame/sfm


    draw_pin_init()
    pin_update(sN,sd,sD)

    update_inner_pin(se,sRm, phi)

    draw_inner_pin_init()
    inner_pin_update(sn,sN,srd,sRd,phi)
    
    draw_inner_circle_init()
    update_inner_circle(se,sn,sN,srd,sRd, phi)

    #draw_circle(se,sD,sd)
    ehypocycloidA_init()
    update_ehypocycloidA(se,sN,sD,sd, phi)
    #update_ehypocycloidB(se,sN,sD,sd, phi)


    fig.canvas.draw_idle()



ani = animation.FuncAnimation(fig, animate,frames=sli_fm.val*(sli_N.val-1), interval=interval)
dpi=100

plt.show()
