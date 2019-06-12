GlowScript 2.7 VPython
scene.caption = """Compton SANRAN
Light  + Energy +> to static electron => weaker light (different PAJANG) + electron Move

on the 
"""
#Constants ==================================
c = 3e8
h = 6.6e-34
me = 9.1e-31

dt = 0.0001
t = 0
rad_to_deg = pi/180
Hit = 0

#Init ==================================

Light = sphere(pos=vector(-8e8,0,0), radius=2e7, color=color.red, make_trail=True)
                
f1 = 3e19
wl1 = c/f1 #1e-8
E1 = h* f1
p_i = h/wl1

print( " Initial Energy = " + E1)
print( " Initial Freq = " + f1)
print( " Initial Wave Length = " + wl1)
print( " Initial Momentum= " + p_i)


Electron  = sphere(pos=vector(0,0,0), radius=2e7, color=color.yellow,
                make_trail=True)


#Compton equation ==================================

Theta = -30 * rad_to_deg
diff_wl =h/(me*c) * (1-cos(Theta))

print("Difference in Wave Length " + diff_wl)


#After Hit =======================

print("AfterHit =========================")
print("AfterHit =========================")
print("AfterHit =========================")

wl2 = wl1 + diff_wl

#Momentum BoZon ==================

p_i = h/wl1
p_f = h/wl2
f2 = c/wl2
E2 = h*f2


Phi = atan(-p_f * sin(Theta) / (p_i-p_f*cos(Theta)))


p_e = p_f * cos(Theta) / sin(Phi)
v_e = sqrt( ( (c**2)*me + sqrt( (c**4)*(me**2) - (p_e * c) ** 2)) / 2*me)
E_e = sqrt( (p_e*c)**2 + (me *(c**2))**2 )


Ediff = E_e + E2 - E1

print("After Energy "+ E2)
print("After Freq "+ f2)
print("After Wave Length "+ wl2)
print("After Momentum "+ p_f)


print("Phi:  " + Phi)

#Constants ==================================

while t<=4e4:
    rate(10000)
    t += 1
    if Hit == 0:
        Light.pos.x = Light.pos.x + c*dt
        Light.pos.y = 1e8 * sin(t / rad_to_deg)
        if (Light.pos.x)**2 + (Light.pos.y)**2 <= Electron.radius ** 2 :
            Hit = 1   
    else: 
        Light.pos.x = Light.pos.x + c*2* dt
        Light.pos.y = 1e8*sin(t/rad_to_deg)
        
        Light.pos.y = -(Light.pos.x * sin(Theta) - Light.pos.y*cos(Theta))
        
        Electron.velocity = vector(v_e*6e29,v_e*6e29*tan(-Phi),0)
        Electron.pos += Electron.velocity *dt 
        

    
    
   
              
    
                
                
                
                


