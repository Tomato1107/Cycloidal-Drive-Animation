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
l0, = ax.plot([], [], 'k-')
l1, = ax.plot([], [], 'k-')
l2, = ax.plot([], [], 'k-')
l3, = ax.plot([], [], 'k-')        
l4, = ax.plot([], [], 'k-')
l5, = ax.plot([], [], 'k-')
l6, = ax.plot([], [], 'k-')
l7, = ax.plot([], [], 'k-' ) 
l8, = ax.plot([], [], 'k-' )
l9, = ax.plot([], [], 'k-' )
l10, = ax.plot([], [], 'k-' ) 
l11, = ax.plot([], [], 'k-' )
l12, = ax.plot([], [], 'k-' )
l13, = ax.plot([], [], 'k-' )        
l14, = ax.plot([], [], 'k-' )
l15, = ax.plot([], [], 'k-' )
l16, = ax.plot([], [], 'k-' )
l17, = ax.plot([], [], 'k-' ) 
l18, = ax.plot([], [], 'k-' )
l19, = ax.plot([], [], 'k-' )
l20, = ax.plot([], [], 'k-' ) 
l21, = ax.plot([], [], 'k-' )
l22, = ax.plot([], [], 'k-' )
l23, = ax.plot([], [], 'k-' )        
l24, = ax.plot([], [], 'k-' )
l25, = ax.plot([], [], 'k-' )
l26, = ax.plot([], [], 'k-' )
l27, = ax.plot([], [], 'k-' ) 
l28, = ax.plot([], [], 'k-' )
l29, = ax.plot([], [], 'k-' )
l30, = ax.plot([], [], 'k-' ) 
l31, = ax.plot([], [], 'k-' )
l32, = ax.plot([], [], 'k-' )
l33, = ax.plot([], [], 'k-' )        
l34, = ax.plot([], [], 'k-' )
l35, = ax.plot([], [], 'k-' )
l36, = ax.plot([], [], 'k-' )
l37, = ax.plot([], [], 'k-' ) 
l38, = ax.plot([], [], 'k-' )
l39, = ax.plot([], [], 'k-' )
l40, = ax.plot([], [], 'k-' ) 
l41, = ax.plot([], [], 'k-' )
l42, = ax.plot([], [], 'k-' )
l43, = ax.plot([], [], 'k-' )        
l44, = ax.plot([], [], 'k-' )
l45, = ax.plot([], [], 'k-' )
l46, = ax.plot([], [], 'k-' )
l47, = ax.plot([], [], 'k-' ) 
l48, = ax.plot([], [], 'k-' )
l49, = ax.plot([], [], 'k-' )
l50, = ax.plot([], [], 'k-' ) 
l51, = ax.plot([], [], 'k-' )
l52, = ax.plot([], [], 'k-' )
l53, = ax.plot([], [], 'k-' )        
l54, = ax.plot([], [], 'k-' )
l55, = ax.plot([], [], 'k-' )
l56, = ax.plot([], [], 'k-' )
l57, = ax.plot([], [], 'k-' ) 
l58, = ax.plot([], [], 'k-' )
l59, = ax.plot([], [], 'k-' )
l60, = ax.plot([], [], 'k-' ) 

def draw_pin_init():
    l0.set_data([0], [0])
    l1.set_data([0], [0])
    l2.set_data([0], [0])  
    l3.set_data([0], [0])
    l4.set_data([0], [0])
    l5.set_data([0], [0])
    l6.set_data([0], [0])
    l7.set_data([0], [0])
    l8.set_data([0], [0])
    l9.set_data([0], [0])
    l10.set_data([0], [0])
    l11.set_data([0], [0])
    l12.set_data([0], [0])  
    l13.set_data([0], [0])
    l14.set_data([0], [0])
    l15.set_data([0], [0])
    l16.set_data([0], [0])
    l17.set_data([0], [0])
    l18.set_data([0], [0])
    l19.set_data([0], [0])
    l20.set_data([0], [0])
    l21.set_data([0], [0])
    l22.set_data([0], [0])  
    l23.set_data([0], [0])
    l24.set_data([0], [0])
    l25.set_data([0], [0])
    l26.set_data([0], [0])
    l27.set_data([0], [0])
    l28.set_data([0], [0])
    l29.set_data([0], [0])
    l30.set_data([0], [0])
    l31.set_data([0], [0])
    l32.set_data([0], [0])  
    l33.set_data([0], [0])
    l34.set_data([0], [0])
    l35.set_data([0], [0])
    l36.set_data([0], [0])
    l37.set_data([0], [0])
    l38.set_data([0], [0])
    l39.set_data([0], [0])
    l40.set_data([0], [0])
    l41.set_data([0], [0])
    l42.set_data([0], [0])  
    l43.set_data([0], [0])
    l44.set_data([0], [0])
    l45.set_data([0], [0])
    l46.set_data([0], [0])
    l47.set_data([0], [0])
    l48.set_data([0], [0])
    l49.set_data([0], [0])
    l50.set_data([0], [0])
    l51.set_data([0], [0])
    l52.set_data([0], [0])  
    l53.set_data([0], [0])
    l54.set_data([0], [0])
    l55.set_data([0], [0])
    l56.set_data([0], [0])
    l57.set_data([0], [0])
    l58.set_data([0], [0])
    l59.set_data([0], [0])
    l60.set_data([0], [0])


