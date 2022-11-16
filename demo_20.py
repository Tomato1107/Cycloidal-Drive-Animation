import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button

interval = 50 # ms, time between animation frames

fig, ax = plt.subplots(figsize=(6,6))
plt.subplots_adjust(left=0.15, bottom=0.35)

ax.set_aspect('equal')
plt.xlim(-1.4*8,1.4*8)
plt.ylim(-1.4*8,1.4*8)
delta = 1

##inner pin:
inner_pin, = ax.plot([0],[0],'g-')
d0, = ax.plot([0],[0],'r-')
dot, = ax.plot([0],[0], 'ro', ms=5)
def update_inner_pin(Rm,rm,rc, phi):
    t = np.linspace(0, 2*np.pi, 2000)
    e = rm - rc
    #x = (rm)*np.cos(t)+e*np.cos(phi)
    #y = (rm)*np.sin(t)+e*np.sin(phi)
    #inner_pin.set_data(x,y)
    #x1 = (rc)*np.cos(t)*np.cos(phi) - (rc)*np.sin(t)*np.sin(phi)
    #y1 = (rc)*np.cos(t)*np.sin(phi) + (rc)*np.sin(t)*np.cos(phi)   
    if e >=0:
        x = (Rm + e)*np.cos(t)+e*np.cos(phi)
        y = (Rm + e)*np.sin(t)+e*np.sin(phi)
    else:
        x = (Rm - e)*np.cos(t)+e*np.cos(phi)
        y = (Rm - e)*np.sin(t)+e*np.sin(phi)        
    inner_pin.set_data(x,y)
    x1 = (Rm)*np.cos(t)*np.cos(phi) - (Rm)*np.sin(t)*np.sin(phi)
    y1 = (Rm)*np.cos(t)*np.sin(phi) + (Rm)*np.sin(t)*np.cos(phi)

    d0.set_data(x1, y1)
    dot.set_data(x1[0], y1[0])


##cycloidA:
cycloidA, = ax.plot([0],[0],'b-')
def update_cycloidA(rm,rc,R):
    t = np.linspace(0, rm*2*np.pi, 2000)
    e = rm-rc
    x = e*np.cos(t)+R*np.cos((rm-rc)/rm*t)
    y = e*np.sin(t)+R*np.sin((rm-rc)/rm*t)
    cycloidA.set_data(x, y)


##Reuleaux triangle:
num_arcs = 5
arcs = [ax.plot([], [], 'g-')[0] for n in range(num_arcs)]
dotR, = ax.plot([0],[0], 'go', ms=5)
def draw_Reuleaux_init():
    for p in arcs:
        p.set_data([0], [0])
def update_reuleaux_triangle(n,rm,rc,R,phis):
    e=rm-rc
    if n == 2:
        t = np.linspace(np.pi/6, 5*np.pi/6, 2000)
        xa = (2*R/(np.sqrt(3))*np.cos(t)) 
        ya = (2*R/(np.sqrt(3))*np.sin(t)) - 1/np.sqrt(3)*R

        # another configuration
        #t = np.linspace(np.pi/3, 2*np.pi/3, 2000)
        #xa = (2*R*np.cos(t)) 
        #ya = (2*R*np.sin(t)) - np.sqrt(3)*R
        
    if n == 3:
        t = np.linspace(np.pi/6, np.pi/2, 2000)
        xa = (np.sqrt(3)*R*np.cos(t)) - R/2 
        ya = (np.sqrt(3)*R*np.sin(t)) - np.sqrt(3)*R/2
    if n == 4:
        t = np.linspace(np.pi/12, 5*np.pi/12, 2000)
        xa = (np.sqrt(2)*R*np.cos(t)) - np.sqrt(2)*R*np.sin(np.pi/12)
        ya = (np.sqrt(2)*R*np.sin(t)) - np.sqrt(2)*R*np.sin(np.pi/12)

    if n == 5:
        t = np.linspace(7*np.pi/60, 51*np.pi/180, 2000)
        xa = (R*np.sin(np.pi/5)/np.sin(np.pi/12))*np.cos(t) - (R*np.sin(np.pi/5)/np.sin(np.pi/12))*np.cos(7*np.pi/60) + R
        ya = (R*np.sin(np.pi/5)/np.sin(np.pi/12))*np.sin(t) - (R*np.sin(np.pi/5)/np.sin(np.pi/12))*np.sin(7*np.pi/60)

    for i in range(int(n)):    
        x = xa*np.cos(i*2*np.pi/n + phis*((rm-rc)/rm)) -  ya*np.sin(i*2*np.pi/n + phis*((rm-rc)/rm)) + e*np.cos(phis)
        y = xa*np.sin(i*2*np.pi/n + phis*((rm-rc)/rm)) +  ya*np.cos(i*2*np.pi/n + phis*((rm-rc)/rm)) + e*np.sin(phis)
        arcs[i].set_data(x,y)
        if i == 0:
            dotR.set_data(x[0], y[0])


