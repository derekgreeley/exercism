"""Solution to Ellen's Alien Game exercise."""
class Alien:
    """Represents an alien in Ellen's game."""

    total_aliens_created = 0
    health = 3  # default health shared at class level

    
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3

        Alien.total_aliens_created += 1
    
    def hit(self):
        self.health -= 1

    def is_alive(self):
        return self.health > 0

    def teleport(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def collision_detection(self, other_object):
        return None

        
def new_aliens_collection(positions):

    return [Alien(x, y) for (x, y) in positions]
