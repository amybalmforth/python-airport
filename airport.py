class Airport:

    def __init__(self):
        self.hangar = []
        self.capacity = 2

    def is_full(self):
        if len(self.hangar) >= self.capacity:
            return True
        else:
            return False

    def land(self, plane):
        if self.is_full():
            return "airport full"
        else:
            self.hangar.append(plane)
            return plane

    def takeoff(self, plane):
        self.hangar.pop()
        return plane


class Plane:
    pass
