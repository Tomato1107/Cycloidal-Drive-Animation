import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button, RadioButtons

interval = 50 # ms, time between animation frames
fig, ax = plt.subplots(figsize=(6,6))
plt.subplots_adjust(left=0.15, bottom=0.35)

ax.set_aspect('equal')
plt.xlim(-1.2*2*40,1.2*2*40)
plt.ylim(-1.2*2*40,1.2*2*40)
t = np.linspace(0, 2*np.pi, 2000)
delta = 1
mode_fig = 0
con_fig = 0
pin_fig = 0

## draw circle
m1, = ax.plot([0], [0],'b-')
m2, = ax.plot([0], [0],'r-')
m3, = ax.plot([0], [0],'c-')
inner_pin, = ax.plot([0], [0],'k-')
dot, = ax.plot([0],[0], 'ko', ms=5)

def draw_circle_init():
    m1.set_data([0], [0])
    m2.set_data([0], [0])
    m3.set_data([0], [0])  

def draw_circle(e,d,D,n,phis,num):
    global mode_fig
    RD1 =D/2
    RD3 = D - e
    N1 = RD3/RD1*n
    if N1%1 == 0:
        N=N1
    else:
        if con_fig == 0:  
            N = int(N1+1)  #N = int(N1)+1  #N = int(N1)-1  #N = int(N1)
        if con_fig == 1: 
            N = int(N1-1)
        if con_fig == 2: 
            N = int(N1) 
    r = d/2
    for i in range(int(num)):
        if mode_fig==0:
            x0 = r*np.sin(t) - e*np.cos(phis+2*i*np.pi/num) 
            y0 = r*np.cos(t) - e*np.sin(phis+2*i*np.pi/num) 
        if mode_fig==1:
            x0 = r*np.sin(t) - e*np.cos(phis + phis/(N) +2*i*np.pi/num) 
            y0 = r*np.cos(t) - e*np.sin(phis + phis/(N) +2*i*np.pi/num)             
        if i == 0:
            m1.set_data(x0,y0)
        if i == 1:
            m2.set_data(x0,y0)
        if i == 2:
            m3.set_data(x0,y0)          

    x = (r-e)*np.cos(t)
    y = (r-e)*np.sin(t)
    inner_pin.set_data(x,y)

    x1 = (r-e)*np.cos(phis)
    y1 = (r-e)*np.sin(phis)
    dot.set_data(x1, y1)

# draw inner cycloid drive circle
p1, = ax.plot([0], [0],'b-')
p2, = ax.plot([0], [0],'r-')
p3, = ax.plot([0], [0],'c-')
def draw_cycloid_inner_circle_init():
    p1.set_data([0], [0])
    p2.set_data([0], [0])
    p3.set_data([0], [0])  
def draw_cycloid_inner_circle(e,r,D,n,phis,num):
    global con_fig 
    global mode_fig 
    RD1 =D/2
    RD3 = D - e
    N1 = RD3/RD1*n
    if N1%1 == 0:
        N=N1
    else:
        if con_fig == 0:  
            N = int(N1+1)  #N = int(N1)+1  #N = int(N1)-1  #N = int(N1)
        if con_fig == 1: 
            N = int(N1-1)
        if con_fig == 2: 
            N = int(N1) 

    RD = D/2
    for i in range(int(num)):
        if mode_fig == 0:
            x0 = r*np.sin(t) + (RD)*np.cos(2*i*np.pi/num) 
            y0 = r*np.cos(t) + (RD)*np.sin(2*i*np.pi/num) 
        if mode_fig == 1:
            x = r*np.sin(t) + (RD)*np.cos(2*i*np.pi/num) 
            y = r*np.cos(t) + (RD)*np.sin(2*i*np.pi/num)
            x0 = x*np.cos(phis/(N)) - y*np.sin(phis/(N)) 
            y0 = x*np.sin(phis/(N)) + y*np.cos(phis/(N))           
        if i == 0:
            p1.set_data(x0,y0)
        if i == 1:
            p2.set_data(x0,y0)
        if i == 2:
            p3.set_data(x0,y0)


## draw output_pin
num_output_pins = 60
ddotN, = ax.plot([0],[0], 'go', ms=5)
output_pins = [ax.plot([], [], 'g-')[0] for n in range(num_output_pins)]
def draw_outpin_init():
    for p in output_pins:
        p.set_data([0], [0])

