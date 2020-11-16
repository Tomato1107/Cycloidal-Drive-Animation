import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button
#plt.rcParams['animation.ffmpeg_path'] = 'D:/portableSoftware/ShareX/ShareX/Tools/ffmpeg.exe'


fig, ax = plt.subplots(figsize=(6,6))
plt.subplots_adjust(left=0.15, bottom=0.35)

ax.set_aspect('equal')
plt.xlim(-1.2*40,1.2*40)
plt.ylim(-1.2*40,1.2*40)
#plt.grid()
t = np.linspace(0, 2*np.pi, 400)
delta = 1
e =2
n=10
RD=40
rd=5
## draw pin
l0, = ax.plot([], [], 'k-', lw=2)
l1, = ax.plot([], [], 'k-', lw=2)
l2, = ax.plot([], [], 'k-', lw=2)
l3, = ax.plot([], [], 'k-', lw=2)        
l4, = ax.plot([], [], 'k-', lw=2)
l5, = ax.plot([], [], 'k-', lw=2)
l6, = ax.plot([], [], 'k-', lw=2)
l7, = ax.plot([], [], 'k-', lw=2) 
l8, = ax.plot([], [], 'k-', lw=2)
l9, = ax.plot([], [], 'k-', lw=2)
l10, = ax.plot([], [], 'k-', lw=2) 
l11, = ax.plot([], [], 'k-', lw=2)
l12, = ax.plot([], [], 'k-', lw=2)
l13, = ax.plot([], [], 'k-', lw=2)        
l14, = ax.plot([], [], 'k-', lw=2)
l15, = ax.plot([], [], 'k-', lw=2)
l16, = ax.plot([], [], 'k-', lw=2)
l17, = ax.plot([], [], 'k-', lw=2) 
l18, = ax.plot([], [], 'k-', lw=2)
l19, = ax.plot([], [], 'k-', lw=2)
l20, = ax.plot([], [], 'k-', lw=2) 
l21, = ax.plot([], [], 'k-', lw=2)
l22, = ax.plot([], [], 'k-', lw=2)
l23, = ax.plot([], [], 'k-', lw=2)        
l24, = ax.plot([], [], 'k-', lw=2)
l25, = ax.plot([], [], 'k-', lw=2)
l26, = ax.plot([], [], 'k-', lw=2)
l27, = ax.plot([], [], 'k-', lw=2) 
l28, = ax.plot([], [], 'k-', lw=2)
l29, = ax.plot([], [], 'k-', lw=2)
l30, = ax.plot([], [], 'k-', lw=2) 
l31, = ax.plot([], [], 'k-', lw=2)
l32, = ax.plot([], [], 'k-', lw=2)
l33, = ax.plot([], [], 'k-', lw=2)        
l34, = ax.plot([], [], 'k-', lw=2)
l35, = ax.plot([], [], 'k-', lw=2)
l36, = ax.plot([], [], 'k-', lw=2)
l37, = ax.plot([], [], 'k-', lw=2) 
l38, = ax.plot([], [], 'k-', lw=2)
l39, = ax.plot([], [], 'k-', lw=2)
l40, = ax.plot([], [], 'k-', lw=2) 


