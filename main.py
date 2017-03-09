import re
from copy import deepcopy
from src import ADT

class Stack:
    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        if len(self.items)==0:
            return self.items==[]
        else:
            return False
    
    def add(self,item):
        self.items.append(item)
        
    def remove(self):
        self.items.pop()
    
    def check_last_item(self):
        return self.items[len(self.items)-1]
        
    def size(self):
        return len(self.items)
        
class World:
    def __init__(self,size):
        self.size=size
        self.map=[[0]*size for _ in range(0,size)]
    
    def setWalls(self,x,y):
        self.map[x][y]=1
        return self.map
    
    def is_feasible(self,x,y):
        if(x<self.size and y<self.size and self.map[x][y]==0):
            return True
        else:
            return False
        
    

class robot:
    def __init__(self,x,y,goalx,goaly):
        self.x=x
        self.y=y
        self.goalx= goalx
        self.goaly= goaly
        self.goal_reached = False
        self.position=[x,y]
    
    def current_position(self):
        return self.position
    
    def move_robot(self,x,y,World):
        if(World.is_feasible(x,y)):
            self.position=[x,y]
        return self.position
    
    def goal_reached(self,goalx,goaly):
        if self.position==[goalx,goaly]:
            return True
        else:
            return False
    
    def find_path(self,world,current_path,position):
        if self.goal_reached:
            return False

        if not world.is_feasible(position[0], position[1]):
            return False

        if position==[self.goalx,self.goaly]:
            self.goal_reached = True
            return current_path

        east = [position[0], position[1] + 1]
        west = [position[0], position[1] - 1]
        north = [position[0] + 1, position[1]]
        south = [position[0] - 1, position[1]]

        world.setWalls(position[0], position[1])
        path_copy = deepcopy(current_path)
        path_copy.push(position)
        return (self.find_path(world, path_copy, north) or self.find_path(world, path_copy, south) or
                self.find_path(world, path_copy, east) or self.find_path(world, path_copy, west))
    
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

def main():
    r=read_data("world1.txt")
    map_size,wall_positions,robot_position,goal=r[1],r[2],r[3],r[4]
    c=World(map_size)
    rbt=robot(int(robot_position[0][1]),int(robot_position[0][2]),int(goal[0][1]),int(goal[0][2]))
    print(rbt.current_position())
    print(goal)
    for i in range(len(wall_positions)):  #set walls
        c.setWalls(int(wall_positions[i][1]),int(wall_positions[i][2]))
    start_path = ADT.LinkedStack()
    start_path.push(rbt.current_position())
    print(c.map)
    path = rbt.find_path(c, start_path, rbt.current_position())
    if path:
        print("A path has been found, Size:")
        print(c.map)

    else:
        print("Sorry, no path was found")
    
    
if __name__ == '__main__':
    main()