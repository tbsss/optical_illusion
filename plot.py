import numpy as np
from matplotlib.patches import Polygon


class Plot:
    def __init__(self, fig, ax):
        self.fig = fig
        self.ax = ax
        self.plot_dict = {}
        self.plot_dict2 = {}

        self.dark_fg = "0.2"
        self.bright_fg = "0.64"
        self.white_bg = "1.0"
        self.gray_bg = "0.5"
        self.black_bg = "0.0"

        # plot points per 90°
        self.num_x = 30

        self.z = 0.2
        self.top_bottom_border = 2 * self.z
        self.paired_function_offset = 0.5
        self.row_offset = 2.0

        self.rows = 12
        self.cols = 10
        self.height = (self.rows - 1) * self.row_offset + 2 * self.z + self.paired_function_offset + 2 * self.top_bottom_border
        self.width = self.cols * 2 * np.pi

        self.r = self.height / self.width
        self.width = self.height

        self.white_triangle = Polygon([[0, self.height],
                                       [0.5 * self.width, self.height],
                                       [0, 0.5 * self.height]],
                                      color=self.white_bg)
        self.gray_polygon = Polygon([[0.5 * self.width, self.height],
                                     [self.width, self.height],
                                     [self.width, 0.5 * self.height],
                                     [0.5 * self.width, 0],
                                     [0, 0],
                                     [0, 0.5 * self.height]], color=self.gray_bg)
        self.black_triangle = Polygon([[self.width, 0.5 * self.height],
                                       [self.width, 0],
                                       [0.5 * self.width, 0]],
                                      color=self.black_bg)

        self.ax.add_patch(self.white_triangle)
        self.ax.add_patch(self.gray_polygon)
        self.ax.add_patch(self.black_triangle)

        for i in range(self.rows):
            if i % 2 == 0:
                colors = (self.dark_fg, self.dark_fg, self.bright_fg, self.bright_fg)
            else:
                colors = (self.bright_fg, self.dark_fg, self.dark_fg, self.bright_fg)
            for j in range(self.cols):
                for k in range(4):
                    xs = np.linspace((2*j+k/2)*np.pi*self.r, (2*j+(k+1)/2)*np.pi*self.r, self.num_x)
                    y1 = self.z * np.sin(xs / self.r) + i * self.row_offset + self.z + self.top_bottom_border
                    y2 = y1 + self.paired_function_offset
                    # keep plots for color changing
                    self.plot_dict[(i, j, k)] = self.ax.plot(xs, y1, color=colors[k])
                    self.plot_dict2[(i, j, k)] = self.ax.plot(xs, y2, color=colors[k])

    def update_white_bg(self, val):
        self.white_triangle.set_color(str(val))
        self.fig.canvas.draw()

    def update_gray_bg(self, val):
        self.gray_polygon.set_color(str(val))
        self.fig.canvas.draw()

    def update_black_bg(self, val):
        self.black_triangle.set_color(str(val))
        self.fig.canvas.draw()

    def update_bright_fg(self, val):
        self.bright_fg = str(val)
        self.update_colors()
        self.fig.canvas.draw()

    def update_dark_fg(self, val):
        self.dark_fg = str(val)
        self.update_colors()
        self.fig.canvas.draw()

    def update_colors(self):
        for i in range(self.rows):
            if i % 2 == 0:
                colors = (self.dark_fg, self.dark_fg, self.bright_fg, self.bright_fg)
            else:
                colors = (self.bright_fg, self.dark_fg, self.dark_fg, self.bright_fg)
            for j in range(self.cols):
                for k in range(4):
                    for l in self.plot_dict[(i, j, k)]:
                        l.set_color(colors[k])
                    for l in self.plot_dict2[(i, j, k)]:
                        l.set_color(colors[k])
