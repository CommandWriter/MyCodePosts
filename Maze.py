def turn_right():
    turn_left()
    turn_left()
    turn_left()
        
while not at_goal():
    if front_is_clear():
        move()
    elif wall_on_right():
        turn_left()
    elif wall_in_front():
        turn_right()
    else: move()
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