for i in range(int(40)):
    x = (5*np.sin(t)+ 40*np.cos(2*i*np.pi/10))
    y = (5*np.cos(t) + 40*np.sin(2*i*np.pi/10))
    if i == 0:
        l0, = ax.plot(x, y,'k-')
    if i == 1:
        l1, = ax.plot(x, y,'k-')
    if i == 2:
        l2, = ax.plot(x, y,'k-')
    if i == 3:
        l3, = ax.plot(x, y,'k-')        
    if i == 4:
        l4, = ax.plot(x, y,'k-')
    if i == 5:
        l5, = ax.plot(x, y,'k-')
    if i == 6:
        l6, = ax.plot(x, y,'k-')
    if i == 7:
        l7, = ax.plot(x, y,'k-')  
    if i == 8:
        l8, = ax.plot(x, y,'k-')
    if i == 9:
        l9, = ax.plot(x, y,'k-')
    if i == 10:
        l10, = ax.plot(x, y,'k-') 
    if i == 11:
        l11, = ax.plot(x, y,'k-')
    if i == 12:
        l12, = ax.plot(x, y,'k-')
    if i == 13:
        l13, = ax.plot(x, y,'k-')        
    if i == 14:
        l14, = ax.plot(x, y,'k-')
    if i == 15:
        l15, = ax.plot(x, y,'k-')
    if i == 16:
        l16, = ax.plot(x, y,'k-')
    if i == 17:
        l17, = ax.plot(x, y,'k-')  
    if i == 18:
        l18, = ax.plot(x, y,'k-')
    if i == 19:
        l19, = ax.plot(x, y,'k-')
    if i == 20:
        l20, = ax.plot(x, y,'k-')
    if i == 21:
        l21, = ax.plot(x, y,'k-')
    if i == 22:
        l22, = ax.plot(x, y,'k-')
    if i == 23:
        l23, = ax.plot(x, y,'k-')        
    if i == 24:
        l24, = ax.plot(x, y,'k-')
    if i == 25:
        l25, = ax.plot(x, y,'k-')
    if i == 26:
        l26, = ax.plot(x, y,'k-')
    if i == 27:
        l27, = ax.plot(x, y,'k-')  
    if i == 28:
        l28, = ax.plot(x, y,'k-')
    if i == 29:
        l29, = ax.plot(x, y,'k-')
    if i == 30:
        l30, = ax.plot(x, y,'k-') 
    if i == 31:
        l31, = ax.plot(x, y,'k-')
    if i == 32:
        l32, = ax.plot(x, y,'k-')
    if i == 33:
        l33, = ax.plot(x, y,'k-')        
    if i == 34:
        l34, = ax.plot(x, y,'k-')
    if i == 35:
        l35, = ax.plot(x, y,'k-')
    if i == 36:
        l36, = ax.plot(x, y,'k-')
    if i == 37:
        l37, = ax.plot(x, y,'k-')  
    if i == 38:
        l38, = ax.plot(x, y,'k-')
    if i == 39:
        l39, = ax.plot(x, y,'k-')
    if i == 40:
        l40, = ax.plot(x, y,'k-')

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
        if i == 133:
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

## draw inner_pin
p0, = ax.plot([], [], 'k-', lw=2)
p1, = ax.plot([], [], 'k-', lw=2)
p2, = ax.plot([], [], 'k-', lw=2)
p3, = ax.plot([], [], 'k-', lw=2)        
p4, = ax.plot([], [], 'k-', lw=2)
p5, = ax.plot([], [], 'k-', lw=2)
p6, = ax.plot([], [], 'k-', lw=2)
p7, = ax.plot([], [], 'k-', lw=2) 
p8, = ax.plot([], [], 'k-', lw=2)
p9, = ax.plot([], [], 'k-', lw=2)


for i in range(int(10)):
    x = (5*np.sin(t)+ 20*np.cos(2*i*np.pi/6))
    y = (5*np.cos(t) + 20*np.sin(2*i*np.pi/6))
    if i == 0:
        p0, = ax.plot(x, y,'k-')
    if i == 1:
        p1, = ax.plot(x, y,'k-')
    if i == 2:
        p2, = ax.plot(x, y,'k-')
    if i == 3:
        p3, = ax.plot(x, y,'k-')        
    if i == 4:
        p4, = ax.plot(x, y,'k-')
    if i == 5:
        p5, = ax.plot(x, y,'k-')
    if i == 6:
        p6, = ax.plot(x, y,'k-')
    if i == 7:
        p7, = ax.plot(x, y,'k-')  
    if i == 8:
        p8, = ax.plot(x, y,'k-')
    if i == 9:
        p9, = ax.plot(x, y,'k-')



