import time
import sys
import pygame
from pygame.locals import *
from random import randint

def initialiseGrille():
  '''
      Initialize the tab 'grille' 7*7 with '0'
  '''
  grille = []
  for ligne in range(7):
    grille.append([0, 0, 0, 0, 0, 0, 0])
  window.blit(pygame.image.load("start.png").convert(), (0,0))
  pygame.display.flip()
  return grille

def changeGrille(grille, ligne, colonne):
  grille[ligne][colonne] +=1
  grille[ligne][colonne] = grille[ligne][colonne] % 4
  return grille

def changeImage(grille, ligne, colonne):
  if grille[ligne][colonne] == 0:
      window.blit(pygame.image.load("none.png").convert(), (colonne * 60, ligne * 60))
  if grille[ligne][colonne] == 1:
      window.blit(pygame.image.load("ball.png").convert(), (colonne * 60, ligne * 60))
  if grille[ligne][colonne] == 2:
      window.blit(pygame.image.load("circle.png").convert(), (colonne * 60, ligne * 60))
  if grille[ligne][colonne] == 3:
      window.blit(pygame.image.load("smil.png").convert(), (colonne * 60, ligne * 60))
  pygame.display.flip()

def genereGrille(grille):
  a = 0
  window.blit(pygame.image.load("valider.png").convert(), (360, 420))
  window.blit(pygame.image.load("solve2.png").convert(), (300, 420))
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
          if event.pos[0] >= 320 and event.pos[1] > 420:
            if grilleValideDebut(grille):
              if grilleValideFin(grille):
                if event.pos[0] > 360:
                  window.blit(pygame.image.load("jouer.png").convert(), (0, 420))
                  pygame.display.flip()
                  game(grille)
                else:
                  window.blit(pygame.image.load("solve.png").convert(), (0, 420))
                  pygame.display.flip()
                  affsol(solve(grille))
                  global reference
                  reference = []
                  ligne, colonne = -1, -1
              else:
                window.blit(pygame.image.load("fin.png").convert(), (0, 420))
              pygame.display.flip()
            else:
              window.blit(pygame.image.load("debut.png").convert(), (0, 420))
              pygame.display.flip()
    if ligne != -1 and colonne != -1:
      changeGrille(grille, ligne, colonne) 
      changeImage(grille, ligne, colonne)
      ligne = -1
      colonne = -1

def grilleValideDebut(grille):
  nombreDebut = 0
  for ligne in range(7):
    for colonne in range(7):
      if grille[ligne][colonne] == 3:
        nombreDebut +=1
  if nombreDebut != 1:
    return False
  return True

def grilleValideFin(grille):
  nombreFin = 0
  for ligne in range(7):
    for colonne in range(7):
      if grille[ligne][colonne] == 2:
        nombreFin +=1
  if nombreFin != 1:
    return False
  return True

#Creation de la grille termine

def droite(grille, ligne, colonne):
  for depla in range(colonne + 1, 7):
    if grille[ligne][depla] == 2:
      if ballout(grille):
        return [ligne, depla, -1]
      else:
        break
    if grille[ligne][depla] == 1:
      grille[ligne][depla] = 0
      return [ligne, depla, 0]
  return [ligne, colonne, 0]

def gauche(grille, ligne, colonne):
  for depla in range(colonne + 1):
    if grille[ligne][colonne - depla] == 2:
      if ballout(grille):
        return [ligne, colonne - depla, -1]
      else:
        break
    if grille[ligne][colonne - depla] == 1:
      grille[ligne][colonne - depla] = 0
      return [ligne, colonne - depla, 0]
  return [ligne, colonne, 0]

def bas(grille, ligne, colonne):
  for depla in range(ligne + 1, 7):
    if grille[depla][colonne] == 2:
      if ballout(grille):
        return [depla, colonne, -1]
      else:
        break
    if grille[depla][colonne] == 1:
      grille[depla][colonne] = 0
      return [depla, colonne, 0]
  return [ligne, colonne, 0]

def haut(grille, ligne, colonne):
  for depla in range(1, ligne + 1):
    if grille[ligne - depla][colonne] == 2:
      if ballout(grille):
        return [ligne - depla, colonne, -1]
      else:
        break  
    if grille[ligne - depla][colonne] == 1:
      grille[ligne - depla][colonne] = 0
      return [ligne - depla, colonne, 0]
  return [ligne, colonne, 0]

def game(grille):
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
                 changeImage(grille, ligne, colonne)
                 window.blit(pygame.image.load("blank.png").convert(), (300, 420))
            window.blit(pygame.image.load("info.png").convert(), (0, 420))
            genereGrille(grille)
          if event.pos[1] > 420 and event.pos[0] < 360 and event.pos[0] > 300:
            for ligne in range(7):
              for colonne in range(7):
                 grille[ligne][colonne] = saveGrille2[ligne][colonne]
                 changeImage(grille, ligne, colonne)
            window.blit(pygame.image.load("jouer.png").convert(), (0, 420))
            game(grille)
      if event.type == KEYDOWN:
        if event.key == K_RIGHT:
          position = droite(grille, ligne, colonne)
        if event.key == K_LEFT:
          position = gauche(grille, ligne, colonne)
        if event.key == K_DOWN:
          position = bas(grille, ligne, colonne)
        if event.key == K_UP:
          position = haut(grille, ligne, colonne)
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

def ballout(grille):
  for ligne in range(7):
    for colonne in range(7):
      if grille[ligne][colonne] == 1:
        return False
  return True

