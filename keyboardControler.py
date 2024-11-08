import pygame
from Arctos import Arctos


pygame.init()
pygame.display.set_mode((1, 1))
spielaktiv = True

start = False

surface = pygame.display.set_mode((1, 1))
import time

arctos = Arctos()

from defines import *
from mksServoCan.mks_enums import Direction, WorkMode, HoldingStrength

arctos.Axis[AxisId.X].setWorkMode(WorkMode.SrClose)
# arctos.Axis[AxisId.X].motors[0].set_holding_current(HoldingStrength.EIGHTY_PERCENT)


t0 = time.time()
t1 = time.time()
while spielaktiv:
    deltaT = time.time() - t0
    if deltaT > 0.01:
        t0 = time.time()

        all_keys = pygame.key.get_pressed()

        if all_keys[pygame.K_w] and all_keys[pygame.K_LSHIFT]:
            arctos.Axis[AxisId.Y].moveAxis(400, Direction.CW)
        elif all_keys[pygame.K_s] and all_keys[pygame.K_LSHIFT]:
            arctos.Axis[AxisId.Y].moveAxis(400, Direction.CCW)
        elif all_keys[pygame.K_s] and not all_keys[pygame.K_LSHIFT]:
            arctos.Axis[AxisId.Z].moveAxis(400, Direction.CW)
        elif all_keys[pygame.K_w] and not all_keys[pygame.K_LSHIFT]:
            arctos.Axis[AxisId.Z].moveAxis(400, Direction.CCW)
        else:
            arctos.Axis[AxisId.Y].moveAxis(0, Direction.CCW)
            arctos.Axis[AxisId.Z].moveAxis(0, Direction.CCW)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    arctos.Axis[AxisId.X].moveAxis(60, Direction.CCW)
                if event.key == pygame.K_d:
                    arctos.Axis[AxisId.X].moveAxis(60, Direction.CW)
                if event.key == pygame.K_q:
                    arctos.Axis[AxisId.A].moveAxis(200, Direction.CCW)
                if event.key == pygame.K_e:
                    arctos.Axis[AxisId.A].moveAxis(200, Direction.CW)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    arctos.Axis[AxisId.X].moveAxis(0, Direction.CCW)
                if event.key == pygame.K_d:
                    arctos.Axis[AxisId.X].moveAxis(0, Direction.CW)
                if event.key == pygame.K_q:
                    arctos.Axis[AxisId.A].moveAxis(0, Direction.CCW)
                if event.key == pygame.K_e:
                    arctos.Axis[AxisId.A].moveAxis(0, Direction.CW)
