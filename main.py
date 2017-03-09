import re

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

class robot:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.position=[x,y]
    
    def current_position(self):
        return self.position
    
    def move_robot(self,x,y,mapw,limits):
        if(is_feasable(x,y,mapw,limits)):
            self.position=[x,y]
            return self.position
    '''
    def move_up(self,x,y,mapw,limits):
        if(is_feasable(x,y,mapw,limits)):
            self.position=[self.x+1,self.y]
            return self.position
    def move_down(self,x,y,mapw,limits):
        if(is_feasable(x,y,mapw,limits)):  
            self.position=[self.x-1,self.y]
            return self.position
    def move_left(self,x,y,mapw,limits):
        if(is_feasable(x,y,mapw,limits)):
            self.position=[self.x,self.y-1]
            return self.position    
    def move_right(self,x,y,mapw,limits):
            self.position=[self.x,self.y+1]
            return self.position
    '''
    def goal_reached(self,goalx,goaly):
        if self.position==[goalx,goaly]:
            return True
        else:
            return False
    '''
    def find_path(self,world,current_path,location,goalx,goaly,mapw,limits,x,y):
        if self.goal_reached(goalx, goaly):
            return False
        if not is_feasable(x, y, mapw, limits):
            return False
        if location == self.
    '''
    
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
    
    
def main():
    r=read_data("world1.txt")
    map_size=r[1]
    c=World(map_size)
    wall_positions=r[2]
    robot_position=r[3]
    rbt=robot(int(robot_position[0][1]),int(robot_position[0][2]))
    print(rbt.current_position())
    for i in range(len(wall_positions)):  #set walls
        c.setWalls(int(wall_positions[i][1]),int(wall_positions[i][2]))
    print(is_feasable(0, 1, c.map, map_size))
    
    print(c.map)
    print()
    print(rbt.current_position())
    '''
    rbt.move_up(1, 0,c.map,map_size)
    print(rbt.current_position())
    rbt.move_up(1, 0,c.map,map_size) 
    print(rbt.current_position())
    rbt.move_right(0, 2,c.map,map_size)
    print(rbt.current_position())
    '''

    if(rbt.goal_reached(7, 0)):
        print("goal reached")
    
if __name__ == '__main__':
    main()