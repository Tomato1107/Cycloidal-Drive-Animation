import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button, RadioButtons


fig, ax = plt.subplots(figsize=(6,6))
plt.subplots_adjust(left=0.15, bottom=0.35)

ax.set_aspect('equal')
plt.xlim(-1.4*40,1.4*40)
plt.ylim(-1.4*40,1.4*40)
#plt.grid()
t = np.linspace(0, 2*np.pi, 10000)
delta = 1
mode_fig = 0
pin_fig = 0
cycloid_fig = 1  
curve_fig = 0


## draw pin
num_pins = 61
pins = [ax.plot([], [], 'k-')[0] for n in range(num_pins)]
def draw_pin_init():
    for p in pins:
        p.set_data([0], [0])

def pin_update(n,d,D,phi):
    global mode_fig 
    for i in range(int(n)): 
        if mode_fig == 1:        
            x = (d/2*np.sin(t)+ D/2*np.cos(2*i*np.pi/n))
            y = (d/2*np.cos(t) + D/2*np.sin(2*i*np.pi/n))
        if mode_fig == 0:
            x = (d/2*np.sin(t)+ D/2*np.cos(2*i*np.pi/n))*np.cos(phi/(n)) - (d/2*np.cos(t) + D/2*np.sin(2*i*np.pi/n))*np.sin(phi/(n))
            y = (d/2*np.sin(t)+ D/2*np.cos(2*i*np.pi/n))*np.sin(phi/(n)) + (d/2*np.cos(t) + D/2*np.sin(2*i*np.pi/n))*np.cos(phi/(n))
        pins[i].set_data(x,y)

## draw inner_pin
num_inner_pins = 10
inner_pins = [ax.plot([], [], 'k-')[0] for n in range(num_inner_pins)]
def draw_inner_pin_init():
    for p in inner_pins:
        p.set_data([0], [0])

def inner_pin_update(n,N,rd,Rd,phi):
    global mode_fig 
    for i in range(int(n)):   
        if mode_fig == 1:
            x = (rd*np.sin(t)+ Rd*np.cos(2*i*np.pi/n))*np.cos(-phi/(N-1)+ 3*np.pi/(N-1)-np.pi/3) - (rd*np.cos(t) + Rd*np.sin(2*i*np.pi/n))*np.sin(-phi/(N-1)+ 3*np.pi/(N-1)-np.pi/3)
            y = (rd*np.sin(t)+ Rd*np.cos(2*i*np.pi/n))*np.sin(-phi/(N-1)+ 3*np.pi/(N-1)-np.pi/3) + (rd*np.cos(t) + Rd*np.sin(2*i*np.pi/n))*np.cos(-phi/(N-1)+ 3*np.pi/(N-1)-np.pi/3)
        if mode_fig == 0:        
            x = (rd*np.sin(t)+ Rd*np.cos(2*i*np.pi/n))*np.cos( 3*np.pi/(N-1)-np.pi/3) - (rd*np.cos(t) + Rd*np.sin(2*i*np.pi/n))*np.sin( 3*np.pi/(N-1)-np.pi/3)
            y = (rd*np.sin(t)+ Rd*np.cos(2*i*np.pi/n))*np.sin( 3*np.pi/(N-1)-np.pi/3) + (rd*np.cos(t) + Rd*np.sin(2*i*np.pi/n))*np.cos( 3*np.pi/(N-1)-np.pi/3)        
        inner_pins[i].set_data(x,y)        


## draw drive_pin
d0, = ax.plot([0],[0],'k-', lw=2)
def drive_pin_update(r):
    x = r*np.sin(t)
    y = r*np.cos(t)
    d0.set_data(x,y)


#inner circleA:
num_inner_circlesA = 10
inner_circlesA = [ax.plot([], [], 'r-')[0] for n in range(num_inner_circlesA)]
def draw_inner_circleA_init():
    for p in inner_circlesA:
        p.set_data([0], [0])

def update_inner_circleA(e,n,N,rd,Rd, phi):
    global mode_fig    
    for i in range(int(n)):
        if mode_fig == 1:
            x = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.cos(-phi/(N-1)+ 3*np.pi/(N-1)-np.pi/3) - ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.sin(-phi/(N-1)+ 3*np.pi/(N-1)-np.pi/3) + e*np.cos(phi)
            y = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.sin(-phi/(N-1)+ 3*np.pi/(N-1)-np.pi/3) + ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.cos(-phi/(N-1)+ 3*np.pi/(N-1)-np.pi/3) + e*np.sin(phi)        
        if mode_fig == 0:
            x = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.cos( 3*np.pi/(N-1)-np.pi/3) - ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.sin( 3*np.pi/(N-1)-np.pi/3) + e*np.cos(phi)
            y = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.sin( 3*np.pi/(N-1)-np.pi/3) + ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.cos( 3*np.pi/(N-1)-np.pi/3) + e*np.sin(phi)        
        inner_circlesA[i].set_data(x,y)         
        

#inner circleB:
num_inner_circlesB = 10
inner_circlesB = [ax.plot([], [], 'b-')[0] for n in range(num_inner_circlesB)]
def draw_inner_circleB_init():
    for p in inner_circlesB:
        p.set_data([0], [0])

