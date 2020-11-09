from pythtb import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

# lattice vectors and orbital positions
lat = [[0.0,0.5,0.5],[0.5,0.0,0.5],[0.5,0.5,0.0]]
orb = [[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],
       [0.25,0.25,0.25],[0.25,0.25,0.25],[0.25,0.25,0.25],[0.25,0.25,0.25]]
model = tb_model(3,3,lat,orb)

# define hopping parameters between orbitals
e1 = -1.79
e2 = -1.362
e3 = 0.69
e4 = 1.73

# define onsite energy
t1 = -3
t2 = 1
model.set_onsite([t1,t2,t2,t2,t1,t2,t2,t2])

def f(gra,a,b,c,d):
    #specify the hopping
    gra.set_hop(a,0,4,[0.0,0.0,0.0],mode="reset")
    gra.set_hop(a,0,4,[0.5,-0.5,-0.5],mode="reset") 
    gra.set_hop(a,0,4,[-1.0,1.0,-1.0],mode="reset")
    gra.set_hop(a,0,4,[-1.0,-1.0,1.0],mode="reset")

    gra.set_hop(b,0,5,[0.0,0.0,0.0],mode="reset")
    gra.set_hop(b,0,5,[1.0,-1.0,-1.0],mode="reset") 
    gra.set_hop(-b,0,5,[-1.0,1.0,-1.0],mode="reset")
    gra.set_hop(-b,0,5,[-1.0,-1.0,1.0],mode="reset")

    gra.set_hop(b,0,6,[0.0,0.0,0.0],mode="reset")
    gra.set_hop(-b,0,6,[1.0,-1.0,-1.0],mode="reset") 
    gra.set_hop(b,0,6,[-1.0,1.0,-1.0],mode="reset")
    gra.set_hop(-b,0,6,[-1.0,-1.0,1.0],mode="reset")

    gra.set_hop(b,0,7,[0.0,0.0,0.0],mode="reset")
    gra.set_hop(-b,0,7,[1.0,-1.0,-1.0],mode="reset") 
    gra.set_hop(-b,0,7,[-1.0,1.0,-1.0],mode="reset")
    gra.set_hop(b,0,7,[-1.0,-1.0,1.0],mode="reset")

    gra.set_hop(-b,4,1,[0.0,0.0,0.0],mode="reset")
    gra.set_hop(-b,4,1,[1.0,-1.0,-1.0],mode="reset") 
    gra.set_hop(b,4,1,[-1.0,1.0,-1.0],mode="reset")
    gra.set_hop(b,4,1,[-1.0,-1.0,1.0],mode="reset")

    gra.set_hop(-b,4,2,[0.0,0.0,0.0],mode="reset")
    gra.set_hop(b,4,2,[1.0,-1.0,-1.0],mode="reset") 
    gra.set_hop(-b,4,2,[-1.0,1.0,-1.0],mode="reset")
    gra.set_hop(b,4,2,[-1.0,-1.0,1.0],mode="reset")

    gra.set_hop(-b,4,3,[0.0,0.0,0.0],mode="reset")
    gra.set_hop(b,4,3,[1.0,-1.0,-1.0],mode="reset") 
    gra.set_hop(b,4,3,[-1.0,1.0,-1.0],mode="reset")
    gra.set_hop(-b,4,3,[-1.0,-1.0,1.0],mode="reset")

    gra.set_hop(c,1,5,[0.0,0.0,0.0],mode="reset")
    gra.set_hop(c,1,5,[1.0,-1.0,-1.0],mode="reset") 
    gra.set_hop(c,1,5,[-1.0,1.0,-1.0],mode="reset")
    gra.set_hop(c,1,5,[-1.0,-1.0,1.0],mode="reset")

    gra.set_hop(c,2,6,[0.0,0.0,0.0],mode="reset")
    gra.set_hop(c,2,6,[1.0,-1.0,-1.0],mode="reset") 
    gra.set_hop(c,2,6,[-1.0,1.0,-1.0],mode="reset")
    gra.set_hop(c,2,6,[-1.0,-1.0,1.0],mode="reset")

    gra.set_hop(c,3,7,[0.0,0.0,0.0],mode="reset")
    gra.set_hop(c,3,7,[1.0,-1.0,-1.0],mode="reset") 
    gra.set_hop(c,3,7,[-1.0,1.0,-1.0],mode="reset")
    gra.set_hop(c,3,7,[-1.0,-1.0,1.0],mode="reset")

    gra.set_hop(d,1,6,[0.0,0.0,0.0],mode="reset")
    gra.set_hop(-d,1,6,[1.0,-1.0,-1.0],mode="reset") 
    gra.set_hop(-d,1,6,[-1.0,1.0,-1.0],mode="reset")
    gra.set_hop(d,1,6,[-1.0,-1.0,1.0],mode="reset")

    gra.set_hop(d,1,7,[0.0,0.0,0.0],mode="reset")
    gra.set_hop(-d,1,7,[1.0,-1.0,-1.0],mode="reset") 
    gra.set_hop(d,1,7,[-1.0,1.0,-1.0],mode="reset")
    gra.set_hop(-d,1,7,[-1.0,-1.0,1.0],mode="reset")

    gra.set_hop(d,2,5,[0.0,0.0,0.0],mode="reset")
    gra.set_hop(-d,2,5,[1.0,-1.0,-1.0],mode="reset") 
    gra.set_hop(-d,2,5,[-1.0,1.0,-1.0],mode="reset")
    gra.set_hop(d,2,5,[-1.0,-1.0,1.0],mode="reset")

    gra.set_hop(d,2,7,[0.0,0.0,0.0],mode="reset")
    gra.set_hop(d,2,7,[1.0,-1.0,-1.0],mode="reset") 
    gra.set_hop(-d,2,7,[-1.0,1.0,-1.0],mode="reset")
    gra.set_hop(-d,2,7,[-1.0,-1.0,1.0],mode="reset")

    gra.set_hop(d,3,5,[0.0,0.0,0.0],mode="reset")
    gra.set_hop(-d,3,5,[1.0,-1.0,-1.0],mode="reset") 
    gra.set_hop(d,3,5,[-1.0,1.0,-1.0],mode="reset")
    gra.set_hop(-d,3,5,[-1.0,-1.0,1.0],mode="reset")

    gra.set_hop(d,3,6,[0.0,0.0,0.0],mode="reset")
    gra.set_hop(d,3,6,[1.0,-1.0,-1.0],mode="reset") 
    gra.set_hop(-d,3,6,[-1.0,1.0,-1.0],mode="reset")
    gra.set_hop(-d,3,6,[-1.0,-1.0,1.0],mode="reset")
    
    return gra

