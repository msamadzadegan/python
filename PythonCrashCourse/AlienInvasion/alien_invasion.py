import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
	"""Overall class to manage game assets and behavior"""

	def __init__(self):
		"""Initilize the game and create game resources"""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((self.settings.screen_width,
			self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)
		self.bullet_flag = False
		self.bullet = pygame.sprite.Group()

	def run_game(self):
		"""Start the main loop for the game"""
		while True:
			self._check_events()
			self.ship.update()
			self.bullet.update()
			self._update_screen()

	def _check_events(self):
		"""Respond to key press and mouse events"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.display.quit()
				pygame.quit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		"""Respond to keypresses"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			pygame.display.quit()
			pygame.quit()
		elif event.key == pygame.K_SPACE:
			self.bullet_flag = True
			self._fire_bullet()

	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _fire_bullet(self):
		"""Create a new bullet and add it to the bullet group"""
		while self.bullet_flag:
			new_bullet = Bullet(self)
			self.bullet.add(new_bullet)

	def _update_screen(self):
		"""Update image on the screen and flip to the new screen"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullet.sprites():
			bullet.draw_bullet()

		pygame.display.flip()


if __name__ == '__main__':
	#Make the game instance and run the game
	ai = AlienInvasion()
	ai.run_game()
