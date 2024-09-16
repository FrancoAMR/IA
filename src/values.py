import pygame

# Window Size
window_width = 1280
window_height = 720

# Colors
gray = (234, 234, 234)
highlight_color = (239, 160, 160, 165)
background_color = (96, 155, 99, 165)

# Field
field_image = pygame.image.load("assets/images/field.png")
field_width = 25*window_width/64
field_height = 17*window_height/36
field_image = pygame.transform.scale(field_image, (field_width, field_height))
field_x = window_width / 2 - field_width / 2
field_y = window_height / 2 - field_height / 2

# Cards
card_image = pygame.image.load("assets/images/card.png")
card_width = 5*window_width/64
card_height = 17*window_height/72
card_image = pygame.transform.scale(card_image, (card_width, card_height))
card_init_x = window_width / 2
card_y = window_height - card_height

# Cards description
card_desc_image = pygame.image.load("assets/images/card_desc.png")
card_desc_width = 17*window_width/128
card_desc_height = 17*window_height/36
card_desc_image = pygame.transform.scale(card_desc_image, (card_desc_width, card_desc_height))
card_desc_x = 0
card_desc_y = field_y