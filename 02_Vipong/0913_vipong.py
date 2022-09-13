from math import pi, sin, cos
import random

# later, usepygraph to make this visualization.
#line = [[1,1],[2,4]]

simulation_num = 10000

#prallel line's max length
parallel_length = 100000

#needle length
needle_length = 1

d = 2
#this is half of d
d_height = d/2

#pecentage
num_cossed = 0
num_ncross = 0
persentA = (2*needle_length)/(d*pi)

simulation_num = int(input("simulation_num: "))
parallel_length = int(input("parallel_length: "))
d = float(input("d : "))

for i in range(simulation_num):
    a_1 = random.uniform(0, parallel_length)
    b_1 = random.uniform(d_height*-1, d_height)
    theta = random.uniform(0, pi/2)
    a_2 = a_1 + needle_length*cos(theta)
    b_2 = b_1 + needle_length*sin(theta)

    #crossed, it will be -1
    if b_2*b_1 <=0:
        num_cossed+=1
    else:
        num_ncross+=1

#find the persentage
calc_presentA = num_cossed/simulation_num

print("simulated %d times, parrallel line is considered %d\nsimulated persentage %.4f, calcuated persentage %.4f" %(simulation_num,parallel_length, calc_presentA, persentA))

difference = (abs(persentA-calc_presentA)/persentA)*100
print("difference persentage %f%%" % difference)
