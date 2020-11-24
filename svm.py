import pygame
from sklearn import svm
import matplotlib.pyplot as plt

import numpy as np


pygame.init()
gamescreen = pygame.display.set_mode((400, 300))
gamescreen.fill((0, 0, 255))
pygame.display.update()
play = True
clust1, clust2 = [], []

while play:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            play = False
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pygame.draw.circle(gamescreen, (255, 255, 0), i.pos, 5)
                clust1.append(0)
            elif i.button == 3:
                pygame.draw.circle(gamescreen, (0, 255, 255), i.pos, 5)
                clust1.append(1)
            clust2.append(i.pos)
        if i.type == pygame.KEYDOWN:
            clf = svm.SVC(kernel="linear")
            clf.fit(clust2,clust1)
			#get vector coefficents
            w = clf.coef_[0]
            a = -w[0] / w[1]
            xx = np.linspace(0, 1024)
            yy = a * xx - (clf.intercept_[0]) / w[1]
            margin = 1 / np.sqrt(np.sum(clf.coef_ ** 2))
            yy_down = yy - np.sqrt(1 + a ** 2) * margin
            yy_up = yy + np.sqrt(1 + a ** 2) * margin
            line = list(zip(xx, yy))
            line_down = list(zip(xx, yy_down))
            line_up = list(zip(xx, yy_up))
            for i in range(1, len(line)):
                pygame.draw.line(gamescreen, (255,255,255), line[i - 1], line[i], 5)
                pygame.draw.line(gamescreen, (255,0,0), line_down[i - 1], line_down[i],3)
                pygame.draw.line(gamescreen, (255,0,0), line_up[i - 1], line_up[i],3)
   
        pygame.display.update()

pygame.quit()