def inner_pin_update(n,N,rd,Rd,phi):
    for i in range(int(n)):    
        x = (rd*np.sin(t)+ Rd*np.cos(2*i*np.pi/n))*np.cos(-phi/(N-1)+ 3*np.pi/(N-1)-np.pi/3) - (rd*np.cos(t) + Rd*np.sin(2*i*np.pi/n))*np.sin(-phi/(N-1)+ 3*np.pi/(N-1)-np.pi/3)
        y = (rd*np.sin(t)+ Rd*np.cos(2*i*np.pi/n))*np.sin(-phi/(N-1)+ 3*np.pi/(N-1)-np.pi/3) + (rd*np.cos(t) + Rd*np.sin(2*i*np.pi/n))*np.cos(-phi/(N-1)+ 3*np.pi/(N-1)-np.pi/3)
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

## draw drive_pin
a = 5*np.sin(t)
b = 5*np.cos(t) 
d0, = ax.plot(a, b,'k-', lw=2)

def drive_pin_update(r):
    x = r*np.sin(t)
    y = r*np.cos(t)
    d0.set_data(x,y)


#inner circleA:
inner_circle1A, = ax.plot([], [], 'r-', lw=2)
inner_circle2A, = ax.plot([], [], 'r-', lw=2)
inner_circle3A, = ax.plot([], [], 'r-', lw=2)
inner_circle4A, = ax.plot([], [], 'r-', lw=2)        
inner_circle5A, = ax.plot([], [], 'r-', lw=2)
inner_circle6A, = ax.plot([], [], 'r-', lw=2)
inner_circle7A, = ax.plot([], [], 'r-', lw=2)
inner_circle8A, = ax.plot([], [], 'r-', lw=2) 
inner_circle9A, = ax.plot([], [], 'r-', lw=2)
inner_circle10A, = ax.plot([], [], 'r-', lw=2)

def draw_inner_circleA_init():
    inner_circle10A.set_data([0], [0])
    inner_circle1A.set_data([0], [0])
    inner_circle2A.set_data([0], [0])  
    inner_circle3A.set_data([0], [0])
    inner_circle4A.set_data([0], [0])
    inner_circle5A.set_data([0], [0])
    inner_circle6A.set_data([0], [0])
    inner_circle7A.set_data([0], [0])
    inner_circle8A.set_data([0], [0])
    inner_circle9A.set_data([0], [0])


for i in range(10):
    x = (rd+e)*np.cos(t)+0.5*RD*np.cos(2*i*np.pi/6)+e
    y = (rd+e)*np.sin(t)+0.5*RD*np.sin(2*i*np.pi/6)
    if i==0:
        inner_circle1A, = ax.plot(x,y,'r-')
    if i==1:
        inner_circle2A, = ax.plot(x,y,'r-')
    if i==2:
        inner_circle3A, = ax.plot(x,y,'r-')
    if i==3:
        inner_circle4A, = ax.plot(x,y,'r-')
    if i==4:
        inner_circle5A, = ax.plot(x,y,'r-')
    if i==5:
        inner_circle6A, = ax.plot(x,y,'r-')
    if i==6:
        inner_circle7A, = ax.plot(x,y,'r-')
    if i==7:
        inner_circle8A, = ax.plot(x,y,'r-')
    if i==8:
        inner_circle9A, = ax.plot(x,y,'r-')
    if i==9:
        inner_circle10A, = ax.plot(x,y,'r-')   

