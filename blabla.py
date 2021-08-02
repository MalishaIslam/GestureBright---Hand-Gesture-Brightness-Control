# import cv2
# import mediapipe as mp
# mp_drawing = mp.solutions.drawing_utils
# mp_hands = mp.solutions.hands
# drawing_styles = mp.solutions.drawing_styles
#
# cap = cv2.VideoCapture(0)
# with mp_hands.Hands(
#     min_detection_confidence=0.5,
#     min_tracking_confidence=0.5) as hands:
#   while cap.isOpened():
#     success, image = cap.read()
#     if not success:
#       print("Ignoring empty camera frame.")
#       # If loading a video, use 'break' instead of 'continue'.
#       continue
#
#     # Flip the image horizontally for a later selfie-view display, and convert
#     # the BGR image to RGB.
#     image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
#     # To improve performance, optionally mark the image as not writeable to
#     # pass by reference.
#     image.flags.writeable = False
#     results = hands.process(image)
#
#     # Draw the hand annotations on the image.
#     image.flags.writeable = True
#     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#     if results.multi_hand_landmarks:
#       for hand_landmarks in results.multi_hand_landmarks:
#         mp_drawing.draw_landmarks(
#             image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
#             #drawing_styles.get_default_hand_landmark_style(),
#             #drawing_styles.get_default_hand_connection_style())
#     cv2.imshow('MediaPipe Hands', image)
#     if cv2.waitKey(5) & 0xFF == 27:
#       break
# cap.release()







# import cv2
# import mediapipe as mp
# import time
#
# capture = cv2.VideoCapture(0)
# mphands = mp.solutions.hands
# mpdraw = mp.solutions.drawing_utils
# drawing_styles = mp.solutions.drawing_styles
#
# ptime = 0
# ctime = 0
#
# hands = mphands.Hands()
# while capture.isOpened():
#     source, frame = capture.read()
#     f_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     result = hands.process(f_RGB)
#     #print(result.multi_hand_landmarks)
#
#     if result.multi_hand_landmarks:
#         for hlm in result.multi_hand_landmarks:
#             for id, lm in enumerate(hlm.landmark):
#                 #print(id,lm)
#                 h, w, c = frame.shape
#                 cx, cy = int(lm.x*w) , int(lm.y*h)
#                 print(id, cx, cy)
#                 #if id == 0:
#                 cv2.circle(frame, (cx,cy), 10, (120,0,120), cv2.FILLED)
#             mpdraw.draw_landmarks(frame,hlm, mphands.HAND_CONNECTIONS,
#             drawing_styles.get_default_hand_landmark_style(),
#             drawing_styles.get_default_hand_connection_style())
#     ctime = time.time()
#     fps = 1/(ctime - ptime)
#     ptime = ctime
#     #print(ctime)
#     #print(ptime)
#     tt = cv2.flip(frame, 0)
#     cv2.putText(tt, str(int(fps)),(10,70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255,0,255),3)
#
#     cv2.imshow('Turukka',frame)
#     if cv2.waitKey(10) == ord('q'):
#         break
# capture.release()

import screen_brightness_control as sbc

# get current brightness value
print(sbc.get_brightness())

# set brightness to 50%
sbc.set_brightness(50)

print(sbc.get_brightness())

# set the brightness of the primary display to 75%
sbc.set_brightness(80, display=0)

print(sbc.get_brightness())

ll = [[1,2],[3,4],[5,6]]
print(ll[2][0])# import cv2
# import mediapipe as mp
# mp_drawing = mp.solutions.drawing_utils
# mp_hands = mp.solutions.hands
# drawing_styles = mp.solutions.drawing_styles
#
# cap = cv2.VideoCapture(0)
# with mp_hands.Hands(
#     min_detection_confidence=0.5,
#     min_tracking_confidence=0.5) as hands:
#   while cap.isOpened():
#     success, image = cap.read()
#     if not success:
#       print("Ignoring empty camera frame.")
#       # If loading a video, use 'break' instead of 'continue'.
#       continue
#
#     # Flip the image horizontally for a later selfie-view display, and convert
#     # the BGR image to RGB.
#     image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
#     # To improve performance, optionally mark the image as not writeable to
#     # pass by reference.
#     image.flags.writeable = False
#     results = hands.process(image)
#
#     # Draw the hand annotations on the image.
#     image.flags.writeable = True
#     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#     if results.multi_hand_landmarks:
#       for hand_landmarks in results.multi_hand_landmarks:
#         mp_drawing.draw_landmarks(
#             image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
#             #drawing_styles.get_default_hand_landmark_style(),
#             #drawing_styles.get_default_hand_connection_style())
#     cv2.imshow('MediaPipe Hands', image)
#     if cv2.waitKey(5) & 0xFF == 27:
#       break
# cap.release()







# import cv2
# import mediapipe as mp
# import time
#
# capture = cv2.VideoCapture(0)
# mphands = mp.solutions.hands
# mpdraw = mp.solutions.drawing_utils
# drawing_styles = mp.solutions.drawing_styles
#
# ptime = 0
# ctime = 0
#
# hands = mphands.Hands()
# while capture.isOpened():
#     source, frame = capture.read()
#     f_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     result = hands.process(f_RGB)
#     #print(result.multi_hand_landmarks)
#
#     if result.multi_hand_landmarks:
#         for hlm in result.multi_hand_landmarks:
#             for id, lm in enumerate(hlm.landmark):
#                 #print(id,lm)
#                 h, w, c = frame.shape
#                 cx, cy = int(lm.x*w) , int(lm.y*h)
#                 print(id, cx, cy)
#                 #if id == 0:
#                 cv2.circle(frame, (cx,cy), 10, (120,0,120), cv2.FILLED)
#             mpdraw.draw_landmarks(frame,hlm, mphands.HAND_CONNECTIONS,
#             drawing_styles.get_default_hand_landmark_style(),
#             drawing_styles.get_default_hand_connection_style())
#     ctime = time.time()
#     fps = 1/(ctime - ptime)
#     ptime = ctime
#     #print(ctime)
#     #print(ptime)
#     tt = cv2.flip(frame, 0)
#     cv2.putText(tt, str(int(fps)),(10,70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255,0,255),3)
#
#     cv2.imshow('Turukka',frame)
#     if cv2.waitKey(10) == ord('q'):
#         break
# capture.release()

