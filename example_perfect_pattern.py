__author__ = 'Kamil Koziara & Taiyeb Zahir'

import cProfile

import numpy
from utils import generate_pop, HexGrid, draw_hex_grid
from stops_ import Stops2

secretion = numpy.array([0,5])
reception = numpy.array([3,4])
receptors = numpy.array([-1,-1])
bound=numpy.array([1,1,1,1,1,1])

base1=numpy.array([0,0,1,0,0,0])
base2=numpy.array([0,0,0,0,0,0])


trans_mat = numpy.array([[0,0,0,0,0,0], #Delta_ligand
                         [20,0,2,0,0,0], #dummy
			 [0,0.0005,0,0,1,0], #Delta
                         [0,-1,-2,0,0,1], #notch receptor
                         [0,0,1,0,0,0],#basal
                         [0,0,0,0,0,0] #sequential activation
                         ])

init_pop = generate_pop([(50, base1), (2450, base2)])
grid = HexGrid(50, 50, 1)

def color_fun(row):
    if row[2]==1:
        return 1
    elif row[3]==1:
        return 0.75
    else:
        return 0.



def run():
    x = Stops2(trans_mat, init_pop, grid.adj_mat, bound, secretion, reception, receptors, secr_amount=6, leak=0, max_con=6, max_dist=1.5, opencl=False)
    for i in range(10000):
        x.step()
        if i%100 == 0:
            print i
            draw_hex_grid("pics/f%04d.png"%i, x.pop, grid, color_fun)


cProfile.run("run()")
