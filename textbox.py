import pygame
class Textbox:
    #TODO : AUTO WIDTH ADJUST ? + continous key press ? 
    def __init__(self, screen, x, y, h, w, color, borderColor=(0, 0, 0),textColor=(255, 255, 255), fontSize=14):
        self.screen = screen
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.color = color
        self.borderColor = borderColor
        self.textColor = textColor
        self.rect = pygame.Rect(x, y, w, h, )
        self.borderWidth = 5
        self.active = False
        self.font = pygame.font.Font(None, fontSize)
        self.text = "a"
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, self.color, self.rect,width=self.borderWidth)
        text_surface = self.font.render(self.text, True, self.textColor)
        self.screen.blit(text_surface, text_surface.get_rect(topleft=(self.x, self.y)))

    
    def listen(self, event):
        if(event.type == pygame.MOUSEBUTTONDOWN):
            print("pos", pygame.mouse.get_pos())
            if(self.rect.collidepoint(pygame.mouse.get_pos())):
                self.active = not self.active
                print("active ?", self.active)
            else:
                self.active = False
            #change color of input box ?

        if(event.type == pygame.KEYDOWN and self.active == True):
            if event.key == pygame.K_RETURN:
                        print(self.text + " return\n")
                        return True
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1] # return all element except last one
            else:
                self.text += event.unicode
                print(self.text)
        self.draw()
            
    def getText(self):
        return self.text
