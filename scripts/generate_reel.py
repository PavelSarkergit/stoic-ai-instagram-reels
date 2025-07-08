import random
from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont
import os

QUOTES = [
    "He who fears death will never do anything worthy of a man who is alive. – Seneca",
    "We suffer more in imagination than in reality. – Seneca",
    # Add more quotes...
]

def get_random_quote():
    return random.choice(QUOTES)

def create_image(quote, output_path):
    img = Image.new('RGB', (1080, 1920), color=(73, 109, 137))
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    d.text((100,900), quote, fill=(255,255,255), font=font)
    img.save(output_path)

def combine_video(image_path, music_path, output_path):
    image_clip = ImageClip(image_path).set_duration(10)
    music_clip = AudioFileClip(music_path).subclip(0,10)
    video = image_clip.set_audio(music_clip)
    video.write_videofile(output_path, fps=24)

def main():
    if not os.path.exists("output"):
        os.makedirs("output")
    quote = get_random_quote()
    image_path = 'output/frame.png'
    music_path = 'data/music.mp3'  # Make sure to add your music file here
    output_video_path = 'output/stoic_reel.mp4'
    create_image(quote, image_path)
    combine_video(image_path, music_path, output_video_path)

if __name__ == "__main__":
    main()