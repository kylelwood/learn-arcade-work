""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME_TITLE = "FLYING COIN RACE"

CHARACTER_SCALING = 1
MOVEMENT_SPEED = 2
DRIFT_SPEED = -.5


def load_texture_pair(filename):
    return [arcade.load_texture(filename), arcade.load_texture(filename, flipped_horizontally=True)]


class FighterPlane1:
    """First of 2 planes that will fly on screen"""
    def __init__(self, position_x, position_y, change_x, change_y, size):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.size = size

        super().__init__()

        self.cur_texture = 0
        self.scale = CHARACTER_SCALING

        main_path1 = ":resources:C:/Users/kylel/OneDrive/Computer Science/biplane-158327_1280.png"

        self.fly_texture_pair = load_texture_pair(f"{main_path1}.png")

        self.texture = self.fly_texture_pair[0]

    def update(self):
        self.position_x += self.change_x
        self.position_y += self.change_y

class FighterPlane2:
    def __init__(self, position_x, position_y, change_x, change_y, size):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.size = size

        super().__init__()

        self.cur_texture = 0
        self.scale = CHARACTER_SCALING

        main_path2 = ":resources:C:/Users/kylel/OneDrive/Computer Science/green-304704_640.png"

        self.fly_texture_pair = load_texture_pair(f"{main_path2}.png")

        self.texture = self.fly_texture_pair[0]

    def update(self):
        self.position_x += self.change_x
        self.position_y += self.change_y



class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, GAME_TITLE)

        self.set_mouse_visible(False)

        self.player1 = FighterPlane1(50, 50, 0, 0, 5)
        self.player2 = FighterPlane2(50, 50, 0, 0, 5)

    def on_draw(self):
        arcade.start_render()
        self.player1.draw()
        self.player2.draw()

    def update(self, delta_time):
        self.player1.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player1.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player1.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.player1.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player1.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player1.change_x = DRIFT_SPEED
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player1.change_y = DRIFT_SPEED

        def draw_sun():
            # draw the sun
            arcade.draw_circle_filled(400, 165, 150, arcade.color.SUNRAY)

        def draw_sea():
            # draw the sea
            arcade.draw_lrtb_rectangle_filled(0, 800, 70, 0, arcade.color.HONOLULU_BLUE)

        def draw_sailboat(x, y):
            # draw a sailboat
            arcade.draw_lrtb_rectangle_filled(380 + x, 420 + x, 60 + y, 50 + y, arcade.color.BLACK)
            arcade.draw_triangle_filled(390 + x, 65 + y, 410 + x, 65 + y, 400 + x, 80 + y, arcade.color.BLACK)
            arcade.draw_lrtb_rectangle_filled(399 + x, 401 + x, 70 + y, 50 + y, arcade.color.BLACK)

        draw_sun()
        draw_sea()
        draw_sailboat(150, 21)
        arcade.set_background_color(arcade.color.BURNT_ORANGE)


def main():
    window = MyGame()
    arcade.run()


main()
