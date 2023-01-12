from tools import v2t, t2v
import numpy as np
import matplotlib.pyplot as plt

arrow_size = 1

def draw_vector(origin, vector, color):
    plt.arrow(origin[0], origin[1], vector[0] - origin[0], vector[1] - origin[1], head_width=0.03, head_length=0.03, fc=color, ec=color)

def draw_point(point, color):
    plt.plot(point[0], point[1], marker="o", markersize=1, color=color)

#pose(x, y, theta)
def draw_frame(pose, color):
    plt.arrow(pose[0], pose[1], np.cos(pose[2]), np.sin(pose[2]), head_width=0.02, head_length=0.03, fc=color, ec=color)
    plt.arrow(pose[0], pose[1], np.cos(pose[2] + np.pi/2), np.sin(pose[2] + np.pi/2), head_width=0.02, head_length=0.03, fc=color, ec=color)

if __name__ == '__main__':
    #x, y, theta
    std_frame = np.array([0, 0, 0])
    new_frame_1 = np.array([-0.5, 0.5, np.pi/2])
    new_frame_2 = np.array([-0.5, -0.5, np.pi])

    draw_frame(std_frame, 'r')
    draw_frame(new_frame_1, 'g')
    draw_frame(new_frame_2, 'y')

    hom_vect = np.array([0.5, 0.5, 1])
    draw_vector(std_frame, hom_vect, 'b')
    
    #transform from std_frame to new_frame
    transform_origin_to_1 = v2t(new_frame_1)
    #transform_origin_to_2 = v2t(new_frame_2)
    new_hom_vect_1 = transform_origin_to_1 @ hom_vect
    #new_hom_vect_2 = transform_origin_to_2 @ hom_vect
    draw_vector(new_frame_1, new_hom_vect_1, 'c')
    
    transform_1_to_2 = v2t(new_frame_2 - new_frame_1)
    new_hom_vect_2_2 = transform_1_to_2 @ transform_origin_to_1 @ hom_vect
    draw_vector(new_frame_2, new_hom_vect_2_2, 'c')

    print("std_frame: ", std_frame)
    print("new_frame_1: ", new_frame_1)
    print("new_frame_2: ", new_frame_2)
    print("hom_vect: ", hom_vect)
    print("transform_origin_to_1: ", transform_origin_to_1)
    print("new_hom_vect_1: ", new_hom_vect_1)
    print("transform_1_to_2: ", transform_1_to_2)
    print("new_hom_vect_2_2: ", new_hom_vect_2_2)

    
    plt.xlim([-2, 2])
    plt.ylim([-3, 2])
    plt.show()