import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button
#plt.rcParams['animation.ffmpeg_path'] = 'D:/portableSoftware/ShareX/ShareX/Tools/ffmpeg.exe'

interval = 50 # ms, time between animation frames

fig, ax = plt.subplots(figsize=(6,6))
plt.subplots_adjust(left=0.15, bottom=0.35)

ax.set_aspect('equal')
plt.xlim(-1.2*40,1.2*40)
plt.ylim(-1.2*40,1.2*40)
#plt.grid()
t = np.linspace(0, 2*np.pi, 2000)
delta = 1
e =2
n=10
RD=40
rd=5
#plt.grid()
## draw pin
l0, = ax.plot([], [], 'r-', lw=2)
ddot, = ax.plot([20],[0], 'ro', ms=5)

def draw_pin_init():
    l0.set_data([0], [0])


def pin_update(e,d,D, phis):
    
    x = (d/2*np.cos(t)+ D/2) + e*np.cos(phis)
    y = (d/2*np.sin(t) ) + e*np.sin(phis)
    l0.set_data(x,y)
    
    x1 = (d/2*np.cos(phis)+ D/2) + e*np.cos(phis)
    y1 = (d/2*np.sin(phis) ) + e*np.sin(phis)
    #self.line.set_data([0,x1],[0,y1])
    ddot.set_data(x1, y1)




## draw drive_pin
a = 5*np.sin(t)
b = 5*np.cos(t) 
d0, = ax.plot(a, b,'k-', lw=2)

def drive_pin_update(r,D):
    x = r*np.sin(t) + D/2 
    y = r*np.cos(t)
    d0.set_data(x,y)



## draw circle
c = 25*np.sin(t)
d = 25*np.cos(t) 
d1, = ax.plot(a, b,'r-', lw=2)

def draw_circle(r):
    x = r*np.sin(t) 
    y = r*np.cos(t)
    d1.set_data(x,y)



##ehypocycloid:

rc = (n-1)*(RD/n)
rm = (RD/n)
xa = (rc+rm)*np.cos(t)-e*np.cos((rc+rm)/rm*t)
ya = (rc+rm)*np.sin(t)-e*np.sin((rc+rm)/rm*t)

dxa = (rc+rm)*(-np.sin(t)+(e/rm)*np.sin((rc+rm)/rm*t))
dya = (rc+rm)*(np.cos(t)-(e/rm)*np.cos((rc+rm)/rm*t))

x = xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya) + e
y = ya + rd/np.sqrt(dxa**2 + dya**2)*dxa
ehypocycloid, = ax.plot(x,y,'r-')
##driver line and dot: (rc+rm) - rd
#self.eline, = self.ax.plot([(rc+rm) - rd, 0],[0,0],'r-')
edot, = ax.plot([(rc+rm) - rd],[0], 'ro', ms=5)

