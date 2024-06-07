import pygame


class Display:
    def __init__(self, cell_size, matrix_size):
        pygame.init()
        self.cell_size = cell_size
        self.matrix_size = matrix_size
        self.width = cell_size * matrix_size
        self.height = cell_size * matrix_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        
        pygame.display.set_caption("Person Flow Simulator")
        self.screen.fill((255, 255, 255))
        self.margin = 5

    def draw_rect(self, row, col, color):
        pygame.draw.rect(self.screen, color, (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size))

    def draw_circle(self, row, col, color):
        radius = self.cell_size // 2 - self.margin
        center_x = col * self.cell_size + self.cell_size // 2
        center_y = row * self.cell_size + self.cell_size // 2
        pygame.draw.circle(self.screen, color, (center_x, center_y), radius)

    def draw_big_circle(self, x, y, radius, color):
        pygame.draw.circle(self.screen, color, (x * self.cell_size, y * self.cell_size), radius * self.cell_size, self.margin)
    
    def display(self):
        pygame.display.flip()

    def end(self):
        pygame.quit()

if __name__ == "__main__":
    display = Display(30, 20)

    display.update_cell(0, 0, (255, 0, 0))
    display.update_cell(0, 1, (0, 255, 0))
    display.update_cell(1, 0, (0, 0, 255))
    display.update_cell(1, 1, (255, 255, 0))

    display.display()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                display.end()
                break
    # pygame.time.wait(5000)
    # display.end()
