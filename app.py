import streamlit as st
from pipeline import run_research_pipeline
from datetime import datetime
from fpdf import FPDF
import tempfile
import time

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Multi-Agent Research System",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM DARK STYLING ---------------- #

st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

.stTextInput > div > div > input {
    background-color: #1E1E1E;
    color: white;
}

.stTextArea textarea {
    background-color: #1E1E1E;
    color: white;
}

div[data-testid="stSidebar"] {
    background-color: #111827;
}

.stButton button {
    background-color: #2563EB;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-weight: bold;
}

.stDownloadButton button {
    background-color: #059669;
    color: white;
    border-radius: 10px;
}

.agent-box {
    padding: 15px;
    border-radius: 12px;
    background-color: #1F2937;
    margin-bottom: 10px;
}

.log-box {
    background-color: black;
    color: #00FFAA;
    padding: 10px;
    border-radius: 10px;
    height: 250px;
    overflow-y: auto;
    font-family: monospace;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("⚙️ Settings")

show_logs = st.sidebar.toggle("Show Agent Logs", value=True)
show_search = st.sidebar.toggle("Show Search Results", value=True)
show_scraped = st.sidebar.toggle("Show Scraped Content", value=True)

theme = st.sidebar.selectbox(
    "Theme",
    ["Dark", "Light"]
)

research_depth = st.sidebar.slider(
    "Research Depth",
    1,
    10,
    5
)

# ---------------- SESSION STATE ---------------- #

if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- TITLE ---------------- #

st.title("🤖 Multi-Agent Research Assistant")

st.markdown("""
Autonomous AI Research System using multiple agents:
- 🔎 Search Agent
- 📄 Reader Agent
- ✍️ Writer Agent
- 🧠 Critic Agent
""")

# ---------------- CHAT UI ---------------- #

user_topic = st.chat_input("Enter a research topic...")

# ---------------- PDF FUNCTION ---------------- #

def generate_pdf(report_text):

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    lines = report_text.split("\n")

    for line in lines:
        pdf.multi_cell(0, 10, line)

    temp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")

    pdf.output(temp_pdf.name)

    return temp_pdf.name

# ---------------- MAIN EXECUTION ---------------- #

if user_topic:

    # Save history
    st.session_state.history.append({
        "topic": user_topic,
        "time": datetime.now().strftime("%H:%M:%S")
    })

    # User message
    with st.chat_message("user"):
        st.markdown(user_topic)

    # Assistant message
    with st.chat_message("assistant"):

        st.markdown("## 🚀 Starting Research Pipeline")

        # ---------------- LIVE LOGS ---------------- #

        if show_logs:

            log_placeholder = st.empty()

            logs = []

            def update_logs(message):
                logs.append(message)

                log_placeholder.markdown(
                    f"""
                    <div class="log-box">
                    {'<br>'.join(logs)}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            update_logs("Initializing agents...")
            time.sleep(0.5)

            update_logs("🔎 Search Agent started...")
            time.sleep(1)

            update_logs("📄 Reader Agent started...")
            time.sleep(1)

            update_logs("✍️ Writer Agent started...")
            time.sleep(1)

            update_logs("🧠 Critic Agent started...")
            time.sleep(1)

        # ---------------- RUN PIPELINE ---------------- #

        try:

            result = run_research_pipeline(user_topic)

            # ---------------- SEARCH RESULTS ---------------- #

            if show_search:

                with st.expander("🔎 Search Results", expanded=False):

                    st.markdown(
                        f"""
                        <div class="agent-box">
                        {result['search_results']}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            # ---------------- SCRAPED CONTENT ---------------- #

            if show_scraped:

                with st.expander("📄 Scraped Content", expanded=False):

                    st.markdown(
                        f"""
                        <div class="agent-box">
                        {result['scraped_content']}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            # ---------------- FINAL REPORT ---------------- #

            st.markdown("## 📝 Final Research Report")

            st.markdown(
                f"""
                <div class="agent-box">
                {result['report']}
                </div>
                """,
                unsafe_allow_html=True
            )

            # ---------------- FEEDBACK ---------------- #

            st.markdown("## 🧠 Critic Feedback")

            st.markdown(
                f"""
                <div class="agent-box">
                {result['feedback']}
                </div>
                """,
                unsafe_allow_html=True
            )

            # ---------------- PDF DOWNLOAD ---------------- #

            pdf_path = generate_pdf(result['report'])

            with open(pdf_path, "rb") as pdf_file:

                st.download_button(
                    label="📥 Download Report as PDF",
                    data=pdf_file,
                    file_name=f"{user_topic}_report.pdf",
                    mime="application/pdf"
                )

            st.success("✅ Research Completed Successfully!")

        except Exception as e:

            st.error(f"❌ Error: {str(e)}")

# ---------------- SIDEBAR HISTORY ---------------- #

st.sidebar.markdown("---")
st.sidebar.subheader("🕘 Research History")

if len(st.session_state.history) == 0:
    st.sidebar.info("No research history yet.")
else:

    for item in reversed(st.session_state.history):

        st.sidebar.markdown(
            f"""
            **📌 {item['topic']}**  
            ⏰ {item['time']}
            """
        )