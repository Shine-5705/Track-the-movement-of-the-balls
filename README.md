 <h1>Ball Tracking using Computer Vision</h1>
    <h2>Overview</h2>
    <p>This project is designed to track the movement of balls of different colors across various quadrants in a video. The program records events where each ball enters or exits a numbered quadrant. The event data is logged with timestamps and saved to a text file. The processed video will have overlays showing the ball's color and the type of event (entry or exit) along with the timestamp.</p>
    
<h2>Task Description</h2>
    <ul>
        <li><strong>Track balls of different colors</strong>: Dark Green, Yellow, White, and Red.</li>
        <li><strong>Record events</strong>: For each ball entering or exiting each numbered quadrant.</li>
        <li><strong>Log format</strong>:</li>
        <pre>
Time, Quadrant Number, Ball Colour, Type (Entry or Exit)
        </pre>
        <li><strong>Timestamp</strong>: Starts from 0 seconds at the beginning of the video and is computed based on the video duration.</li>
        <li><strong>Input</strong>: A video file provided by the user.</li>
        <li><strong>Output</strong>:</li>
        <ul>
            <li>Processed video with tracking and overlay text.</li>
            <li>Text file with event records.</li>
        </ul>
    </ul>
    
 <h2>Video to Process</h2>
    <p>The video for processing can be downloaded from <a href="https://drive.google.com/file/d/1goI3aHVE29Gko9lpTzgi_g3CZZPjJq8w/view?usp=sharing">this link</a>.</p>
    
  <h2>Output</h2>
    <h3>Processed Video</h3>
    <p>The processed video will incorporate:</p>
    <ul>
        <li>Ball tracking with color.</li>
        <li>Overlay text showing "Entry" or "Exit" and the timestamp at the time of entering or exiting a numbered quadrant.</li>
    </ul>
    
   <h3>Text File</h3>
    <p>The text file will contain records in the format:</p>
    <pre>
Time, Quadrant Number, Ball Colour, Type (Entry or Exit)
    </pre>
    
  <h2>Getting Started</h2>
    <h3>Prerequisites</h3>
    <ul>
        <li>Python 3.7+</li>
        <li>OpenCV</li>
        <li>NumPy</li>
    </ul>
    
  <h3>Installation</h3>
    <ol>
        <li>Clone the repository:
            <pre>
git clone https://github.com/Shine-5705/Track-the-movement-of-the-balls.git
cd Track-the-movement-of-the-balls
            </pre>
        </li>
        <li>Create a virtual environment:
            <pre>
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
            </pre>
        </li>
        <li>Install dependencies:
            <pre>
pip install -r requirements.txt
            </pre>
        </li>
    </ol>
    
   <h3>Running the Code</h3>
    <ol>
        <li>Place your input video in the <code>input</code> directory.</li>
        <li>Update the paths in the <code>main.py</code> script:
            <pre>
video_path = './input/video.mp4'  # Path to your input video
output_path = './output/processed_video.mp4'  # Path to save the processed video
event_log_path = './output/event_log.csv'  # Path to save the event log CSV file
            </pre>
        </li>
        <li>Run the script:
            <pre>
python main.py
            </pre>
        </li>
        <li>The processed video and event log will be saved in the <code>output</code> directory.</li>
    </ol>
    
   <h2>Code Explanation</h2>
    <h3>Main Script (<code>main.py</code>)</h3>
    <p>The script performs the following tasks:</p>
    <ul>
        <li>Detects balls of specific colors in each frame using HSV color space.</li>
        <li>Tracks the movement of these balls and identifies the quadrant each ball is in.</li>
        <li>Records entry and exit events along with timestamps.</li>
        <li>Overlays text on the video for visual confirmation of events.</li>
        <li>Saves the processed video and event log.</li>
    </ul>
    
  <h3>Quadrant Detection</h3>
    <p>Quadrants are determined based on the position of the ball's center:</p>
    <ul>
      <li>Quadrant 1: Top-left</li>
        <li>Quadrant 2: Top-right</li>
        <li>Quadrant 3: Bottom-left</li>
        <li>Quadrant 4: Bottom-right</li>
    </ul>
    
  <h3>Event Logging</h3>
    <p>Events are logged when a ball enters or exits a quadrant, recording the time, quadrant number, ball color, and event type.</p>
    
   <h2>Issues and Contributions</h2>
    <p> Contributions to improve the project are welcome. Feel free to fork the repository and create pull requests.</p>
    
    
</body>
</html>
