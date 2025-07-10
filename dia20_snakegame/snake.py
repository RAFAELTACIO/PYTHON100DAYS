from turtle import Screen, Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0


class Snake:
    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]
        self.last_heading = 0

    def createSnake(self):
        for position in START_POSITIONS:
            self.addSegment(position)

    def addSegment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    def extendSnake(self):
        self.addSegment(self.segments[-1].position())

    def move(self):

        if abs(self.head.heading() - self.last_heading) == 180:
            self.head.setheading(self.last_heading)

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

        # Update the last_heading property at the end
        self.last_heading = self.head.heading()


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
