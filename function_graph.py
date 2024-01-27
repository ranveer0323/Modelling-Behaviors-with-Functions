import matplotlib.pyplot as plt
import numpy as np

def cumulative_views(t, vmax, a_category, a_people, a_language, a_music, 
a_subscribers, a_avg_views, a_engagement, a_avg_ctr):

    """
    Cumulative views function with uncertainty variables.

    Parameters:
    - t: time
    - vmax: maximum achievable views
    - a_category, a_people, ..., a_avg_ctr: coefficients for uncertainty variables

    Returns:
    - Cumulative views at time t
    """
    return vmax * (1 - np.exp(-(
        a_category * t +
        a_people * t +
        a_language * t +
        a_music * t +
        a_subscribers * t +
        a_avg_views * t +
        a_engagement * t +
        a_avg_ctr * t
    )))

# Set parameters for the cumulative views model
vmax = 1000000  # Maximum achievable views
a_category = 0.1
a_people = 0.2
a_language = 0.05
a_music = 0.2
a_subscribers = 0.05
a_avg_views = 0.1
a_engagement = 0.15
a_avg_ctr = 0.2

# Generate time values
t_values = np.linspace(0, 30, 100)  # Assuming time is in days

# Calculate cumulative views for each time value
views_values = cumulative_views(t_values, vmax, a_category, a_people, 
a_language, a_music, a_subscribers, a_avg_views, a_engagement, a_avg_ctr)

# Plot the cumulative views function
plt.plot(t_values, views_values, label='Cumulative Views')
plt.title('Cumulative Views Over Time with Uncertainty Variables')
plt.xlabel('Time (days)')
plt.ylabel('Cumulative Number of Views')
plt.legend()
plt.grid(True)
plt.show()
