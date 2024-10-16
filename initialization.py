import cv2
import mediapipe as mp

def initializeFaceMesh():
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5)
    mp_drawing = mp.solutions.drawing_utils
    return face_mesh, mp_drawing, mp_face_mesh