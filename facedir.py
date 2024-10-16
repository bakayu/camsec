def getFaceDir(landmarks, baseline):
    nose_tip_index = 1
    left_eye_outer_index = 33
    right_eye_outer_index = 263
    left_eye_inner_index = 133
    right_eye_inner_index = 362

    nose_tip = landmarks.landmark[nose_tip_index]
    left_eye_outer = landmarks.landmark[left_eye_outer_index]
    right_eye_outer = landmarks.landmark[right_eye_outer_index]
    left_eye_inner = landmarks.landmark[left_eye_inner_index]
    right_eye_inner = landmarks.landmark[right_eye_inner_index]

    horizontal_center = (left_eye_outer.x + right_eye_outer.x) / 2
    vertical_center = (left_eye_outer.y + right_eye_outer.y) / 2

    if nose_tip.x < baseline['horizontal_center'] - 0.02:
        horizontal_direction = "Face pointing Right"
    elif nose_tip.x > baseline['horizontal_center'] + 0.02:
        horizontal_direction = "Face pointing Left"
    else:
        horizontal_direction = "Looking Forward"

    eye_mid_y = (left_eye_inner.y + right_eye_inner.y) / 2
    if nose_tip.y < baseline['eye_mid_y'] - 0.02:
        vertical_direction = "Up"
    elif nose_tip.y > baseline['eye_mid_y'] + 0.15:
        vertical_direction = "Down"
    else:
        vertical_direction = "Straight"

    return f"{horizontal_direction} and {vertical_direction}"