def update_inner_circleA(e,n,N,rd,Rd, phi):
    
    for i in range(int(n)):
        
        x = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.cos(-phi/(N-1)+ 3*np.pi/(N-1)-np.pi/3) - ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.sin(-phi/(N-1)+ 3*np.pi/(N-1)-np.pi/3) + e*np.cos(phi)
        y = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.sin(-phi/(N-1)+ 3*np.pi/(N-1)-np.pi/3) + ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.cos(-phi/(N-1)+ 3*np.pi/(N-1)-np.pi/3) + e*np.sin(phi)        
        if i==0:
            inner_circle1A.set_data(x,y)
        if i==1:
            inner_circle2A.set_data(x,y)
        if i==2:
            inner_circle3A.set_data(x,y)
        if i==3:
            inner_circle4A.set_data(x,y)
        if i==4:
            inner_circle5A.set_data(x,y)
        if i==5:
            inner_circle6A.set_data(x,y)
        if i==6:
            inner_circle7A.set_data(x,y)
        if i==7:
            inner_circle8A.set_data(x,y)
        if i==8:
            inner_circle9A.set_data(x,y)
        if i==9:
            inner_circle10A.set_data(x,y)

#inner circleB:
inner_circle1B, = ax.plot([], [], 'b-', lw=2)
inner_circle2B, = ax.plot([], [], 'b-', lw=2)
inner_circle3B, = ax.plot([], [], 'b-', lw=2)
inner_circle4B, = ax.plot([], [], 'b-', lw=2)        
inner_circle5B, = ax.plot([], [], 'b-', lw=2)
inner_circle6B, = ax.plot([], [], 'b-', lw=2)
inner_circle7B, = ax.plot([], [], 'b-', lw=2)
inner_circle8B, = ax.plot([], [], 'b-', lw=2) 
inner_circle9B, = ax.plot([], [], 'b-', lw=2)
inner_circle10B, = ax.plot([], [], 'b-', lw=2)

def draw_inner_circleB_init():
    inner_circle10B.set_data([0], [0])
    inner_circle1B.set_data([0], [0])
    inner_circle2B.set_data([0], [0])  
    inner_circle3B.set_data([0], [0])
    inner_circle4B.set_data([0], [0])
    inner_circle5B.set_data([0], [0])
    inner_circle6B.set_data([0], [0])
    inner_circle7B.set_data([0], [0])
    inner_circle8B.set_data([0], [0])
    inner_circle9B.set_data([0], [0])


for i in range(10):
    x = (rd+e)*np.cos(t)+0.5*RD*np.cos(2*i*np.pi/6)- e*np.cos(np.pi/3)
    y = (rd+e)*np.sin(t)+0.5*RD*np.sin(2*i*np.pi/6)- e*np.sin(np.pi/3)
    if i==0:
        inner_circle1B, = ax.plot(x,y,'b-')
    if i==1:
        inner_circle2B, = ax.plot(x,y,'b-')
    if i==2:
        inner_circle3B, = ax.plot(x,y,'b-')
    if i==3:
        inner_circle4B, = ax.plot(x,y,'b-')
    if i==4:
        inner_circle5B, = ax.plot(x,y,'b-')
    if i==5:
        inner_circle6B, = ax.plot(x,y,'b-')
    if i==6:
        inner_circle7B, = ax.plot(x,y,'b-')
    if i==7:
        inner_circle8B, = ax.plot(x,y,'b-')
    if i==8:
        inner_circle9B, = ax.plot(x,y,'b-')
    if i==9:
        inner_circle10B, = ax.plot(x,y,'b-')   

def update_inner_circleB(e,n,N,rd,Rd, phi):
    
    for i in range(int(n)):
        x = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.cos(-phi/(N-1)+ 3*np.pi/(N-1) - np.pi/(3)) - ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.sin(-phi/(N-1)+ 3*np.pi/(N-1)- np.pi/(3)) - e*np.cos(phi-np.pi/3)
        y = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.sin(-phi/(N-1)+ 3*np.pi/(N-1)- np.pi/(3)) + ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.cos(-phi/(N-1)+ 3*np.pi/(N-1)- np.pi/(3)) - e*np.sin(phi-np.pi/3)
        if i==0:
            inner_circle1B.set_data(x,y)
        if i==1:
            inner_circle2B.set_data(x,y)
        if i==2:
            inner_circle3B.set_data(x,y)
        if i==3:
            inner_circle4B.set_data(x,y)
        if i==4:
            inner_circle5B.set_data(x,y)
        if i==5:
            inner_circle6B.set_data(x,y)
        if i==6:
            inner_circle7B.set_data(x,y)
        if i==7:
            inner_circle8B.set_data(x,y)
        if i==8:
            inner_circle9B.set_data(x,y)
        if i==9:
            inner_circle10B.set_data(x,y)


