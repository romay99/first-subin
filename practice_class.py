class unit:
    def __init__(self):
        print("Unit 생성자")

class flyable:
    def __init__(self):
        print("Flyable 생성자")

class flyableunit(flyable,unit):
    def __init__(self):
        unit.__init__(self)
        flyable.__init__(self)

dropship=flyableunit()