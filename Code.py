import turtle
import math

#Trying Git
bob=turtle.Turtle()
bob.getscreen().bgcolor('#994444')


x=int(turtle.numinput("X + i*Y", "Your X:", 1000))+1
y=int(turtle.numinput("X + i*Y", "Your Y:", 1000))
head=int(turtle.numinput("Initial Direction", "1:Real(+)  2:Real(-)", 1000))
ini_x=0
ini_y=0
ini_x=x
ini_y=y
turtle.speed(0)

if(head==2):
    turtle.left(180)
pop_ini=turtle.heading()

#Function to perform some modification
def mutate():
    turtle.color("blue")
    turtle.circle(1)
    turtle.color("black")
    turtle.left(90)
#Finding prime numbers 
def prime(number):
    c=0
    for j in range(2,number+1):
        if(number%j==0):
            c=c+1
    if(c==1):
         mutate()


#Loop
    
while(True):
    
    turtle.forward(5)
    #If real part is zero
    if(x==0):
        if((math.fabs(y)-3)%4==0):
            prime(y)
                
    #If imaginary part is zero        
    elif(y==0):
        if((math.fabs(x)-3)%4==0):
            c=0
            prime(x)


    #If both are zero
    elif((x!=0) & (y!=0)):
        num=x**2 + y**2
        if((num-3)%4!=0):
            prime(num)
                
    #Controlling Co-ordinates
    pos=turtle.heading()
    if(pos==0.0):
        x=x+1
    elif(pos==90.0):
        y=y+1
    elif(pos==180.0):
        x=x-1
    elif(pos==270.0):
        y=y-1
        
    
    
    k=x
    p=y
    if((k==ini_x)&(p==ini_y)&(pos==pop_ini)):
        break
turtle.done()
