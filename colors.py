class Colors:
    # UI
    grey = (26, 31, 40)
    dark_grey = (82, 82, 82)
    black = (0, 0, 0)
    white = (255, 255, 255)

    # Blocks
    green = (47, 230, 23)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    purple = (166, 0, 247)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)

    @classmethod
    def get_cell_colors(cls):
        return [cls.grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]