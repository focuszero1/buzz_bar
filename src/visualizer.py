import pygame

def run_visualizer(get_spectrum_callback):
    """Creates window and draws spectrum bars based on callback."""
    pygame.init()
    window_size = (600, 100)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Buzz Bar")

    num_bars = 16
    bar_spacing = 4
    bar_color = (255, 140, 0)

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        bars_data = get_spectrum_callback()

        # Scaling: find max value to normalize (prevent huge jumps)
        max_value = max(max(bars_data), 0.05)  # Don't let it normalize to < 0.05
        screen.fill((0, 0, 0))

        total_spacing = bar_spacing * (num_bars - 1)
        bar_width = (window_size[0] - total_spacing) // num_bars

        for i, value in enumerate(bars_data):
            x = i * (bar_width + bar_spacing)
            scaled_height = int((value / max_value) * window_size[1])  # scale to window height
            y = window_size[1] - scaled_height
            pygame.draw.rect(screen, bar_color, (x, y, bar_width, scaled_height))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
