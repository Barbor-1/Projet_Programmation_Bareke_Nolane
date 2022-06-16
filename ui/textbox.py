import pygame


class Textbox:
    # TODO : AUTO WIDTH ADJUST ? + continous key press ?
    """Textbox class  => for typing text

    :param screen: surface to draw onto
    :type screen: pygame.Surface
    :param x: x coordinate of the textbox
    :type x: int
    :param y: y coordinate of the textbox
    :type y: int
    :param h:  height of the textbox
    :type h: int
    :param w:  width of the function
    :type w: int
    :param color: color of the textbox (background)
    :type color: tupple : (r g, b) with rgb spanning from 0 to 255
    :param borderColor: color of the border
    :type borderColor: tupple : (r g, b) with rgb spanning from 0 to 255
    :param textColor: color fo the text inside the textbox
    :type textColor: tupple : (r g, b) with rgb spanning from 0 to 255
    :param fontSize: size of the font
    :type fontSize: int
    """
    def __init__(self, screen, x, y, h, w, color, borderColor=(0, 0, 0), textColor=(255, 255, 255), fontSize=14):
        """
        init the textbox
      
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.color = color
        self.borderColor = borderColor
        self.textColor = textColor
        self.rect = pygame.Rect(x, y, w, h, ) # rectangle
        self.rect.center = (self.x, self.y)
        self.borderWidth = 5
        self.active = False
        self.font = pygame.font.Font("Sprite/CORBEL.TTF", fontSize)
        self.text = ""
        self.cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_IBEAM) # I cursor

    def draw(self):
        """
        draw the textbox
        """
        text_surface = self.font.render(self.text, True, self.textColor) # text surface
        pygame.draw.rect(self.screen, self.color, self.rect) # main rect
        pygame.draw.rect(self.screen, self.borderColor, self.rect, width=self.borderWidth) #border rect
        self.screen.blit(text_surface, text_surface.get_rect(center=(self.x, self.y))) # draw everythingon the screen

    def listen(self, event):  # listen for events => clicked event ....
        """
        listen for events and manage the textbox (updating and drawing text inside it ...) dont forget to update the surface / screen after

        :param event: event to listen to (only one event)
        :rtype: pygame.Event
        :return: True if entered
        :rtype: bool
        """
        if (event.type == pygame.MOUSEBUTTONDOWN): # click 
            # print("pos", pygame.mouse.get_pos())
            if (self.rect.collidepoint(pygame.mouse.get_pos())): # on a cliqué dans la textbox
                self.active = not self.active #actif
                # print("active ?", self.active)
            else:
                self.active = False # non actif
            # change color of input box ?
            if (self.active == True):
                pygame.mouse.set_cursor(self.cursor)  # changing cursor to I
            if (self.active == False):
                pygame.mouse.set_cursor(pygame.cursors.arrow)  # changing cursor to default
        if (event.type == pygame.KEYDOWN and self.active == True):
            if event.key == pygame.K_RETURN: # return True (not used)
                # print(self.text + " return\n")
                return True
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]  # return all element except last one
            else:
                self.text += event.unicode # update text
                # print(self.text)

        self.draw() # update textbox

    def getText(self):
        """return the text that was typed inside the textbox

        :return: the text that was typed inside the textbox
        :rtype: string
        """
        return self.text 