axcolor = 'lightgoldenrodyellow'

ax_fm = plt.axes([0.25, 0.18, 0.5, 0.02], facecolor=axcolor)
ax_Rm = plt.axes([0.25, 0.15, 0.5, 0.02], facecolor=axcolor)
ax_rc = plt.axes([0.25, 0.12, 0.5, 0.02], facecolor=axcolor)
ax_rm = plt.axes([0.25, 0.09, 0.5, 0.02], facecolor=axcolor)
ax_N = plt.axes([0.25, 0.06, 0.5, 0.02], facecolor=axcolor)
ax_R = plt.axes([0.25, 0.03, 0.5, 0.02], facecolor=axcolor)


sli_fm = Slider(ax_fm, 'fm', 10, 80, valinit=40, valstep=delta)
sli_Rm = Slider(ax_Rm, 'Rm', 0.5, 40, valinit=3, valstep=0.1*delta)
sli_rc = Slider(ax_rc, 'rc', 1, 20, valinit=2, valstep=delta)
sli_rm = Slider(ax_rm, 'rm', 1, 20, valinit=3,valstep=delta)
sli_N = Slider(ax_N, 'N', 2, 5, valinit=3,valstep=delta)
sli_R = Slider(ax_R, 'R', 1, 80, valinit=7.3,valstep=0.1*delta)

def update(val):
    sfm = sli_fm.val
    sRm = sli_Rm.val
    src = sli_rc.val
    srm = sli_rm.val
    sN = sli_N.val
    sR = sli_R.val
    ax.set_xlim(-1.4*sR,1.4*sR)
    ax.set_ylim(-1.4*sR,1.4*sR)

sli_fm.on_changed(update)
sli_Rm.on_changed(update)
sli_rc.on_changed(update)
sli_rm.on_changed(update)
sli_N.on_changed(update)
sli_R.on_changed(update)

resetax = plt.axes([0.86, 0.02, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    sli_fm.reset()    
    sli_Rm.reset() 
    sli_rc.reset()
    sli_rm.reset()
    sli_N.reset() 
    sli_R.reset()

button.on_clicked(reset)

def animate(frame):
    sfm = sli_fm.val
    sRm = sli_Rm.val
    src = sli_rc.val
    srm = sli_rm.val
    sN = sli_N.val
    sR = sli_R.val
    frame = frame+1
    phi = 2*np.pi*frame/sfm

    update_inner_pin(sRm,srm,src, phi)
    update_cycloidA(srm,src,sR)
    draw_Reuleaux_init()
    update_reuleaux_triangle(sN,srm,src,sR,phi)

    fig.canvas.draw_idle()

ani = animation.FuncAnimation(fig, animate,frames=sli_fm.val*sli_N.val*int(sli_fm.val/10), interval=interval)
dpi=100

plt.show()
