import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from .core import get_ax
from ..probability.experiments import generate_monte_carlo_point

_anim = None


def animate_monte_carlo(n_points: int):
    """
    Animate Monte-Carlo method with auto acceleration.
    
    Arguments:
        n_points (int): Amount of points.
    """
    global _anim
    
    ax = get_ax()
    
    ax.set_xlim(-1.9, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_aspect('equal')
    ax.set_title(f"Monte Carlo Simulation (Goal: {n_points})")

    square = plt.Rectangle((-1, -1), 2, 2, fill=False, edgecolor='black', linewidth=2)
    circle = plt.Circle((0, 0), 1, color='lightblue', alpha=0.3)
    ax.add_artist(square)
    ax.add_artist(circle)

    text_info = ax.text(-1.8, 1.0, 'Starting...', fontsize=12, 
                        bbox=dict(facecolor='white', alpha=0.8),
                        verticalalignment='top')

    x_in, y_in = [], []
    x_out, y_out = [], []
    
    scat_in = ax.scatter([], [], color='limegreen', s=15, label='Inside')
    scat_out = ax.scatter([], [], color='salmon', s=15, label='Outside')
    ax.legend(loc='upper right')

    stats = {'total': 0, 'inside': 0}

    def update(frame):
        current_count = stats['total']
        
        if current_count < 500:
            batch_size = 1
        elif current_count < 1000:
            batch_size = 50
        else:
            batch_size = 500
            
        for _ in range(batch_size):
            if stats['total'] >= n_points:
                if _anim and _anim.event_source:
                    _anim.event_source.stop()
                break

            x, y, is_inside = generate_monte_carlo_point()
            
            stats['total'] += 1
            
            if is_inside:
                x_in.append(x)
                y_in.append(y)
                stats['inside'] += 1
            else:
                x_out.append(x)
                y_out.append(y)
        
        if len(x_in) > 0:
            scat_in.set_offsets(list(zip(x_in, y_in)))
        else:
            scat_in.set_offsets(np.zeros((0, 2)))
            
        if len(x_out) > 0:
            scat_out.set_offsets(list(zip(x_out, y_out)))
        else:
            scat_out.set_offsets(np.zeros((0, 2)))

        if stats['total'] > 0:
            pi_est = 4 * stats['inside'] / stats['total']
            text_info.set_text(f"Points: {stats['total']}/{n_points}\n"
                               f"Speed: x{batch_size}\n"
                               f"π ≈ {pi_est:.5f}")
            
        return scat_in, scat_out, text_info

    _anim = animation.FuncAnimation(
        ax.figure, 
        update, 
        interval=1,
        blit=False,
        repeat=False,
        save_count=n_points 
    )
    
    plt.show()