def pin_update(n,d,D):
    for i in range(int(n)):    
        x = (d/2*np.sin(t)+ D/2*np.cos(2*i*np.pi/n))
        y = (d/2*np.cos(t) + D/2*np.sin(2*i*np.pi/n))
        if i == 0:
            l0.set_data(x,y)
        if i == 1:
            l1.set_data(x,y)
        if i == 2:
            l2.set_data(x,y)
        if i == 3:
            l3.set_data(x,y)        
        if i == 4:
            l4.set_data(x,y)
        if i == 5:
            l5.set_data(x,y)
        if i == 6:
            l6.set_data(x,y)
        if i == 7:
            l7.set_data(x,y)  
        if i == 8:
            l8.set_data(x,y)
        if i == 9:
            l9.set_data(x,y)
        if i == 10:
            l10.set_data(x,y)
        if i == 11:
            l11.set_data(x,y)
        if i == 12:
            l12.set_data(x,y)           
        if i == 13:
            l13.set_data(x,y)        
        if i == 14:
            l14.set_data(x,y)
        if i == 15:
            l15.set_data(x,y)
        if i == 16:
            l16.set_data(x,y)
        if i == 17:
            l17.set_data(x,y)
        if i == 18:
            l18.set_data(x,y)
        if i == 19:
            l19.set_data(x,y)
        if i == 20:
            l20.set_data(x,y)
        if i == 21:
            l21.set_data(x,y)
        if i == 22:
            l22.set_data(x,y)
        if i == 23:
            l23.set_data(x,y)        
        if i == 24:
            l24.set_data(x,y)
        if i == 25:
            l25.set_data(x,y)
        if i == 26:
            l26.set_data(x,y)
        if i == 27:
            l27.set_data(x,y)  
        if i == 28:
            l28.set_data(x,y)
        if i == 29:
            l29.set_data(x,y)
        if i == 30:
            l30.set_data(x,y)
        if i == 31:
            l31.set_data(x,y)
        if i == 32:
            l32.set_data(x,y)           
        if i == 33:
            l33.set_data(x,y)        
        if i == 34:
            l34.set_data(x,y)
        if i == 35:
            l35.set_data(x,y)
        if i == 36:
            l36.set_data(x,y)
        if i == 37:
            l37.set_data(x,y)
        if i == 38:
            l38.set_data(x,y)
        if i == 39:
            l39.set_data(x,y)
        if i == 40:
            l40.set_data(x,y)
        if i == 41:
            l41.set_data(x,y)
        if i == 42:
            l42.set_data(x,y)
        if i == 43:
            l43.set_data(x,y)        
        if i == 44:
            l44.set_data(x,y)
        if i == 45:
            l45.set_data(x,y)
        if i == 46:
            l46.set_data(x,y)
        if i == 47:
            l47.set_data(x,y)  
        if i == 48:
            l48.set_data(x,y)
        if i == 49:
            l49.set_data(x,y)
        if i == 50:
            l50.set_data(x,y)
        if i == 51:
            l51.set_data(x,y)
        if i == 52:
            l52.set_data(x,y)           
        if i == 53:
            l53.set_data(x,y)        
        if i == 54:
            l54.set_data(x,y)
        if i == 55:
            l55.set_data(x,y)
        if i == 56:
            l56.set_data(x,y)
        if i == 57:
            l57.set_data(x,y)
        if i == 58:
            l58.set_data(x,y)
        if i == 59:
            l59.set_data(x,y)
        if i == 60:
            l60.set_data(x,y)
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
p0, = ax.plot([], [], 'g-')
p1, = ax.plot([], [], 'g-')
p2, = ax.plot([], [], 'g-')
p3, = ax.plot([], [], 'g-')        
p4, = ax.plot([], [], 'g-')
p5, = ax.plot([], [], 'g-')
p6, = ax.plot([], [], 'g-')
p7, = ax.plot([], [], 'g-') 
p8, = ax.plot([], [], 'g-')
p9, = ax.plot([], [], 'g-')

