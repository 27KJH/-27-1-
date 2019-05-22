GlowScript 2.7 VPython
scene.caption = """Compton SANRAN
Light  + Energy +> to static electron => weaker light (different PAJANG) + electron Move

on the 
"""
#Init ==================================

Light = sphere(pos=vector(-1.5e9,0,0), radius=3e7, color=color.red, 
                make_trail=True)

Electron  = sphere(pos=vector(0,0,0), radius=3e7, color=color.yellow,
                make_trail=True, interval=10, retain=50)


#Constants ==================================
c = 3e8
h = 6.6e-34
me = 9.1e-31

dt = 0.0001
t = 0
rad_to_deg = pi/180

r_constant = 0.05
T = 180/ r_constant * dt
f = 1/T
Hit = 0 

wl = c/ f

print("T" + T+"__f" + f +"__wl" + wl + "__diff_wl" + diff_wl  )

#wl = h *c / E
#Compton equation ==================================

Theta = 30 *rad_to_deg
Phi = 60* rad_to_deg

diff_wl =h/((me)*(c**2)) * (1-cos(Theta))

#Constants ==================================

print("E = hf = "+h*f)
print("init_wl = " + wl)
while True:
    rate(10000)
    t = t + 1
    Light.pos.x = Light.pos.x + c*dt
    Light.pos.y = 3e8 * sin(r_constant*t * rad_to_deg)
    if (Light.pos.x)**2 + (Light.pos.y)**2 <= Electron.radius ** 2 :
        Hit = 1
               
if Hit ==1 :
    print(diff_wl)
    print(wl - diffwl)
    
    
                
                
                
                