def outpin_update(e,n,d,D, phis):
    global con_fig 
    global mode_fig
    RD1 =D/2
    RD3 = D - e
    N1 = RD3/RD1*n
    if N1%1 == 0:
        N=N1
    else:
        if con_fig == 0:  
            N = int(N1+1)  #N = int(N1)+1  #N = int(N1)-1  #N = int(N1)
        if con_fig == 1: 
            N = int(N1-1)
        if con_fig == 2: 
            N = int(N1)            
    #print(int(N1),N1, N)

    for i in range(int(N)):   
        xd = d/2*np.cos(t) + (RD3)*np.cos(2*i*np.pi/N)
        yd = d/2*np.sin(t) + (RD3)*np.sin(2*i*np.pi/N)
        if mode_fig == 0:
            if con_fig == 0:
                if ((N)/2+1)%2 != 0:
                    x = xd*np.cos(-phis/(N)) - yd*np.sin(-phis/(N)) 
                    y = xd*np.sin(-phis/(N)) + yd*np.cos(-phis/(N))
                if ((N)/2+1)%2 != 1:
                    #print(N)
                    x = xd*np.cos(-phis/(N) + np.pi/(N)) - yd*np.sin(-phis/(N) + np.pi/(N)) 
                    y = xd*np.sin(-phis/(N) + np.pi/(N)) + yd*np.cos(-phis/(N) + np.pi/(N))  
            if con_fig == 1:
                if ((N)/2+1)%2 != 1:
                    x = xd*np.cos(-phis/(N)) - yd*np.sin(-phis/(N)) 
                    y = xd*np.sin(-phis/(N)) + yd*np.cos(-phis/(N))
                if ((N)/2+1)%2 != 0:
                    #print(N)
                    x = xd*np.cos(-phis/(N) + np.pi/(N)) - yd*np.sin(-phis/(N) + np.pi/(N)) 
                    y = xd*np.sin(-phis/(N) + np.pi/(N)) + yd*np.cos(-phis/(N) + np.pi/(N))  
            if con_fig == 2:
                if ((N+1)/2+1)%2 != 0:
                    x = xd*np.cos(-phis/(N)) - yd*np.sin(-phis/(N)) 
                    y = xd*np.sin(-phis/(N)) + yd*np.cos(-phis/(N))
                if ((N+1)/2+1)%2 != 1:
                    #print(N)
                    x = xd*np.cos(-phis/(N) + np.pi/(N)) - yd*np.sin(-phis/(N) + np.pi/(N)) 
                    y = xd*np.sin(-phis/(N) + np.pi/(N)) + yd*np.cos(-phis/(N) + np.pi/(N)) 
        if mode_fig == 1:                     
            if con_fig == 0:
                if ((N)/2+1)%2 != 0:
                    x = xd
                    y = yd
                if ((N)/2+1)%2 != 1:
                    #print(N)
                    x = xd*np.cos( np.pi/(N)) - yd*np.sin( np.pi/(N)) 
                    y = xd*np.sin( np.pi/(N)) + yd*np.cos( np.pi/(N))  
            if con_fig == 1:
                if ((N)/2+1)%2 != 1:
                    x = xd 
                    y = yd
                if ((N)/2+1)%2 != 0:
                    #print(N)
                    x = xd*np.cos( np.pi/(N)) - yd*np.sin( np.pi/(N)) 
                    y = xd*np.sin( np.pi/(N)) + yd*np.cos( np.pi/(N))  
            if con_fig == 2:
                if ((N+1)/2+1)%2 != 0:
                    x = xd
                    y = yd
                if ((N+1)/2+1)%2 != 1:
                    #print(N)
                    x = xd*np.cos( np.pi/(N)) - yd*np.sin( np.pi/(N)) 
                    y = xd*np.sin( np.pi/(N)) + yd*np.cos( np.pi/(N))  
        output_pins[i].set_data(x,y)

