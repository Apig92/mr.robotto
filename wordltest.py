'''
Created on 9 Mar 2017

@author: pigna
'''

import sys
import re
from main import World,robot

def read_data(filename):
    f = open(filename,"r")
    content = f.readlines()
    f.close()
    map_size=int(content[0][0])
    walls=[]
    r2d2=[]
    goal=[]
    for i in range(len(content)):
        pattern=re.compile("\s*(w)s*,*\s*(-{0,1}\d+)\s*,*\s*(-{0,1}\d+)\s*") #eliminates all unnecessary whitespace
        if pattern.match(content[i]) != None:
            parsed_content=pattern.match(content[i]).groups()
            walls.append(parsed_content)
        pattern1=re.compile("\s*(r2d2)s*,*\s*(-{0,1}\d+)\s*,*\s*(-{0,1}\d+)\s*") #eliminates all unnecessary whitespace
        if pattern1.match(content[i]) != None:
            parsed_content1=pattern1.match(content[i]).groups()
            r2d2.append(parsed_content1)
        pattern2=re.compile("\s*(goal)s*,*\s*(-{0,1}\d+)\s*,*\s*(-{0,1}\d+)\s*") #eliminates all unnecessary whitespace
        if pattern2.match(content[i]) != None:
            parsed_content2=pattern2.match(content[i]).groups()
            goal.append(parsed_content2)
    
    return content,map_size,walls,r2d2,goal

def is_feasable(x,y,mapw,limits):
        if(x<limits and y<limits and mapw[x][y]==0):
            return True
        else:
            return False
    

def test(did_pass):
    line_num=sys._getframe(1).f_lineno
    if did_pass:
        msg="Test at line {0} ok.".format(line_num)
    else:
        msg=("Test at line {0} FAILED.".format(line_num))
    print(msg)
    
def tests_simple():
    r=read_data("world1.txt")
    c=World(r[1])
    w=r[2]
    rc=r[3]
    rb=robot(int(rc[0][1]),int(rc[0][2]))
    print(rb.current_position())
    for i in range(len(r[2])):
        c.setWalls(int(w[i][1]),int(w[i][2]))
  
    print(c.map)
    print()
    rb.move_robot(4, 1,c.map,r[1])
    print(rb.current_position())
    rb.move_robot(9, 1,c.map,r[1])
    print(rb.current_position())
    rb.move_robot(7, 0,c.map,r[1])
    if(rb.goal_reached(7, 0)):
        print("goal reached")