def update_ehypocycloid(e,n,D,d, phis):
    RD=D/2
    rd=d/2
    rc = (n-1)*(RD/n)
    rm = (RD/n)
    xa = (rc+rm)*np.cos(t)-e*np.cos((rc+rm)/rm*t)
    ya = (rc+rm)*np.sin(t)-e*np.sin((rc+rm)/rm*t)

    dxa = (rc+rm)*(-np.sin(t)+(e/rm)*np.sin((rc+rm)/rm*t))
    dya = (rc+rm)*(np.cos(t)-(e/rm)*np.cos((rc+rm)/rm*t))
    
    #x = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))
    #y = (ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)
    x = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.cos(-phis/(n-1) + np.pi/(n-1))-(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.sin(-phis/(n-1) + np.pi/(n-1))  
    y = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.sin(-phis/(n-1) + np.pi/(n-1))+(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.cos(-phis/(n-1) + np.pi/(n-1)) 
    ehypocycloid.set_data(x,y)

    #self.eline.set_data([e*np.cos(phis),x[0]],[e*np.sin(phis),y[0]])
    edot.set_data(x[0], y[0])




axcolor = 'lightgoldenrodyellow'

ax_fm = plt.axes([0.25, 0.21, 0.5, 0.02], facecolor=axcolor)
#ax_Rm = plt.axes([0.25, 0.24, 0.5, 0.02], facecolor=axcolor)
#ax_n = plt.axes([0.25, 0.21, 0.5, 0.02], facecolor=axcolor)
ax_Rd = plt.axes([0.25, 0.18, 0.5, 0.02], facecolor=axcolor)
ax_rd = plt.axes([0.25, 0.15, 0.5, 0.02], facecolor=axcolor)
ax_e = plt.axes([0.25, 0.12, 0.5, 0.02], facecolor=axcolor)
ax_N = plt.axes([0.25, 0.09, 0.5, 0.02], facecolor=axcolor)
ax_d = plt.axes([0.25, 0.06, 0.5, 0.02], facecolor=axcolor)
ax_D = plt.axes([0.25, 0.03, 0.5, 0.02], facecolor=axcolor)

sli_fm = Slider(ax_fm, 'fm', 10, 100, valinit=50, valstep=delta)
#sli_Rm = Slider(ax_Rm, 'Rm', 1, 10, valinit=20, valstep=delta)
#sli_n = Slider(ax_n, 'n', 3, 10, valinit=6, valstep=delta)
sli_Rd = Slider(ax_Rd, 'Rd', 1, 40, valinit=20, valstep=delta)
sli_rd = Slider(ax_rd, 'rd', 0.5, 10, valinit=1.5, valstep=delta)
sli_e = Slider(ax_e, 'e', 0.1, 10, valinit=2, valstep=delta/10)
sli_N = Slider(ax_N, 'N', 3, 40, valinit=10, valstep=delta)
sli_d = Slider(ax_d, 'd', 2, 20, valinit=10,valstep=delta)
sli_D = Slider(ax_D, 'D', 5, 100, valinit=80,valstep=delta)

def update(val):
    sfm = sli_Rd.val
    #sRm = sli_Rm.val
    sRd = sli_Rd.val
    #sn = sli_n.val
    srd = sli_rd.val    
    se = sli_e.val
    sN = sli_N.val
    sd = sli_d.val
    sD = sli_D.val
    ax.set_xlim(-1.2*0.5*sD,1.2*0.5*sD)
    ax.set_ylim(-1.2*0.5*sD,1.2*0.5*sD)



sli_fm.on_changed(update)
#sli_Rm.on_changed(update)
sli_Rd.on_changed(update)
#sli_n.on_changed(update)
sli_rd.on_changed(update)
sli_e.on_changed(update)
sli_N.on_changed(update)
sli_d.on_changed(update)
sli_D.on_changed(update)

resetax = plt.axes([0.8, 0.0, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    sli_fm.reset()    
    #sli_Rm.reset()
    #sli_n.reset()
    sli_rd.reset()
    sli_Rd.reset()    
    sli_e.reset()
    sli_N.reset()
    sli_d.reset()
    sli_D.reset()

button.on_clicked(reset)

def animate(frame):
    sfm = sli_fm.val
    #sRm = sli_Rm.val
    sRd = sli_Rd.val
    #sn = sli_n.val
    srd = sli_rd.val    
    se = sli_e.val
    sN = sli_N.val
    sd = sli_d.val
    sD = sli_D.val
    frame = frame+1
    phi = 2*np.pi*frame/sfm


    draw_pin_init()
    draw_circle(sRd)

    pin_update(se,sd,sD, phi)


    drive_pin_update(srd,sD)

    update_ehypocycloid(se,sN,sD,sd, phi)

    fig.canvas.draw_idle()



ani = animation.FuncAnimation(fig, animate,frames=sli_fm.val*(sli_N.val-1), interval=interval)
dpi=100
##un-comment the next line, if you want to save the animation as gif:
#hypo.animation.save('myhypocycloid.gif', writer='pillow', fps=10, dpi=75)
#ani.save('myGUI1.mp4', writer="ffmpeg",dpi=dpi)
plt.show()