def draw_inner_pin_init():
    p0.set_data([0], [0])
    p1.set_data([0], [0])
    p2.set_data([0], [0])  
    p3.set_data([0], [0])
    p4.set_data([0], [0])
    p5.set_data([0], [0])
    p6.set_data([0], [0])
    p7.set_data([0], [0])
    p8.set_data([0], [0])
    p9.set_data([0], [0])


def inner_pin_update(n,N,rd,Rd,phi):
    num = (N-2)/2
    for i in range(int(n)):    
        x = (rd*np.sin(t)+ Rd*np.cos(2*i*np.pi/n))*np.cos(-phi/(num)) - (rd*np.cos(t) + Rd*np.sin(2*i*np.pi/n))*np.sin(-phi/(num))
        y = (rd*np.sin(t)+ Rd*np.cos(2*i*np.pi/n))*np.sin(-phi/(num)) + (rd*np.cos(t) + Rd*np.sin(2*i*np.pi/n))*np.cos(-phi/(num))
        if i == 0:
            p0.set_data(x,y)
        if i == 1:
            p1.set_data(x,y)
        if i == 2:
            p2.set_data(x,y)
        if i == 3:
            p3.set_data(x,y)        
        if i == 4:
            p4.set_data(x,y)
        if i == 5:
            p5.set_data(x,y)
        if i == 6:
            p6.set_data(x,y)
        if i == 7:
            p7.set_data(x,y)  
        if i == 8:
            p8.set_data(x,y)
        if i == 9:
            p9.set_data(x,y)

#inner circle:
inner_circle1, = ax.plot([], [], 'r-')
inner_circle2, = ax.plot([], [], 'r-')
inner_circle3, = ax.plot([], [], 'r-')
inner_circle4, = ax.plot([], [], 'r-')        
inner_circle5, = ax.plot([], [], 'r-')
inner_circle6, = ax.plot([], [], 'r-')
inner_circle7, = ax.plot([], [], 'r-')
inner_circle8, = ax.plot([], [], 'r-') 
inner_circle9, = ax.plot([], [], 'r-')
inner_circle10, = ax.plot([], [], 'r-')

def draw_inner_circle_init():
    inner_circle10.set_data([0], [0])
    inner_circle1.set_data([0], [0])
    inner_circle2.set_data([0], [0])  
    inner_circle3.set_data([0], [0])
    inner_circle4.set_data([0], [0])
    inner_circle5.set_data([0], [0])
    inner_circle6.set_data([0], [0])
    inner_circle7.set_data([0], [0])
    inner_circle8.set_data([0], [0])
    inner_circle9.set_data([0], [0])

def update_inner_circle(e,n,N,rd,Rd, phi):
    num = (N-2)/2
    for i in range(int(n)):
        x = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.cos(-phi/(num)) - ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.sin(-phi/(num)) + e*np.cos(phi)
        y = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.sin(-phi/(num)) + ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.cos(-phi/(num)) + e*np.sin(phi)
        if i==0:
            inner_circle1.set_data(x,y)
        if i==1:
            inner_circle2.set_data(x,y)
        if i==2:
            inner_circle3.set_data(x,y)
        if i==3:
            inner_circle4.set_data(x,y)
        if i==4:
            inner_circle5.set_data(x,y)
        if i==5:
            inner_circle6.set_data(x,y)
        if i==6:
            inner_circle7.set_data(x,y)
        if i==7:
            inner_circle8.set_data(x,y)
        if i==8:
            inner_circle9.set_data(x,y)
        if i==9:
            inner_circle10.set_data(x,y)

