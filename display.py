import unit
import character
import attack

class Display:
    def __init__(self, width, height, viewWidth, viewHeight, units, attacks, hero):
        self.width = width
        self.height = height
        self.viewWidth = viewWidth
        self.viewHeight = viewHeight
        self.playArea = [[' ' for i in range(self.width)] for j in range(self.height)]
        self.units = units
        self.attacks = attacks
        self.hero = hero

    def display_play_area(self):
        halfViewW, halfViewH = int(self.viewWidth / 2), int(self.viewHeight / 2)
        heroX, heroY = self.hero.x, self.hero.y
        print('--' * (halfViewW * 2 + 1))
        for j in range(heroY - halfViewH, heroY + halfViewH):
            print('|', end = '')     
            for i in range(heroX - halfViewW, heroX + halfViewW):
                if j >= 0 and j < len(self.playArea) and i >= 0 and i < len(self.playArea[0]):
                    print(self.playArea[j][i] + ' ', end = '')
                else:
                    print('X ', end = '')
            print('|\n', end = '')            
        print('--' * (halfViewW * 2 + 1))

    def display_menu_area(self):
        print('Health = ', self.hero.health)

    def display_all(self):
        self.draw_clear_background()
        self.draw_border()
        self.draw_units()
        self.draw_attacks()

        self.display_play_area()
        self.display_menu_area()
        self.clear_attacks()
        self.clear_dead_units()

    def draw_clear_background(self):
        for j in range(0, self.height):     
            for i in range(0, self.width):
                self.playArea[j][i] = ' '

    def draw_border(self):
        for j in range(0, self.height):
            for i in range(0, self.width):
                if i == 0 or j == 0 or i == self.width - 1 or j == self.height - 1:
                    self.playArea[j][i] = 'X'

    def draw_units(self):
        for unit in self.units:
            if unit.x < 1: unit.x = 1
            if unit.x > self.width - 2: unit.x = self.width - 2
            
            if unit.y < 1: unit.y = 1
            if unit.y > self.height - 2: unit.y = self.height - 2

            self.playArea[unit.y][unit.x] = unit.symbol 

    def draw_attacks(self):
        for att in self.attacks:
            self.playArea[att.y][att.x] = att.symbol

    def clear_attacks(self):
        for att in reversed(range(len(self.attacks))):
            del self.attacks[att]

    def clear_dead_units(self):
        for un in reversed(range(len(self.units))):
            if self.units[un].isAlive == False:
                del self.units[un]
                