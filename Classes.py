class GameObject:
    Position = None
    Image = None
    ColliderRect = None

    def SpawnObject(self):
        self.Position = 1

    def DestroyObject(self):
        self.Position = 1


class Entity(GameObject):
    HealthPoint = None


class Player(Entity):
    Points = None


class Enemy(Entity):
    IQ = None


class WorldObject(GameObject):
    Coordinates = None


class Wall(WorldObject):
    Color = None


class Food(WorldObject):
    Color = None
