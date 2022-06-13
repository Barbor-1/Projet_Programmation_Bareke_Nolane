import pygame


class Textbox:
    # TODO : AUTO WIDTH ADJUST ? + continous key press ?
    """
   Textbox class

    """
    def __init__(self, screen, x, y, h, w, color, borderColor=(0, 0, 0), textColor=(255, 255, 255), fontSize=14):
        """

        :param screen: surface to draw onto
        :param x: x coordinate of the textbox
        :param y: y coordinate of the textbox
        :param h:  height of the textbox
        :param w:  width of the function
        :param color:  color of the textbox (background)
        :param borderColor: color of the border
        :param textColor: color fo the text inside the textbox
        :param fontSize: size of the font
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.color = color
        self.borderColor = borderColor
        self.textColor = textColor
        self.rect = pygame.Rect(x, y, w, h, )
        self.rect.center = (self.x, self.y)
        self.borderWidth = 5
        self.active = False
        self.font = pygame.font.Font("Sprite/CORBEL.TTF", fontSize)
        self.text = ""
        self.cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_IBEAM)

    def draw(self):
        """
        draw the textbox
        :return:
        """
        text_surface = self.font.render(self.text, True, self.textColor)
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, self.borderColor, self.rect, width=self.borderWidth)
        self.screen.blit(text_surface, text_surface.get_rect(center=(self.x, self.y)))

    def listen(self, event):  # listen for events => clicked event ....
        """
        listen for events and manage the textbox (updating and drawing text inside it ...) dont forget to update the surface / screen after

        :param event: event to listen to (only one event)
        :return:
        """
        if (event.type == pygame.MOUSEBUTTONDOWN):
            # print("pos", pygame.mouse.get_pos())
            if (self.rect.collidepoint(pygame.mouse.get_pos())):
                self.active = not self.active
                # print("active ?", self.active)
            else:
                self.active = False
            # change color of input box ?
            if (self.active == True):
                pygame.mouse.set_cursor(self.cursor)  # changing cursor to I
            if (self.active == False):
                pygame.mouse.set_cursor(pygame.cursors.arrow)  # changing cursor to default
        if (event.type == pygame.KEYDOWN and self.active == True):
            if event.key == pygame.K_RETURN:
                # print(self.text + " return\n")
                return True
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]  # return all element except last one
            else:
                self.text += event.unicode
                # print(self.text)

        self.draw()

    def getText(self):
        """

        :return: the text that was typed inside the textbox
        """
        return self.text