import numpy as np

def calibrate(face_landmarks, calibration_data):
    nose_tip = face_landmarks.landmark[1]
    left_eye_outer = face_landmarks.landmark[33]
    right_eye_outer = face_landmarks.landmark[263]
    left_eye_inner = face_landmarks.landmark[133]
    right_eye_inner = face_landmarks.landmark[362]

    horizontal_center = (left_eye_outer.x + right_eye_outer.x) / 2
    eye_mid_y = (left_eye_inner.y + right_eye_inner.y) / 2

    calibration_data.append({
        'horizontal_center': horizontal_center,
        'eye_mid_y': eye_mid_y
    })

def computeBaseline(calibration_data):
    horizontal_centers = [data['horizontal_center'] for data in calibration_data]
    eye_mid_ys = [data['eye_mid_y'] for data in calibration_data]
    return {
        'horizontal_center': np.mean(horizontal_centers),
        'eye_mid_y': np.mean(eye_mid_ys)
    }