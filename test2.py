import time
import sys
import pygame
from pygame.locals import *
from random import randint

def initialiseGrille():
  '''
      Initialize the tab 'grille' 7*7 with '0'
  '''
  global grille
  grille = []
  for ligne in range(7):
    grille.append([0, 0, 0, 0, 0, 0, 0])
  window.blit(pygame.image.load("start.png").convert(), (0,0))
  pygame.display.flip()

def changeGrille(ligne, colonne):
  grille[ligne][colonne] +=1
  grille[ligne][colonne] = grille[ligne][colonne] % 4

def changeImage(ligne, colonne):
  if grille[ligne][colonne] == 0:
      window.blit(pygame.image.load("none.png").convert(), (colonne * 60, ligne * 60))
  if grille[ligne][colonne] == 1:
      window.blit(pygame.image.load("ball.png").convert(), (colonne * 60, ligne * 60))
  if grille[ligne][colonne] == 2:
      window.blit(pygame.image.load("circle.png").convert(), (colonne * 60, ligne * 60))
  if grille[ligne][colonne] == 3:
      window.blit(pygame.image.load("smil.png").convert(), (colonne * 60, ligne * 60))
  pygame.display.flip()

def genereGrille():
  window.blit(pygame.image.load("valider.png").convert(), (360, 420))
  pygame.display.flip()
  ligne = -1
  ligne = -1
  fin = True
  while fin:
    pygame.time.Clock().tick(30)
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
          if event.pos[1] < 60:
            ligne = 0
          if event.pos[1] < 120 and event.pos[1] >= 60:
            ligne = 1
          if event.pos[1] < 180 and event.pos[1] >= 120:
            ligne = 2
          if event.pos[1] < 240 and event.pos[1] >= 180:
            ligne = 3
          if event.pos[1] < 300 and event.pos[1] >= 240:
            ligne = 4
          if event.pos[1] < 360 and event.pos[1] >= 300:
            ligne = 5
          if event.pos[1] < 420 and event.pos[1] >= 360:
            ligne = 6
          if event.pos[0] < 60:
            colonne = 0
          if event.pos[0] < 120 and event.pos[0] >= 60:
            colonne = 1
          if event.pos[0] < 180 and event.pos[0] >= 120:
            colonne = 2
          if event.pos[0] < 240 and event.pos[0] >= 180:
            colonne = 3
          if event.pos[0] < 300 and event.pos[0] >= 240:
            colonne = 4
          if event.pos[0] < 360 and event.pos[0] >= 300:
            colonne = 5
          if event.pos[0] >= 360:
            colonne = 6
          if event.pos[0] >= 360 and event.pos[1] > 420:
            if grilleValideDebut():
              if grilleValideFin():
                if event.pos[1] > 450:
                  window.blit(pygame.image.load("jouer.png").convert(), (0, 420))
                  pygame.display.flip()
                  game()
                else:
                  for ligne in range(7):
                    for colonne in range(7):
                      if grille[ligne][colonne] == 3:
                        repere1 = [ligne, colonne]
                  window.blit(pygame.image.load("solve.png").convert(), (0, 420))
                  pygame.display.flip()
                  affsol(solve(grille))
                  for ligne in range(7):
                    for colonne in range(7):
                      if grille[ligne][colonne] == 3:
                        repere2 = [ligne, colonne]
                  grille[repere1[0]][repere1[1]] = 3
                  grille[repere2[0]][repere2[1]] = 2
                  ligne, colonne = -1, -1
              else:
                window.blit(pygame.image.load("fin.png").convert(), (0, 420))
              pygame.display.flip()
            else:
              window.blit(pygame.image.load("debut.png").convert(), (0, 420))
              pygame.display.flip()
    if ligne != -1 and colonne != -1:
      changeGrille(ligne, colonne) 
      changeImage(ligne, colonne)
      ligne = -1
      colonne = -1

def grilleValideDebut():
  nombreDebut = 0
  for ligne in range(7):
    for colonne in range(7):
      if grille[ligne][colonne] == 3:
        nombreDebut +=1
  if nombreDebut != 1:
    return False
  return True