#inner circleC:
inner_circle1C, = ax.plot([], [], 'g-', lw=2)
inner_circle2C, = ax.plot([], [], 'g-', lw=2)
inner_circle3C, = ax.plot([], [], 'g-', lw=2)
inner_circle4C, = ax.plot([], [], 'g-', lw=2)        
inner_circle5C, = ax.plot([], [], 'g-', lw=2)
inner_circle6C, = ax.plot([], [], 'g-', lw=2)
inner_circle7C, = ax.plot([], [], 'g-', lw=2)
inner_circle8C, = ax.plot([], [], 'g-', lw=2) 
inner_circle9C, = ax.plot([], [], 'g-', lw=2)
inner_circle10C, = ax.plot([], [], 'g-', lw=2)

def draw_inner_circleC_init():
    inner_circle10C.set_data([0], [0])
    inner_circle1C.set_data([0], [0])
    inner_circle2C.set_data([0], [0])  
    inner_circle3C.set_data([0], [0])
    inner_circle4C.set_data([0], [0])
    inner_circle5C.set_data([0], [0])
    inner_circle6C.set_data([0], [0])
    inner_circle7C.set_data([0], [0])
    inner_circle8C.set_data([0], [0])
    inner_circle9C.set_data([0], [0])


for i in range(10):
    x = (rd+e)*np.cos(t)+0.5*RD*np.cos(2*i*np.pi/6)- e*np.cos(-np.pi/3)
    y = (rd+e)*np.sin(t)+0.5*RD*np.sin(2*i*np.pi/6)- e*np.sin(-np.pi/3)
    if i==0:
        inner_circle1C, = ax.plot(x,y,'g-')
    if i==1:
        inner_circle2C, = ax.plot(x,y,'g-')
    if i==2:
        inner_circle3C, = ax.plot(x,y,'g-')
    if i==3:
        inner_circle4C, = ax.plot(x,y,'g-')
    if i==4:
        inner_circle5C, = ax.plot(x,y,'g-')
    if i==5:
        inner_circle6C, = ax.plot(x,y,'g-')
    if i==6:
        inner_circle7C, = ax.plot(x,y,'g-')
    if i==7:
        inner_circle8C, = ax.plot(x,y,'g-')
    if i==8:
        inner_circle9C, = ax.plot(x,y,'g-')
    if i==9:
        inner_circle10C, = ax.plot(x,y,'g-')   

def update_inner_circleC(e,n,N,rd,Rd, phi):
    
    for i in range(int(n)):
        x = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.cos(-phi/(N-1) + 3*np.pi/(N-1) - np.pi/(3)) - ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.sin(-phi/(N-1) + 3*np.pi/(N-1)- np.pi/(3)) - e*np.cos(phi+np.pi/3)
        y = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.sin(-phi/(N-1) + 3*np.pi/(N-1)- np.pi/(3)) + ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.cos(-phi/(N-1) + 3*np.pi/(N-1)- np.pi/(3)) - e*np.sin(phi+np.pi/3)
        if i==0:
            inner_circle1C.set_data(x,y)
        if i==1:
            inner_circle2C.set_data(x,y)
        if i==2:
            inner_circle3C.set_data(x,y)
        if i==3:
            inner_circle4C.set_data(x,y)
        if i==4:
            inner_circle5C.set_data(x,y)
        if i==5:
            inner_circle6C.set_data(x,y)
        if i==6:
            inner_circle7C.set_data(x,y)
        if i==7:
            inner_circle8C.set_data(x,y)
        if i==8:
            inner_circle9C.set_data(x,y)
        if i==9:
            inner_circle10C.set_data(x,y)


