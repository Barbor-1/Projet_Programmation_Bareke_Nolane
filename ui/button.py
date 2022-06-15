
import pygame
class Button:
    """button class

    :param x: x position of button
    :type x: int
    :param y: y position of button
    :type y: int
    :param color: color of button (text)
    :type color: tupple of three int between 0 and 255
    :param background_color: color of button (background)
    :type background_color: tupple of three floats between 0 and 1
    :param screen: surface 
    :type screen: pygame.Surface
    :param size: size of text, defaults to 32
    :type size: int, optional

    """
    def __init__(self, x, y, color, background_color, screen, size=32):
        """init function for the class
       
        """
        self.x = x
        self.y = y
        self.screen = screen
        self.color = color
        self.size = size
        self.background_color = background_color

    def initButton(self, label, center=False): # Initialisation
        """init button

        :param label: text of button
        :type label: string
        :param center: if True => center the button (x, y are now center of the button), defaults to False
        :type center: bool, optional
        """
        self.label = label
        smallfont = pygame.font.SysFont("Sprite/CORBEL.TTF",self.size) # can change it ?
        self.text = smallfont.render(self.label, True , self.color) # render font
        if(center == False): # for button centering
            self.text_rect = self.text.get_rect(topleft=(self.x, self.y)) # get rectangle
        else:
            self.text_rect = self.text.get_rect(center=(self.x, self.y)) # get rectangle

    def drawButton(self):
        """draw the button
        """
        pygame.draw.rect(self.screen, self.background_color, (self.text_rect.x, self.text_rect.y, self.text_rect.width, self.text_rect.height))
        self.screen.blit(self.text, self.text_rect) # blit it

    def collide(self, pos): # Appeler quand on clique sur le bouton
        """check collision with button

        :param pos: mouse position
        :type pos: (int x, int y), x and y are the position of the mouse pointer
        :return: True if collision, otherwise false
        :rtype: bool
        """
        return self.text_rect.collidepoint(pos)


