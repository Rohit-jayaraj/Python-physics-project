import pyglet
import pymunk as pym
from pymunk.pyglet_util import DrawOptions
from math import degrees 


window=pyglet.window.Window(1280,720,"Pym test", resizable=False)
options=DrawOptions()
batch=pyglet.graphics.Batch()



space=pym.Space()
space.gravity=0,-1000

mass=1
radius=65
sprites=[]



segment_shape1=pym.Segment(space.static_body,(0,0),(800,90),2)
segment_shape1.body.position=500,400
segment_shape1.elasticity=0.9
segment_shape1.friction=0.9
space.add(segment_shape1)

segment_shape2=pym.Segment(space.static_body,(0,100),(800,0),2)
segment_shape2.body.position=100,100
segment_shape2.elasticity=0.9
segment_shape2.friction=0.9
space.add(segment_shape2)







@window.event
def on_draw():
    window.clear()
    space.debug_draw(options)
    batch.draw()

@window.event
def on_mouse_press(x,y,button,modifiers):
    circle_moment=pym.moment_for_circle(mass,0,radius)
    circle_body=pym.Body(mass,circle_moment)
    circle_body.position=x,y
    circle_shape=pym.Circle(circle_body,radius)
    circle_shape.elasticity= 1.0
    circle_shape.friction=0.9
    
    space.add(circle_shape,circle_body)




def update(dt):
    space.step(dt)
    
    
    


if __name__== "__main__":
    pyglet.clock.schedule_interval(update,1.0/60)
    pyglet.app.run()
