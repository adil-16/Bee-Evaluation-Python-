import pygame
import random
import math

#imports all pygame modules
pygame.init()

pygame.display.set_caption("AI Project")
#win is the total display (surface) size e.g. resolution
win = pygame.display.set_mode((1000,600))
# surface = pygame.Surface((1000, 600))
surface = pygame.image.load("pic.jpeg")
Mediumfont = pygame.font.SysFont('Calibri', 20, True, False)
WHITE = (255,255,255)

#this is the initial position of our character
x = 20
y = 20

#This width and height is same for all obstacles and our character
width = 20
height = 20
vel = 10
Level = 0
Check = True


def CreateBee():

    #These are the x and y movements of the obstacles
    #When The obstacle meets the X and Y end value... It disappears
    XStart = random.randint(100,1000)
    YStart = random.randint(100,600)
    XEnd = random.randint(0,1000)
    YEnd = random.randint(0,600)
    Velocity = random.randint(5,20)
    return XStart,YStart,XEnd,YEnd,Velocity

#This method selects parent and does a crossover
def Training(Sample):
    TotalScore = 0
    HighestScore = 0
    Scores = []
    BabyChosen = False
    for x in Sample:
        #velocity/commulative distance
        if x[4]/x[5] > HighestScore:
            #In x[6] +1 is incremented
            #commulative distance / +1 incremented 
            HighestScore = x[5]//x[6]
            
            
    for x in Sample:

        Scores.append(HighestScore - (x[4]//x[5]))
        TotalScore = TotalScore + (HighestScore - (x[4]//x[5]))
    #Selecting Parents
    Choice1 = random.randint(0,TotalScore)
    Choice2 = random.randint(0,TotalScore)
    Temp = 0
    Chosen1 = False
    Chosen2 = False
    #Creating a new OffSpring
    while not BabyChosen:
        if Choice1 - Scores[Temp] <0:
            print(f"{Choice1 - Scores[Temp]}")
            #Index of Score array is stored where lowest value is observed
            if not Chosen1:
                Position1 = Temp
                Chosen1 = True
        if Choice2 - Scores[Temp] <0:
            print(f"{Choice2 - Scores[Temp]}")
            #Index of Score array is stored where lowest value is observed
            if not Chosen2:
                Position2 = Temp
                Chosen2 = True
             
        Choice1 = Choice1 - Scores[Temp]
        Choice2 = Choice2 - Scores[Temp]
        if Chosen1 and Chosen2:
            BabyChosen = True
        Temp = Temp + 1 
    VelocityChoice = random.randint(0,100)
    
    #crossover having 50% attributes from its parents
    if VelocityChoice >= 50:
        NewBee = (Sample[Position1][0],Sample[Position2][1],Sample[Position1][2],Sample[Position2][3],Sample[Position1][4])
        VelocityChoice = random.randint(0,100)
        #attribute mutations
        if VelocityChoice >= 90:
            ChangeNumber = random.randint(-200,200)
            if Sample[Position1][0] + ChangeNumber >0 and Sample[Position1][0] + ChangeNumber <1000: 
                NewBee = (Sample[Position1][0] + ChangeNumber,Sample[Position2][1],Sample[Position1][2],Sample[Position2][3],Sample[Position1][4])
        VelocityChoice = random.randint(0,100)
        if VelocityChoice >= 90:
            ChangeNumber = random.randint(-200,200)
            if Sample[Position1][1] + ChangeNumber >0 and Sample[Position1][1] + ChangeNumber <600: 
                NewBee = (Sample[Position1][0],Sample[Position2][1] + ChangeNumber,Sample[Position1][2],Sample[Position2][3],Sample[Position1][4])
        if VelocityChoice >= 90:
            ChangeNumber = random.randint(-200,200)
            if Sample[Position1][2] + ChangeNumber >0 and Sample[Position1][2] + ChangeNumber <1000: 
                NewBee = (Sample[Position1][0],Sample[Position2][1],Sample[Position1][2] + ChangeNumber,Sample[Position2][3],Sample[Position1][4])
        VelocityChoice = random.randint(0,100)
        if VelocityChoice >= 90:
            ChangeNumber = random.randint(-200,200)
            if Sample[Position1][3] + ChangeNumber >0 and Sample[Position1][3] + ChangeNumber <600: 
                NewBee = (Sample[Position1][0],Sample[Position2][1],Sample[Position1][2],Sample[Position2][3] + ChangeNumber,Sample[Position1][4])
        VelocityChoice = random.randint(0,100)
        if VelocityChoice >= 90:
            ChangeNumber = random.randint(-10,10)
            if Sample[Position1][4] + ChangeNumber >0 and Sample[Position1][4] + ChangeNumber <30: 
                NewBee = (Sample[Position1][0],Sample[Position2][1],Sample[Position1][2],Sample[Position2][3],Sample[Position1][4] + ChangeNumber)
                
    if VelocityChoice < 50:
        NewBee = (Sample[Position2][0],Sample[Position1][1],Sample[Position2][2],Sample[Position1][3],Sample[Position2][4])
        VelocityChoice = random.randint(0,100)
        if VelocityChoice >= 90:
            ChangeNumber = random.randint(-200,200)
            if Sample[Position2][0] + ChangeNumber >0 and Sample[Position2][0] + ChangeNumber <1000: 
                NewBee = (Sample[Position2][0] + ChangeNumber,Sample[Position1][1],Sample[Position2][2],Sample[Position1][3],Sample[Position2][4])
        VelocityChoice = random.randint(0,100)
        if VelocityChoice >= 90:
            ChangeNumber = random.randint(-200,200)
            if Sample[Position2][1] + ChangeNumber >0 and Sample[Position2][1] + ChangeNumber <600: 
                NewBee = (Sample[Position2][0],Sample[Position1][1] + ChangeNumber,Sample[Position2][2],Sample[Position1][3],Sample[Position2][4])
        if VelocityChoice >= 90:
            ChangeNumber = random.randint(-200,200)
            if Sample[Position2][2] + ChangeNumber >0 and Sample[Position2][2] + ChangeNumber <1000: 
                NewBee = (Sample[Position2][0],Sample[Position1][1],Sample[Position2][2] + ChangeNumber,Sample[Position1][3],Sample[Position2][4])
        VelocityChoice = random.randint(0,100)
        if VelocityChoice >= 90:
            ChangeNumber = random.randint(-200,200)
            if Sample[Position2][3] + ChangeNumber >0 and Sample[Position2][3] + ChangeNumber <600: 
                NewBee = (Sample[Position2][0],Sample[Position1][1],Sample[Position2][2],Sample[Position1][3] + ChangeNumber,Sample[Position2][4])
        VelocityChoice = random.randint(0,100)
        if VelocityChoice >= 90:
            ChangeNumber = random.randint(-10,10)
            if Sample[Position2][4] + ChangeNumber >0 and Sample[Position2][4] + ChangeNumber <30: 
                NewBee = (Sample[Position2][0],Sample[Position1][1],Sample[Position2][2],Sample[Position1][3],Sample[Position2][4] + ChangeNumber)

    return NewBee
run = True
Start = True

#The No. of obstacles
AmountOfBees = 10
Bees = []
BeesEvolution = []

while run:
    #This is the surface image that is shown on the UI
    # surface.fill((100,100,100))
    surface = pygame.image.load("pic.jpeg")
    surface = pygame.transform.scale(surface , (1000, 600))
    # surface.set_alpha(0)
    #This is the color black behind the surface
    win.fill((0,0,0))
    #It is like fps in a game and speed of the movement
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()

    #As we defined the initial position of our character movement as x=20, so this position is our left most
    if keys[pygame.K_LEFT] and x>=20:
        x = x-vel

    #As we defined the most right position of our character movement as x=950 in pygame.draw.rect(), so this position is our right most
    if keys[pygame.K_RIGHT] and x <= 950:
        x = x +vel

    #As we defined the initial position of our character movement as y=20, so this position is our top most
    if keys[pygame.K_UP] and y >=20:
        y = y -vel

    #As we defined the most bottom position of our character movement as y=550 in pygame.draw.rect(), so this position is our bottom most
    if keys[pygame.K_DOWN] and y <=550:
        y = y +vel

    if Start:
        #loop from 0 to 10
        for n in range(0,AmountOfBees):
          #character and obstacles will be created
          #Info stores x, y start and end along with the velocity of every obstacle per iteration
            Info = CreateBee()
            Bees.append(Info)
            Info = Info + (0,0,)
            BeesEvolution.append(Info)
        Start = False

    BeesEvolutionTemp = []

    #This if statement runs if the Bees array is empty
    #This if statement will run with every level except level 0
    #crossover?
    if not Bees:
        count = 0
        for x in range(0,AmountOfBees):
            if x != AmountOfBees-1:
                Info = Training(BeesEvolution)
                count = count+1
                #Bees Stores population
                Bees.append(Info)
                Info = Info + (0,0,)
                BeesEvolutionTemp.append(Info)
            
            #For the last obstacle, we are randomly generated positions
            else:
                Info = CreateBee()
                Bees.append(Info)
                Info = Info + (0,0,)
                BeesEvolutionTemp.append(Info)         
        BeesEvolution = BeesEvolutionTemp

        #Here Amount of Bees is increasing per level
        AmountOfBees = AmountOfBees + 5
    #This is the Goal Rectangle

    goalX = 950
    goalY = 550
    goalWidth = 100
    goalHeight = 60
    thruster_x = goalX
    thruster_y = goalY + goalHeight // 2
    thruster_width = 50
    thruster_height = 20

    points = [(goalX - width // 2, goalY - height // 2),
              (goalX + width // 2, goalY - height // 2),
              (goalX, goalY + height // 2)]
    pygame.draw.polygon(surface, (249, 148, 4), points)
    pygame.draw.circle(surface, (97, 97, 118), (goalX, goalY - goalHeight // 4), goalWidth // 4)

    # Draw the thruster
    pygame.draw.rect(surface, (0, 255, 255), (thruster_x - thruster_width // 2, thruster_y - thruster_height // 2, thruster_width, thruster_height))
    # pygame.draw.rect(surface, (155,96,12), pygame.Rect(950,550,1000,600))

    
    
    Temp = 0 
    for bee in Bees:
        #if the difference of the start and end of X and Y dimensions of a bee is greater than [-10,10]
        #Then this if statement executes
        if not (bee[0] - bee[2] <=10 and bee[0] - bee[2] >= -10 and bee[1] - bee[3] <=10 and bee[1] - bee[3] >= -10):
            #It is used to draw a rectangle
            #1st parameter is the surface where to draw...
            #2nd parameter is the color (rgb)
            #3rd parameter is the positions and dimensions and width and height
            #These Are the Obstacles

            eye_x = bee[0] + width // 2
            eye_y = bee[1] + height // 2
            eye_radius = 20
            pupil_width = 10
            pupil_height = 10

            # pygame.draw.rect(surface, (100,100,0), pygame.Rect(bee[0],bee[1],width,height))
            
            # Draw the monster's body
            pygame.draw.circle(surface, (255, 255, 255), (bee[0], bee[1]), width // 2)

            # Draw the eyes
            pygame.draw.circle(surface, (255, 255, 255), (eye_x - width // 4, eye_y - height // 4), eye_radius)
            pygame.draw.circle(surface, (255, 255, 255), (eye_x + width // 4, eye_y - height // 4), eye_radius)

            # Draw the pupils
            pygame.draw.rect(surface, (0, 0, 0), (eye_x - width // 4 - pupil_width // 2, eye_y - height // 4 - pupil_height // 2, pupil_width, pupil_height))
            pygame.draw.rect(surface, (0, 0, 0), (eye_x + width // 4 - pupil_width // 2, eye_y - height // 4 - pupil_height // 2, pupil_width, pupil_height))

        
        #If XStart is greater than XEnd
        #This is crossover
        if bee[0] > bee[2]:
            if bee[0] - (bee[4]//2) > bee[2]:
                Bees[Temp] = (Bees[Temp][0] - (bee[4]//2),Bees[Temp][1],Bees[Temp][2],Bees[Temp][3], Bees[Temp][4])
            else:
                Bees[Temp] = (Bees[Temp][2],Bees[Temp][1],Bees[Temp][2],Bees[Temp][3], Bees[Temp][4])
        
        #If YStart is greater than YEnd
        if bee[1] > bee[3]:
            if bee[1] - (bee[4]//2) > bee[3]:
                Bees[Temp] = (Bees[Temp][0],Bees[Temp][1] - (bee[4]//2),Bees[Temp][2],Bees[Temp][3], Bees[Temp][4])
            else:
                Bees[Temp] = (Bees[Temp][0],Bees[Temp][3],Bees[Temp][2],Bees[Temp][3], Bees[Temp][4])
        #If XStart is smaller than XEnd
        if bee[0] < bee[2]:
            if bee[0] + (bee[4]//2) < bee[2]:
                Bees[Temp] = (Bees[Temp][0] + (bee[4]//2),Bees[Temp][1],Bees[Temp][2],Bees[Temp][3], Bees[Temp][4])
            else:
                Bees[Temp] = (Bees[Temp][2],Bees[Temp][1],Bees[Temp][2],Bees[Temp][3], Bees[Temp][4])
        #If YStart is smaller than YEnd
        if bee[1] < bee[3]:
            if bee[1] + (bee[4]//2) < bee[3]:
                Bees[Temp] = (Bees[Temp][0],Bees[Temp][1] + (bee[4]//2),Bees[Temp][2],Bees[Temp][3], Bees[Temp][4])
            else:
                Bees[Temp] = (Bees[Temp][0],Bees[Temp][3],Bees[Temp][2],Bees[Temp][3], Bees[Temp][4])
        Temp1 = 0
        #Population completes here
        for EvoBee in BeesEvolution:
            if EvoBee[2] == bee[2] and EvoBee[3] == bee[3]:
                #Distance is calculated using the initial Position of the obstacle which is closer to our character
                Intial = ((bee[0] - x)**2) + ((bee[1] - y)**2)
                Distance = math.sqrt(Intial)
                BeesEvolution[Temp1] = (BeesEvolution[Temp1][0],BeesEvolution[Temp1][1],BeesEvolution[Temp1][2],BeesEvolution[Temp1][3],BeesEvolution[Temp1][4],BeesEvolution[Temp1][5]+Distance,BeesEvolution[Temp1][6]+1 )
            Temp1 = Temp1 +1
        
        Temp = Temp + 1
        

    #This is the goal position for our character
    #Level is incremented here
    if x >900 and y >500:
        Bees = []
        x = 20
        y = 20
        Level = Level + 1
    Collision = False
    
    #If our character collides with obstacles, game restarts
    for w in range(0,width):
        for h in range(0,height):
            #we will get the color at this specific position on the surface
            #It is using 32 bits per pixel (RGBA)
            #Here Alpha value is set to 255 means the surface is opaque
            Colour = surface.get_at((x+w,y+h))
            #(0,0,0,255) is black
            #(0,255,0,255) is green
            if Colour == (255,255,255,255):
                Collision = True
                Bees = []
                BeesEvolution = []
                Level = 0
                
    if Collision == True:
        Start = True
        AmountOfBees = 10
        x = 20
        y = 20        
    #new level starts here... with a level increment
    else:
        #Red Color
        # pygame.draw.rect(surface, (255,255,255), pygame.Rect(x,y,width,height))

        # Draw the stickman's body
        pygame.draw.line(surface, (67, 12, 77), (x, y), (x, y + height), width)

        # Draw the stickman's arms
        pygame.draw.line(surface, (77, 29, 12), (x - width, y + height // 2), (x + width, y + height // 2), width)

        # Draw the stickman's legs
        pygame.draw.line(surface, (12, 21, 77), (x, y + height), (x - width, y + height * 2), width)
        pygame.draw.line(surface, (12, 21, 77), (x, y + height), (x + width, y + height * 2), width)

        # Draw the stickman's head
        pygame.draw.circle(surface, (0, 0, 0), (x, y), width)

         # Draw the stickman's hands
        pygame.draw.circle(surface, (239, 147, 14), (x - width, y + height // 2), width // 2)
        pygame.draw.circle(surface, (239, 147, 14), (x + width, y + height // 2), width // 2)
    
    text = Mediumfont.render("Level: "+str(Level), True, WHITE)
    #To Draw the surface
    win.blit(surface, (0,0))
    win.blit(text,(900,30))  
    pygame.display.update()

pygame.quit()

