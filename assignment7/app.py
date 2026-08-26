import streamlit as st
import pandas as pd
import os
import requests
from urllib.parse import quote
from dotenv import load_dotenv
from google import genai

load_dotenv()

st.set_page_config(
    page_title="Life-OS",
    layout="wide"
)

# -------------------------
# Gemini Client
# -------------------------

@st.cache_resource
def get_client():
    return genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
    )

client = get_client()

# -------------------------
# Load Data
# -------------------------

df = pd.read_csv("screentime.csv")
df["Date"] = pd.to_datetime(df["Date"])

# -------------------------
# Header
# -------------------------

st.title("Life-OS")
st.caption("Your personal digital wellbeing command center.")

# -------------------------
# Sidebar
# -------------------------

st.sidebar.header("Life-OS Controls")

dates = sorted(df["Date"].dt.strftime("%Y-%m-%d").unique(), reverse=True)

selected_date = st.sidebar.selectbox(
    "Select Day",
    dates
)

daily_goal = st.sidebar.slider(
    "Daily Screen-Time Goal",
    min_value=60,
    max_value=600,
    value=240,
    step=30,
    help="Maximum screen time allowed per day in minutes."
)

# -------------------------
# Selected Day Data
# -------------------------

day_df = df[
    df["Date"].dt.strftime("%Y-%m-%d") == selected_date
]

total_minutes = int(day_df["Minutes_Used"].sum())

app_usage = (
    day_df.groupby("App_Name")["Minutes_Used"]
    .sum()
    .sort_values(ascending=False)
)

category_usage = (
    day_df.groupby("Category")["Minutes_Used"]
    .sum()
    .sort_values(ascending=False)
)

most_used_app = app_usage.index[0]

goal_difference = total_minutes - daily_goal

hours = total_minutes // 60
minutes = total_minutes % 60

time_display = f"{hours}h {minutes}m"

# -------------------------
# KPI Row
# -------------------------

st.subheader("Today's Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Screen Time",
        time_display,
        delta=f"{goal_difference:+d} min vs goal",
        delta_color="inverse"
    )

with col2:
    st.metric(
        "Most Used App",
        most_used_app,
        f"{int(app_usage.iloc[0])} min"
    )

with col3:
    status = "Within Goal" if goal_difference <= 0 else "Over Goal"

    st.metric(
        "Daily Goal",
        f"{daily_goal} min",
        status
    )

# -------------------------
# Severity Message
# -------------------------

if total_minutes <= daily_goal:
    st.success("🟢 You're within your screen-time goal. Keep the balance.")
elif total_minutes <= daily_goal + 120:
    st.info("🟡 You're slightly over your goal. Time to reclaim some offline hours.")
elif total_minutes <= daily_goal + 240:
    st.warning("🟠 Your screen time is getting high. Your attention is being taxed.")
else:
    st.error("🔴 Brutal truth: your screen is consuming a serious part of your day.")

# -------------------------
# Charts
# -------------------------

st.subheader("Screen-Time Trend")

daily_usage = (
    df.groupby("Date")["Minutes_Used"]
    .sum()
    .sort_index()
)

st.line_chart(daily_usage)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Usage by Category")
    st.bar_chart(category_usage)

with col2:
    st.subheader("Usage by App")
    st.bar_chart(app_usage)

# -------------------------
# Data Bridge
# -------------------------

summary = category_usage.to_string()

app_summary = app_usage.to_string()

# -------------------------
# Gemini Coach
# -------------------------

st.subheader("Your AI Life Coach")

if st.button("Analyze My Day"):

    prompt = f"""
You are Life-OS, a brutally honest but fair productivity
and lifestyle coach.

Analyze this user's digital wellbeing data.

Date:
{selected_date}

Total screen time:
{total_minutes} minutes

Daily goal:
{daily_goal} minutes

Usage by category:
{summary}

Usage by application:
{app_summary}

Your job is NOT to simply tell the user to "use their phone less".

Identify:
1. Their biggest digital time drains.
2. Whether their usage is productive or distracting.
3. Specific unhealthy patterns.
4. Real-world replacements for wasted digital time.
5. A practical plan for tomorrow.
6. One challenging but achievable action.

Give physical, real-world alternatives such as:
walking, exercise, reading, meal preparation,
social interaction, hobbies, outdoor activities,
sleep improvement, or focused study.

Be brutally honest but constructive.

Keep the response under 300 words.
Use clear headings and bullet points.
"""

    with st.spinner("Your AI coach is analyzing your habits..."):

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            coaching = response.text

            st.markdown(coaching)

        except Exception as e:
            st.error("Gemini is currently unavailable.")
            st.caption(str(e))

# -------------------------
# Guilt-Trip Avatar
# -------------------------

st.subheader("Your Digital Wellbeing Avatar")

if total_minutes > daily_goal + 240:
    avatar_prompt = (
        "A tired exhausted zombie sitting in a dark room "
        "staring at a glowing smartphone, digital addiction, "
        "messy desk, cinematic lighting, dramatic realistic art"
    )

elif total_minutes > daily_goal:
    avatar_prompt = (
        "A distracted person surrounded by smartphone notifications "
        "trying to focus on a book, modern room, cinematic digital art"
    )

else:
    avatar_prompt = (
        "A focused disciplined young person reading a book "
        "after finishing productive computer work, sunlight, "
        "healthy lifestyle, peaceful room, cinematic inspirational art"
    )

if st.button("Generate My Life-OS Avatar"):

    with st.spinner("Creating your wellbeing avatar..."):

        try:
            encoded_prompt = quote(avatar_prompt)

            url = (
                f"https://image.pollinations.ai/prompt/"
                f"{encoded_prompt}"
                f"?width=768&height=512"
            )

            response = requests.get(url, timeout=30)

            if response.status_code == 200:
                st.image(
                    response.content,
                    caption="Your current digital wellbeing state"
                )
            else:
                st.toast(
                    "Image server is busy. Skipping avatar."
                )

        except Exception:
            st.toast(
                "Image server is unavailable. Skipping avatar."
            )

# -------------------------
# Footer
# -------------------------

st.divider()

st.caption(
    "Life-OS | Built with Streamlit • Pandas • Gemini • Pollinations AI"
)