##inner pinA:
#x = (rd+e)*np.cos(t)+e
#y = (rd+e)*np.sin(t)
#inner_pinA, = ax.plot(x,y,'r-')
inner_pinA, = ax.plot([0],[0],'r-')
##driver line and dot:
#self.line, = self.ax.plot([self.rd+self.e + self.e, 0],[0,0],'r-')
#dotA, = ax.plot([rd+ e+ e],[0], 'ro', ms=5)
dotA, = ax.plot([0],[0], 'ro', ms=5)
def update_inner_pinA(e,Rm, phi):
    x = (Rm+e)*np.cos(t)+e*np.cos(phi)
    y = (Rm+e)*np.sin(t)+e*np.sin(phi)
    inner_pinA.set_data(x,y)
    
    x1 = (Rm+e)*np.cos(phi)+e*np.cos(phi)
    y1 = (Rm+e)*np.sin(phi)+e*np.sin(phi)
    #self.line.set_data([0,x1],[0,y1])
    dotA.set_data(x1, y1)

##inner pinB:
#x = (rd+e)*np.cos(t)-e*np.cos(np.pi/3)
#y = (rd+e)*np.sin(t)-e*np.sin(np.pi/3)
#inner_pinB, = ax.plot(x,y,'b-')
inner_pinB, = ax.plot([0],[0],'b-')
##driver line and dot:
#self.line, = self.ax.plot([self.rd+self.e + self.e, 0],[0,0],'r-')
#dotB, = ax.plot([-rd- e- e],[0], 'bo', ms=5)
dotB, = ax.plot([0],[0], 'bo', ms=5)

def update_inner_pinB(e,Rm, phi):
    x = (Rm+e)*np.cos(t)-e*np.cos(phi-np.pi/3)
    y = (Rm+e)*np.sin(t)-e*np.sin(phi-np.pi/3)
    inner_pinB.set_data(x,y)
    
    x1 = (Rm+e)*np.cos(phi+2*np.pi/3)-e*np.cos(phi-np.pi/3)
    y1 = (Rm+e)*np.sin(phi+2*np.pi/3)-e*np.sin(phi-np.pi/3)
    #self.line.set_data([0,x1],[0,y1])
    dotB.set_data(x1, y1)

##inner pinC:
#x = (rd+e)*np.cos(t)-e*np.cos(-np.pi/3)
#y = (rd+e)*np.sin(t)-e*np.sin(-np.pi/3)
#inner_pinC, = ax.plot(x,y,'g-')
inner_pinC, = ax.plot([0],[0],'g-')
##driver line and dot:
#self.line, = self.ax.plot([self.rd+self.e + self.e, 0],[0,0],'r-')
#dotC, = ax.plot([-rd- e- e],[0], 'go', ms=5)
dotC, = ax.plot([0],[0], 'go', ms=5)

def update_inner_pinC(e,Rm, phi):
    x = (Rm+e)*np.cos(t)-e*np.cos(phi+np.pi/3)
    y = (Rm+e)*np.sin(t)-e*np.sin(phi+np.pi/3)
    inner_pinC.set_data(x,y)
    
    x1 = (Rm+e)*np.cos(phi-2*np.pi/3)-e*np.cos(phi+np.pi/3)
    y1 = (Rm+e)*np.sin(phi-2*np.pi/3)-e*np.sin(phi+np.pi/3)
    #self.line.set_data([0,x1],[0,y1])
    dotC.set_data(x1, y1)

##ehypocycloidA:

#rc = (n-1)*(RD/n)
#rm = (RD/n)
#xa = (rc+rm)*np.cos(t)-e*np.cos((rc+rm)/rm*t)
#ya = (rc+rm)*np.sin(t)-e*np.sin((rc+rm)/rm*t)