##ehypocycloidA:
ehypocycloidA0, = ax.plot([0],[0],'r-')
ehypocycloidA1, = ax.plot([0],[0],'r-')
ehypocycloidA2, = ax.plot([0],[0],'r-')
ehypocycloidA3, = ax.plot([0],[0],'r-')
ehypocycloidA4, = ax.plot([0],[0],'r-')
ehypocycloidA5, = ax.plot([0],[0],'r-')
ehypocycloidA6, = ax.plot([0],[0],'r-')
ehypocycloidA7, = ax.plot([0],[0],'r-')
ehypocycloidA8, = ax.plot([0],[0],'r-')
ehypocycloidA9, = ax.plot([0],[0],'r-')
ehypocycloidA10, = ax.plot([0],[0],'r-')
ehypocycloidA11, = ax.plot([0],[0],'r-')
ehypocycloidA12, = ax.plot([0],[0],'r-')
ehypocycloidA13, = ax.plot([0],[0],'r-')
ehypocycloidA14, = ax.plot([0],[0],'r-')
ehypocycloidA15, = ax.plot([0],[0],'r-')
ehypocycloidA16, = ax.plot([0],[0],'r-')
ehypocycloidA17, = ax.plot([0],[0],'r-')
ehypocycloidA18, = ax.plot([0],[0],'r-')
ehypocycloidA19, = ax.plot([0],[0],'r-')
ehypocycloidA20, = ax.plot([0],[0],'r-')
ehypocycloidA21, = ax.plot([0],[0],'r-')
ehypocycloidA22, = ax.plot([0],[0],'r-')
ehypocycloidA23, = ax.plot([0],[0],'r-')
ehypocycloidA24, = ax.plot([0],[0],'r-')
ehypocycloidA25, = ax.plot([0],[0],'r-')
ehypocycloidA26, = ax.plot([0],[0],'r-')
ehypocycloidA27, = ax.plot([0],[0],'r-')
ehypocycloidA28, = ax.plot([0],[0],'r-')
ehypocycloidA29, = ax.plot([0],[0],'r-')
ehypocycloidA30, = ax.plot([0],[0],'r-')
ehypocycloidA31, = ax.plot([0],[0],'r-')
ehypocycloidA32, = ax.plot([0],[0],'r-')
ehypocycloidA33, = ax.plot([0],[0],'r-')
ehypocycloidA34, = ax.plot([0],[0],'r-')
ehypocycloidA35, = ax.plot([0],[0],'r-')
ehypocycloidA36, = ax.plot([0],[0],'r-')
ehypocycloidA37, = ax.plot([0],[0],'r-')
ehypocycloidA38, = ax.plot([0],[0],'r-')
ehypocycloidA39, = ax.plot([0],[0],'r-')
ehypocycloidA40, = ax.plot([0],[0],'r-')
ehypocycloidA41, = ax.plot([0],[0],'r-')
ehypocycloidA42, = ax.plot([0],[0],'r-')
ehypocycloidA43, = ax.plot([0],[0],'r-')
ehypocycloidA44, = ax.plot([0],[0],'r-')
ehypocycloidA45, = ax.plot([0],[0],'r-')
ehypocycloidA46, = ax.plot([0],[0],'r-')
ehypocycloidA47, = ax.plot([0],[0],'r-')
ehypocycloidA48, = ax.plot([0],[0],'r-')
ehypocycloidA49, = ax.plot([0],[0],'r-')
ehypocycloidA50, = ax.plot([0],[0],'r-')

