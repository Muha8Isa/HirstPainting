# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import random

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
              (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50),
              (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
              (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208),
              (168, 99, 102)]

modified_color_list = [(r / 255, g / 255, b / 255) for r, g, b in color_list] #Because turtle reads color intensity as a range between 0 and 1

from turtle import Turtle, Screen

screen = Screen()
screen.screensize(500, 500)

tom = Turtle()


def draw_dots():
    tom.penup()
    tom.setpos(-200, -200)
    tom.hideturtle()
    tom.speed("fastest")
    for i in range(-150,350, 50):
        for _ in range(0,10):
            tom.dot(20, random.choice(modified_color_list))
            tom.fd(50)
        tom.setx(-200)
        tom.sety(i)


draw_dots()
screen.exitonclick()
