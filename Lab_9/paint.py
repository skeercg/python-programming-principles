from math import sqrt
import pygame

def triangle_height(a, b):
    return sqrt((b - a)**2 - ((b - a) // 2)**2)

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'
    points = []
    obj = []
    eraser = False
    drawer = True
    rect = False
    circ = False
    rhomb = False
    square = False
    eq_triangle = False
    right_triangle = False
    drag_start = False

    queue = 0
    

    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                #Eraser
                elif event.key == pygame.K_e:
                    eraser = True
                    drawer = False
                    rect = False
                    circ = False
                    square = False
                    rhomb = False
                    eq_triangle = False
                    right_triangle = False
                #Drawer
                elif event.key == pygame.K_d:
                    drawer = True
                    eraser = False
                    rect = False
                    circ = False
                    square = False
                    rhomb = False
                    eq_triangle = False
                    right_triangle = False
                #Draw rectangle
                elif event.key == pygame.K_1:
                    rect = True
                    drawer = False
                    eraser = False
                    circ = False
                    square = False
                    rhomb = False
                    eq_triangle = False
                    right_triangle = False
                #Draw circle
                elif event.key == pygame.K_2:
                    circ = True
                    drawer = False
                    eraser = False
                    rect = False
                    square = False
                    rhomb = False
                    eq_triangle = False
                    right_triangle = False
                #Draw square
                elif event.key == pygame.K_3:
                    square = True
                    circ = False
                    drawer = False
                    eraser = False
                    rect = False
                    rhomb = False
                    eq_triangle = False
                    right_triangle = False
                #Draw rhombus
                elif event.key == pygame.K_4:
                    rhomb = True
                    square = False
                    circ = False
                    drawer = False
                    eraser = False
                    rect = False
                    eq_triangle = False
                    right_triangle = False
                #Draw equilateral triangle
                elif event.key == pygame.K_5:
                    eq_triangle = True
                    rhomb = False
                    square = False
                    circ = False
                    drawer = False
                    eraser = False
                    rect = False
                    right_triangle = False
                elif event.key == pygame.K_6:
                    right_triangle = True
                    eq_triangle = False
                    rhomb = False
                    square = False
                    circ = False
                    drawer = False
                    eraser = False
                    rect = False
            
            if circ:
                if event.type == pygame.MOUSEBUTTONDOWN and not drag_start:
                    position = event.pos
                    circ_start_x, circ_start_y = position
                    drag_start = True
                elif event.type == pygame.MOUSEMOTION and drag_start:
                    position = event.pos
                    circ_finish_x, circ_finish_y = position
                    
                    if mode == 'blue':
                        color = (0, 0, 255)
                    elif mode == 'red':
                        color = (255, 0, 0)
                    elif mode == 'green':
                        color = (0, 255, 0)
                    if len(obj) > 0: 
                        obj.pop()
                    obj.append((pygame.Rect(circ_start_x, circ_start_y, min(circ_finish_x-circ_start_x, circ_finish_y-circ_start_y), min(circ_finish_x-circ_start_x, circ_finish_y-circ_start_y)), color, 0, queue))
                    queue += 1

                elif event.type == pygame.MOUSEBUTTONUP:
                    position = event.pos
                    circ_finish_x, circ_finish_y = position
                    drag_start = False
                    # print ("FINISH", rect_finish_x, rect_finish_y)
                    if mode == 'blue':
                        color = (0, 0, 255)
                    elif mode == 'red':
                        color = (255, 0, 0)
                    elif mode == 'green':
                        color = (0, 255, 0)
                    obj.append((pygame.Rect(circ_start_x, circ_start_y, min(circ_finish_x-circ_start_x, circ_finish_y-circ_start_y), min(circ_finish_x-circ_start_x, circ_finish_y-circ_start_y)), color, 0, queue))
                    queue += 1

            if rect:
                if event.type == pygame.MOUSEBUTTONDOWN and not drag_start:
                    position = event.pos
                    rect_start_x, rect_start_y = position
                    drag_start = True
                    
                elif event.type == pygame.MOUSEMOTION and drag_start:
                    position = event.pos
                    rect_finish_x, rect_finish_y = position
                    if mode == 'blue':
                        color = (0, 0, 255)
                    elif mode == 'red':
                        color = (255, 0, 0)
                    elif mode == 'green':
                        color = (0, 255, 0)
                    cor = [(rect_start_x, rect_start_y), (rect_finish_x, rect_finish_y)]
                    cor = sorted(cor)
                    if len(obj) > 0: 
                        obj.pop()
                    obj.append((pygame.Rect(cor[0][0], cor[0][1], cor[1][0]-cor[0][0], cor[1][1]-cor[0][1]), color, 1, queue))
                    queue += 1
                    
                elif event.type == pygame.MOUSEBUTTONUP:
                    position = event.pos
                    rect_finish_x, rect_finish_y = position
                    drag_start = False
                    # print ("FINISH", rect_finish_x, rect_finish_y)
                    if mode == 'blue':
                        color = (0, 0, 255)
                    elif mode == 'red':
                        color = (255, 0, 0)
                    elif mode == 'green':
                        color = (0, 255, 0)
                    cor = [(rect_start_x, rect_start_y), (rect_finish_x, rect_finish_y)]
                    cor = sorted(cor)
                    obj.append((pygame.Rect(cor[0][0], cor[0][1], cor[1][0]-cor[0][0], cor[1][1]-cor[0][1]), color, 1, queue))
                    queue += 1
            
            if square:
                if event.type == pygame.MOUSEBUTTONDOWN and not drag_start:
                    position = event.pos
                    sq_start_x, sq_start_y = position
                    drag_start = True
                    
                elif event.type == pygame.MOUSEMOTION and drag_start:
                    position = event.pos
                    sq_finish_x, sq_finish_y = position
                    if mode == 'blue':
                        color = (0, 0, 255)
                    elif mode == 'red':
                        color = (255, 0, 0)
                    elif mode == 'green':
                        color = (0, 255, 0)
                    cor = [(sq_start_x, sq_start_y), (sq_finish_x, sq_finish_y)]
                    cor = sorted(cor)
                    if len(obj) > 0: 
                        obj.pop()
                    obj.append((pygame.Rect(cor[0][0], cor[0][1], min(cor[1][0]-cor[0][0], cor[1][1]-cor[0][1]), min(cor[1][0]-cor[0][0], cor[1][1]-cor[0][1])), color, 1, queue))
                    queue += 1
                    
                elif event.type == pygame.MOUSEBUTTONUP:
                    position = event.pos
                    sq_finish_x, sq_finish_y = position
                    drag_start = False
                    # print("START", sq_start_x, sq_start_y)
                    # print ("FINISH", sq_finish_x, sq_finish_y)
                    if mode == 'blue':
                        color = (0, 0, 255)
                    elif mode == 'red':
                        color = (255, 0, 0)
                    elif mode == 'green':
                        color = (0, 255, 0)
                    cor = [(sq_start_x, sq_start_y), (sq_finish_x, sq_finish_y)]
                    cor = sorted(cor)
                    obj.append((pygame.Rect(cor[0][0], cor[0][1], min(cor[1][0]-cor[0][0], cor[1][1]-cor[0][1]), min(cor[1][0]-cor[0][0], cor[1][1]-cor[0][1])), color, 1, queue))
                    queue += 1

            if rhomb:
                if event.type == pygame.MOUSEBUTTONDOWN and not drag_start:
                    position = event.pos
                    rh_start_x, rh_start_y = position
                    drag_start = True
                    
                elif event.type == pygame.MOUSEMOTION and drag_start:
                    position = event.pos
                    rh_finish_x, rh_finish_y = position
                    if mode == 'blue':
                        color = (0, 0, 255)
                    elif mode == 'red':
                        color = (255, 0, 0)
                    elif mode == 'green':
                        color = (0, 255, 0)
                    if len(obj) > 0: 
                        obj.pop()
                    obj.append(([((rh_finish_x + rh_start_x) // 2, rh_start_y), (rh_start_x, (rh_finish_y + rh_start_y) // 2), ((rh_finish_x + rh_start_x) // 2, rh_finish_y), (rh_finish_x, (rh_finish_y + rh_start_y) // 2)], color, 2, queue))
                    queue += 1
                    
                elif event.type == pygame.MOUSEBUTTONUP:
                    position = event.pos
                    rh_finish_x, rh_finish_y = position
                    drag_start = False
                    if mode == 'blue':
                        color = (0, 0, 255)
                    elif mode == 'red':
                        color = (255, 0, 0)
                    elif mode == 'green':
                        color = (0, 255, 0)
                    obj.append(([((rh_finish_x + rh_start_x) // 2, rh_start_y), (rh_start_x, (rh_finish_y + rh_start_y) // 2), ((rh_finish_x + rh_start_x) // 2, rh_finish_y), (rh_finish_x, (rh_finish_y + rh_start_y) // 2)], color, 2, queue))
                    queue += 1

            if eq_triangle:
                if event.type == pygame.MOUSEBUTTONDOWN and not drag_start:
                    position = event.pos
                    eq_tr_start_x, eq_tr_start_y = position
                    drag_start = True
                    
                elif event.type == pygame.MOUSEMOTION and drag_start:
                    position = event.pos
                    eq_tr_finish_x, eq_tr_finish_y = position
                    if mode == 'blue':
                        color = (0, 0, 255)
                    elif mode == 'red':
                        color = (255, 0, 0)
                    elif mode == 'green':
                        color = (0, 255, 0)
                    if len(obj) > 0: 
                        obj.pop()
                    obj.append(([((eq_tr_finish_x + eq_tr_start_x) // 2, eq_tr_start_y), (eq_tr_start_x, eq_tr_start_y + triangle_height(eq_tr_start_x, eq_tr_finish_x)), (eq_tr_finish_x, eq_tr_start_y + triangle_height(eq_tr_start_x, eq_tr_finish_x))], color, 2, queue))
                    queue += 1
                    
                elif event.type == pygame.MOUSEBUTTONUP:
                    position = event.pos
                    eq_tr_finish_x, eq_tr_finish_y = position
                    drag_start = False
                    if mode == 'blue':
                        color = (0, 0, 255)
                    elif mode == 'red':
                        color = (255, 0, 0)
                    elif mode == 'green':
                        color = (0, 255, 0)
                    obj.append(([((eq_tr_finish_x + eq_tr_start_x) // 2, eq_tr_start_y), (eq_tr_start_x, eq_tr_start_y + triangle_height(eq_tr_start_x, eq_tr_finish_x)), (eq_tr_finish_x, eq_tr_start_y + triangle_height(eq_tr_start_x, eq_tr_finish_x))], color, 2, queue))
                    queue += 1

            if right_triangle:
                if event.type == pygame.MOUSEBUTTONDOWN and not drag_start:
                    position = event.pos
                    rg_tr_start_x, rg_tr_start_y = position
                    drag_start = True
                    
                elif event.type == pygame.MOUSEMOTION and drag_start:
                    position = event.pos
                    rg_tr_finish_x, rg_tr_finish_y = position
                    if mode == 'blue':
                        color = (0, 0, 255)
                    elif mode == 'red':
                        color = (255, 0, 0)
                    elif mode == 'green':
                        color = (0, 255, 0)
                    if len(obj) > 0: 
                        obj.pop()
                    obj.append(([(rg_tr_start_x, rg_tr_start_y), (rg_tr_start_x, rg_tr_finish_y), (rg_tr_finish_x, rg_tr_finish_y)], color, 2, queue))
                    queue += 1
                    
                elif event.type == pygame.MOUSEBUTTONUP:
                    position = event.pos
                    rg_tr_finish_x, rg_tr_finish_y = position
                    drag_start = False
                    if mode == 'blue':
                        color = (0, 0, 255)
                    elif mode == 'red':
                        color = (255, 0, 0)
                    elif mode == 'green':
                        color = (0, 255, 0)
                    obj.append(([(rg_tr_start_x, rg_tr_start_y), (rg_tr_start_x, rg_tr_finish_y), (rg_tr_finish_x, rg_tr_finish_y)], color, 2, queue))
                    queue += 1

            if eraser:
                if event.type == pygame.MOUSEMOTION:
                    # if mouse moved, add point to list
                    position = event.pos
                    points = points + [(position, 'white', queue)]
                    queue += 1

            # if event.type == pygame.MOUSEBUTTONUP:
            if drawer: 
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     if event.button == 1: # left click grows radius
                #         radius = min(200, radius + 1)
                #     elif event.button == 3: # right click shrinks radius
                #         radius = max(1, radius - 1)
                if event.type == pygame.MOUSEMOTION:
                    # if mouse moved, add point to list
                    position = event.pos
                    points = points + [(position, mode, queue)]
                    queue += 1
                    # points = points[-256:]
                
        screen.fill((255, 255, 255))
        
        # draw all points
        i = 0
        j = 0
        for k in range(queue):
            if i < len(obj) and j < len(points) - 1:
                if obj[i][3] < points[j][2]:
                    if obj[i][2] == 1:
                        pygame.draw.rect(screen, obj[i][1], obj[i][0])
                    elif obj[i][2] == 0:
                        pygame.draw.ellipse(screen, obj[i][1], obj[i][0])
                    elif obj[i][2] == 2:
                        pygame.draw.polygon(screen, obj[i][1], obj[i][0])
                    i += 1
                else:
                    drawLineBetween(screen,points[j], points[j + 1], radius)
                    j += 1
            
            if i < len(obj) and not j < len(points) - 1:
                while i < len(obj):
                    if obj[i][2] == 1:
                        pygame.draw.rect(screen, obj[i][1], obj[i][0])
                    elif obj[i][2] == 0:
                        pygame.draw.ellipse(screen, obj[i][1], obj[i][0])
                    elif obj[i][2] == 2:
                        print(obj[i][0])
                        pygame.draw.polygon(screen, obj[i][1], obj[i][0])
                    i += 1
            if not i < len(obj) and j < len(points) - 1:
                while j < len(points) - 1:
                    drawLineBetween(screen,points[j], points[j + 1], radius)
                    j += 1
        
        


        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, start, end, width):
    if (start[1] == end[1]):
        if start[1] == 'blue':
            color = (0, 0, 255)
        elif start[1] == 'red':
            color = (255, 0, 0)
        elif start[1] == 'green':
            color = (0, 255, 0)
        elif start[1] == 'white':
            color = (255, 255, 255)
    
        dx = start[0][0] - end[0][0]
        dy = start[0][1] - end[0][1]
        iterations = max(abs(dx), abs(dy))
        
        for i in range(iterations):
            progress = 1.0 * i / iterations
            aprogress = 1 - progress
            x = int(aprogress * start[0][0] + progress * end[0][0])
            y = int(aprogress * start[0][1] + progress * end[0][1])
            pygame.draw.circle(screen, color, (x, y), width)

main()