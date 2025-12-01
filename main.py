import os
import random
from gtts import gTTS
from moviepy.editor import *

# 25+ VIRAL TOPICS (Bible sayings + marriage tips)
VIRAL_TOPICS = [
    "productivity hacks", "morning routine", "study hacks", "time blocking",
    "health tips", "mental health", "sleep optimization", "vitamin D benefits",
    "money saving tips", "passive income ideas", "side hustles 2025", "budgeting hacks",
    "fitness motivation", "home workouts", "meal prep ideas", "weight loss journey",
    "tech tips 2025", "phone battery hacks", "gadget reviews", "AI productivity tools",
    "bible sayings", "tiktok algorithm", "content creation tips", "marriage tips",
    "motivational sayings", "success mindset", "discipline quotes", "millionaire morning",
    "crypto investing basics", "stock market for beginners", "real estate tips", "dropshipping 2025"
]

def generate_script(topic):
    scripts = {
        "productivity hacks": "Want 3X productivity? Hack 1: Time block 90-min focus. Hack 2: Single-task only. Hack 3: Weekly reviews. Start NOW!",
        "health tips": "Boost immunity! 2 garlic cloves daily. 8hr sleep. 10K steps. Morning sunlight!",
        "money saving tips": "Save $5K/year! Skip lattes. Bulk cook. Cancel subs. Track spending!",
        "fitness motivation": "30-day transformation! 100 pushups. 30min walks. 4L water!",
        "tech tips 2025": "Double phone battery! Kill background apps. 30% brightness. Charge to 80%!",
        "bible sayings": "Bible wisdom: 'Be strong and courageous' Joshua 1:9. 'Love your neighbor' Mark 12:31. 'Trust the Lord' Proverbs 3:5. Timeless truth!",
        "marriage tips": "Save your marriage! Never sleep angry. Compliment daily. Date night weekly. Say 'I love you' every morning!",
        "motivational sayings": "Your only limit is YOU. Wake up. Work hard. Repeat. Success is earned!",
        "side hustles 2025": "Earn $1K/mo side hustle! Print-on-demand. Affiliate links. Digital products. Start FREE!",
    }
    return scripts.get(topic, f"Master {topic} today! 🚀")

def create_short():
    topic = random.choice(VIRAL_TOPICS)
    print(f"🎥 Random topic: {topic}")
    
    script = generate_script(topic)
    
    # TTS Audio
    tts = gTTS(script, lang='en')
    tts.save('narration.mp3')
    
    # Vertical short (1080x1920)
    duration = 25
    video = ColorClip(size=(1080,1920), color=(20,40,80), duration=duration)
    
    # Text overlay
    txt = (TextClip(script, fontsize=55, color='white', font='Arial-Bold')
           .set_position('center').set_duration(duration))
    
    audio = AudioFileClip('narration.mp3').subclip(0, duration)
    final = CompositeVideoClip([video.set_audio(audio), txt])
    
    output = f"short_{random.randint(1000,9999)}.mp4"
    final.write_videofile(output, fps=24, audio_codec='aac', verbose=False, logger=None)
    
    # Cleanup
    final.close(); video.close(); audio.close(); txt.close()
    os.remove('narration.mp3')
    
    title = f"🔥 {topic.title()} (#shorts #viral)"
    return output, title

if __name__ == "__main__":
    print("🚀 YouTube Shorts Bot")
    video_file, title = create_short()
    print(f"✅ Created: {title}")
    print(f"📱 File: {video_file}")
