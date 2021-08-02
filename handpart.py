import cv2
import mediapipe as mp
import time

class handdetector():
    def __init__(self, static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.static_image_mode = static_image_mode
        self.max_num_hands = max_num_hands
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

        self.mphands = mp.solutions.hands
        self.hands = self.mphands.Hands(self.static_image_mode, self.max_num_hands,
                                        self.min_detection_confidence, self.min_tracking_confidence)
        self.mpdraw = mp.solutions.drawing_utils
        self.drawing_styles = mp.solutions.drawing_styles

    def findhands(self, frame, draw = True):
        f_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(f_RGB)
        # print(result.multi_hand_landmarks)
        if self.result.multi_hand_landmarks:
            for hlm in self.result.multi_hand_landmarks:
                if draw:
                    self.mpdraw.draw_landmarks(frame, hlm, self.mphands.HAND_CONNECTIONS,
                                               self.drawing_styles.get_default_hand_landmark_style(),
                                               self.drawing_styles.get_default_hand_connection_style())
        return frame

    def findpos(self, frame, handno=0, draw=True):
        lmlist = []
        if self.result.multi_hand_landmarks:
            myhand = self.result.multi_hand_landmarks[handno]
            for id, lm in enumerate(myhand.landmark):
                # print(idx,lm)
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                #print(id, cx, cy)
                lmlist.append([id, cx, cy])
                # if id == 0:
                if draw:
                    cv2.circle(frame, (cx, cy), 10, (120, 0, 120), cv2.FILLED)
        return lmlist




def main():
    ptime = 0
    ctime = 0
    capture = cv2.VideoCapture(0)
    handdetect = handdetector()
    while capture.isOpened():
        source, frame = capture.read()
        frame = handdetect.findhands(frame)
        lmlist = handdetect.findpos(frame)
        if len(lmlist) != 0:
            print(lmlist[4])
        ctime = time.time()
        fps = 1 / (ctime - ptime)
        ptime = ctime
        # print(ctime)
        # print(ptime)
        tt = cv2.flip(frame, 0)
        cv2.putText(tt, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)

        cv2.imshow('Turukka', frame)
        if cv2.waitKey(10) == ord('q'):
            break
    capture.release()

if __name__ == "__main__":
    main()