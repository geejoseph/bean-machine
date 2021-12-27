from vpython import *

# Metric units
g = 9.81 # m/s^2

box_width = 700 # m, could also calculate from n_layers
box_height = 700 # m
canvas(title='Bean machine', width=box_width, height=box_height)

peg_radius = 0.01 # m, pegs are cylinders
peg_width = 0.02 # m
gap_between_pegs = 0.06 # m, horizontal gap between pegs
gap_between_layers = 0.04 # m, vertical gap between layers
n_layers = 5

ball_radius = 0.01 # m
ball_mass = 0.2 # kg

# Initialize pegs (next: keep list of pegs)
center_v = vector(0, 0, 0)
initial_peg_pos = center_v + vector(0, 0, -peg_width/2) # position of first peg
peg_axis = vector(0, 0, peg_width)
peg_gap = vector(gap_between_pegs, 0, 0)
layer_gap = vector(-gap_between_pegs/2, -gap_between_layers, 0)

pegs = []
for i in range(n_layers):
    for j in range(i+1):
        peg_pos = initial_peg_pos + i*layer_gap + j*peg_gap
        peg = cylinder(pos=peg_pos, axis=peg_axis, radius=peg_radius)
        peg.truecenter = peg_pos + vector(0, 0, peg_width/2)
        pegs.append(peg)
 
# Initialize floor and walls at bottom

floor_level = -n_layers*gap_between_layers # really "wall start level"

# Generate ball above first peg (next: randomly generate balls in window above)
# Starting with zero velocity

offcenter = 0.0012
initial_ball_pos = center_v + vector(offcenter, 0.6*gap_between_layers, 0)
ball = sphere(pos=initial_ball_pos, radius=ball_radius)
ball.mass = ball_mass
ball.v = vector(0, 0, 0)
ball.a = vector(0, -g, 0)
dt = 0.0002
frame_rate = 200
# if dt is smaller, frame rate has to be larger?
tolerance = 0.00001
bounce_radius = 0.001
contact_dist2 = (ball_radius + peg_radius)**2

def intersection(ball):
    for peg in pegs:
        c2c = peg.truecenter - ball.pos # center to center
        if abs(mag2(c2c) - contact_dist2) < tolerance:
            # reverse component of velocity along normal vector
            normal_v = proj(ball.v, c2c)
            ball.v -= 2*normal_v
            ball.v *= 0.75 #damping
            ball.pos += ball.v*dt
            ball.v += ball.a*dt
            ball.pos += ball.v*dt
            ball.v += ball.a*dt
            break

touchdown = False
while not touchdown:
    rate(frame_rate)
    ball.pos += ball.v*dt
    ball.v += ball.a*dt
    intersection(ball)
    if ball.pos.y < floor_level:
        touchdown = True

# Keep list of balls?
# On each run, check if ball has hit floor
# Then check each ball against each peg
# Next: organize pegs by layers and keep track of which layer ball is on
# Next: for each ball, keep track of if it has reached bottom
# Next: for each ball, keep track of the next peg it will hit
# and during collision use if it is going left or right
# Next: remove nonactive balls from list
# If ball hits
# To stack balls, can just change ground level for each slot as balls fall in
