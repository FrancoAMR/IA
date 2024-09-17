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
card_width = 5*window_width/64 #100
card_height = 17*window_height/72 #170
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

# End Turn Button
end_button_image = pygame.image.load("assets/images/endphase.png")
end_button_width = 100
end_button_height = 100
end_button_image = pygame.transform.scale(end_button_image,(end_button_width,end_button_height))
end_button_x = field_x + field_width - end_button_width/2 + 100
end_button_y = field_y + field_height/2 - end_button_height/2

# LP
lp_image = pygame.image.load("assets/images/lp.png")
lp_width = 200
lp_height = 146
lp_image = pygame.transform.scale(lp_image,(lp_width,lp_height))
lp_x = 0
lp_y = window_height - lp_height