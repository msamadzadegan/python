class Settings:
	"""A class to store all settings for Alien Invasion"""

	def __init__(self):
		"""Initialize the game settings"""
		#screen settings
		self.screen_width = 800
		self.screen_height = 600
		self.bg_color = (230, 230, 230)

		#Ship settings
		self.ship_speed = 1.5

		#إBullet settings
		self.bullet_speed = 0.5
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3
		