def update_inner_circleB(e,n,N,rd,Rd, phi):
    global mode_fig
    global cycloid_fig       
    for i in range(int(n)):
        if mode_fig == 1:
            if cycloid_fig == 3:
                x = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.cos(-phi/(N-1)+ 3*np.pi/(N-1) - np.pi/(3)) - ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.sin(-phi/(N-1)+ 3*np.pi/(N-1)- np.pi/(3)) - e*np.cos(phi-np.pi/3)
                y = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.sin(-phi/(N-1)+ 3*np.pi/(N-1)- np.pi/(3)) + ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.cos(-phi/(N-1)+ 3*np.pi/(N-1)- np.pi/(3)) - e*np.sin(phi-np.pi/3)
            if cycloid_fig == 2:
                x = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.cos(-phi/(N-1) + 3*np.pi/(N-1) - np.pi/(3)) - ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.sin(-phi/(N-1) + 3*np.pi/(N-1) - np.pi/(3)) - e*np.cos(phi)
                y = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.sin(-phi/(N-1) + 3*np.pi/(N-1) - np.pi/(3)) + ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.cos(-phi/(N-1) + 3*np.pi/(N-1) - np.pi/(3)) - e*np.sin(phi)
         
        if mode_fig == 0:
            if cycloid_fig == 3:            
                x = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.cos( 3*np.pi/(N-1) - np.pi/(3)) - ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.sin( 3*np.pi/(N-1)- np.pi/(3)) - e*np.cos(phi-np.pi/3)
                y = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.sin( 3*np.pi/(N-1) - np.pi/(3)) + ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.cos( 3*np.pi/(N-1)- np.pi/(3)) - e*np.sin(phi-np.pi/3)
            if cycloid_fig == 2:            
                x = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.cos( 3*np.pi/(N-1) - np.pi/(3)) - ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.sin( 3*np.pi/(N-1) - np.pi/(3)) - e*np.cos(phi)
                y = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.sin( 3*np.pi/(N-1) - np.pi/(3)) + ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.cos( 3*np.pi/(N-1) - np.pi/(3)) - e*np.sin(phi)
        inner_circlesB[i].set_data(x,y)           
    

#inner circleC:
num_inner_circlesC = 10
inner_circlesC = [ax.plot([], [], 'g-')[0] for n in range(num_inner_circlesC)]
def draw_inner_circleC_init():
    for p in inner_circlesC:
        p.set_data([0], [0])

def update_inner_circleC(e,n,N,rd,Rd, phi):
    global mode_fig     
    for i in range(int(n)):
        if mode_fig == 1:
            x = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.cos(-phi/(N-1) + 3*np.pi/(N-1) - np.pi/(3)) - ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.sin(-phi/(N-1) + 3*np.pi/(N-1)- np.pi/(3)) - e*np.cos(phi+np.pi/3)
            y = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.sin(-phi/(N-1) + 3*np.pi/(N-1)- np.pi/(3)) + ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.cos(-phi/(N-1) + 3*np.pi/(N-1)- np.pi/(3)) - e*np.sin(phi+np.pi/3)
        if mode_fig == 0:
            x = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.cos( 3*np.pi/(N-1) - np.pi/(3)) - ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.sin( 3*np.pi/(N-1)- np.pi/(3)) - e*np.cos(phi+np.pi/3)
            y = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.sin( 3*np.pi/(N-1) - np.pi/(3)) + ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.cos( 3*np.pi/(N-1)- np.pi/(3)) - e*np.sin(phi+np.pi/3)
        inner_circlesC[i].set_data(x,y)                
       

##inner pinA:
inner_pinA, = ax.plot([0],[0],'r-')
dotA, = ax.plot([0],[0], 'ro', ms=5)
def update_inner_pinA(e,Rm, phi):
    x = (Rm+e)*np.cos(t)+e*np.cos(phi)
    y = (Rm+e)*np.sin(t)+e*np.sin(phi)
    inner_pinA.set_data(x,y)
    
    x1 = (Rm+e)*np.cos(phi)+e*np.cos(phi)
    y1 = (Rm+e)*np.sin(phi)+e*np.sin(phi)
    dotA.set_data(x1, y1)

##inner pinB:
inner_pinB, = ax.plot([0],[0],'b-')
dotB, = ax.plot([0],[0], 'bo', ms=5)
def update_inner_pinB(e,Rm, phi):
    global cycloid_fig   
    if cycloid_fig==3:  
        x = (Rm+e)*np.cos(t)-e*np.cos(phi-np.pi/3)
        y = (Rm+e)*np.sin(t)-e*np.sin(phi-np.pi/3)
    if cycloid_fig==2:  
        x = (Rm+e)*np.cos(t)-e*np.cos(phi)
        y = (Rm+e)*np.sin(t)-e*np.sin(phi)        
    inner_pinB.set_data(x,y)
    if cycloid_fig==3:      
        x1 = (Rm+e)*np.cos(phi+2*np.pi/3)-e*np.cos(phi-np.pi/3)
        y1 = (Rm+e)*np.sin(phi+2*np.pi/3)-e*np.sin(phi-np.pi/3)
    if cycloid_fig==2:      
        x1 = (Rm+e)*np.cos(phi+np.pi)-e*np.cos(phi)
        y1 = (Rm+e)*np.sin(phi+np.pi)-e*np.sin(phi)    
    dotB.set_data(x1, y1)


