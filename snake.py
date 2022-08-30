class Snake:

    n = 3
    points = [[500,500],[550,500],[600,500],[650,500]]
    pHead = points[0]
    leap = 20


    def __init__(self):
        pass
    def MoveSnake(self,pt):
        for i in range(len(self.points) - 1):
            self.points[-1 - i][0] = self.points[-2-i][0]

            self.points[-1 - i][1] = self.points[-2-i][1]



        if pt[0] > self.points[0][0]:
            self.points[0][0] += self.leap
        else:
            self.points[0][0] -= self.leap

        if pt[1] > self.points[0][1]:
            self.points[0][1] += self.leap
        else:
            self.points[0][1] -= self.leap





    def GrowSnake(self):
        pt = self.points[-1][0:2]
        self.points.append(pt)


    def IsFoodEaten(self, pt1,pt2):
        if self.points[0][0] > pt1[0] :
            if self.points[0][0] < pt2[0]:
                if self.points[0][1] > pt1[1]:
                    if self.points[0][1]<pt2[1  ]:
                        return 1


        return 0