def grilleValideFin():
  nombreFin = 0
  for ligne in range(7):
    for colonne in range(7):
      if grille[ligne][colonne] == 2:
        nombreFin +=1
  if nombreFin != 1:
    return False
  return True

#Creation de la grille termine

def droite(ligne, colonne):
  for depla in range(colonne + 1, 7):
    if grille[ligne][depla] == 2:
      if ballout():
        return [ligne, depla, -1]
      else:
        break
    if grille[ligne][depla] == 1:
      grille[ligne][depla] = 0
      return [ligne, depla, 0]
  return [ligne, colonne, 0]

def gauche(ligne, colonne):
  for depla in range(colonne + 1):
    if grille[ligne][colonne - depla] == 2:
      if ballout():
        return [ligne, colonne - depla, -1]
      else:
        break
    if grille[ligne][colonne - depla] == 1:
      grille[ligne][colonne - depla] = 0
      return [ligne, colonne - depla, 0]
  return [ligne, colonne, 0]

def bas(ligne, colonne):
  for depla in range(ligne + 1, 7):
    if grille[depla][colonne] == 2:
      if ballout():
        return [depla, colonne, -1]
      else:
        break
    if grille[depla][colonne] == 1:
      grille[depla][colonne] = 0
      return [depla, colonne, 0]
  return [ligne, colonne, 0]

def haut(ligne, colonne):
  for depla in range(1, ligne + 1):
    if grille[ligne - depla][colonne] == 2:
      if ballout():
        return [ligne - depla, colonne, -1]
      else:
        break  
    if grille[ligne - depla][colonne] == 1:
      grille[ligne - depla][colonne] = 0
      return [ligne - depla, colonne, 0]
  return [ligne, colonne, 0]

def game():
  window.blit(pygame.image.load("modifier.png").convert(), (360, 420))
  window.blit(pygame.image.load("tryagain.png").convert(), (300, 420))
  pygame.display.flip()
  saveGrille2 = []
  for ligne in range(7):
    saveGrille2.append([0, 0, 0, 0, 0, 0, 0])
  for ligne in range(7):
    for colonne in range(7):
      saveGrille2[ligne][colonne] = grille[ligne][colonne]
  for ligne in range(7):
    for colonne in range(7):
      if grille[ligne][colonne] == 3:
          position = [ligne, colonne, 0]
          break
  ligne = position[0]
  colonne = position[1]
  window.blit(pygame.image.load("smil.png").convert(), (colonne * 60, ligne * 60))
  pygame.display.flip()
  while True:
    pygame.time.Clock().tick(30)
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
          if event.pos[1] > 420 and event.pos[0] > 360:
            for ligne in range(7):
              for colonne in range(7):
                 grille[ligne][colonne] = saveGrille2[ligne][colonne]
                 changeImage(ligne, colonne)
                 window.blit(pygame.image.load("blank.png").convert(), (300, 420))
            window.blit(pygame.image.load("info.png").convert(), (0, 420))
            genereGrille()
          if event.pos[1] > 420 and event.pos[0] < 360 and event.pos[0] > 300:
            for ligne in range(7):
              for colonne in range(7):
                 grille[ligne][colonne] = saveGrille2[ligne][colonne]
                 changeImage(ligne, colonne)
            window.blit(pygame.image.load("jouer.png").convert(), (0, 420))
            game()
      if event.type == KEYDOWN:
        if event.key == K_RIGHT:
          position = droite(ligne, colonne)
        if event.key == K_LEFT:
          position = gauche(ligne, colonne)
        if event.key == K_DOWN:
          position = bas(ligne, colonne)
        if event.key == K_UP:
          position = haut(ligne, colonne)
    if position[0] != ligne or position[1] != colonne:
      if ligne != position[0]:
        if ligne < position[0]:
          for depla in range(ligne, position[0]):
            window.blit(pygame.image.load("filantebas.jpg").convert(), (colonne * 60, depla * 60))
          window.blit(pygame.image.load("smil.png").convert(), (colonne * 60, position[0] * 60))
        else:
          for depla in range(position[0] + 1, ligne +1):
            window.blit(pygame.image.load("filantehaut.jpg").convert(), (colonne * 60, depla * 60))
          window.blit(pygame.image.load("smil.png").convert(), (colonne * 60, position[0] * 60))
      if colonne != position[1]:
        if colonne < position[1]:
          for depla in range(colonne, position[1]):
            window.blit(pygame.image.load("filantedroite.jpg").convert(), (depla * 60, ligne * 60))
          window.blit(pygame.image.load("smil.png").convert(), (position[1] * 60, ligne * 60))
        else:
          for depla in range(position[1] + 1, colonne + 1):
            window.blit(pygame.image.load("filantegauche.jpg").convert(), (depla * 60, ligne * 60))
          window.blit(pygame.image.load("smil.png").convert(), (position[1] * 60, ligne * 60))
      if position[2] == -1:
        winner()
      ligne = position[0]
      colonne = position[1]
      pygame.display.flip()

