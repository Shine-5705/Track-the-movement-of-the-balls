import cv2
import numpy as np
import csv
import time
from functools import reduce  # Import reduce from functools

# Define the function to detect balls based on color
def detect_balls(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    masks = {
        'red': cv2.inRange(hsv, (0, 120, 70), (10, 255, 255)) + cv2.inRange(hsv, (170, 120, 70), (180, 255, 255)),
        'yellow': cv2.inRange(hsv, (20, 100, 100), (30, 255, 255)),
        'dark_green': cv2.inRange(hsv, (60, 50, 50), (90, 255, 255)),
        'white': cv2.inRange(hsv, (0, 0, 200), (180, 20, 255))
    }
    
    balls = []
    for color, mask in masks.items():
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 500:  # Adjust the threshold based on ball size
                x, y, w, h = cv2.boundingRect(cnt)
                balls.append((x, y, w, h, color))
    return balls, masks

# Define the function to check quadrant entry/exit
def check_quadrant(x, y, width, height):
    if x < width / 2 and y < height / 2:
        return 1
    elif x >= width / 2 and y < height / 2:
        return 2
    elif x < width / 2 and y >= height / 2:
        return 3
    elif x >= width / 2 and y >= height / 2:
        return 4
    return None

# Utility function to visualize masks
def visualize_masks(frame, masks):
    combined_mask = reduce(cv2.bitwise_or, list(masks.values()))  # Use reduce correctly
    result = cv2.bitwise_and(frame, frame, mask=combined_mask)
    return result

# Process the video
def process_video(video_path, output_path, event_log_path):
    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))
    
    # Initialize tracking data structures
    last_positions = {}
    
    start_time = time.time()
    
    with open(event_log_path, 'w', newline='') as csvfile:
        fieldnames = ['Time', 'Quadrant Number', 'Ball Colour', 'Type']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            balls, masks = detect_balls(frame)
            current_time = time.time() - start_time
            for (x, y, w, h, color) in balls:
                cx, cy = x + w // 2, y + h // 2
                current_quadrant = check_quadrant(cx, cy, width, height)
                
                if color not in last_positions:
                    last_positions[color] = current_quadrant
                elif last_positions[color] != current_quadrant:
                    event_type = 'Exit' if last_positions[color] is not None else 'Entry'
                    writer.writerow({'Time': current_time, 'Quadrant Number': last_positions[color], 'Ball Colour': color, 'Type': event_type})
                    last_positions[color] = current_quadrant
                    
                    # Overlay text on video
                    overlay_text = f"{event_type} at Quadrant {last_positions[color]} - Time: {current_time:.2f}s"
                    cv2.putText(frame, overlay_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
                
                # Draw the ball and quadrant on the frame
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, color, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
            
            masked_frame = visualize_masks(frame, masks)
            combined_frame = cv2.addWeighted(frame, 0.6, masked_frame, 0.4, 0)
            
            # Overlay quadrant numbers on the frame
            cv2.putText(combined_frame, '1', (width // 4, height // 4), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(combined_frame, '2', (3 * width // 4, height // 4), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(combined_frame, '3', (width // 4, 3 * height // 4), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(combined_frame, '4', (3 * width // 4, 3 * height // 4), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            
            out.write(combined_frame)
            cv2.imshow('frame', combined_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    
    cap.release()
    out.release()
    cv2.destroyAllWindows()


# Example usage
video_path = 'AI Assignment video.mp4'  # Path to your input video
output_path = './output/processed_video.mp4'  # Path to save the processed video
event_log_path = 'ouput/event_log.csv'  # Path to save the event log CSV file
process_video(video_path, output_path, event_log_path)
