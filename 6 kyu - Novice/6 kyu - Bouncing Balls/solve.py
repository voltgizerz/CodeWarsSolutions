def bouncingBall(h, bounce, window):
    return 2 + bouncingBall(h * bounce, bounce, window) if (h > 0 and bounce > 0 and bounce < 1 and window < h)  else -1