def ballout():
  for ligne in range(7):
    for colonne in range(7):
      if grille[ligne][colonne] == 1:
        return False
  return True

#debut de solution

def possible(Grille):
  possible = 0
  for ligne in range(7):
    for colonne in range(7):
      if Grille[ligne][colonne] !=0:
        possible +=1
  return possible - 1

def copie(Grille):
  for ligne in range(7):
    saveGrille1.append([0, 0, 0, 0, 0, 0, 0])
    for colonne in range(7):
      saveGrille1[ligne][colonne] = Grille[ligne][colonne]

def increref():
  print(reference)
  i = 0
  a = 0
  while i == a:
    reference[i] += 1
    if reference[i] == 5:
      reference[i] = 1
      a += 1
    i += 1

def actionref(positionsave):
  for k in reference:
    if k != 0:
      if k == 1:
        droitesave(positionsave)
      else:
        if k == 2:
          bassave(positionsave)
        else:
          if k == 3:
            gauchesave(positionsave)
          else:
            if k == 4:
              hautsave(positionsave)

def finish():
  for ligne in range(7):
    for colonne in range(7):
      if saveGrille1[ligne][colonne] != 0 and saveGrille1[ligne][colonne] != 3:
        return True
  return False

def positionsafe():
  for ligne in range(7):
    for colonne in range(7):
      if saveGrille1[ligne][colonne] == 3:
        return [ligne, colonne]

def les2():
  for ligne in range(7):
    for colonne in range(7):
      if saveGrille1[ligne][colonne] == 1:
        return False
  return True

def droitesave(positionsave):
  for depla in range(positionsave[1] + 1, 7):
    if saveGrille1[positionsave[0]][depla] != 0 and saveGrille1[positionsave[0]][depla] != 2:
      saveGrille1[positionsave[0]][depla] = 0
      positionsave[1] = depla
      break
    else:
      if saveGrille1[positionsave[0]][depla] == 2:
        if les2():
          saveGrille1[positionsave[0]][depla] = 0
          positionsave[1] = depla
          break
        else:
          break

def bassave(positionsave):
  for depla in range(positionsave[0] + 1, 7):
    if saveGrille1[depla][positionsave[1]] != 0 and saveGrille1[depla][positionsave[1]] != 2:
      saveGrille1[depla][positionsave[1]] = 0
      positionsave[0] = depla
      break
    else:
      if saveGrille1[depla][positionsave[1]] == 2:
        if les2():
          saveGrille1[depla][positionsave[1]] = 0
          positionsave[0] = depla
          break
        else:
          break

def gauchesave(positionsave):
  for depla in range(positionsave[1] + 1):
    if saveGrille1[positionsave[0]][positionsave[1] - depla] != 0 and saveGrille1[positionsave[0]][positionsave[1] - depla] != 2:
      saveGrille1[positionsave[0]][positionsave[1] - depla] = 0
      positionsave[1] = positionsave[1] - depla
      break
    else:
      if saveGrille1[positionsave[0]][positionsave[1] - depla] == 2:
        if les2():
          saveGrille1[positionsave[0]][positionsave[1] - depla] = 0
          positionsave[1] = positionsave[1] - depla
          break
        else:
          break

