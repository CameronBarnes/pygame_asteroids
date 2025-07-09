import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
	def __init__(self, x: float, y: float, radius: float) -> None:
		super().__init__(x, y, radius)
	
	def draw(self, screen: pygame.Surface):
		pygame.draw.circle(screen, "white", self.position, self.radius, 2)
	
	def update(self, dt: float):
		self.position += self.velocity * dt
	
	def split(self):
		import random
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		angle = random.uniform(20, 50)
		min = self.velocity.rotate(-angle)
		max = self.velocity.rotate(angle)
		first = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
		first.velocity = min * 1.2
		second = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
		second.velocity = max * 1.2