##ehypocycloidOut:
ehypocycloidOut, = ax.plot([0],[0],'g-')
edotOut, = ax.plot([0],[0], 'go', ms=5)
def update_ehypocycloidOut(e,n,D,d, phis):
    global con_fig 
    global mode_fig 
    RD1 =D/2
    RD3 = D - e
    rd=d/2
    N1 = RD3/RD1*n
    if N1%1 == 0:
        N=N1
    else:
        if con_fig == 0:  
            N = int(N1+1)  #N = int(N1)+1  #N = int(N1)-1  #N = int(N1)
        if con_fig == 1: 
            N = int(N1-1)
        if con_fig == 2: 
            N = int(N1)            
    #print(int(N1),N1, N)
    
    x_out1 = (RD3)*np.cos(t) - e*np.cos((N+1)*t) - (rd-e)*np.cos(t - np.arctan(((N+1)*e*np.sin((N)*t))/(RD3-(N+1)*e*np.cos((N)*t))))
    y_out1 = (RD3)*np.sin(t) - e*np.sin((N+1)*t) - (rd-e)*np.sin(t - np.arctan(((N+1)*e*np.sin((N)*t))/(RD3-(N+1)*e*np.cos((N)*t))))
    if mode_fig == 0:  
        if con_fig == 0:  
            for i in range(int(N)):   
                if ((N)/2+1)%2 != 0: #Even   
                    x_out = x_out1*np.cos(-phis/(N)) - y_out1*np.sin(-phis/(N)) 
                    y_out = x_out1*np.sin(-phis/(N)) + y_out1*np.cos(-phis/(N))
                if ((N)/2+1)%2 != 1:
                    x_out = x_out1*np.cos(-phis/(N) + np.pi/(N)) - y_out1*np.sin(-phis/(N) + np.pi/(N)) 
                    y_out = x_out1*np.sin(-phis/(N) + np.pi/(N)) + y_out1*np.cos(-phis/(N) + np.pi/(N)) 
        if con_fig == 1:  
            for i in range(int(N)):   
                if ((N)/2+1)%2 != 1: #Even  
                    x_out = x_out1*np.cos(-phis/(N)) - y_out1*np.sin(-phis/(N)) 
                    y_out = x_out1*np.sin(-phis/(N)) + y_out1*np.cos(-phis/(N))
                if ((N)/2+1)%2 != 0:
                    x_out = x_out1*np.cos(-phis/(N) + np.pi/(N)) - y_out1*np.sin(-phis/(N) + np.pi/(N)) 
                    y_out = x_out1*np.sin(-phis/(N) + np.pi/(N)) + y_out1*np.cos(-phis/(N) + np.pi/(N)) 
        if con_fig == 2:  
            for i in range(int(N)):   
                if ((N+1)/2+1)%2 != 0: #Even    
                    x_out = x_out1*np.cos(-phis/(N)) - y_out1*np.sin(-phis/(N)) 
                    y_out = x_out1*np.sin(-phis/(N)) + y_out1*np.cos(-phis/(N))
                if ((N+1)/2+1)%2 != 1:
                    x_out = x_out1*np.cos(-phis/(N) + np.pi/(N)) - y_out1*np.sin(-phis/(N) + np.pi/(N)) 
                    y_out = x_out1*np.sin(-phis/(N) + np.pi/(N)) + y_out1*np.cos(-phis/(N) + np.pi/(N))  
    if mode_fig == 1:  
        if con_fig == 0:  
            for i in range(int(N)):   
                if ((N)/2+1)%2 != 0: #Even   
                    x_out = x_out1
                    y_out = y_out1
                if ((N)/2+1)%2 != 1:
                    x_out = x_out1*np.cos( np.pi/(N)) - y_out1*np.sin( np.pi/(N)) 
                    y_out = x_out1*np.sin( np.pi/(N)) + y_out1*np.cos( np.pi/(N)) 
        if con_fig == 1:  
            for i in range(int(N)):   
                if ((N)/2+1)%2 != 1: #Even  
                    x_out = x_out1 
                    y_out = y_out1
                if ((N)/2+1)%2 != 0:
                    x_out = x_out1*np.cos( np.pi/(N)) - y_out1*np.sin( np.pi/(N)) 
                    y_out = x_out1*np.sin( np.pi/(N)) + y_out1*np.cos( np.pi/(N)) 
        if con_fig == 2:  
            for i in range(int(N)):   
                if ((N+1)/2+1)%2 != 0: #Even    
                    x_out = x_out1
                    y_out = y_out1
                if ((N+1)/2+1)%2 != 1:
                    x_out = x_out1*np.cos( np.pi/(N)) - y_out1*np.sin( np.pi/(N)) 
                    y_out = x_out1*np.sin( np.pi/(N)) + y_out1*np.cos( np.pi/(N))                      

    ehypocycloidOut.set_data(x_out,y_out)
    edotOut.set_data(x_out[0], y_out[0])

##ehypocycloidA:
ehypocycloidA1, = ax.plot([0],[0],'b-')
ehypocycloidA2, = ax.plot([0],[0],'r-')
ehypocycloidA3, = ax.plot([0],[0],'c-')
edotA1, = ax.plot([0],[0], 'bo', ms=5)

def ehypocycloidA_init():
    ehypocycloidA1.set_data([0], [0])
    ehypocycloidA2.set_data([0], [0])
    ehypocycloidA3.set_data([0], [0])  