def hautsave(positionsave):
  for depla in range(1, positionsave[0] + 1):
    if saveGrille1[positionsave[0] - depla][positionsave[1]] != 0 and saveGrille1[positionsave[0] - depla][positionsave[1]] != 2:
      saveGrille1[positionsave[0] - depla][positionsave[1]] = 0
      positionsave[0] = positionsave[0] - depla
      break
    else:
      if saveGrille1[positionsave[0] - depla][positionsave[1]] == 2:
        if les2():
          saveGrille1[positionsave[0] - depla][positionsave[1]] = 0
          positionsave[0] = positionsave[0] - depla
          break
        else:
          break

def coupre():
  for k in range(len(reference) - 1):
    if reference[k] == 1 and reference[k + 1] == 3:
      return False
    else:
      if reference[k] == 3 and reference[k + 1] == 1:
        return False
      else:
        if reference[k] == 2 and reference[k + 1] == 4:
          return False
        else:
          if reference[k] == 4 and reference[k + 1] == 2:
            return False
  return True

def solve(Grille):
  positionsave = [0, 0]
  reference.append(0)
  for pos in range(1, possible(Grille)):
    reference.append(1)
  copie(Grille)
  positionsave[0] = positionsafe()[0]
  positionsave[1] = positionsafe()[1]
  positioninit = [positionsave[0], positionsave[1]]
  Grille[positionsave[0]][positionsave[1]] = 0
  while finish():
    copie(Grille)
    positionsave = [positioninit[0], positioninit[1]]
    increref()
    if coupre():
      actionref(positionsave)
  print("affichage de reference")
  print (reference)
  print("fin de l'affichage de reference")
  Grille[positionsave[0]][positionsave[1]] = 3
  return reference

def affsol(reference):
  solution = []
  for k in reference:
    if k == 1:
      solution.append("droite")
    else:
      if k == 2:
        solution.append("bas")
      else:
        if k == 3:
          solution.append("gauche")
        else:
          if k == 4:
            solution.append("haut")
  print(solution)

#fin de solution

def ballsave():
  for ligne in range(7):
    for colonne in range(7):
      if rentreGrille[ligne][colonne] == 1:
        return False
  return True

def drorentre(ligne, colonne):
  for depla in range(colonne + 1, 7):
    if rentreGrille[ligne][depla] == 2:
      if ballsave():
        return [ligne, depla, -1]
      else:
        break
    if rentreGrille[ligne][depla] == 1:
      rentreGrille[ligne][depla] = 0
      return [ligne, depla, 0]
  return [ligne, colonne, 0]

def gaurentre(ligne, colonne):
  for depla in range(colonne + 1):
    if rentreGrille[ligne][colonne - depla] == 2:
      if ballsave():
        return [ligne, colonne - depla, -1]
      else:
        break
    if rentreGrille[ligne][colonne - depla] == 1:
      rentreGrille[ligne][colonne - depla] = 0
      return [ligne, colonne - depla, 0]
  return [ligne, colonne, 0]

def basrentre(ligne, colonne):
  for depla in range(ligne + 1, 7):
    if rentreGrille[depla][colonne] == 2:
      if ballsave():
        return [depla, colonne, -1]
      else:
        break
    if rentreGrille[depla][colonne] == 1:
      rentreGrille[depla][colonne] = 0
      return [depla, colonne, 0]
  return [ligne, colonne, 0]

def haurentre(ligne, colonne):
  for depla in range(1, ligne + 1):
    if rentreGrille[ligne - depla][colonne] == 2:
      if ballsave():
        return [ligne - depla, colonne, -1]
      else:
        break  
    if rentreGrille[ligne - depla][colonne] == 1:
      rentreGrille[ligne - depla][colonne] = 0
      return [ligne - depla, colonne, 0]
  return [ligne, colonne, 0]




def winner():
  window.blit(pygame.image.load("win.png").convert(), (0,420))

if __name__ == '__main__':
  grille = []
  reference = []
  saveGrille1 = []
  pygame.init()
  window = pygame.display.set_mode((420,480), RESIZABLE)
  initialiseGrille()
  genereGrille()
