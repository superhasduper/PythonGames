import arcade

arcade.open_window(600, 600, "Drawing Example")

arcade.set_background_color(arcade.color.BLIZZARD_BLUE)

arcade.start_render()

arcade.draw_circle_outline(300, 285, 200, arcade.color.BLACK_BEAN, 3)

arcade.draw_circle_outline(300, 185, 70, arcade.color.BLACK_BEAN, 5)
arcade.draw_circle_filled(420, 300, 40, arcade.color.BLACK_BEAN)
arcade.draw_circle_filled(320, 300, 40, arcade.color.BLACK_BEAN)

arcade.finish_render()

arcade.run()

