# roadmaps.py

# roadmaps.py

from textwrap import dedent

from textwrap import dedent

from textwrap import dedent
from youtube_fetcher import fetch_youtube_courses


from youtube_fetcher import fetch_youtube_courses
from textwrap import dedent

from textwrap import dedent
import html
from youtube_fetcher import fetch_youtube_courses


import html

import re
import requests
import os

from textwrap import dedent
from youtube_fetcher import fetch_youtube_courses


import html
import re

def extract_video_id(youtube_url):
    if not youtube_url:
        return None
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", youtube_url)
    return match.group(1) if match else None

def is_youtube_video_available(video_id):
    import requests
    import os
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv("YOUTUBE_API_KEY")

    url = f"https://www.googleapis.com/youtube/v3/videos?part=status&id={video_id}&key={api_key}"
    try:
        response = requests.get(url)
        data = response.json()
        return bool(data["items"]) and data["items"][0]["status"]["privacyStatus"] == "public"
    except Exception as e:
        print("[YouTube API Error]", e)
        return False

def get_roadmap_html(career):
    steps = career_roadmaps.get(career, [])
    
    if not steps:
        return f"<div class='empty-roadmap'>No roadmap found for <b>{career}</b>.</div>"

    parts = [
        "<div class='road-container'>",
        f"<h3 class='career-title'>🚀 {career} Roadmap</h3>",
        "<div class='road'>"
    ]

    for i, item in enumerate(steps, 1):
        step_text_raw = item.get("step", "Step description unavailable.")
        step_text = html.escape(step_text_raw)
        video_link = None

        # Try dynamic fetch first
        try:
            results = fetch_youtube_courses(step_text_raw, max_results=1)
            if results:
                video_link = results[0]['url']
            else:
                video_link = item.get("video_link")
        except Exception as e:
            print(f"[YouTube Fetch Error] {e}")
            video_link = item.get("video_link")

        video_html = f'<br>▶️ <a href="{video_link}" target="_blank" rel="noopener noreferrer">Watch Tutorial</a>' if video_link else ''
        
        parts.extend([
            "<div class='checkpoint'>",
            f"<div class='flag'>{i}</div>",
            f"<div class='step'>{step_text}{video_html}</div>",
            "</div>"
        ])

    parts.extend(["</div>", "</div>"])  # Close .road and .road-container
    return "\n".join(parts)



roadmap_css = dedent("""
<style>
.road-container {
    background: #f9f9fc;
    border-left: 6px solid #4a90e2;
    padding: 1rem;
    border-radius: 10px;
    margin-bottom: 2rem;
}
.career-title {
    color: #333;
    margin-bottom: 1rem;
    font-weight: bold;
    font-family: 'Segoe UI', sans-serif;
}
.road {
    position: relative;
    padding-left: 2rem;
    border-left: 3px dashed #4a90e2;
    margin-left: 1rem;
}
.checkpoint {
    display: flex;
    align-items: center;
    margin-bottom: 1rem;
}
.flag {
    background: #4a90e2;
    color: white;
    border-radius: 50%;
    width: 30px;
    height: 30px;
    text-align: center;
    line-height: 30px;
    font-weight: bold;
    margin-right: 1rem;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}
.step {
    font-size: 1rem;
    font-family: 'Segoe UI', sans-serif;
}
.empty-roadmap {
    background: #e6f0ff;
    color: #333;
    padding: 0.8rem;
    border-radius: 8px;up
    margin-bottom: 1rem;
}
</style>
""")

