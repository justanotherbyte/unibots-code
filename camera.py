import cv2

# Typical HSV range for an ORANGE ping pong ball

class Colours:
    orange_lb = (5, 100, 100)
    orange_ub = (15, 255, 255)

def get_ball_position(frame: cv2.typing.MatLike):
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, Colours.orange_lb, Colours.orange_ub) # type: ignore
    mask = cv2.erode(mask, None, iterations=2) # type: ignore
    mask = cv2.dilate(mask, None, iterations=2) # type: ignore

    cnts, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        if radius > 10: # Minimum size to ignore noise
            return int(x), int(y), int(radius)

    return None
