# def bouncing_ball(h, bounce, window):
#     if not (h > 0 and 0 < bounce < 1 and window < h):
#         return -1
#     else:
#         return 1 if h < window else 2 + bouncing_ball((h * bounce), bounce, window)
#

def bouncing_ball(initial_height, bounce_factor, window_height):
    # Check if the input parameters represent a valid scenario
    if not (initial_height > 0 and 0 < bounce_factor < 1 and window_height < initial_height):
        # If not, return -1 to indicate an invalid scenario
        return -1
    else:
        # If the ball is initially below the window, it won't bounce
        if initial_height < window_height:
            return 1
        else:
            # The ball is above the window, simulate a bounce and recursion
            new_height_after_bounce = initial_height * bounce_factor
            # Recursively call the function with updated parameters
            result_after_bounce = bouncing_ball(new_height_after_bounce, bounce_factor, window_height)
            # The final result is the number of bounces plus passing through the window
            return 2 + result_after_bounce
