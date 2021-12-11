from vpython import *

# Metric units
g = 9.81 # m/s^2

box_width = 700 # m, could also calculate from n_layers
box_height = 700 # m
canvas(title='Bean machine', width=box_width, height=box_height)

peg_radius = 0.02 # m, pegs are cylinders
peg_width = 0.02 # m
gap_between_pegs = 0.1 # m, horizontal gap between pegs
gap_between_layers = 0.08 # m, vertical gap between layers
n_layers = 5

ball_radius = 0.015 # m
ball_mass = 0.2 # kg

# Initialize pegs (next: keep list of pegs)
initial_peg_pos = vector(0, 0, 0) # position of first peg
peg_axis = vector(0, 0, peg_width)
peg_gap = vector(gap_between_pegs, 0, 0)
layer_gap = vector(-gap_between_pegs/2, -gap_between_layers, 0)

for i in range(n_layers):
    for j in range(i+1):
        peg_pos = initial_peg_pos + i*layer_gap + j*peg_gap 
        cylinder(pos=peg_pos, axis=peg_axis, radius=peg_radius)
    
# Initialize floor and walls at bottom



# Generate ball above first peg (next: randomly generate balls in window above)
# Starting with zero velocity

# Keep list of balls?
# On each run, check if ball has hit floor
# Then check each ball against each peg
# Next: organize pegs by layers and keep track of which layer ball is on
# Next: for each ball, keep track of if it has reached bottom
# Next: for each ball, keep track of the next peg it will hit and during collision use if it is going left or right
# Next: remove nonactive balls from list
# If ball hits