##inner pinC:
inner_pinC, = ax.plot([0],[0],'g-')
dotC, = ax.plot([0],[0], 'go', ms=5)
def update_inner_pinC(e,Rm, phi):
    x = (Rm+e)*np.cos(t)-e*np.cos(phi+np.pi/3)
    y = (Rm+e)*np.sin(t)-e*np.sin(phi+np.pi/3)
    inner_pinC.set_data(x,y)
    
    x1 = (Rm+e)*np.cos(phi-2*np.pi/3)-e*np.cos(phi+np.pi/3)
    y1 = (Rm+e)*np.sin(phi-2*np.pi/3)-e*np.sin(phi+np.pi/3)
    dotC.set_data(x1, y1)


##ehypocycloidA:
ehypocycloidA, = ax.plot([0], [0],'r-')
edotA, = ax.plot([0],[0], 'ro', ms=5)
def update_ehypocycloidA(lamuda,e,n,D,d, phis):
    global mode_fig    
    global curve_fig 
    if mode_fig == 1:
        if curve_fig == 0:
            RD=D/2
            rd=d/2
            rc = (n-1)*(RD/n)
            rm = (RD/n)
            xa = (rc+rm)*np.cos(t)-e*np.cos((rc+rm)/rm*t)
            ya = (rc+rm)*np.sin(t)-e*np.sin((rc+rm)/rm*t)

            dxa = (rc+rm)*(-np.sin(t)+(e/rm)*np.sin((rc+rm)/rm*t))
            dya = (rc+rm)*(np.cos(t)-(e/rm)*np.cos((rc+rm)/rm*t))        
            x = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.cos(-phis/(n-1))-(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.sin(-phis/(n-1))  + e*np.cos(phis)
            y = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.sin(-phis/(n-1))+(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.cos(-phis/(n-1))  + e*np.sin(phis)
            ehypocycloidA.set_data(x,y)
            edotA.set_data(x[0], y[0])   
        if curve_fig == 1:
            #lamuda = 0.9
            RD=D/2
            rd=d/2
            rc = (n-1)*(RD/n)
            rm = (RD/n)
            xa = (rc+rm)*np.cos(t)-e*lamuda*np.cos((rc+rm)/rm*t)-rd*(np.cos(t) - lamuda*np.cos((rc+rm)/rm*t))/np.sqrt(1 + lamuda**2 - 2*lamuda*np.cos(rc/rm*t)) 
            ya = (rc+rm)*np.sin(t)-e*lamuda*np.sin((rc+rm)/rm*t)-rd*(np.sin(t) - lamuda*np.sin((rc+rm)/rm*t))/np.sqrt(1 + lamuda**2 - 2*lamuda*np.cos(rc/rm*t))         
            
            x = (xa)*np.cos(-phis/(n-1))-(ya)*np.sin(-phis/(n-1))  + e*np.cos(phis)
            y = (xa)*np.sin(-phis/(n-1))+(ya)*np.cos(-phis/(n-1))  + e*np.sin(phis)
            ehypocycloidA.set_data(x,y)
            edotA.set_data(x[0], y[0])  

    if mode_fig == 0:
        if curve_fig == 0:
            RD=D/2
            rd=d/2
            rc = (n-1)*(RD/n)
            rm = (RD/n)
            xa = (rc+rm)*np.cos(t)-e*np.cos((rc+rm)/rm*t)
            ya = (rc+rm)*np.sin(t)-e*np.sin((rc+rm)/rm*t)

            dxa = (rc+rm)*(-np.sin(t)+(e/rm)*np.sin((rc+rm)/rm*t))
            dya = (rc+rm)*(np.cos(t)-(e/rm)*np.cos((rc+rm)/rm*t))          

            x = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))  + e*np.cos(phis)
            y = (ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)  + e*np.sin(phis)
            ehypocycloidA.set_data(x,y)
            edotA.set_data(x[0], y[0]) 
        if curve_fig == 1:
            #lamuda = 0.9
            RD=D/2
            rd=d/2
            rc = (n-1)*(RD/n)
            rm = (RD/n)
            xa = (rc+rm)*np.cos(t)-e*lamuda*np.cos((rc+rm)/rm*t)-rd*(np.cos(t) - lamuda*np.cos((rc+rm)/rm*t))/np.sqrt(1 + lamuda**2 - 2*lamuda*np.cos(rc/rm*t)) 
            ya = (rc+rm)*np.sin(t)-e*lamuda*np.sin((rc+rm)/rm*t)-rd*(np.sin(t) - lamuda*np.sin((rc+rm)/rm*t))/np.sqrt(1 + lamuda**2 - 2*lamuda*np.cos(rc/rm*t))           

            x = (xa)  + e*np.cos(phis)
            y = (ya)  + e*np.sin(phis)
            ehypocycloidA.set_data(x,y)
            edotA.set_data(x[0], y[0])     


