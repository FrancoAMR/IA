import pygame

# Window Size
window_Width = 1280
window_Height = 720

# Colors
gray = (234, 234, 234)
highlight_Color = (239, 160, 160, 165)
background_Color = (96, 155, 99, 165)
stat_Color = (101, 101, 102)
phase1_Color = (255, 233, 163)

# Field
field_Image = pygame.image.load("assets/images/field.png")
field_Width = 25*window_Width/64
field_Height = 17*window_Height/36
field_Image = pygame.transform.scale(field_Image, (field_Width, field_Height))
field_X = window_Width / 2 - field_Width / 2
field_Y = window_Height / 2 - field_Height / 2

# Cards
red_Card_Image = pygame.image.load("assets/images/redCard.png")
blue_Card_Image = pygame.image.load("assets/images/blueCard.png")
card_Width = 5*window_Width/64 #100
card_Height = 17*window_Height/72 #170
red_Card_Image = pygame.transform.scale(red_Card_Image, (card_Width, card_Height))
blue_Card_Image = pygame.transform.scale(blue_Card_Image, (card_Width, card_Height))
card_Init_X = window_Width / 2
card_Y = window_Height - card_Height

# Cards description
card_Desc_Image = pygame.image.load("assets/images/card_desc.png")
card_Desc_Width = 17*window_Width/128
card_Desc_Height = 17*window_Height/36
card_Desc_Image = pygame.transform.scale(card_Desc_Image, (card_Desc_Width, card_Desc_Height))
card_Desc_X = 0
card_Desc_Y = field_Y

# End Turn Button
end_Button_Image = pygame.image.load("assets/images/endphase.png")
mask = pygame.mask.from_surface(end_Button_Image)
end_Button_Width = 150
end_Button_Height = 150
end_Button_Image = pygame.transform.scale(end_Button_Image,(end_Button_Width,end_Button_Height))
end_Button_X = field_X + field_Width - end_Button_Width/2 + 150
end_Button_Y = field_Y + field_Height/2 - end_Button_Height/2

# LP
lp_Image = pygame.image.load("assets/images/lp.png")
lp_Width = 200
lp_Height = 146
lp_Image = pygame.transform.scale(lp_Image,(lp_Width,lp_Height))
lp_X = 0
lp_Y = window_Height - lp_Height

# x & y positions for matrix
positionX = [field_X,field_X+card_Width,field_X+card_Width*2,field_X+card_Width*3,field_X+card_Width*4]
positionY = [card_Y, window_Height/2, window_Height/2-card_Height, 0]

# Monster images
monster_images_array = ["1"] 
monster_image = pygame.image.load(f"assets/images/monster{monster_images_array[0]}.png")

# Difficult buttons images
difficulty_width = 300
difficulty_height = 100
easy_image = pygame.image.load("assets/images/easy.png")
easy_image = pygame.transform.scale(easy_image,(difficulty_width,difficulty_height))
medium_image = pygame.image.load("assets/images/medium.png")
medium_image = pygame.transform.scale(medium_image,(difficulty_width,difficulty_height))
hard_image = pygame.image.load("assets/images/hard.png")
hard_image = pygame.transform.scale(hard_image,(difficulty_width,difficulty_height))

