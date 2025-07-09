import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SHOOT_COOLDOWN, PLAYER_SHOOT_SPEED, PLAYER_SPEED, PLAYER_TURN_SPEED
from shot import Shot

class Player(CircleShape):
	def __init__(self, x: float, y: float) -> None:
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation: float = 0
		self.shoot_timer: float = 0

	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]

	def draw(self, screen: pygame.Surface):
		pygame.draw.polygon(screen, "white", self.triangle(), 2)
	
	def rotate(self, dt: float):
		self.rotation += PLAYER_TURN_SPEED * dt
	
	def update(self, dt: float):
		self.shoot_timer -= dt
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a]:
			self.rotate(-dt)
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_SPACE] and self.shoot_timer <= 0:
			self.shoot()

		self.move(dt)
	
	def move(self, dt: float):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt
	
	def shoot(self):
		self.shoot_timer = PLAYER_SHOOT_COOLDOWN
		shot = Shot(self.position[0], self.position[1])
		shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED 