#debut de solution

def possible(grille):
  possible = 0
  for ligne in range(7):
    for colonne in range(7):
      if grille[ligne][colonne] !=0:
        possible +=1
  return possible - 1

def copie(saveGrille1, grille):
  for ligne in range(7):
    for colonne in range(7):
      saveGrille1[ligne][colonne] = grille[ligne][colonne]
  return saveGrille1

def increref():
  i = 0
  a = 0
  while i == a:
    reference[i] += 1
    if reference[i] == 5:
      reference[i] = 1
      a += 1
    i += 1

def actionref(tailleref, saveGrille1, positionsave):
  for p in range(tailleref):
    k = reference[- p - 1]
    if k == 1:
      droitesave(-p-1, saveGrille1, positionsave)
    else:
      if k == 2:
        bassave(-p-1,saveGrille1, positionsave)
      else:
        if k == 3:
          gauchesave(-p-1,saveGrille1, positionsave)
        else:
          if k == 4:
            hautsave(-p-1,saveGrille1, positionsave)

def finish(saveGrille1):
  for ligne in range(7):
    for colonne in range(7):
      if saveGrille1[ligne][colonne] != 0 and saveGrille1[ligne][colonne] != 3:
        return True
  return False

def positionsafe(saveGrille1):
  for ligne in range(7):
    for colonne in range(7):
      if saveGrille1[ligne][colonne] == 3:
        return [ligne, colonne]

def les2(saveGrille1):
  for ligne in range(7):
    for colonne in range(7):
      if saveGrille1[ligne][colonne] == 1:
        return False
  return True

def droitesave(p,saveGrille1, positionsave):
  for depla in range(positionsave[1] + 1, 7):
    if saveGrille1[positionsave[0]][depla] != 0 and saveGrille1[positionsave[0]][depla] != 2:
      saveGrille1[positionsave[0]][depla] = 0
      positionsave[1] = depla
      break
    else:
      if saveGrille1[positionsave[0]][depla] == 2:
        if les2(saveGrille1):
          saveGrille1[positionsave[0]][depla] = 0
          positionsave[1] = depla
          break
        else:
          break

def bassave(p,saveGrille1, positionsave):
  for depla in range(positionsave[0] + 1, 7):
    if saveGrille1[depla][positionsave[1]] != 0 and saveGrille1[depla][positionsave[1]] != 2:
      saveGrille1[depla][positionsave[1]] = 0
      positionsave[0] = depla
      break
    else:
      if saveGrille1[depla][positionsave[1]] == 2:
        if les2(saveGrille1):
          saveGrille1[depla][positionsave[1]] = 0
          positionsave[0] = depla
          break
        else:
          break

def gauchesave(p,saveGrille1, positionsave):
  for depla in range(positionsave[1] + 1):
    if saveGrille1[positionsave[0]][positionsave[1] - depla] != 0 and saveGrille1[positionsave[0]][positionsave[1] - depla] != 2:
      saveGrille1[positionsave[0]][positionsave[1] - depla] = 0
      positionsave[1] = positionsave[1] - depla
      break
    else:
      if saveGrille1[positionsave[0]][positionsave[1] - depla] == 2:
        if les2(saveGrille1):
          saveGrille1[positionsave[0]][positionsave[1] - depla] = 0
          positionsave[1] = positionsave[1] - depla
          break
        else:
          break

def hautsave(p,saveGrille1, positionsave):
  for depla in range(1, positionsave[0] + 1):
    if saveGrille1[positionsave[0] - depla][positionsave[1]] != 0 and saveGrille1[positionsave[0] - depla][positionsave[1]] != 2:
      saveGrille1[positionsave[0] - depla][positionsave[1]] = 0
      positionsave[0] = positionsave[0] - depla
      break
    else:
      if saveGrille1[positionsave[0] - depla][positionsave[1]] == 2:
        if les2(saveGrille1):
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

def solve(grille):
  saveGrille1 = []
  positionsave = [0, 0]
  reference.append(0)
  for ligne in range(7):
    saveGrille1.append([0, 0, 0, 0, 0, 0, 0])
  for pos in range(1, possible(grille)):
    reference.append(1)
  tailleref = len(reference)
  saveGrille1 = copie(saveGrille1, grille)
  positionsave[0] = positionsafe(saveGrille1)[0]
  positionsave[1] = positionsafe(saveGrille1)[1]
  positioninit = [positionsave[0], positionsave[1]]
  grille[positionsave[0]][positionsave[1]] = 0
  fichier = open("base.txt","w")
  while finish(saveGrille1):
    saveGrille1 = copie(saveGrille1, grille)
    positionsave = [positioninit[0], positioninit[1]]
    increref()
    if coupre():
      actionref(tailleref, saveGrille1, positionsave)
      fichier.write(str(reference))
      fichier.write("\n")
    increref()
  fichier.close()
  print("affichage de reference")
  print(reference)
  print("fin de l'affichage de reference")
  print("affichage de la solution en inverse a reference")
  inverse = []
  for j in range(tailleref):
    inverse.append(reference[- j - 1])
  print inverse
  print("fin de l'affichage de la solution en inverse a reference")
  grille[positionsave[0]][positionsave[1]] = 3
  return inverse

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


def winner():
  window.blit(pygame.image.load("win.png").convert(), (0,420))

if __name__ == '__main__':
  reference = []
  pygame.init()
  window = pygame.display.set_mode((420,480), RESIZABLE)
  genereGrille(initialiseGrille())
