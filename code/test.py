import pygame, sys
from pytmx.util_pygame import load_pygame

class Tile(pygame.sprite.Sprite):
	def __init__(self,pos,surf,groups):
		super().__init__(groups)
		self.image = surf
		self.rect = self.image.get_rect(topleft = pos)

pygame.init()
screen = pygame.display.set_mode((1280,720))
tmx_data = load_pygame('../data/tmx/map.tmx')
sprite_group = pygame.sprite.Group()

# cycle through all layers
for layer in tmx_data.visible_layers:
	# if layer.name in ('Floor', 'Plants and rocks', 'Pipes')
	if hasattr(layer,'data'):
		for x,y,surf in layer.tiles():
			pos = (x * 64, y * 64)
			Tile(pos = pos, surf = surf, groups = sprite_group)

for obj in tmx_data.objects:
	pos = obj.x,obj.y
	if obj.type in ('Building', 'Vegetation'):
		Tile(pos = pos, surf = obj.image, groups = sprite_group)


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.fill('black')
	sprite_group.draw(screen)
	
	pygame.display.update()