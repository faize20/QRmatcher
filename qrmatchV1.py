import cv2
from pyzbar.pyzbar import decode
import numpy as np

#INFO DARI QR
QR1 = 'N,N,N,W,4'
QR2 = 'N,E,E,S,0'
QR3 = 'N,N,E,S,0'
QR4 = 'W,E,S,S,2'
QR5 = 'W,N,E,W,3'
QR6 = 'W,S,S,S,1'
QR7 = '3 victim'
QR8 = '6 victim'
QR9 = 'FIRE'
QR10 = 'top pole good'
QR11 = 'water pump disconnect'
QR12 = 'Window Crack'
QR13 = 'Wire Insulator Broken'

qr_list = [QR1, QR2, QR3, QR4, QR5, QR6, QR7, QR8, QR9, QR10, QR11, QR12, QR13]

qr_data = ''  # Shared variable

def QRMATCH(data):
    if data in qr_list:
        print("QR MATCH")
    else:
        print("QR Not match")

def main():
    global qr_data
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open webcam")
        return

    print("Press 'q' to quit...\n")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        decoded_objects = decode(frame)
        for obj in decoded_objects:
            qr_data = obj.data.decode("utf-8")
            print("QR CODE:",qr_data, type(qr_data))

            # Call QRMATCH() when QR is found
            QRMATCH(qr_data)

            # Draw rectangle
            x, y, w, h = obj.rect.left, obj.rect.top, obj.rect.width, obj.rect.height
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Show QR data on image
            cv2.putText(frame, qr_data, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

        cv2.imshow("QR Code Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

main()

