import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Drawing Program')
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    drawing = False
    color = BLACK
    
    while True:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  
                    mode = 'rectangle'
                elif event.key == pygame.K_c:  
                    mode = 'circle'
                elif event.key == pygame.K_e:  
                    mode = 'eraser'
                elif event.key == pygame.K_1: 
                    color = BLACK
                elif event.key == pygame.K_2:  
                    color = RED
                elif event.key == pygame.K_3:  
                    color = GREEN
                elif event.key == pygame.K_4:  
                    color = BLUE
                elif event.key == pygame.K_5:  
                    mode = 'square'
                elif event.key == pygame.K_6:  
                    mode = 'right_triangle'
                elif event.key == pygame.K_7:  
                    mode = 'equilateral_triangle'
                elif event.key == pygame.K_8:  
                    mode = 'rhombus'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
                    points = [event.pos]
                elif event.button == 3:
                    if mode == 'circle':
                        pygame.draw.circle(screen, WHITE, event.pos, radius + 1)
                    elif mode == 'rectangle':
                        pygame.draw.rect(screen, WHITE, (event.pos[0] - radius, event.pos[1] - radius, radius * 2, radius * 2))
                    elif mode == 'square':
                        side_length = radius * 2
                        pygame.draw.rect(screen, WHITE, (event.pos[0], event.pos[1], side_length, side_length))
                    elif mode == 'right_triangle':
                        pygame.draw.polygon(screen, WHITE, [event.pos, (event.pos[0] + radius * 2, event.pos[1]), (event.pos[0], event.pos[1] + radius * 2)])
                    elif mode == 'equilateral_triangle':
                        height = radius * 2 * (3 ** 0.5) / 2
                        pygame.draw.polygon(screen, WHITE, [event.pos, (event.pos[0] + radius * 2, event.pos[1]), (event.pos[0] + radius, event.pos[1] - height)])
                    elif mode == 'rhombus':
                        pygame.draw.polygon(screen, WHITE, [(event.pos[0], event.pos[1] - radius), (event.pos[0] + radius, event.pos[1]), (event.pos[0], event.pos[1] + radius), (event.pos[0] - radius, event.pos[1])])
                    elif mode == 'eraser':
                        pygame.draw.circle(screen, WHITE, event.pos, radius)
            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False
                if mode == 'circle':
                    pygame.draw.circle(screen, color, event.pos, radius)
                elif mode == 'rectangle':
                    pygame.draw.rect(screen, color, (points[0][0], points[0][1], event.pos[0] - points[0][0], event.pos[1] - points[0][1]))
        
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    points.append(event.pos)
                    if mode == 'circle':
                        pygame.draw.circle(screen, color, event.pos, radius)
                    elif mode == 'rectangle':
                        pygame.draw.rect(screen, color, (points[0][0], points[0][1], event.pos[0] - points[0][0], event.pos[1] - points[0][1]))

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
