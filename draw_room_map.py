import gopigo

ANALOG_PIN = 15
DIGITAL_PIN = 10

GRID_SIZE = 10 #cm
ORIGIN=(0,0)
# (0, 1, 2, 3) (top, right, bottom, left) (north, east, south, west)
STARTING_DIRECTION = 1 # right, east
STOP_DISTANCE = 10 # cm



def draw_room_map(node, x, y, origin=(0,0), grid_size=GRID_SIZE):
    ''' Main runtime
        Traverses a room until obstacles are encountered
        Records room shape as 2D cartesian plot with fuzz factor
        fuzz factor is a 4 tuple of obstacle distances with structure:
        (north, east, south, west) where calibraton defaults to
        south -- y-origin
        west -- x-origin
        
        Arguments:
        node -- two-tuple (x, y) of node to traverse
        origin --  two-tuple  is calibrated to be the origin (0, 0)  
        e.g.
        [ [0, 0, (
        
        ]
    '''


def detect_spherical_edges(grid_size=(10,10,10)):
    ''' Maps bounding polygon using spherical coordinate system (rho, theta, phi)
    '''
    raise NotImplementedError

def detect_catestian_edges(grid_size=GRID_SIZE, origin=(0, 0)):
    ''' Maps a bounding polygon using 2d cartestian coordinate system
    '''


def advance_cursor(current_direction, cursor):
    if current_direction == 0:
        new_cursor = (cursor[0], cursor[1]+1)
    elif current_direction == 1:
        new_cursor = (cursor[0]+1, cursor[1])
    elif current_direction == 2:
        new_cursor = (cursor[0], cursor[1]-1)
    elif current_direction == 3:
        new_cursor = (cursor[0]-1, cursor[1])
    return cursor


def follow_axis(cursor, current_direction, room_map=[[]], stop_distance=STOP_DISTANCE):
    (x, y) = cursor
    print(ultrasonic_range())
    while ultrasonic_range() > stop_distance:
        print(x, y)
        # extend known graph boundaries
        # extend x-axis
        if len(room_map) <= x:
            room_map.append([])
            room_map[x][y] = [None, None, None, None]
        # extend y-axis
        if len(room_map[x]) <= y:
            room_map[x].append([])
            room_map[x][y] = [None, None, None, None]
        room_map[x][y][current_direction] = 10
        cursor = advance_cursor(current_direction, cursor)
        gopigo.fwd(GRID_SIZE)
        return follow_axis(cursor, current_direction, room_map)
    # obstacle encountered
    room_map[x][y][current_direction] = ultrasonic_range()
    new_direction = current_direction + 1 if current_direction < 3 else 0
    cursor = advance_cursor(new_direction, cursor)
    gopigo.turn_right_wait_for_completion(90)
    return follow_axis(cursor, new_direction, room_map)

def ultrasonic_range(pin=ANALOG_PIN):
    return gopigo.us_dist(pin)



# main runtime
# yoinked directly from https://en.wikipedia.org/wiki/Flood_fill#Fixed-memory_method_.28right-hand_fill_method.29
if __name__ == '__main__':
    # begin initialization
    cursor = ORIGIN
    current_direction = STARTING_DIRECTION
    mark_1 = None
    mark_2 = None
    backtrack = False
    findloop = False

    # 'paint' forwards in starting direction
    room_map  = follow_axis(cursor, current_direction)
    print(room_map)



    
