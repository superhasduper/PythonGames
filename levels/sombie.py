import arcade
import os

SPRITE_SCALING = 0.5
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

SCREEN_WIDTH = SPRITE_SIZE * 14
SCREEN_HEIGHT = SPRITE_SIZE * 10

MOVEMENT_SPEED = 5
COIN_SCALE = 0.7

class Room:
    """
    This class holds all the information about the
    different rooms.
    """
    def __init__(self):
        # You may want many lists. Lists for coins, monsters, etc.
        self.wall_list = None
        self.coin_list = None
        self.door_list = None
        self.smallpotion_list = None
        self.bigpotion_list = None
        # This holds the background images. If you don't want changing
        # background images, you can delete this part.
        self.background = None
        self.score = 0



def setup_room_1():
    """
    Create and return room 1.
    If your program gets large, you may want to separate this into different
    files.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    

    room.wall_list = arcade.SpriteList()
    room.door_list = arcade.SpriteList()
    room.coin_list = arcade.SpriteList()
   
    room.smallpotion_list = arcade.SpriteList()
    room.bigpotion_list = arcade.SpriteList()

    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite("gravel_dirt.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        # Loop for each box going across
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            # Skip making a block 4 and 5 blocks up on the right side
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x == 0:
                wall = arcade.Sprite("gravel_dirt.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        # Loop for each box going across
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):            
            if not (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x == 0:
                door = arcade.Sprite("fence.png", SPRITE_SCALING)
                door.left = x
                door.bottom = y
                room.door_list.append(door)

    wall = arcade.Sprite("gravel_dirt.png", SPRITE_SCALING)
    wall.left = 7 * SPRITE_SIZE
    wall.bottom = 5 * SPRITE_SIZE
    room.wall_list.append(wall)
    
    # If you want coins or monsters in a level, then add that code here.

    # Load the background image for this level.
    room.background = arcade.load_texture("g.png")
    for i in range(300,600,75):
        coin = arcade.Sprite("coin.png",COIN_SCALE)
        coin.center_x = i
        coin.center_y = 500
        room.coin_list.append(coin)
    
    smallpotion = arcade.Sprite("big.png",0.05)
    smallpotion.center_x = 100
    smallpotion.center_y = 900
    room.smallpotion_list.append(smallpotion)
    return room


def setup_room_2():
    """
    Create and return room 2.
    """
    room = Room()
    
    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.door_list = arcade.SpriteList()
    room.wall_list = arcade.SpriteList()
    room.coin_list = arcade.SpriteList()
    room.smallpotion_list = arcade.SpriteList()
    room.bigpotion_list = arcade.SpriteList()
    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        # Loop for each box going across
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            # Skip making a block 4 and 5 blocks up
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x != 0:
                wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 1 * SPRITE_SIZE
    wall.bottom = 6 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 1 * SPRITE_SIZE
    wall.bottom = 3 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 2 * SPRITE_SIZE
    wall.bottom = 5.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 2 * SPRITE_SIZE
    wall.bottom = 3.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 3 * SPRITE_SIZE
    wall.bottom = 3.5 * SPRITE_SIZE
    room.wall_list.append(wall)
    
    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 4 * SPRITE_SIZE
    wall.bottom = 3.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 4 * SPRITE_SIZE
    wall.bottom = 4.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 2 * SPRITE_SIZE
    wall.bottom = 5.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 2 * SPRITE_SIZE
    wall.bottom = 6.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 3 * SPRITE_SIZE
    wall.bottom = 6.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 4 * SPRITE_SIZE
    wall.bottom = 6.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 5 * SPRITE_SIZE
    wall.bottom = 6.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 6 * SPRITE_SIZE
    wall.bottom = 6.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 6 * SPRITE_SIZE
    wall.bottom = 5.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 6 * SPRITE_SIZE
    wall.bottom = 4.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 4 * SPRITE_SIZE
    wall.bottom = 2.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 6 * SPRITE_SIZE
    wall.bottom =3.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 6 * SPRITE_SIZE
    wall.bottom = 4.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 6 * SPRITE_SIZE
    wall.bottom = 0.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 6 * SPRITE_SIZE
    wall.bottom = 1.5 * SPRITE_SIZE
    room.wall_list.append(wall)


    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 7 * SPRITE_SIZE
    wall.bottom = 3.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 7 * SPRITE_SIZE
    wall.bottom = 1.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 8 * SPRITE_SIZE
    wall.bottom = 1.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 8 * SPRITE_SIZE
    wall.bottom = 3.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 9 * SPRITE_SIZE
    wall.bottom = 1.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 10 * SPRITE_SIZE
    wall.bottom = 1.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 10 * SPRITE_SIZE
    wall.bottom = 2.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 10 * SPRITE_SIZE
    wall.bottom = 3.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 10 * SPRITE_SIZE
    wall.bottom = 4.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 8 * SPRITE_SIZE
    wall.bottom = 4.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 10 * SPRITE_SIZE
    wall.bottom = 5.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 10 * SPRITE_SIZE
    wall.bottom = 6.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 9 * SPRITE_SIZE
    wall.bottom = 6.5 * SPRITE_SIZE
    room.wall_list.append(wall)


    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 8 * SPRITE_SIZE
    wall.bottom = 6.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 8 * SPRITE_SIZE
    wall.bottom = 7.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("stone_snow.png", SPRITE_SCALING)
    wall.left = 8 * SPRITE_SIZE
    wall.bottom = 8 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("g.png")

    bigpotion = arcade.Sprite("small.png",0.05)
    bigpotion.center_x = 800
    bigpotion.center_y = 100
    room.bigpotion_list.append(bigpotion)
    return room


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        """
        Initializer
        """
        super().__init__(width, height,"Tocate el pnnywise")

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.current_room = 0

        # Set up the player
        self.game_over = False
        self.door_list = None
        self.rooms = None
        self.score = 0
        self.coin_list = None
        self.player_sprite = None
        self.physics_engine = None
        self.smallpotion_list = None
        self.bigpotion_list = None
    def setup(self):
        """ Set up the game and initialize the variables. """
        # Set up the player
        self.player_sprite =  arcade.AnimatedWalkingSprite()
        self.score = 0
        self.coin_list = arcade.SpriteList()
        self.smallpotion_list = arcade.SpriteList()
        self.bigpotion_list = arcade.SpriteList()
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 150
        character_scale = 0.75
        self.player_sprite.stand_right_textures = []
        self.player_sprite.stand_right_textures.append(arcade.load_texture("zombie_stand.png",
                                                                    scale=character_scale))
        self.player_sprite.stand_left_textures = []
        self.player_sprite.stand_left_textures.append(arcade.load_texture("zombie_stand.png",
                                                                   scale=character_scale, mirrored=True))

        self.player_sprite.walk_right_textures = []

        self.player_sprite.walk_right_textures.append(arcade.load_texture("zombie_walk1.png",
                                                                   scale=character_scale))
        self.player_sprite.walk_right_textures.append(arcade.load_texture("zombie_walk2.png",
                                                                   scale=character_scale))

        self.player_sprite.walk_left_textures = []

        self.player_sprite.walk_left_textures.append(arcade.load_texture("zombie_walk1.png",
                                                                  scale=character_scale, mirrored=True))
        self.player_sprite.walk_left_textures.append(arcade.load_texture("zombie_walk2.png",
                                                                  scale=character_scale, mirrored=True))


        # Our list of rooms
        self.rooms = []

        # Create the rooms. Extend the pattern for each room.
        room = setup_room_1()
        self.rooms.append(room)

        room = setup_room_2()
        self.rooms.append(room)

        # Our starting room number
        self.current_room = 0

        # Create a physics engine for this room
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].door_list)


    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        

        arcade.start_render()

        # Draw the background texture
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.rooms[self.current_room].background)
        
        # Draw all the walls in this room
     

        self.rooms[self.current_room].door_list.draw()
        self.rooms[self.current_room].wall_list.draw()
        self.rooms[self.current_room].coin_list.draw()
        self.rooms[self.current_room].bigpotion_list.draw()
        self.rooms[self.current_room].smallpotion_list.draw()
        # If you have coins or monsters, then copy and modify the line
        # above for each list.
        output = "Score: {}".format(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        self.player_sprite.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.W:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.player_sprite.change_y = -MOVEMENT_SPEED
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
            

        self.player_sprite.update_animation()
        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update() 

        # Do some logic here to figure out what room we are in, and if we need to go
        # to a different room.
        if self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 0:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0
        elif self.player_sprite.center_x < 0 and self.current_room == 1:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = SCREEN_WIDTH
        hit_list = arcade.check_for_collision_with_list(self.player_sprite,self.rooms[self.current_room].coin_list)
        hit_list2 = arcade.check_for_collision_with_list(self.player_sprite,self.rooms[self.current_room].bigpotion_list)
        hit_list3 = arcade.check_for_collision_with_list(self.player_sprite,self.rooms[self.current_room].smallpotion_list)
        
        for coin in hit_list:
            coin.kill()
            self.score += 1
            my_sound = arcade.load_sound("coinsound.wav")
            arcade.play_sound(my_sound)
        if self.score == 4:
            for i in self.rooms[self.current_room].door_list:
                i.kill()
                your_sound = arcade.load_sound("door.wav")
                arcade.play_sound(your_sound)

        for smallpotion in hit_list3:
            smallpotion.kill()
            self.player_sprite.scale=0.5
            tu_sound = arcade.load_sound("shrink.wav")
            arcade.play_sound(tu_sound)
        
        for bigpotion in hit_list2:
            bigpotion.kill()
            self.player_sprite.scale=1
            yo_sound = arcade.load_sound("grow.wav")
            arcade.play_sound(yo_sound)
        


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()