##ehypocycloidB:
ehypocycloidB, = ax.plot([0],[0],'b-')
edotB, = ax.plot([0],[0], 'bo', ms=5)
def update_ehypocycloidB(lamuda,e,n,D,d, phis):
    global mode_fig
    global cycloid_fig
    global curve_fig

    if mode_fig == 1:
        if cycloid_fig == 3:
            if curve_fig == 0:
                RD=D/2
                rd=d/2
                rc = (n-1)*(RD/n)
                rm = (RD/n)
                xa = (rc+rm)*np.cos(t)+e*np.cos((rc+rm)/rm*t)
                ya = (rc+rm)*np.sin(t)+e*np.sin((rc+rm)/rm*t)

                dxa = (rc+rm)*(-np.sin(t)-(e/rm)*np.sin((rc+rm)/rm*t))
                dya = (rc+rm)*(np.cos(t)+(e/rm)*np.cos((rc+rm)/rm*t))                
                x = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.cos(-phis/(n-1) + np.pi/3/(n-1))-(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.sin(-phis/(n-1) + np.pi/3/(n-1))  - e*np.cos(phis-np.pi/3)
                y = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.sin(-phis/(n-1) + np.pi/3/(n-1))+(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.cos(-phis/(n-1) + np.pi/3/(n-1))  - e*np.sin(phis-np.pi/3)
                ehypocycloidB.set_data(x,y)
                edotB.set_data(x[0], y[0])  

            if curve_fig == 1:
                #lamuda = 0.9
                RD=D/2
                rd=d/2
                rc = (n-1)*(RD/n)
                rm = (RD/n)

                xa = (rc+rm)*np.cos(t)-e*lamuda*np.cos((rc+rm)/rm*t)-rd*(np.cos(t) - lamuda*np.cos((rc+rm)/rm*t))/np.sqrt(1 + lamuda**2 - 2*lamuda*np.cos(rc/rm*t)) 
                ya = (rc+rm)*np.sin(t)-e*lamuda*np.sin((rc+rm)/rm*t)-rd*(np.sin(t) - lamuda*np.sin((rc+rm)/rm*t))/np.sqrt(1 + lamuda**2 - 2*lamuda*np.cos(rc/rm*t))   


                x = (xa)*np.cos(-phis/(n-1) + np.pi/3/(n-1) + np.pi/(n-1))-(ya)*np.sin(-phis/(n-1) + np.pi/3/(n-1) + np.pi/(n-1))  - e*np.cos(phis-np.pi/3)
                y = (xa)*np.sin(-phis/(n-1) + np.pi/3/(n-1) + np.pi/(n-1))+(ya)*np.cos(-phis/(n-1) + np.pi/3/(n-1) + np.pi/(n-1))  - e*np.sin(phis-np.pi/3)
                ehypocycloidB.set_data(x,y)
                edotB.set_data(x[0], y[0])                  

        if cycloid_fig == 2:
            if curve_fig == 0:
                RD=D/2
                rd=d/2
                rc = (n-1)*(RD/n)
                rm = (RD/n)
                xa = (rc+rm)*np.cos(t)+e*np.cos((rc+rm)/rm*t)
                ya = (rc+rm)*np.sin(t)+e*np.sin((rc+rm)/rm*t)

                dxa = (rc+rm)*(-np.sin(t)-(e/rm)*np.sin((rc+rm)/rm*t))
                dya = (rc+rm)*(np.cos(t)+(e/rm)*np.cos((rc+rm)/rm*t)) 

                x = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.cos(-phis/(n-1) )-(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.sin(-phis/(n-1))  - e*np.cos(phis)
                y = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.sin(-phis/(n-1) )+(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.cos(-phis/(n-1))  - e*np.sin(phis)
                ehypocycloidB.set_data(x,y)
                edotB.set_data(x[0], y[0])       
    
            if curve_fig == 1:
                #lamuda = 0.9
                RD=D/2
                rd=d/2
                rc = (n-1)*(RD/n)
                rm = (RD/n)
                xa = (rc+rm)*np.cos(t)-e*lamuda*np.cos((rc+rm)/rm*t)-rd*(np.cos(t) - lamuda*np.cos((rc+rm)/rm*t))/np.sqrt(1 + lamuda**2 - 2*lamuda*np.cos(rc/rm*t)) 
                ya = (rc+rm)*np.sin(t)-e*lamuda*np.sin((rc+rm)/rm*t)-rd*(np.sin(t) - lamuda*np.sin((rc+rm)/rm*t))/np.sqrt(1 + lamuda**2 - 2*lamuda*np.cos(rc/rm*t))   

                #dxa = xa*np.cos(np.pi/(n-1)) - ya*np.sin(np.pi/(n-1))
                #dya = xa*np.sin(np.pi/(n-1)) + ya*np.cos(np.pi/(n-1))

                x = (xa)*np.cos(-phis/(n-1) + np.pi/(n-1))-(ya)*np.sin(-phis/(n-1) + np.pi/(n-1))  - e*np.cos(phis)
                y = (xa)*np.sin(-phis/(n-1) + np.pi/(n-1) )+(ya)*np.cos(-phis/(n-1) + np.pi/(n-1))  - e*np.sin(phis)
                ehypocycloidB.set_data(x,y)
                edotB.set_data(x[0], y[0])    
    if mode_fig == 0:
        if cycloid_fig == 3:   
            if curve_fig == 0:
                RD=D/2
                rd=d/2
                rc = (n-1)*(RD/n)
                rm = (RD/n)
                xa = (rc+rm)*np.cos(t)+e*np.cos((rc+rm)/rm*t)
                ya = (rc+rm)*np.sin(t)+e*np.sin((rc+rm)/rm*t)

                dxa = (rc+rm)*(-np.sin(t)-(e/rm)*np.sin((rc+rm)/rm*t))
                dya = (rc+rm)*(np.cos(t)+(e/rm)*np.cos((rc+rm)/rm*t)) 

                x = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.cos( np.pi/3/(n-1))-(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.sin( np.pi/3/(n-1))  - e*np.cos(phis-np.pi/3)
                y = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.sin( np.pi/3/(n-1))+(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.cos( np.pi/3/(n-1))  - e*np.sin(phis-np.pi/3)
                ehypocycloidB.set_data(x,y)
                edotB.set_data(x[0], y[0])   
            if curve_fig == 1:
                #lamuda = 0.9
                RD=D/2
                rd=d/2
                rc = (n-1)*(RD/n)
                rm = (RD/n)
                xa = (rc+rm)*np.cos(t)-e*lamuda*np.cos((rc+rm)/rm*t)-rd*(np.cos(t) - lamuda*np.cos((rc+rm)/rm*t))/np.sqrt(1 + lamuda**2 - 2*lamuda*np.cos(rc/rm*t)) 
                ya = (rc+rm)*np.sin(t)-e*lamuda*np.sin((rc+rm)/rm*t)-rd*(np.sin(t) - lamuda*np.sin((rc+rm)/rm*t))/np.sqrt(1 + lamuda**2 - 2*lamuda*np.cos(rc/rm*t))   


                x = (xa)*np.cos( np.pi/3/(n-1) + np.pi/(n-1))-(ya)*np.sin( np.pi/3/(n-1) + np.pi/(n-1))  - e*np.cos(phis-np.pi/3)
                y = (xa)*np.sin( np.pi/3/(n-1) + np.pi/(n-1))+(ya)*np.cos( np.pi/3/(n-1) + np.pi/(n-1))  - e*np.sin(phis-np.pi/3)
                ehypocycloidB.set_data(x,y)
                edotB.set_data(x[0], y[0])                         
        if cycloid_fig == 2:   
            if curve_fig == 0:
                RD=D/2
                rd=d/2
                rc = (n-1)*(RD/n)
                rm = (RD/n)
                xa = (rc+rm)*np.cos(t)+e*np.cos((rc+rm)/rm*t)
                ya = (rc+rm)*np.sin(t)+e*np.sin((rc+rm)/rm*t)

                dxa = (rc+rm)*(-np.sin(t)-(e/rm)*np.sin((rc+rm)/rm*t))
                dya = (rc+rm)*(np.cos(t)+(e/rm)*np.cos((rc+rm)/rm*t)) 



                x = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))  - e*np.cos(phis)
                y = (ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)  - e*np.sin(phis)
                ehypocycloidB.set_data(x,y)
                edotB.set_data(x[0], y[0])           
    
            if curve_fig == 1:
                #lamuda = 0.9
                RD=D/2
                rd=d/2
                rc = (n-1)*(RD/n)
                rm = (RD/n)
                xa = (rc+rm)*np.cos(t)-e*lamuda*np.cos((rc+rm)/rm*t)-rd*(np.cos(t) - lamuda*np.cos((rc+rm)/rm*t))/np.sqrt(1 + lamuda**2 - 2*lamuda*np.cos(rc/rm*t)) 
                ya = (rc+rm)*np.sin(t)-e*lamuda*np.sin((rc+rm)/rm*t)-rd*(np.sin(t) - lamuda*np.sin((rc+rm)/rm*t))/np.sqrt(1 + lamuda**2 - 2*lamuda*np.cos(rc/rm*t))   

                x = (xa)*np.cos(np.pi/(n-1))-(ya)*np.sin(np.pi/(n-1))  - e*np.cos(phis)
                y = (xa)*np.sin(np.pi/(n-1))+(ya)*np.cos(np.pi/(n-1))  - e*np.sin(phis)
                ehypocycloidB.set_data(x,y)
                edotB.set_data(x[0], y[0])  


##ehypocycloidC:
ehypocycloidC, = ax.plot([0],[0],'g-')
edotC, = ax.plot([0],[0], 'go', ms=5)
def update_ehypocycloidC(lamuda,e,n,D,d, phis):
    global mode_fig
    global curve_fig
    if mode_fig == 1:
        if curve_fig == 0:
            RD=D/2
            rd=d/2
            rc = (n-1)*(RD/n)
            rm = (RD/n)
            xa = (rc+rm)*np.cos(t)+e*np.cos((rc+rm)/rm*t)
            ya = (rc+rm)*np.sin(t)+e*np.sin((rc+rm)/rm*t)

            dxa = (rc+rm)*(-np.sin(t)-(e/rm)*np.sin((rc+rm)/rm*t))
            dya = (rc+rm)*(np.cos(t)+(e/rm)*np.cos((rc+rm)/rm*t))

            x = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.cos(-phis/(n-1) - np.pi/3/(n-1))-(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.sin(-phis/(n-1) - np.pi/3/(n-1))  - e*np.cos(phis+np.pi/3)
            y = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.sin(-phis/(n-1) - np.pi/3/(n-1))+(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.cos(-phis/(n-1) - np.pi/3/(n-1))  - e*np.sin(phis+np.pi/3)
            
            ehypocycloidC.set_data(x,y)
            edotC.set_data(x[0], y[0])   

        if curve_fig == 1:
            #lamuda = 0.9
            RD=D/2
            rd=d/2
            rc = (n-1)*(RD/n)
            rm = (RD/n)

            xa = (rc+rm)*np.cos(t)-e*lamuda*np.cos((rc+rm)/rm*t)-rd*(np.cos(t) - lamuda*np.cos((rc+rm)/rm*t))/np.sqrt(1 + lamuda**2 - 2*lamuda*np.cos(rc/rm*t)) 
            ya = (rc+rm)*np.sin(t)-e*lamuda*np.sin((rc+rm)/rm*t)-rd*(np.sin(t) - lamuda*np.sin((rc+rm)/rm*t))/np.sqrt(1 + lamuda**2 - 2*lamuda*np.cos(rc/rm*t))   


            x = (xa)*np.cos(-phis/(n-1) - np.pi/3/(n-1) + np.pi/(n-1))-(ya)*np.sin(-phis/(n-1) - np.pi/3/(n-1) + np.pi/(n-1))  - e*np.cos(phis+np.pi/3)
            y = (xa)*np.sin(-phis/(n-1) - np.pi/3/(n-1) + np.pi/(n-1))+(ya)*np.cos(-phis/(n-1) - np.pi/3/(n-1) + np.pi/(n-1))  - e*np.sin(phis+np.pi/3)
            
            ehypocycloidC.set_data(x,y)
            edotC.set_data(x[0], y[0]) 

    if mode_fig == 0:  
        if curve_fig == 0:
            RD=D/2
            rd=d/2
            rc = (n-1)*(RD/n)
            rm = (RD/n)
            xa = (rc+rm)*np.cos(t)+e*np.cos((rc+rm)/rm*t)
            ya = (rc+rm)*np.sin(t)+e*np.sin((rc+rm)/rm*t)

            dxa = (rc+rm)*(-np.sin(t)-(e/rm)*np.sin((rc+rm)/rm*t))
            dya = (rc+rm)*(np.cos(t)+(e/rm)*np.cos((rc+rm)/rm*t))                  
            x = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.cos( - np.pi/3/(n-1))-(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.sin( - np.pi/3/(n-1))  - e*np.cos(phis+np.pi/3)
            y = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.sin( - np.pi/3/(n-1))+(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.cos( - np.pi/3/(n-1))  - e*np.sin(phis+np.pi/3)
     
            ehypocycloidC.set_data(x,y)
            edotC.set_data(x[0], y[0])   
        if curve_fig == 1:
            #lamuda = 0.9
            RD=D/2
            rd=d/2
            rc = (n-1)*(RD/n)
            rm = (RD/n)

            xa = (rc+rm)*np.cos(t)-e*lamuda*np.cos((rc+rm)/rm*t)-rd*(np.cos(t) - lamuda*np.cos((rc+rm)/rm*t))/np.sqrt(1 + lamuda**2 - 2*lamuda*np.cos(rc/rm*t)) 
            ya = (rc+rm)*np.sin(t)-e*lamuda*np.sin((rc+rm)/rm*t)-rd*(np.sin(t) - lamuda*np.sin((rc+rm)/rm*t))/np.sqrt(1 + lamuda**2 - 2*lamuda*np.cos(rc/rm*t))   
                
            x = (xa)*np.cos( - np.pi/3/(n-1) + np.pi/(n-1))-(ya)*np.sin( - np.pi/3/(n-1) + np.pi/(n-1))  - e*np.cos(phis+np.pi/3)
            y = (xa)*np.sin( - np.pi/3/(n-1) + np.pi/(n-1))+(ya)*np.cos( - np.pi/3/(n-1) + np.pi/(n-1))  - e*np.sin(phis+np.pi/3)
     
            ehypocycloidC.set_data(x,y)
            edotC.set_data(x[0], y[0])  


##ehypocycloid_Pin:
ehypocycloid_Pin, = ax.plot([0],[0],'k-')
edot_Pin, = ax.plot([0],[0], 'ko', ms=5)
def update_ehypocycloid_Pin(lamuda,e,n,D,d, phis):
    global mode_fig
    global curve_fig
    if mode_fig == 1:
        if curve_fig == 0:
            RD=D/2
            rd=d/2
            rc = (n)*(RD/(n+1))
            rm = (RD/(n+1))
            xa = (rc+rm)*np.cos(t)+e*np.cos((rc+rm)/rm*t)
            ya = (rc+rm)*np.sin(t)+e*np.sin((rc+rm)/rm*t)

            dxa = (rc+rm)*(-np.sin(t)-(e/rm)*np.sin((rc+rm)/rm*t))
            dya = (rc+rm)*(np.cos(t)+(e/rm)*np.cos((rc+rm)/rm*t))            
            x = (xa + (rd-e)/np.sqrt(dxa**2 + dya**2)*(-dya))*np.cos( np.pi/(n)) - (ya + (rd-e)/np.sqrt(dxa**2 + dya**2)*dxa)*np.sin( np.pi/(n)) 
            y = (xa + (rd-e)/np.sqrt(dxa**2 + dya**2)*(-dya))*np.sin( np.pi/(n)) + (ya + (rd-e)/np.sqrt(dxa**2 + dya**2)*dxa)*np.cos( np.pi/(n))
            
        if curve_fig == 1:
            #lamuda = 0.9
            RD=D/2
            rd=d/2
            rc = (n)*(RD/(n+1))
            rm = (RD/(n+1))
            xa = (rc+rm)*np.cos(t)-e*lamuda*np.cos((rc+rm)/rm*t)-(rd-e)*(np.cos(t) - lamuda*np.cos((rc+rm)/rm*t))/np.sqrt(1 + lamuda**2 - 2*lamuda*np.cos(rc/rm*t)) 
            ya = (rc+rm)*np.sin(t)-e*lamuda*np.sin((rc+rm)/rm*t)-(rd-e)*(np.sin(t) - lamuda*np.sin((rc+rm)/rm*t))/np.sqrt(1 + lamuda**2 - 2*lamuda*np.cos(rc/rm*t)) 

            x = (xa)
            y = (ya)

    if mode_fig == 0: 
        if curve_fig == 0:  
            RD=D/2
            rd=d/2
            rc = (n)*(RD/(n+1))
            rm = (RD/(n+1))
            xa = (rc+rm)*np.cos(t)+e*np.cos((rc+rm)/rm*t)
            ya = (rc+rm)*np.sin(t)+e*np.sin((rc+rm)/rm*t)

            dxa = (rc+rm)*(-np.sin(t)-(e/rm)*np.sin((rc+rm)/rm*t))
            dya = (rc+rm)*(np.cos(t)+(e/rm)*np.cos((rc+rm)/rm*t))               

            x = (xa + (rd-e)/np.sqrt(dxa**2 + dya**2)*(-dya))*np.cos(phis/(n) + np.pi/(n))-(ya + (rd-e)/np.sqrt(dxa**2 + dya**2)*dxa)*np.sin(phis/(n) + np.pi/(n)) 
            y = (xa + (rd-e)/np.sqrt(dxa**2 + dya**2)*(-dya))*np.sin(phis/(n) + np.pi/(n))+(ya + (rd-e)/np.sqrt(dxa**2 + dya**2)*dxa)*np.cos(phis/(n) + np.pi/(n)) 
        if curve_fig == 1:
            #lamuda = 0.9
            RD=D/2
            rd=d/2
            rc = (n)*(RD/(n+1))
            rm = (RD/(n+1))
            xa = (rc+rm)*np.cos(t)-e*lamuda*np.cos((rc+rm)/rm*t)-(rd-e)*(np.cos(t) - lamuda*np.cos((rc+rm)/rm*t))/np.sqrt(1 + lamuda**2 - 2*lamuda*np.cos(rc/rm*t)) 
            ya = (rc+rm)*np.sin(t)-e*lamuda*np.sin((rc+rm)/rm*t)-(rd-e)*(np.sin(t) - lamuda*np.sin((rc+rm)/rm*t))/np.sqrt(1 + lamuda**2 - 2*lamuda*np.cos(rc/rm*t)) 

            x = (xa)*np.cos(phis/(n))-(ya)*np.sin(phis/(n)) 
            y = (xa)*np.sin(phis/(n))+(ya)*np.cos(phis/(n))    
    
    ehypocycloid_Pin.set_data(x,y)
    edot_Pin.set_data(x[0], y[0])


axcolor = 'lightgoldenrodyellow'
ax_la = plt.axes([0.25, 0.20, 0.5, 0.015], facecolor=axcolor)
ax_fm = plt.axes([0.25, 0.18, 0.5, 0.015], facecolor=axcolor)
ax_Rm = plt.axes([0.25, 0.16, 0.5, 0.015], facecolor=axcolor)
ax_n = plt.axes([0.25, 0.14, 0.5, 0.015], facecolor=axcolor)
ax_Rd = plt.axes([0.25, 0.12, 0.5, 0.015], facecolor=axcolor)
ax_rd = plt.axes([0.25, 0.10, 0.5, 0.015], facecolor=axcolor)
ax_e = plt.axes([0.25, 0.08, 0.5, 0.015], facecolor=axcolor)
ax_N = plt.axes([0.25, 0.06, 0.5, 0.015], facecolor=axcolor)
ax_d = plt.axes([0.25, 0.04, 0.5, 0.015], facecolor=axcolor)
ax_D = plt.axes([0.25, 0.02, 0.5, 0.015], facecolor=axcolor)

sli_la = Slider(ax_la, 'la', 0.8, 0.98, valinit=0.90, valstep=delta/100)
sli_fm = Slider(ax_fm, 'fm', -100, 100, valinit=100, valstep=delta*20)
sli_Rm = Slider(ax_Rm, 'Rm', 1, 10, valinit=5, valstep=delta)
sli_n = Slider(ax_n, 'n', 2, 10, valinit=6, valstep=delta)
sli_Rd = Slider(ax_Rd, 'Rd', 1, 40, valinit=20, valstep=delta)
sli_rd = Slider(ax_rd, 'rd', 1, 10, valinit=5, valstep=delta)
sli_e = Slider(ax_e, 'e', 0.1, 10, valinit=2, valstep=delta/10)
sli_N = Slider(ax_N, 'N', 2, 40, valinit=10, valstep=delta)
sli_d = Slider(ax_d, 'd', 2, 20, valinit=10,valstep=delta)
sli_D = Slider(ax_D, 'D', 5, 150, valinit=80,valstep=delta)

def update(val):
    lamuda = sli_la.val
    sfm = sli_Rm.val
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


sli_la.on_changed(update)
sli_fm.on_changed(update)
sli_Rm.on_changed(update)
sli_Rd.on_changed(update)
sli_n.on_changed(update)
sli_rd.on_changed(update)
sli_e.on_changed(update)
sli_N.on_changed(update)
sli_d.on_changed(update)
sli_D.on_changed(update)

resetax = plt.axes([0.85, 0.001, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')
rax = plt.axes([0.025, 0.60, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('Motion_1', 'Motion_2'), active=0)
rax_1 = plt.axes([0.025, 0.40, 0.15, 0.15], facecolor=axcolor)
radio_1 = RadioButtons(rax_1, ('Pin', 'NonePin'), active=0)
rax_2 = plt.axes([0.025, 0.20, 0.15, 0.15], facecolor=axcolor)
radio_2 = RadioButtons(rax_2, ('Single', 'Dual', 'Triple'), active=0)

rax_3 = plt.axes([0.025, 0.80, 0.15, 0.15], facecolor=axcolor)
radio_3 = RadioButtons(rax_3, ('Curve_1', 'Curve_2'), active=0)

def reset(event):

    sli_la.reset()
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

def modefunc(label):
    global mode_fig
    if label == 'Motion_1':        
        mode_fig = 0
    if label == 'Motion_2':
        mode_fig = 1
radio.on_clicked(modefunc)

def pin_modefunc(label):
    global pin_fig
    if label == 'Pin':        
        pin_fig = 0
    if label == 'NonePin':
        pin_fig = 1
radio_1.on_clicked(pin_modefunc)

def cycloid_modefunc(label):
    global cycloid_fig
    if label == 'Single':        
        cycloid_fig = 1
    if label == 'Dual':
        cycloid_fig = 2
    if label == 'Triple':
        cycloid_fig = 3        
radio_2.on_clicked(cycloid_modefunc)

def curve_modefunc(label):
    global curve_fig
    if label == 'Curve_1':        
        curve_fig = 0
    if label == 'Curve_2':
        curve_fig = 1
radio_3.on_clicked(curve_modefunc)

def animate(frame):
    global pin_fig
    global cycloid_fig 
    global curve_fig 
    sla = sli_la.val
    sfm = sli_fm.val
    sRm = sli_Rm.val
    sRd = sli_Rd.val
    sn = sli_n.val
    srd = sli_rd.val    
    se = sli_e.val
    sN = sli_N.val
    sd = sli_d.val
    sD = sli_D.val

    if curve_fig == 0:
        ax_la.set_visible(0) 
    if curve_fig == 1:    
        ax_la.set_visible(1) 

    if sfm == 0:
        phi = 0
    if sfm != 0:    
        phi = 2*np.pi*frame/sfm
        frame = frame+1

    draw_pin_init()
    draw_inner_pin_init()
    draw_inner_circleA_init()
    draw_inner_circleB_init()
    draw_inner_circleC_init()
    #ehypocycloid_Pin_init()    

    if pin_fig == 0:    
        pin_update(sN,sd,sD,phi)
        ehypocycloid_Pin.set_visible(0)
        edot_Pin.set_visible(0)
    if pin_fig == 1:     
        ehypocycloid_Pin.set_visible(1)    
        edot_Pin.set_visible(1) 
        update_ehypocycloid_Pin(sla,se,sN,sD,sd, phi)


    inner_pin_update(sn,sN,srd,sRd,phi)    
    #inner_pin_update(sn,sN,srd,sRd,0)
    drive_pin_update(sRm)

    inner_pinB.set_visible(1)
    dotB.set_visible(1)        
    inner_pinC.set_visible(1)
    dotC.set_visible(1)
    ehypocycloidB.set_visible(1)
    ehypocycloidC.set_visible(1)
    edotB.set_visible(1)
    edotC.set_visible(1)

    if cycloid_fig == 3:      
        update_inner_pinA(se,sRm, phi)
        update_inner_pinB(se,sRm, phi)
        update_inner_pinC(se,sRm, phi)   
        update_inner_circleA(se,sn,sN,srd,sRd, phi)
        update_inner_circleB(se,sn,sN,srd,sRd, phi)
        update_inner_circleC(se,sn,sN,srd,sRd, phi)    
        update_ehypocycloidA(sla,se,sN,sD,sd, phi)
        update_ehypocycloidB(sla,se,sN,sD,sd, phi)
        update_ehypocycloidC(sla,se,sN,sD,sd, phi)


    if cycloid_fig == 2:          
        update_inner_pinA(se,sRm, phi)
        update_inner_pinB(se,sRm, phi)   
        update_inner_circleA(se,sn,sN,srd,sRd, phi)
        update_inner_circleB(se,sn,sN,srd,sRd, phi)  
        update_ehypocycloidA(sla,se,sN,sD,sd, phi)
        update_ehypocycloidB(sla,se,sN,sD,sd, phi)
        edotC.set_visible(0)         
        inner_pinC.set_visible(0)
        dotC.set_visible(0)
        ehypocycloidC.set_visible(0)
        edotC.set_visible(0)        
    if cycloid_fig == 1:          
        update_inner_pinA(se,sRm, phi)
        update_inner_circleA(se,sn,sN,srd,sRd, phi)
        update_ehypocycloidA(sla,se,sN,sD,sd, phi)
        inner_pinB.set_visible(0)
        dotB.set_visible(0)        
        inner_pinC.set_visible(0)
        dotC.set_visible(0)
        ehypocycloidB.set_visible(0)
        ehypocycloidC.set_visible(0)
        edotB.set_visible(0)
        edotC.set_visible(0)
    fig.canvas.draw_idle()



ani = animation.FuncAnimation(fig, animate,frames=sli_fm.val*(sli_N.val-1), interval=150)
dpi=100
plt.show()
