# AI-Powered Mood Journal

**Project Type:** Web Application  
**Tech Stack:** Python, Flask, MySQL, HTML/CSS/JS, Chart.js  

---

## **Overview**
The AI-Powered Mood Journal is a web app that allows users to record daily journal entries and get instant mood analysis using AI. The app visualizes mood trends over time with interactive charts.

---

## **Features**
- Submit daily journal entries.  
- AI-powered sentiment analysis (Hugging Face API).  
- “Dummy Mode” for demo purposes (random mood generation).  
- Visualize mood trends with line charts colored by mood.  
- Responsive and simple UI for easy use.

---

## **Getting Started**

### Install dependencies:
```bash
pip install -r requirements.txt

### Set environment variables:
export DB_HOST=your_mysql_host
export DB_USER=your_mysql_user
export DB_PASSWORD=your_mysql_password
export DB_NAME=your_database_name
export HF_API_TOKEN=your_huggingface_token

## Run the app locally:
python app.py

## Open your browser at:
http://localhost:5000

Project Structure
mood-journal/
├─ app.py                # Flask backend
├─ requirements.txt      # Python dependencies
├─ templates/
│   └─ index.html        # Frontend HTML
├─ static/
│   └─ script.js         # JS for charts

Demo

Users can check the "Use Dummy Mode" checkbox to see AI results without making real API calls.

Mood trends are displayed as a color-coded line chart (green = positive, red = negative).

Team

Developed by: Juliet Asiedu

License

MIT License