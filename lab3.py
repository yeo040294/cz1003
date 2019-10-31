from sense_hat import SenseHat
sense = SenseHat()

sense.show_message("hello")
sense.set_rotation(180)
sense.show_message("hello", text_colour = (255,255,0))
sense.show_message("hello", back_colour = (255,255,0))
sense.show_message("hello", scroll_speed = 0.5)

sense.clear()



from sense_hat import SenseHat
sense = SenseHat()


msga = int(input("input your msga: "))
msgb = int(input("input your msgb"))


colour_msg = (255.255.0)
colour_bg = (255.0.0)
speed = (0.2)




sense.show_message("i got it", text_colour = colour_msg, back_colour = colour_bg, scroll_speed = scroll_speed = speed)

