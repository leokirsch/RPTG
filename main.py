import display
import character
import unit
import attack
import random

units = []
attacks = []
envWidth, envHeight = 40, 30 # environment

numRocks = 30
for n in range(numRocks):
    x = random.randint(1,envWidth-2)
    y = random.randint(1,envHeight-2)
    rock = unit.Unit(x,y,'rock','o',False)
    units.append(rock)

numEnemies = 5
enemies = []
for n in range(numEnemies):
    x = random.randint(1,envWidth-2)
    y = random.randint(1,envHeight-2)
    enemy = character.Character(x, y, 'Enemy','>',2,units,attacks)
    enemies.append(enemy)
    units.append(enemy)

x = random.randint(1,envWidth-2)
y = random.randint(1,envHeight-2)
hero = character.Character(x,y,'Leo','S',2,units,attacks)
units.append(hero)

viewWidth, viewHeight = 15, 10
disp = display.Display(envWidth, envHeight, viewWidth, viewHeight, units, attacks, hero)

while True:
    disp.display_all()

    if hero.isAlive:
        action = input('...')
        action = action[0] # only first character

        if action == 'w':
            hero.move_up()
        elif action == 'a':
            hero.move_left()
        elif action == 's':
            hero.move_down()
        elif action == 'd':
            hero.move_right()
        elif action == 'x':
            hero.melee_attack()
        elif action == 'b':
            break
        elif action == 'n':
            for unit in units:
                print(unit.name)

    for enemy in enemies:
        if enemy.isAlive:
            actions = ['w','a','s','d']
            for x in range(3):
                actions.append('x')
            action = random.choice(actions)
            if action == 'w':
                enemy.move_up()
            elif action == 'a':
                enemy.move_left()
            elif action == 's':
                enemy.move_down()
            elif action == 'd':
                enemy.move_right()
            elif action == 'x':
                enemy.melee_attack()
