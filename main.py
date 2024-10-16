import cv2
import sys
from initialization import initializeFaceMesh
from calibrate import calibrate, computeBaseline
from facedir import getFaceDir

def main():
    face_mesh, mp_drawing, mp_face_mesh = initializeFaceMesh()
    cap = cv2.VideoCapture(0)

    calibration_frames = 50
    calibration_data = []
    calibrated = False
    baseline = None
    frame_count = 0

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    image=frame,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 255), thickness=1, circle_radius=1))

                if not calibrated:
                    sys.stdout.write("\rCalibrating... ")
                    sys.stdout.flush()
                    calibrate(face_landmarks, calibration_data)
                    frame_count += 1

                    if frame_count >= calibration_frames:
                        baseline = computeBaseline(calibration_data)
                        calibrated = True
                        sys.stdout.write("\rCalibration complete\n")
                        sys.stdout.flush()
                else:
                    face_direction = getFaceDir(face_landmarks, baseline)
                    sys.stdout.write(f"\r{' ' * 50}\r{face_direction}")
                    sys.stdout.flush()

        cv2.imshow('MediaPipe Face Mesh with Face Tracking', frame)

        if cv2.waitKey(5) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()