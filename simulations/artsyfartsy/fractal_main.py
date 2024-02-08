# Fractal simulation
# Video: https://www.youtube.com/watch?v=ob8teyuR8dA

import turtle

# Fractal setup
GENERATIONS = 15
CHR_1, RULE_1 = 'A', 'AB'
CHR_2, RULE_2 = 'B', 'A'
STEPSIZE = 50
ANGLE = 60

# Turtle setup
sam = turtle.Turtle()
sam.pensize(1)
sam.speed(0)
sam.pencolor('orange')
sam.color('orange')
sam.clear()

# Screen setup
screen = turtle.Screen()
screen.bgcolor('black')
screen.delay(0)

'''
    Applies the L-system rules on the given axiom.
'''
def apply_rules(axiom):
    
    return ''.join([RULE_1 if c == CHR_1 else RULE_2 for c in axiom])

'''
    Draws a fractal given a fractal, a turtle, and a screen object.
'''
def draw_fractal(fractal, turtle):
    
    for c in fractal:
        turtle.left(ANGLE) if c == CHR_1 else turtle.right(ANGLE)
        turtle.forward(STEPSIZE)

def main():
    axiom = 'A'
    
    for gen in range(GENERATIONS):
        print(f'Generation {gen}: {axiom}')
        axiom = apply_rules(axiom)
     
    #sam.forward(STEPSIZE)    
    draw_fractal(axiom, sam)
    
if __name__ == '__main__':
    main()

# Allow window to close
screen.exitonclick()