career_roadmaps = {
    "Data Scientist": [
        {"step": "Learn Python programming", "video_link": "https://www.youtube.com/watch?v=rfscVS0vtbw"},
        {"step": "Study statistics and linear algebra", "video_link": "https://www.youtube.com/watch?v=xxpc-HPKN28"},
        {"step": "Get hands-on with Pandas and NumPy", "video_link": "https://www.youtube.com/watch?v=vmEHCJofslg"},
        {"step": "Explore data visualization (Matplotlib, Seaborn)", "video_link": "https://www.youtube.com/watch?v=0P7QnIQDBJY"},
        {"step": "Take a beginner course in Machine Learning (e.g., Andrew Ng's Coursera)", "video_link": "https://www.coursera.org/learn/machine-learning"},
        {"step": "Practice on Kaggle datasets", "video_link": "https://www.kaggle.com/learn"},
        {"step": "Build personal projects (e.g., prediction, classification, clustering)"}
    ],

    "AI/ML Engineer": [
        {"step": "Master Python and mathematics for ML", "video_link": "https://www.youtube.com/watch?v=7eh4d6sabA0"},
        {"step": "Understand machine learning fundamentals", "video_link": "https://www.youtube.com/watch?v=Gv9_4yMHFhI"},
        {"step": "Learn deep learning using TensorFlow or PyTorch", "video_link": "https://www.youtube.com/watch?v=aircAruvnKk"},
        {"step": "Explore computer vision and NLP basics", "video_link": "https://www.youtube.com/watch?v=5L3Ao5KuCC0"},
        {"step": "Contribute to open-source ML projects"},
        {"step": "Build end-to-end AI applications"},
        {"step": "Read research papers (arXiv) & stay updated", "video_link": "https://www.youtube.com/watch?v=Zq06kzGm5SU"}
    ],

    "UI/UX Designer": [
        {"step": "Understand design principles and color theory", "video_link": "https://www.youtube.com/watch?v=3eZFPq1dH-Y"},
        {"step": "Learn tools like Figma, Sketch, Adobe XD", "video_link": "https://www.youtube.com/watch?v=FTFaQWZBqQ8"},
        {"step": "Study user psychology and behavior"},
        {"step": "Practice with wireframing and prototyping", "video_link": "https://www.youtube.com/watch?v=SjShw7IJT1o"},
        {"step": "Build UI projects and get peer feedback"},
        {"step": "Explore UX research techniques"},
        {"step": "Create and publish a design portfolio", "video_link": "https://www.youtube.com/watch?v=WGiDEyzjOY8"}
    ],

    "Doctor": [
        {"step": "Focus on Biology, Chemistry, and Physics in school"},
        {"step": "Prepare for NEET or medical entrance exams", "video_link": "https://www.youtube.com/watch?v=cKxRvEZd3Mw"},
        {"step": "Gain admission to a reputed medical college"},
        {"step": "Complete MBBS and practical training"},
        {"step": "Choose a specialization via PG or MD"},
        {"step": "Undertake hospital internships and residencies"},
        {"step": "Stay updated with latest medical research"}
    ],

    "Engineer": [
        {"step": "Focus on PCM (Physics, Chemistry, Math) subjects"},
        {"step": "Crack JEE or state-level engineering entrance", "video_link": "https://youtu.be/EPERdm_ZUrc?feature=shared"},
        {"step": "Pursue B.Tech or B.E. in your interest area"},
        {"step": "Work on hardware/software projects", "video_link": "https://youtu.be/D1Rs4GlhahQ?feature=shared"},
        {"step": "Intern at tech or core industry companies"},
        {"step": "Participate in hackathons and tech fests"},
        {"step": "Explore MS/MTech or certifications if needed"}
    ],

    "Content Creator": [
        {"step": "Pick a niche (tech, education, lifestyle, etc.)"},
        {"step": "Learn video editing, scripting, and basic design", "video_link": "https://www.youtube.com/watch?v=8szQ_U5gqtw"},
        {"step": "Start a YouTube/Instagram/TikTok channel", "video_link": "https://www.youtube.com/watch?v=V74l_zS1x8E"},
        {"step": "Be consistent with uploading content"},
        {"step": "Engage with your audience"},
        {"step": "Explore monetization options", "video_link": "https://www.youtube.com/watch?v=xPIz3vjeH0w"},
        {"step": "Collaborate with other creators"}
    ],

    "Entrepreneur": [
        {"step": "Learn basics of business, finance, and marketing", "video_link": "https://www.youtube.com/watch?v=9aXYj0GkAbU"},
        {"step": "Identify a real-world problem"},
        {"step": "Brainstorm scalable solutions"},
        {"step": "Create MVP (Minimum Viable Product)", "video_link": "https://www.youtube.com/watch?v=LKjNMGD1Ha4"},
        {"step": "Learn pitching and build a startup team"},
        {"step": "Raise initial funding or bootstrap"},
        {"step": "Join incubators, accelerators, and get mentorship"}
    ],

    "Game Developer": [
        {"step": "Learn C++/Python/Java and game logic", "video_link": "https://www.youtube.com/watch?v=3r1EvcXp0O8"},
        {"step": "Understand game engines like Unity or Unreal", "video_link": "https://www.youtube.com/watch?v=GZ4d3HEn9zg"},
        {"step": "Study game physics, rendering, and design"},
        {"step": "Take short courses on game development", "video_link": "https://www.udemy.com/course/unitycourse/"},
        {"step": "Build mini-games as projects"},
        {"step": "Contribute to indie game communities"},
        {"step": "Publish games on platforms (Steam, Play Store)"}
    ],

    "Psychologist": [
        {"step": "Study Psychology in high school if available"},
        {"step": "Pursue a B.A./B.Sc. in Psychology", "video_link": "https://www.youtube.com/watch?v=ddnKoLKotrw"},
        {"step": "Complete internships in clinics or NGOs"},
        {"step": "Specialize in clinical/counseling/organizational psychology"},
        {"step": "Earn an M.A./M.Sc. and optionally Ph.D.", "video_link": "https://www.youtube.com/watch?v=wnlRbpxpZ9k"},
        {"step": "Get certified and licensed as per regulations"},
        {"step": "Open practice or join healthcare orgs"}
    ],

    "Product Manager": [
        {"step": "Understand software & tech basics"},
        {"step": "Learn market research and user personas"},
        {"step": "Explore Agile & Scrum methodologies", "video_link": "https://www.youtube.com/watch?v=Z9QbYZh1YXY"},
        {"step": "Build mock product specs"},
        {"step": "Take PM courses (Coursera, Udemy)", "video_link": "https://www.coursera.org/learn/uva-darden-digital-product-management"},
        {"step": "Intern or shadow experienced PMs"},
        {"step": "Work on product-focused projects"}
    ],

    "Digital Marketer": [
        {"step": "Understand marketing fundamentals", "video_link": "https://www.youtube.com/watch?v=n8m_NnBEg0E"},
        {"step": "Learn SEO, SEM, and social media tactics"},
        {"step": "Master tools like Google Ads, Meta Business Suite"},
        {"step": "Run small ad campaigns and track metrics"},
        {"step": "Get certified (Google, HubSpot, Meta)", "video_link": "https://skillshop.exceedlms.com/student/catalog/list?category_ids=53-google-ads"},
        {"step": "Create and manage brand accounts"},
        {"step": "Build a marketing portfolio"}
    ],

    "Bioinformatician": [
        {"step": "Learn biology and computer science basics"},
        {"step": "Pursue B.Sc./M.Sc. in Bioinformatics"},
        {"step": "Study statistics, genetics, and genomics", "video_link": "https://www.youtube.com/watch?v=vyGFMzXHOiY"},
        {"step": "Learn tools like BLAST, Bioconductor, Python"},
        {"step": "Analyze biological datasets"},
        {"step": "Intern in biotech or research labs"},
        {"step": "Stay updated with biotech advances"}
    ],

    "Health Tech Innovator": [
        {"step": "Explore intersection of biology and technology"},
        {"step": "Understand healthcare challenges"},
        {"step": "Prototype wearable or tech-based health solutions"},
        {"step": "Learn app/web development", "video_link": "https://www.youtube.com/watch?v=3P2FFzUb5ck"},
        {"step": "Collaborate with clinicians"},
        {"step": "Join healthcare hackathons"},
        {"step": "Pitch your idea to investors or mentors"}
    ],

    "Mechatronics Engineer": [
        {"step": "Understand basics of mechanical + electrical systems", "video_link": "https://www.youtube.com/watch?v=Ac2GpG7RbmY"},
        {"step": "Learn robotics, control systems, and PLCs", "video_link": "https://www.youtube.com/watch?v=ad79nYk2keg"},
        {"step": "Work on automation and embedded projects", "video_link": "https://www.youtube.com/watch?v=CbXB0bM5Uyo"},
        {"step": "Use tools like Arduino, Raspberry Pi", "video_link": "https://www.youtube.com/watch?v=nL34zDTPkcs"},
        {"step": "Participate in robotics contests"},
        {"step": "Intern at industrial automation firms"},
        {"step": "Specialize in robotics, AI, or IoT", "video_link": "https://www.youtube.com/watch?v=i1F71BvPBOY"}
    ],

    "Legal Consultant": [
        {"step": "Prepare for CLAT or equivalent law exams", "video_link": "https://www.youtube.com/watch?v=4syAvI4Jldw"},
        {"step": "Pursue B.A. LLB or 5-year law degree"},
        {"step": "Intern with law firms or NGOs"},
        {"step": "Understand tech, contract, IP, and data privacy laws"},
        {"step": "Take moot court and client counseling seriously"},
        {"step": "Get licensed as an advocate"},
        {"step": "Join tech firms or consultancy"}
    ],

    "Environmental Scientist": [
        {"step": "Study biology, chemistry, and environment in school"},
        {"step": "Pursue B.Sc. or M.Sc. in Environmental Science"},
        {"step": "Learn GIS, remote sensing, EIA basics", "video_link": "https://www.youtube.com/watch?v=tgN1GkM6Jtg"},
        {"step": "Volunteer in sustainability orgs"},
        {"step": "Work on water/air/soil quality projects"},
        {"step": "Publish papers and research"},
        {"step": "Apply for fellowships, NGOs, or government roles"}
    ],

    "Space Scientist": [
        {"step": "Study Physics, Math, and Chemistry seriously"},
        {"step": "Prepare for ISRO/JEST/IISc entrance exams", "video_link": "https://www.youtube.com/watch?v=3t7tMHDfWkI"},
        {"step": "Pursue B.Sc./B.Tech in Physics/Aerospace"},
        {"step": "Intern at labs like IUCAA, PRL, DRDO"},
        {"step": "Learn simulation tools and coding"},
        {"step": "Publish or assist in research papers"},
        {"step": "Apply to ISRO, NASA, or academia"}
    ]
}

fallback_videos = {}

for steps in career_roadmaps.values():
    for item in steps:
        step = item.get("step")
        link = item.get("video_link")
        if step and link:
            fallback_videos[step] = link


def get_roadmap_for_career(career):
    return career_roadmaps.get(career, ["Roadmap coming soon for this career."])
# At the bottom of roadmaps.py
__all__ = ["roadmap_css", "get_roadmap_html", "get_roadmap_for_career", "career_roadmaps"]

