import matplotlib.pyplot as plt
from IPython import display

import numpy as np

def interactive_loss_plot(plot_iter, plot_loss):
    
    # Clear and plot
    plt.plot(plot_iter, plot_loss)
    display.clear_output(wait=True)
    plt.show()
    
iters = 100
all_iters = []
all_losses = []
for iter in range(iters):
    loss = np.random.random()
    
    all_iters.append(iter)
    all_losses.append(loss)
    
    interactive_loss_plot(all_iters, all_losses)