def update_ehypocycloidA(e,n,D,d, phis,num):
    global mode_fig     
    RD=D/2
    rd=d/2
    rc = (n-1)*(RD/n)
    rm = (RD/n)
    xa = (rc+rm)*np.cos(t)-e*np.cos((rc+rm)/rm*t)
    ya = (rc+rm)*np.sin(t)-e*np.sin((rc+rm)/rm*t)

    dxa = (rc+rm)*(-np.sin(t)+(e/rm)*np.sin((rc+rm)/rm*t))
    dya = (rc+rm)*(np.cos(t)-(e/rm)*np.cos((rc+rm)/rm*t))
    
    x1 = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya)) 
    y1 = (ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)   

    RD1 =D/2
    RD3 = D - e
    rd=d/2
    N1 = RD3/RD1*n
    if N1%1 == 0:
        N=N1
    else:
        if con_fig == 0:  
            N = int(N1+1)  #N = int(N1)+1  #N = int(N1)-1  #N = int(N1)
        if con_fig == 1: 
            N = int(N1-1)
        if con_fig == 2: 
            N = int(N1)   

    for i in range(int(num)):
        if mode_fig == 0:   
            if (n+1)%2 != 0:
                x = x1*np.cos(-phis/(n-1) + 2*i*np.pi/num) - y1*np.sin(-phis/(n-1) + 2*i*np.pi/num) + RD *np.cos(2*i*np.pi/num)  
                y = x1*np.sin(-phis/(n-1) + 2*i*np.pi/num) + y1*np.cos(-phis/(n-1) + 2*i*np.pi/num) + RD *np.sin(2*i*np.pi/num)  
            if (n+1)%2 == 0:
                x = x1*np.cos(-phis/(n-1) + 2*i*np.pi/num + np.pi/(n-1)) - y1*np.sin(-phis/(n-1) + 2*i*np.pi/num + np.pi/(n-1)) + RD *np.cos(2*i*np.pi/num) 
                y = x1*np.sin(-phis/(n-1) + 2*i*np.pi/num + np.pi/(n-1)) + y1*np.cos(-phis/(n-1) + 2*i*np.pi/num + np.pi/(n-1)) + RD *np.sin(2*i*np.pi/num) 
        
        if mode_fig == 1:   
            if (n+1)%2 != 0:
                x = x1*np.cos(-phis/(n-1) + phis/(N) + 2*i*np.pi/num) - y1*np.sin(-phis/(n-1) + phis/(N) + 2*i*np.pi/num) + RD *np.cos(2*i*np.pi/num+ phis/(N) )  
                y = x1*np.sin(-phis/(n-1) + phis/(N) + 2*i*np.pi/num) + y1*np.cos(-phis/(n-1) + phis/(N) + 2*i*np.pi/num) + RD *np.sin(2*i*np.pi/num+ phis/(N) )  
                
            if (n+1)%2 == 0:
                x = x1*np.cos(-phis/(n-1) + phis/(N) + 2*i*np.pi/num + np.pi/(n-1)) - y1*np.sin(-phis/(n-1) + phis/(N) + 2*i*np.pi/num + np.pi/(n-1)) + RD *np.cos(2*i*np.pi/num+ phis/(N) ) 
                y = x1*np.sin(-phis/(n-1) + phis/(N) + 2*i*np.pi/num + np.pi/(n-1)) + y1*np.cos(-phis/(n-1) + phis/(N) + 2*i*np.pi/num + np.pi/(n-1)) + RD *np.sin(2*i*np.pi/num+ phis/(N) ) 
              
        if i == 0:
            ehypocycloidA1.set_data(x,y)
            edotA1.set_data(x[0], y[0])
        if i == 1:
            ehypocycloidA2.set_data(x,y)
        if i == 2:
            ehypocycloidA3.set_data(x,y)  

axcolor = 'lightgoldenrodyellow'

ax_fm = plt.axes([0.25, 0.21, 0.5, 0.02], facecolor=axcolor)
#ax_Rm = plt.axes([0.25, 0.24, 0.5, 0.02], facecolor=axcolor)
ax_n = plt.axes([0.25, 0.15, 0.5, 0.02], facecolor=axcolor)
ax_Rd = plt.axes([0.25, 0.18, 0.5, 0.02], facecolor=axcolor)
#ax_rd = plt.axes([0.25, 0.15, 0.5, 0.02], facecolor=axcolor)
ax_e = plt.axes([0.25, 0.12, 0.5, 0.02], facecolor=axcolor)
ax_N = plt.axes([0.25, 0.09, 0.5, 0.02], facecolor=axcolor)
ax_d = plt.axes([0.25, 0.06, 0.5, 0.02], facecolor=axcolor)
ax_D = plt.axes([0.25, 0.03, 0.5, 0.02], facecolor=axcolor)

