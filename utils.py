def save_plot(fig, filename):
    """Save a Matplotlib figure to file."""
    fig.savefig(filename, bbox_inches='tight')
    print(f"Plot saved: {filename}")
