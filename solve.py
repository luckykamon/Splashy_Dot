def solve():
  debut = []
  for ligne in range(7):
    for colonne in range(7):
      if grille[ligne][colonne] == 3:
        debut = [ligne, colonne]
  point = []
  for ligne in range(7):
    point.append([[False, False, False, False], [False, False, False, False], [False, False, False, False], [False, False, False, False], [False, False, False, False], [False, False, False, False], [False, False, False, False]])
  for ligne in range(7):
    for colonne in range(7):
      if grille[ligne][colonne] == 1 or grille[ligne][colonne] == 3: #point vert ou smil
        if drosans(ligne,colonne)[1] != colonne:
          point[ligne][colonne][0] = [ligne, drosans(ligne,colonne)[1]]
        if gausans(ligne,colonne)[1] != colonne:
          point[ligne][colonne][1] = [ligne, gausans(ligne,colonne)[1]]
        if bassans(ligne,colonne)[0] != ligne:
          point[ligne][colonne][2] = [bassans(ligne,colonne)[0], colonne]
        if hausans(ligne,colonne)[0] != ligne:
          point[ligne][colonne][3] = [hausans(ligne,colonne)[0], colonne]
  trace = []
  for ligne in range(7):
    trace.append([[False, False, False, False], [False, False, False, False], [False, False, False, False], [False, False, False, False], [False, False, False, False], [False, False, False, False], [False, False, False, False]])
  for ligne in range(7):
    for colonne in range(7):
      for pos in range(4):
        trace[ligne][colonne][pos] == point[ligne][colonne][pos]
  #trace est cree
  tab = []
  for ligne in range(7):
    tab.append([0, 0, 0, 0, 0, 0, 0])
  for ligne in range(7):
    for colonne in range(7):
      tab[ligne][colonne] = grille[ligne][colonne]
  test = True
  save = rentre(trace, debut)
  while test:
    save1 = []
    for k in range(len(save)):
      if k % 3 == 0:
        save1.append(rentre(save[k], save[k+1], save[k+2]))
    for j in range(len(save1)):
      if j % 3 == 0:
        rentreGrille = []
        for ligne in range(7):
          rentreGrille.append([0, 0, 0, 0, 0, 0, 0])
        for ligne in range(7):
          for colonne in range(7):
            rentreGrille[ligne][colonne] = grille[ligne][colonne]
        for h in save1[j]:
          if h == "droite":
          
def rentre(sol, trace, debut): #debut de la solution
  save = []
  trace0 = [[[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]], [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]], [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]], [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]], [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]], [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]], [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]]
  trace1 = [[[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]], [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]], [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]], [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]], [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]], [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]], [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]]
  trace2 = [[[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]], [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]], [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]], [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]], [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]], [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]], [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]]
  trace3 = [[[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]], [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]], [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]], [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]], [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]], [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]], [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]]
  for ligne in range(7):
    for colonne in range(7):
      for choix in range(4):
        trace0[ligne][colonne][choix] = trace[ligne][colonne][choix]
        trace1[ligne][colonne][choix] = trace[ligne][colonne][choix]
        trace2[ligne][colonne][choix] = trace[ligne][colonne][choix]
        trace3[ligne][colonne][choix] = trace[ligne][colonne][choix]
  for choix in range(4):
    if trace0[debut[0]][debut[1]][choix] != False:
      if choix == 0:
        debut1 = [debut[0], debut[1]]
        for l in range(7):
          for c in range(7):
            for n in range(4):
              if trace0[l][c][n] == [debut1[0], debut1[1]]:
                trace0[l][c][n] = False
        debut1[0] = drosans(debut1[0], debut1[1])[0]
        debut1[1] = drosans(debut1[0], debut1[1])[1]
        save.append(sol + ["droite"])
        save.append(trace0)
        save.append(debut1)
      if choix == 1:
        debut2 = [debut[0], debut[1]]
        for l in range(7):
          for c in range(7):
            for n in range(4):
              if trace1[l][c][n] == [debut2[0], debut2[1]]:
                trace1[l][c][n] = False
        debut2[0] = gausans(debut2[0], debut2[1])[0]
        debut2[1] = gausans(debut2[0], debut2[1])[1]
        save.append(sol + ["gauche"])
        save.append(trace1)
        save.append(debut2)
      if choix == 2:
        debut3 = [debut[0], debut[1]]
        for l in range(7):
          for c in range(7):
            for n in range(4):
              if trace2[l][c][n] == [debut3[0], debut3[1]]:
                trace2[l][c][n] = False
        debut3[0] = bassans(debut3[0], debut3[1])[0]
        debut3[1] = bassans(debut3[0], debut3[1])[1]
        save.append(sol + ["bas"])
        save.append(trace2)
        save.append(debut3)
      if choix == 3:
        debut4 = [debut[0], debut[1]]
        for l in range(7):
          for c in range(7):
            for n in range(4):
              if trace3[l][c][n] == [debut4[0], debut4[1]]:
                trace3[l][c][n] = False
        debut4[0] = hausans(debut4[0], debut4[1])[0]
        debut4[1] = hausans(debut4[0], debut4[1])[1]
        save.append(sol + ["haut"])
        save.append(trace3)
        save.append(debut4)
  return save

def drosans(ligne, colonne):
  for depla in range(colonne + 1, 7):
    if grille[ligne][depla] == 2:
      if ballout():
        return [ligne, depla, -1]
      else:
        break
    if grille[ligne][depla] == 1:
      return [ligne, depla, 0]
  return [ligne, colonne, 0]  

def gausans(ligne, colonne):
  for depla in range(colonne + 1):
    if grille[ligne][colonne - depla] == 2:
      if ballout():
        return [ligne, colonne - depla, -1]
      else:
        break
    if grille[ligne][colonne - depla] == 1:
      return [ligne, colonne - depla, 0]
  return [ligne, colonne, 0]

def bassans(ligne, colonne):
  for depla in range(ligne + 1, 7):
    if grille[depla][colonne] == 2:
      if ballout():
        return [depla, colonne, -1]
      else:
        break
    if grille[depla][colonne] == 1:
      return [depla, colonne, 0]
  return [ligne, colonne, 0]

def hausans(ligne, colonne):
  for depla in range(1, ligne + 1):
    if grille[ligne - depla][colonne] == 2:
      if ballout():
        return [ligne - depla, colonne, -1]
      else:
        break  
    if grille[ligne - depla][colonne] == 1:
      return [ligne - depla, colonne, 0]
  return [ligne, colonne, 0]  
