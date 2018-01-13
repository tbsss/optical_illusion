import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from plot import Plot


def main():
    fig, ax = plt.subplots()
    ax.set_aspect("equal")
    ax.set_aspect("equal")
    plot = Plot(fig, ax)

    s_fig, s_axs = plt.subplots(5, 1, figsize=(10,2))

    s_bbg = Slider(s_axs[0], 'white triangle', 0.0, 1.0, valinit=1.0)
    s_gbg = Slider(s_axs[1], 'gray polygon', 0.0, 1.0, valinit=0.42)
    s_dbg = Slider(s_axs[2], 'black triangle', 0.0, 1.0, valinit=0.0)
    s_dfg = Slider(s_axs[3], 'dark sinus', 0.0, 1.0, valinit=0.24)
    s_bfg = Slider(s_axs[4], 'bright sinus', 0.0, 1.0, valinit=0.64)

    s_bbg.on_changed(plot.update_white_bg)
    s_gbg.on_changed(plot.update_gray_bg)
    s_dbg.on_changed(plot.update_black_bg)
    s_dfg.on_changed(plot.update_dark_fg)
    s_bfg.on_changed(plot.update_bright_fg)

    plt.show()


if __name__ == "__main__":
    main()