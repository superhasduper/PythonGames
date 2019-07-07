
import random
import arcade
import os

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.3
SPRITE_SCALING_COIN = 0.3
COIN_COUNT = 50
ROTTEN_COIN_COUNT = 25
SPRITE_NATIVE_SIZE = 128
SPRITE_SCALING = 0.5
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

VIEWPORT_MARGIN = 40
RIGHT_MARGIN = 150
SCREEN_WIDTH = 1000

SCREEN_HEIGHT = 700

MOVEMENT_SPEED = 5
JUMP_SPEED = 14
GRAVITY = 0.9
class rotten_Coin(arcade.Sprite):
    """
    This class represents the coins on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):

        # Reset the coin to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        # Move the coin
        self.center_y -= 1

        # See if the coin has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()

class Coin(arcade.Sprite):
    """
    This class represents the coins on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):

        # Reset the coin to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        # Move the coin
        self.center_y -= 1

        # See if the coin has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Variables that will hold sprite lists
        self.all_sprites_list = None
        self.coin_list = None
        self.rotten_coin_list = None
        self.golden_coin_list = None
        self.wall_list = None
        # Set up the player info
        self.player_sprite = None
        self.score = 0
        self.physics_engine = None
        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.wall_list = arcade.SpriteList()
        self.all_sprites_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.rotten_coin_list = arcade.SpriteList()
        self.golden_coin_list = arcade.SpriteList()
        # Draw the walls on the bottom
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite("grassMid.png", SPRITE_SCALING)

            wall.bottom = 0
            wall.left = x
            self.wall_list.append(wall)
            # draw platforms
        for x in range(SPRITE_SIZE * 1, SPRITE_SIZE* 10, SPRITE_SIZE * 8):
            wall = arcade.Sprite("grassMid.png", SPRITE_SCALING)

            wall.bottom = SPRITE_SIZE * 3
            wall.left = x
            self.wall_list.append(wall)
        for x in range(SPRITE_SIZE * 5, SPRITE_SIZE* 10, SPRITE_SIZE * 8):
            wall = arcade.Sprite("grassMid.png", SPRITE_SCALING)

            wall.bottom = SPRITE_SIZE * 6
            wall.left = x
            self.wall_list.append(wall)
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("bunnywalk.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.all_sprites_list.append(self.player_sprite)
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list, gravity_constant=GRAVITY)
        # Starting position of the player
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 270
        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = Coin("carrot.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.all_sprites_list.append(coin)
            self.coin_list.append(coin)
        for i in range(ROTTEN_COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            rotten_coin = Coin("carrot rotten.png", SPRITE_SCALING_COIN)

            # Position the coin
            rotten_coin.center_x = random.randrange(SCREEN_WIDTH)
            rotten_coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.all_sprites_list.append(rotten_coin)
            self.rotten_coin_list.append(rotten_coin)
    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.all_sprites_list.draw()

        # Put the text on the screen.
        output = f'Score: {self.score}'
        arcade.draw_text(output, 20, 680, arcade.color.WHITE, 14)
        self.wall_list.draw()
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED
        elif key == arcade.key.A:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.all_sprites_list.update()

        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.coin_list)
        self.physics_engine.update()
        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in hit_list:
            coin.kill()
            self.score += 1
        for rotten_coin in hit_list:
            rotten_coin.kill()
            self.score -= 1
        if self.player_sprite.center_x > SCREEN_WIDTH:
            self.player_sprite.center_x = 0
        elif self.player_sprite.center_x < 0:
            self.player_sprite.center_x = SCREEN_WIDTH

def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
