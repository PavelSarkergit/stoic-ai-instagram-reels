import schedule
import time
from datetime import datetime
# from instagrapi import Client  # Uncomment if using unofficial API

def upload_reel():
    # AI logic to select next video, or optimal posting time
    reel_path = "output/stoic_reel.mp4"
    caption = "Daily Stoic Wisdom 🌿\n#stoic #ai"

    # -- Official API (business accounts) pseudocode --
    # authenticate_with_graph_api()
    # post_video_via_graph_api(reel_path, caption)

    # -- Unofficial API (personal accounts) example --
    # client = Client()
    # client.login('username', 'password')
    # client.video_upload(reel_path, caption)
    print(f"Uploaded at {datetime.now()}")

# Schedule: every day at 10am and 6pm
schedule.every().day.at("10:00").do(upload_reel)
schedule.every().day.at("18:00").do(upload_reel)

while True:
    schedule.run_pending()
    time.sleep(60)