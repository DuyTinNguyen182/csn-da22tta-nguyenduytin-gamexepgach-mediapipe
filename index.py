import cv2
import mediapipe as mp
import time
import pyautogui # Thư viện điều khiển chuột
from websocket_server import WebsocketServer

###
import base64
import json
###

# Khởi tạo MediaPipe Hand
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

server = WebsocketServer(host='127.0.0.1', port=12345)
def send_frame_to_web(frame):
    _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 95])
    frame_data = base64.b64encode(buffer).decode('utf-8')
    message = json.dumps({"type": "frame", "data": frame_data})
    server.send_message_to_all(message)

def detect_gesture(fingers):
    # Xác định cử chỉ dựa trên trạng thái ngón tay
    if fingers == [1, 1, 1, 1, 1]:
        return "UP"
    # elif fingers == [0, 1, 1, 0, 0]:
    #     return "DOWN"
    elif fingers == [1, 0, 0, 0, 0]:
        return "LEFT"
    elif fingers == [0, 0, 0, 0, 1]:
        return "RIGHT"
    return None

def send_command_to_game(command):
    print(f"Sending command to game: {command}")
    message = json.dumps({"type": "command", "data": command})
    server.send_message_to_all(message)

# Hàm xử lý khi WebSocket có kết nối
def on_new_client(client, server):
    print(f"New client connected: {client}")

server.set_fn_new_client(on_new_client)
server.run_forever(threaded=True)

pTime = 0
cap = cv2.VideoCapture(0)
finger_id = [4, 8, 12, 16, 20]
# Lấy kích thước màn hình
screen_width, screen_height = pyautogui.size()

click_state = False # Lưu trạng thái click chuột
last_click_time = 0
move_time = 0 # Thời gian khối gạch di chuyển lần cuối
move_down_time = 0

prev_x, prev_y = None, None

# Hệ số điều chỉnh tốc độ chuột
SPEED_FACTOR = 3  # Tăng để chuột di chuyển nhanh hơn


while True:
    success, frame = cap.read() # success trả về True nếu có webcam. 
    frame = cv2.flip(frame, 1)

    # Chuyển đổi ảnh thành RGB
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb) # chứa tất cả dữ liệu liên quan đến kết quả xử lý hình ảnh
    
    # Hiển thị FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime 
    cv2.putText(frame, f'FPS: {int(fps)}', (10, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (5, 5, 235), 2)

    if(results.multi_hand_landmarks):
        num_hands = len(results.multi_hand_landmarks)
        if(num_hands > 1):
            cv2.putText(frame, 'Chi su dung 1 ban tay!!!!', (30, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
            # send_frame_to_web(frame)
        else:
            for hand_index, hand_landmarks in enumerate(results.multi_hand_landmarks):
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                hand_label = results.multi_handedness[hand_index].classification[0].label # Bàn tay trái hoặc phải
                fingers = [0, 0, 0, 0, 0]
                
                if(hand_label == 'Right'):
                    #Xử lí cho ngón cái - khối gạch qua trái
                    if(hand_landmarks.landmark[finger_id[0]].x < (hand_landmarks.landmark[finger_id[0] - 2].x - 0.03)):
                        fingers[0]=1

                    #Xử lí cho ngón út - khối gạch qua phải
                    if(hand_landmarks.landmark[finger_id[4]].y < hand_landmarks.landmark[finger_id[4] - 2].y):
                        fingers[4]=1

                else: #Bàn tay trái
                    #Xử lí cho ngón cái - khối gạch qua phải
                    if(hand_landmarks.landmark[finger_id[0]].x > (hand_landmarks.landmark[finger_id[0] - 2].x + 0.03)):
                        fingers[4]=1

                    #Xử lí cho ngón út - khối gạch qua trái
                    if(hand_landmarks.landmark[finger_id[4]].y < hand_landmarks.landmark[finger_id[4] - 2].y):
                        fingers[0]=1

                for i in range(1, 4):
                    if(hand_landmarks.landmark[finger_id[i]].y < hand_landmarks.landmark[finger_id[i] - 2].y):
                        fingers[i]=1
                # print(fingers)
                gesture = detect_gesture(fingers)
                if gesture and (cTime-move_time) > 0.4:
                    print(f"Detected gesture: {gesture}")
                    send_command_to_game(gesture)
                    move_time=cTime
            
            #Điều khiển chuột
            h, w, z = frame.shape
            # Lấy tọa độ ngón trỏ (landmark số 8)
            x1 = hand_landmarks.landmark[8].x * w
            y1 = hand_landmarks.landmark[8].y * h

            # Nếu là khung hình đầu tiên
            if prev_x is None or prev_y is None:
                prev_x, prev_y = x1, y1
           
            delta_x = (x1 - prev_x) * SPEED_FACTOR
            delta_y = (y1 - prev_y) * SPEED_FACTOR
                        
            # Di chuyển chuột từ vị trí hiện tại
            if fingers[1] == 1:
                if sum(fingers) == 1:
                    # Lấy vị trí hiện tại của chuột
                    current_x, current_y = pyautogui.position()
                    
                    # Tính vị trí mới dựa trên delta
                    new_x = current_x + delta_x
                    new_y = current_y + delta_y
                    
                    # Giới hạn vị trí trong phạm vi màn hình
                    new_x = max(5, min(screen_width - 5, new_x))
                    new_y = max(5, min(screen_height - 5, new_y))

                    # Di chuyển chuột tới vị trí mới
                    pyautogui.moveTo(new_x, new_y)

                elif fingers[0] == 1 and sum(fingers) == 2:
                    if not click_state and (cTime - last_click_time) > 2:
                        pyautogui.click()
                        click_state = True
                        last_click_time = cTime
                    else:
                        click_state = False
            # Cập nhật tọa độ ngón trỏ cho khung hình tiếp theo
            prev_x, prev_y = x1, y1
    else:
        if(cTime - move_down_time)>0.3:
            print(f"Detected gesture: DOWN")
            send_command_to_game("DOWN")
            move_down_time = cTime
    send_frame_to_web(frame)
                                           
    # Hiển thị ảnh
    cv2.imshow("Hand Tracking", frame)
    
    # Nhấn phím 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'): #Chờ 1 mili giây để hiển thị khung hình và xử lí sự kiện như nhấn phím. Toán tử & để lấy 8 bit thấp nhất giá trị trả về từ cv2.waitkey()
        break

# Giải phóng bộ nhớ
cap.release()
cv2.destroyAllWindows()
