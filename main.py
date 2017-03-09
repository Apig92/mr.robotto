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
    
    def is_feasable(self,x,y):
        if(x<self.size and y<self.size and self.map[x][y]==0):
            return True
        else:
            return False
    

class robot:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.position=[x,y]
    
    def current_position(self):
        return self.position
    
    def move_robot(self,x,y,World):
        if(World.is_feasable(x,y)):
            self.position=[x,y]
        return self.position
    
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

def main():
    r=read_data("world1.txt")
    map_size,wall_positions,robot_position,goal=r[1],r[2],r[3],r[4]
    c=World(map_size)
    rbt=robot(int(robot_position[0][1]),int(robot_position[0][2]))
    print(rbt.current_position())
    for i in range(len(wall_positions)):  #set walls
        c.setWalls(int(wall_positions[i][1]),int(wall_positions[i][2]))
    print(c.is_feasable(1, 2))
    print(c.map)
    #print(rbt.move_robot(0, 2,c))
    '''
    rbt.move_up(1, 0,c.map,map_size)
    print(rbt.current_position())
    rbt.move_up(1, 0,c.map,map_size) 
    print(rbt.current_position())
    rbt.move_right(0, 2,c.map,map_size)
    print(rbt.current_position())
    '''
    #rbt.move_robot(7, 0,c)
    rbt.move_robot(0, 7, c)
    print(rbt.current_position())

    print(rbt.current_position())
    if(rbt.goal_reached(int(goal[0][1]), int(goal[0][2]))):
        print("goal reached")
    
if __name__ == '__main__':
    main()