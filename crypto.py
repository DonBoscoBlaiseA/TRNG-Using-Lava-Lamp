import cv2 as cv
import hashlib as hash

def process_frame(frame):
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    hash_obj = hash.sha256(gray_frame.tobytes())
    hexadecimal = hash_obj.hexdigest()
    return hexadecimal

capture = cv.VideoCapture('lava_lamp.mp4')
move_unit = 0
move_unit_end = move_unit+16
index=0
while True:
    index+=1
    isRead,frame = capture.read()
    if isRead != True:
        print("END OF FOOTAGE")
        capture.release()
        cv.destroyAllWindows
        break
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("Gray Scale Lamp", gray_frame)
    hexadecimal = process_frame(frame)
    frame_2 = cv.putText(frame, "Code: "+str(hexadecimal[move_unit:move_unit_end]), (85, 348), cv.FONT_HERSHEY_PLAIN, 1.5, (255, 255, 255), 2)
    cv.imshow("Lava Lamp", frame_2)
    if(move_unit_end==64):
       move_unit_end=16
       move_unit=0
    move_unit+=1
    move_unit_end+=1
    print(f"Frame {index}: Key: {hexadecimal}")
    if cv.waitKey(60) & 0xFF == ord('s'):
        break
