cases = int(input())

while cases > 0:
    #width, height, # of shots
    w, h, n = input().split(" ")
    width = int(w)
    height = int(h)
    n = int(n)

    p1coords = []
    p2coords = []

    shots = []

    #Extract coords for ships
    for h in range(height):
        c = input()
        for itx, j in enumerate(c):
            if j == "#":
                p1coords.append((str(itx), str((height - 1) - h)))
    
    for h in range(height):
        c = input()
        for itx, j in enumerate(c):
            if j == "#":
                p2coords.append((str(itx), str((height - 1) - h)))

    #Add shot coordinates
    for i in range(n):
        c1, c2 = input().split(" ")
        shots.append((c1, c2))

    player1 = 0
    finish = False
    pcoords = []
    pcoords.append(p1coords)
    pcoords.append(p2coords)

    #The game
    for i in shots:

        #If the game is finished - continue. (Ain't gonna mess with break)
        if finish:
            continue
        
        #If coords detected in player coordinate
        if i in pcoords[1 - player1]:

            #Remove the coordinate
            pcoords[1 - player1].remove(i)

            #If that player have no coordinates left...
            if len(pcoords[1 - player1]) == 0:

                #Switch player regardless (despite hitting)
                player1 = 1 - player1

                #If it is the first player's turn, then the game is over.
                if player1 == 0:
                    finish = True
        
        #Else switch player
        else:
            player1 = 1 - player1        

    #The conditions - if any ships left -> draw
    #If any player has more ship then the other, they win.
    if len(p1coords) > 0 and len(p2coords) == 0:
        print("player one wins")
    elif len(p1coords) == 0 and len(p2coords) > 0:
        print("player two wins")
    else:
        print("draw")
    
    cases -= 1