def ehypocycloidA_init():
    ehypocycloidA0.set_data([0], [0])
    ehypocycloidA1.set_data([0], [0])
    ehypocycloidA2.set_data([0], [0])  
    ehypocycloidA3.set_data([0], [0])
    ehypocycloidA4.set_data([0], [0])
    ehypocycloidA5.set_data([0], [0])
    ehypocycloidA6.set_data([0], [0])
    ehypocycloidA7.set_data([0], [0])
    ehypocycloidA8.set_data([0], [0])
    ehypocycloidA9.set_data([0], [0])
    ehypocycloidA10.set_data([0], [0])
    ehypocycloidA11.set_data([0], [0])
    ehypocycloidA12.set_data([0], [0])  
    ehypocycloidA13.set_data([0], [0])
    ehypocycloidA14.set_data([0], [0])
    ehypocycloidA15.set_data([0], [0])
    ehypocycloidA16.set_data([0], [0])
    ehypocycloidA17.set_data([0], [0])
    ehypocycloidA18.set_data([0], [0])
    ehypocycloidA19.set_data([0], [0])
    ehypocycloidA20.set_data([0], [0])
    ehypocycloidA21.set_data([0], [0])
    ehypocycloidA22.set_data([0], [0])  
    ehypocycloidA23.set_data([0], [0])
    ehypocycloidA24.set_data([0], [0])
    ehypocycloidA25.set_data([0], [0])
    ehypocycloidA26.set_data([0], [0])
    ehypocycloidA27.set_data([0], [0])
    ehypocycloidA28.set_data([0], [0])
    ehypocycloidA29.set_data([0], [0])
    ehypocycloidA30.set_data([0], [0])
    ehypocycloidA31.set_data([0], [0])
    ehypocycloidA32.set_data([0], [0])  
    ehypocycloidA33.set_data([0], [0])
    ehypocycloidA34.set_data([0], [0])
    ehypocycloidA35.set_data([0], [0])
    ehypocycloidA36.set_data([0], [0])
    ehypocycloidA37.set_data([0], [0])
    ehypocycloidA38.set_data([0], [0])
    ehypocycloidA39.set_data([0], [0])
    ehypocycloidA40.set_data([0], [0])  
    ehypocycloidA41.set_data([0], [0])
    ehypocycloidA42.set_data([0], [0])  
    ehypocycloidA43.set_data([0], [0])
    ehypocycloidA44.set_data([0], [0])
    ehypocycloidA45.set_data([0], [0])
    ehypocycloidA46.set_data([0], [0])
    ehypocycloidA47.set_data([0], [0])
    ehypocycloidA48.set_data([0], [0])
    ehypocycloidA49.set_data([0], [0])
    ehypocycloidA50.set_data([0], [0])



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
            ehypocycloidA0.set_data(x,y)
            edotA.set_data(x[0], y[0])
        if i == 1:
            ehypocycloidA1.set_data(x,y)
        if i == 2:
            ehypocycloidA2.set_data(x,y)
        if i == 3:
            ehypocycloidA3.set_data(x,y)        
        if i == 4:
            ehypocycloidA4.set_data(x,y)
        if i == 5:
            ehypocycloidA5.set_data(x,y)
        if i == 6:
            ehypocycloidA6.set_data(x,y)
        if i == 7:
            ehypocycloidA7.set_data(x,y)  
        if i == 8:
            ehypocycloidA8.set_data(x,y)
        if i == 9:
            ehypocycloidA9.set_data(x,y)
        if i == 10:
            ehypocycloidA10.set_data(x,y)
        if i == 11:
            ehypocycloidA11.set_data(x,y)
        if i == 12:
            ehypocycloidA12.set_data(x,y)           
        if i == 13:
            ehypocycloidA13.set_data(x,y)        
        if i == 14:
            ehypocycloidA14.set_data(x,y)
        if i == 15:
            ehypocycloidA15.set_data(x,y)
        if i == 16:
            ehypocycloidA16.set_data(x,y)
        if i == 17:
            ehypocycloidA17.set_data(x,y)
        if i == 18:
            ehypocycloidA18.set_data(x,y)
        if i == 19:
            ehypocycloidA19.set_data(x,y)
        if i == 20:
            ehypocycloidA20.set_data(x,y)
        if i == 21:
            ehypocycloidA21.set_data(x,y)
        if i == 22:
            ehypocycloidA22.set_data(x,y)
        if i == 23:
            ehypocycloidA23.set_data(x,y)        
        if i == 24:
            ehypocycloidA24.set_data(x,y)
        if i == 25:
            ehypocycloidA25.set_data(x,y)
        if i == 26:
            ehypocycloidA26.set_data(x,y)
        if i == 27:
            ehypocycloidA27.set_data(x,y)  
        if i == 28:
            ehypocycloidA28.set_data(x,y)
        if i == 29:
            ehypocycloidA29.set_data(x,y)
        if i == 30:
            ehypocycloidA30.set_data(x,y)
        if i == 31:
            ehypocycloidA31.set_data(x,y)
        if i == 32:
            ehypocycloidA32.set_data(x,y)           
        if i == 33:
            ehypocycloidA33.set_data(x,y)        
        if i == 34:
            ehypocycloidA34.set_data(x,y)
        if i == 35:
            ehypocycloidA35.set_data(x,y)
        if i == 36:
            ehypocycloidA36.set_data(x,y)
        if i == 37:
            ehypocycloidA37.set_data(x,y)
        if i == 38:
            ehypocycloidA38.set_data(x,y)
        if i == 39:
            ehypocycloidA39.set_data(x,y)
        if i == 40:
            ehypocycloidA40.set_data(x,y)
        if i == 41:
            ehypocycloidA41.set_data(x,y)
        if i == 42:
            ehypocycloidA42.set_data(x,y)           
        if i == 43:
            ehypocycloidA43.set_data(x,y)        
        if i == 44:
            ehypocycloidA44.set_data(x,y)
        if i == 45:
            ehypocycloidA45.set_data(x,y)
        if i == 46:
            ehypocycloidA46.set_data(x,y)
        if i == 47:
            ehypocycloidA47.set_data(x,y)
        if i == 48:
            ehypocycloidA48.set_data(x,y)
        if i == 49:
            ehypocycloidA49.set_data(x,y)
        if i == 50:
            ehypocycloidA50.set_data(x,y)


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