#dxa = (rc+rm)*(-np.sin(t)+(e/rm)*np.sin((rc+rm)/rm*t))
#dya = (rc+rm)*(np.cos(t)-(e/rm)*np.cos((rc+rm)/rm*t))

#x = xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya) + e
#y = ya + rd/np.sqrt(dxa**2 + dya**2)*dxa
##ehypocycloidA, = ax.plot(x,y,'r-')
ehypocycloidA, = ax.plot([0], [0],'r-')
##driver line and dot: (rc+rm) - rd
#self.eline, = self.ax.plot([(rc+rm) - rd, 0],[0,0],'r-')
#edotA, = ax.plot([(rc+rm) - rd],[0], 'ro', ms=5)
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

    x = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.cos(-phis/(n-1))-(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.sin(-phis/(n-1))  + e*np.cos(phis)
    y = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.sin(-phis/(n-1))+(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.cos(-phis/(n-1))  + e*np.sin(phis)
    ehypocycloidA.set_data(x,y)

    #self.eline.set_data([e*np.cos(phis),x[0]],[e*np.sin(phis),y[0]])
    edotA.set_data(x[0], y[0])

##ehypocycloidB:

#rc = (n-1)*(RD/n)
#rm = (RD/n)
#xa = (rc+rm)*np.cos(t)+e*np.cos((rc+rm)/rm*t)
#ya = (rc+rm)*np.sin(t)+e*np.sin((rc+rm)/rm*t)

#dxa = (rc+rm)*(-np.sin(t)-(e/rm)*np.sin((rc+rm)/rm*t))
#dya = (rc+rm)*(np.cos(t)+(e/rm)*np.cos((rc+rm)/rm*t))

#x = xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya) - e*np.cos(np.pi/3)
#y = ya + rd/np.sqrt(dxa**2 + dya**2)*dxa - e*np.sin(np.pi/3)
#ehypocycloidB, = ax.plot(x,y,'b-')
ehypocycloidB, = ax.plot([0],[0],'b-')
##driver line and dot: (rc+rm) - rd
#self.eline, = self.ax.plot([(rc+rm) - rd, 0],[0,0],'r-')
#edotB, = ax.plot([(rc+rm) - rd],[0], 'bo', ms=5)
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

    x = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.cos(-phis/(n-1) + np.pi/3/(n-1))-(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.sin(-phis/(n-1) + np.pi/3/(n-1))  - e*np.cos(phis-np.pi/3)
    y = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.sin(-phis/(n-1) + np.pi/3/(n-1))+(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.cos(-phis/(n-1) + np.pi/3/(n-1))  - e*np.sin(phis-np.pi/3)
    ehypocycloidB.set_data(x,y)

    #self.eline.set_data([e*np.cos(phis),x[0]],[e*np.sin(phis),y[0]])
    edotB.set_data(x[0], y[0])


##ehypocycloidC:

#rc = (n-1)*(RD/n)
#rm = (RD/n)
#xa = (rc+rm)*np.cos(t)+e*np.cos((rc+rm)/rm*t)
#ya = (rc+rm)*np.sin(t)+e*np.sin((rc+rm)/rm*t)

#dxa = (rc+rm)*(-np.sin(t)-(e/rm)*np.sin((rc+rm)/rm*t))
#dya = (rc+rm)*(np.cos(t)+(e/rm)*np.cos((rc+rm)/rm*t))

#x = xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya) - e*np.cos(-np.pi/3)
#y = ya + rd/np.sqrt(dxa**2 + dya**2)*dxa - e*np.sin(-np.pi/3)
#ehypocycloidC, = ax.plot(x,y,'g-')
ehypocycloidC, = ax.plot([0],[0],'g-')
##driver line and dot: (rc+rm) - rd
#self.eline, = self.ax.plot([(rc+rm) - rd, 0],[0,0],'r-')
#edotC, = ax.plot([(rc+rm) - rd],[0], 'go', ms=5)
edotC, = ax.plot([0],[0], 'go', ms=5)
def update_ehypocycloidC(e,n,D,d, phis):
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

    #self.eline.set_data([e*np.cos(phis),x[0]],[e*np.sin(phis),y[0]])
    edotC.set_data(x[0], y[0])




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

sli_fm = Slider(ax_fm, 'fm', 10, 100, valinit=50, valstep=delta)
sli_Rm = Slider(ax_Rm, 'Rm', 1, 10, valinit=5, valstep=delta)
sli_n = Slider(ax_n, 'n', 2, 10, valinit=6, valstep=delta)
sli_Rd = Slider(ax_Rd, 'Rd', 1, 40, valinit=20, valstep=delta)
sli_rd = Slider(ax_rd, 'rd', 1, 10, valinit=5, valstep=delta)
sli_e = Slider(ax_e, 'e', 0.1, 10, valinit=2, valstep=delta/10)
sli_N = Slider(ax_N, 'N', 3, 40, valinit=10, valstep=delta)
sli_d = Slider(ax_d, 'd', 2, 20, valinit=10,valstep=delta)
sli_D = Slider(ax_D, 'D', 5, 100, valinit=80,valstep=delta)

def update(val):
    sfm = sli_Rm.val
    sRm = sli_Rm.val
    sRd = sli_Rd.val
    sn = sli_n.val
    srd = sli_rd.val    
    se = sli_e.val
    sN = sli_N.val
    sd = sli_d.val
    sD = sli_D.val
    ax.set_xlim(-1.2*0.5*sD,1.2*0.5*sD)
    ax.set_ylim(-1.2*0.5*sD,1.2*0.5*sD)



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
    draw_inner_pin_init()
    draw_inner_circleA_init()
    draw_inner_circleB_init()
    draw_inner_circleC_init()
    pin_update(sN,sd,sD)

    update_inner_pinA(se,sRm, phi)
    update_inner_pinB(se,sRm, phi)
    update_inner_pinC(se,sRm, phi)
    #update_inner_pinA(se,sRm, 0)
    #update_inner_pinB(se,sRm, 0)
    #update_inner_pinC(se,sRm, 0)
    inner_pin_update(sn,sN,srd,sRd,phi)    
    #inner_pin_update(sn,sN,srd,sRd,0)
    drive_pin_update(sRm)
    update_inner_circleA(se,sn,sN,srd,sRd, phi)
    update_inner_circleB(se,sn,sN,srd,sRd, phi)
    update_inner_circleC(se,sn,sN,srd,sRd, phi)    
    #update_inner_circleA(se,sn,sN,srd,sRd, 0)
    #update_inner_circleB(se,sn,sN,srd,sRd, 0)
    #update_inner_circleC(se,sn,sN,srd,sRd, 0)
    update_ehypocycloidA(se,sN,sD,sd, phi)
    update_ehypocycloidB(se,sN,sD,sd, phi)
    update_ehypocycloidC(se,sN,sD,sd, phi)
    #update_ehypocycloidA(se,sN,sD,sd, 0)
    #update_ehypocycloidB(se,sN,sD,sd, 0)
    #update_ehypocycloidC(se,sN,sD,sd, 0)


    fig.canvas.draw_idle()



ani = animation.FuncAnimation(fig, animate,frames=sli_fm.val*(sli_N.val-1), interval=150)
dpi=100
##un-comment the next line, if you want to save the animation as gif:
#hypo.animation.save('myhypocycloid.gif', writer='pillow', fps=10, dpi=75)
#ani.save('myGUI_2.gif', writer='Pillow',fps=10,dpi=dpi)
#ani.save('myGUI_2.mp4', writer='ffmpeg',dpi=dpi)
plt.show()