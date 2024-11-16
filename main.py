import direct.directbase.DirectStart
from direct.showbase import DirectObject
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import *

class Game(DirectObject.DirectObject):

    def __init__(self):
        self.accept("escape", self.cleanup)
        self.accept("arrow_up", self.adjust_sunlight)
        self.accept("arrow_down", self.adjust_shade)
        self.accept("arrow_left", self.adjust_water)
        self.accept("arrow_right", self.adjust_nutrients)

        self.sunlight = 50
        self.shade = 50
        self.water = 50
        self.nutrients = 50

        self.plant = loader.loadModel("models/plant.obj")

        self.plant.reparentTo(render)
        self.plant.setScale(0.5)
        self.plant.setPos(0, 0, 0)

        self.sunlight_label = OnscreenText(text = "Sunlight: " + str(self.sunlight), pos = (-0.9, 0.9), scale = 0.07, fg = (1,1,1,1))
        self.shade_label = OnscreenText(text = "Shade: " + str(self.shade), pos = (-0.9, 0.8), scale = 0.07, fg = (1,1,1,1))
        self.water_label = OnscreenText(text = "Water: " + str(self.water), pos = (-0.9, 0.7), scale = 0.07, fg = (1,1,1,1))
        self.nutrients_label = OnscreenText(text = "Nutrients: " + str(self.nutrients), pos = (-0.9, 0.6), scale = 0.07, fg = (1,1,1,1))

    def adjust_sunlight(self):
        self.sunlight = max(0, min(100, self.sunlight + 5))
        self.sunlight_label.setText("Sunlight: " + str(self.sunlight))

    def adjust_shade(self):
        self.shade = max(0, min(100, self.shade + 5))
        self.shade_label.setText("Shade: " + str(self.shade))

    def adjust_water(self):
        self.water = max(0, min(100, self.water + 5))
        self.water_label.setText("Water: " + str(self.water))

    def adjust_nutrients(self):
        self.nutrients = max(0, min(100, self.nutrients + 5))
        self.nutrients_label.setText("Nutrients: " + str(self.nutrients))

    def cleanup(self):
        self.plant.removeNode()
        self.sunlight_label.destroy()
        self.shade_label.destroy()
        self.water_label.destroy()
        self.nutrients_label.destroy()
        base.userExit()

game = Game()
run()