model1 = f(model,e1,e2,e3,e4)

# solve model on a path in k-space
k = [[0.5,0.5,0.5],[0.0,0.0,0.0],[0.25,0.0,0.25],[0.375,0.375,0.75],[0.0,0.0,0.0]]
(k_vec,k_dist,k_node)=model1.k_path(k, 100)
evals=model1.solve_all(k_vec)

# plot bandstructure
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
l1, = plt.plot(k_dist,evals[0,:])
l2, = plt.plot(k_dist,evals[1,:])
l3, = plt.plot(k_dist,evals[2,:])
l4, = plt.plot(k_dist,evals[3,:])
l5, = plt.plot(k_dist,evals[4,:])
l6, = plt.plot(k_dist,evals[5,:])
l7, = plt.plot(k_dist,evals[6,:])
l8, = plt.plot(k_dist,evals[7,:])
ax.set_xticks(k_node)
ax.set_xticklabels(["L","$\Gamma$","X","K","$\Gamma$"])
ax.set_xlim(k_node[0],k_node[-1])
ax.set_ylim(-12,12)


#define the interactive part
axcolor = 'lightgoldenrodyellow'
axt1 = plt.axes([0.25, 0.035, 0.65, 0.03], facecolor=axcolor) 
axt2 = plt.axes([0.25, 0.07, 0.65, 0.03], facecolor=axcolor)
axt3 = plt.axes([0.25, 0.105, 0.65, 0.03], facecolor=axcolor)
axt4 = plt.axes([0.25, 0.14, 0.65, 0.03], facecolor=axcolor)

st1 = Slider(axt1, 'hop1', -5.0, 5.0, valinit=e1)
st2 = Slider(axt2, 'hop2', -5.0, 5.0, valinit=e2)
st3 = Slider(axt3, 'hop3', -5.0, 5.0, valinit=e3)
st4 = Slider(axt4, 'hop4', -5.0, 5.0, valinit=e4)


def update(val):
    e1 = st1.val  
    e2 = st2.val
    e3 = st3.val
    e4 = st4.val
    model1 = f(model,e1,e2,e3,e4)
    k = [[0.5,0.5,0.5],[0.0,0.0,0.0],[0.25,0.0,0.25],[0.375,0.375,0.75],[0.0,0.0,0.0]]
    (k_vec,k_dist,k_node)=model.k_path(k, 100)
    evals=model.solve_all(k_vec)
    l1.set_ydata(evals[0,:])
    l2.set_ydata(evals[1,:])
    l3.set_ydata(evals[2,:])
    l4.set_ydata(evals[3,:])
    l5.set_ydata(evals[4,:])
    l6.set_ydata(evals[5,:])
    l7.set_ydata(evals[6,:])
    l8.set_ydata(evals[7,:])
    fig.canvas.draw_idle()

    
st1.on_changed(update) 
st2.on_changed(update)
st3.on_changed(update)
st4.on_changed(update)

resetax = plt.axes([0.05, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    st1.reset()
    st2.reset()
    st3.reset()
    st4.reset()

button.on_clicked(reset)

plt.show()