sli_fm = Slider(ax_fm, 'fm', 10, 100, valinit=50, valstep=delta)
#sli_Rm = Slider(ax_Rm, 'Rm', 1, 10, valinit=20, valstep=delta)
sli_n = Slider(ax_n, 'n', 1, 3, valinit=1, valstep=delta)
sli_Rd = Slider(ax_Rd, 'Rd', 1, 40, valinit=10, valstep=delta)
#sli_rd = Slider(ax_rd, 'rd', 0.1, 10, valinit=1.5, valstep=delta/10)
sli_e = Slider(ax_e, 'e', 0.1, 10, valinit=2, valstep=delta/10)
sli_N = Slider(ax_N, 'N', 2, 20, valinit=10, valstep=delta)
sli_d = Slider(ax_d, 'd', 2, 20, valinit=10,valstep=delta)
sli_D = Slider(ax_D, 'D', 5, 100, valinit=80,valstep=delta)

def update(val):
    sfm = sli_Rd.val
    #sRm = sli_Rm.val
    sRd = sli_Rd.val
    sn = sli_n.val
    #srd = sli_rd.val    
    se = sli_e.val
    sN = sli_N.val
    sd = sli_d.val
    sD = sli_D.val
    ax.set_xlim(-1.2*sD,1.2*sD)
    ax.set_ylim(-1.2*sD,1.2*sD)



sli_fm.on_changed(update)
#sli_Rm.on_changed(update)
sli_Rd.on_changed(update)
sli_n.on_changed(update)
#sli_rd.on_changed(update)
sli_e.on_changed(update)
sli_N.on_changed(update)
sli_d.on_changed(update)
sli_D.on_changed(update)

resetax = plt.axes([0.8, 0.0, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')
rax = plt.axes([0.025, 0.45, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('Config 1', 'Config 2', 'Config 3'), active=0)
rax_1 = plt.axes([0.025, 0.25, 0.15, 0.15], facecolor=axcolor)
radio_1 = RadioButtons(rax_1, ('NonePin', 'Pin'), active=0)
rax_2 = plt.axes([0.025, 0.65, 0.15, 0.15], facecolor=axcolor)
radio_2 = RadioButtons(rax_2, ('Mode 1', 'Mode 2'), active=0)

def reset(event):
    sli_fm.reset()    
    #sli_Rm.reset()
    sli_n.reset()
    #sli_rd.reset()
    sli_Rd.reset()    
    sli_e.reset()
    sli_N.reset()
    sli_d.reset()
    sli_D.reset()

button.on_clicked(reset)

def configfunc(label):
    global con_fig
    if label == 'Config 1':        
        con_fig = 0
    if label == 'Config 2':
        con_fig = 1
    if label == 'Config 3':
        con_fig = 2
radio.on_clicked(configfunc)

def pin_modefunc(label):
    global pin_fig
    if label == 'NonePin':        
        pin_fig = 0
    if label == 'Pin':
        pin_fig = 1
radio_1.on_clicked(pin_modefunc)

def modefunc(label):
    global mode_fig
    if label == 'Mode 1':        
        mode_fig = 0
    if label == 'Mode 2':
        mode_fig = 1
radio_2.on_clicked(modefunc)

def animate(frame):
    sfm = sli_fm.val
    #sRm = sli_Rm.val
    sRd = sli_Rd.val
    sn = sli_n.val
    #srd = sli_rd.val    
    se = sli_e.val
    sN = sli_N.val
    sd = sli_d.val
    sD = sli_D.val
    frame = frame+1
    phi = 2*np.pi*frame/sfm

    draw_circle_init()
    draw_circle(se,sd,sD,sN,phi,sn)

    draw_cycloid_inner_circle_init()    
    draw_cycloid_inner_circle(se,sRd,sD,sN,phi,sn)

    ehypocycloidA_init()
    update_ehypocycloidA(se,sN,sD,sd, phi,sn)


    draw_outpin_init()
    if pin_fig == 1:    
        outpin_update(se,sN,sd,sD, phi)
        ehypocycloidOut.set_visible(0)
        edotOut.set_visible(0)
    if pin_fig == 0:     
        ehypocycloidOut.set_visible(1)    
        edotOut.set_visible(1) 
        update_ehypocycloidOut(se,sN,sD,sd, phi)

    fig.canvas.draw_idle()



ani = animation.FuncAnimation(fig, animate,frames=sli_fm.val*(sli_N.val-1), interval=interval)
dpi=100

plt.show()
