# Life-OS Wellbeing Dashboard

Life-OS is a Streamlit-based digital wellbeing dashboard that analyzes daily screen-time data. It uses Google Gemini as a personalized, brutally honest but fair productivity and lifestyle coach, helping users understand their digital habits and identify practical offline alternatives.

## Features

- 14+ days of synthetic screen-time data stored in `screentime.csv`
- Date selection and adjustable daily screen-time goal through the sidebar
- KPI cards built with `st.columns` and `st.metric`
- Total daily screen time and most-used app
- Goal comparison with a delta
- 14-day screen-time trend visualization
- Category and app usage charts
- Gemini-powered personalized coaching
- Pandas-to-Gemini data aggregation bridge
- Real-world lifestyle recommendations based on usage patterns
- Guilt-Trip Avatar generated with Pollinations AI
- Graceful Gemini and avatar API error handling

## Tech Stack

| Technology | Purpose |
| --- | --- |
| Python | Application development |
| Streamlit | Dashboard interface |
| Pandas | Data loading and aggregation |
| Google Gemini API (`google-genai`) | Personalized coaching |
| Pollinations AI | AI-generated wellbeing avatar |
| Requests | Image API requests |
| python-dotenv | Local environment variable loading |

## Project Structure

```text
assignment7/
├── app.py
├── screentime.csv
├── requirements.txt
└── README.md
```

`screentime.csv` contains synthetic data created for this project.

## How It Works

1. The app loads `screentime.csv`.
2. The user selects a date and daily screen-time goal.
3. Pandas aggregates app and category usage.
4. KPIs and charts visualize the selected day's data and the 14-day trend.
5. The summarized data is sent to Gemini.
6. Gemini provides personalized productivity and lifestyle recommendations.
7. Pollinations generates a visual avatar based on the user's screen-time state.

## Setup

```bash
pip install -r requirements.txt
streamlit run app.py
```

A Gemini API key must be stored locally in `.env` and must never be committed to GitHub:

```env
GEMINI_API_KEY=your_api_key_here
```

## Deployment

The application can be deployed using [Streamlit Community Cloud](https://streamlit.io/cloud). Since this project is inside the `mirai-intern` repository, set the main file path to:

`assignment7/app.py`

Live Demo: https://mirai-internship-yfx7yr3dgjgk9ja9b25kt4.streamlit.app/

## Internship Context

This project was completed as part of the MirAI School of Technology Virtual Summer Internship 2026, AI Builder Track.

## Learning Outcomes

This project demonstrates:

- Streamlit dashboard design
- Pandas data processing
- Data visualization
- API integration
- Prompt engineering
- Gemini integration
- AI-generated visual content
- Error handling
- Environment variable management
- Deployment

## Thanks

Thank you to MirAI School of Technology for the opportunity to build this project.
