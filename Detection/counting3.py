from datetime import datetime

import cv2
import csv
import numpy as np

cap = cv2.VideoCapture("video.mp4")

min_width_rect = 80  
min_height_rect = 80 

count_line_pos = 560
algo = cv2.createBackgroundSubtractorMOG2()

def center_handle(x, y, w, h):
    x1 = int(w/2)
    y1 = int(h/2)
    cx = x + x1
    cy = y + y1
    return cx, cy

def is_left_half(x, frame_width):
    return x < frame_width / 2

detect = []
offset = 5
counter = 0

csv_filename = 'vehicle_count3.csv'
csv_header = ['ID', 'Timestamp', 'Count']
csv_data = []
count_id = 1

while True:
    ret, frame1 = cap.read()
    frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # Get the frame width
    
    grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (3, 3), 5)
    img_sub = algo.apply(blur)
    dilate = cv2.dilate(img_sub, np.ones((5, 5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilateada = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel)
    dilateada = cv2.morphologyEx(dilateada, cv2.MORPH_CLOSE, kernel)
    counterShape, h = cv2.findContours(dilateada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.line(frame1, (10, count_line_pos), (550, count_line_pos), (255, 127, 0), 5)

    for (i, c) in enumerate(counterShape):
        (x, y, w, h) = cv2.boundingRect(c)
        validate_counter = (w >= min_width_rect) and (h >= min_height_rect)
        if not validate_counter:
            continue

        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame1, "Vehicle"+str(counter), (x, y-20), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 244, 0), 2)

        center = center_handle(x, y, w, h)
        detect.append(center)
        cv2.circle(frame1, center, 4, (0, 0, 255), -1)

        if is_left_half(center[0], frame_width) and y < count_line_pos + offset and y > count_line_pos - offset:
            counter += 1
            print("Count: " + str(counter))
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            csv_data.append([count_id, timestamp, counter])
            count_id += 1

    cv2.putText(frame1, "COUNT: " + str(counter), (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)

    cv2.imshow("Video Original", frame1)

    if cv2.waitKey(30) == 13:
        break

with open(csv_filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(csv_header)
    csvwriter.writerows(csv_data)

cv2.destroyAllWindows()
cap.release()
