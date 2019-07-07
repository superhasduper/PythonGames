import arcade
import random
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_PECES = 0.5
peces_count = 50
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
my_sound = arcade.load_sound("eating.wav")
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "el oso tiene HAMBREEE!")
        self.player_list = None
        self.peces_list = None
        self.player_sprite = None
        self.score = 0
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.peces_list = arcade.SpriteList()
        self.score = 0
        my_sound = arcade.load_sound("eating.wav")
        self.player_sprite = arcade.Sprite("bear.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)
        for i in range(peces_count):
            numero = random.randrange(1,4)
            objeto = arcade.Sprite(f"objeto{numero}.png", SPRITE_SCALING_PECES)
            objeto.center_x = random.randrange(SCREEN_WIDTH)
            objeto.center_y = random.randrange(SCREEN_HEIGHT)
            self.peces_list.append(objeto)

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.peces_list.draw()
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y
    def update(self, delta_time):
        self.player_list.update()
        peces_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.peces_list)
        for peces in peces_hit_list:
            peces.kill()
            self.score += 1
            arcade.play_sound(my_sound)

def main():
    Window = MyGame()
    Window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
