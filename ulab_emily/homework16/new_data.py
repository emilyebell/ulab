#new_data.py

import torch
import numpy as np
def hidden_function(X, Y):
    """Generates a pattern using a hidden function and adds noise to obscure the data."""
    pattern = np.sin(X) + np.cos(Y)
    noise = np.random.normal(0, 0.2, size=pattern.shape)
    return pattern + noise

x_data = np.linspace(-3 * np.pi, 3 * np.pi, 1000)
y_data = np.linspace(-3 * np.pi, 3 * np.pi, 1000)
X, Y = np.meshgrid(x_data, y_data)
pattern = hidden_function(X, Y)

N, D_in, H, D_out = 1000, 2, 50, 1

x = torch.randn(N, D_in) * 3.1415
y = (x[:, 0].sin() + x[:, 1].cos()).unsqueeze(1)

noise = torch.randn(N, D_out) * 0.2  
y += noise

x_values = x.numpy()[:, 0]
y_values = x.numpy()[:, 1]
color_values = y.numpy().flatten()
