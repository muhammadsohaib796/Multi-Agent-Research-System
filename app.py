import streamlit as st

st.set_page_config(page_title="Test")

st.title("✅ Streamlit is Working")
st.write("If you can see this, deployment is successful.")


# import streamlit as st
# from pipeline import run_research_pipeline

# # ==========================================================
# # PAGE CONFIG
# # ==========================================================

# st.set_page_config(
#     page_title="TetraAgent Synthesizer",
#     page_icon="🧠",
#     layout="wide",
# )

# # ==========================================================
# # SESSION STATE
# # ==========================================================

# if "report" not in st.session_state:
#     st.session_state.report = ""

# if "feedback" not in st.session_state:
#     st.session_state.feedback = ""

# if "generated" not in st.session_state:
#     st.session_state.generated = False

# # ==========================================================
# # CUSTOM CSS
# # ==========================================================

# st.markdown("""
# <style>
# /* Hide Streamlit Menu & Header/Footer */
# #MainMenu { visibility: hidden; }
# header { visibility: hidden; }
# footer { visibility: hidden; }

# /* Background */
# .stApp {
#     background: linear-gradient(180deg, #07111F 0%, #10192D 100%);
# }

# /* Page Container Width */
# .block-container {
#     padding-top: 2rem;
#     padding-left: 8%;
#     padding-right: 8%;
# }

# /* Hero Typography */
# .hero-title {
#     font-size: 58px;
#     font-weight: 800;
#     color: white;
#     text-align: center;
#     margin-bottom: 8px;
# }

# .hero-highlight {
#     color: #4F9DFF;
# }

# .hero-subtitle {
#     text-align: center;
#     font-size: 22px;
#     color: #9FB3C8;
#     margin-bottom: 20px;
# }

# .hero-description {
#     max-width: 850px;
#     margin: auto;
#     text-align: center;
#     font-size: 16px;
#     line-height: 1.8;
#     color: #CBD5E1;
#     margin-bottom: 35px;
# }

# /* Input Styles */
# div[data-testid="stTextInput"] input {
#     background: #162233;
#     color: white;
#     border-radius: 12px;
#     border: 1px solid rgba(255, 255, 255, .08);
#     padding: 15px;
# }

# /* Button Styles */
# div[data-testid="stButton"] button {
#     width: 100%;
#     height: 52px;
#     border: none;
#     border-radius: 12px;
#     font-size: 17px;
#     font-weight: 700;
#     color: white;
#     background: linear-gradient(90deg, #2563EB, #3B82F6);
# }

# div[data-testid="stButton"] button:hover {
#     box-shadow: 0 0 20px rgba(37, 99, 235, .45);
# }

# /* Section Titles */
# .section-title {
#     font-size: 32px;
#     font-weight: 700;
#     color: white;
#     margin-top: 40px;
#     margin-bottom: 20px;
# }
# </style>
# """, unsafe_allow_html=True)

# # ==========================================================
# # HERO SECTION
# # ==========================================================

# st.markdown("""
# <div class="hero-title">
#     🧠 TetraAgent <span class="hero-highlight">Synthesizer</span>
# </div>
# <div class="hero-subtitle">
#     Autonomous Multi Agent Research Platform
# </div>
# <div class="hero-description">
#     Four intelligent AI agents collaborate to search trusted web sources,
#     read relevant content, generate a professional research report,
#     and review the final output for quality and accuracy.
# </div>
# """, unsafe_allow_html=True)

# # ==========================================================
# # USER INPUT & TRIGGER
# # ==========================================================

# topic = st.text_input(
#     "Research Topic",
#     placeholder="Enter your research topic...",
#     label_visibility="collapsed"
# )

# generate = st.button("🚀 Generate Research Report", use_container_width=True)

# st.divider()

# # ==========================================================
# # PIPELINE EXECUTION LOGIC
# # ==========================================================

# if generate:
#     if not topic.strip():
#         st.warning("Please enter a research topic before generating.")
#     else:
#         with st.spinner("🧠 TetraAgent Synthesizer is executing pipeline..."):
#             state = run_research_pipeline(topic)
#             st.session_state.report = state.get("report", "")
#             st.session_state.feedback = state.get("feedback", "")
#             st.session_state.generated = True
#         st.rerun()

# # ==========================================================
# # AI TEAM GRID
# # ==========================================================

# st.markdown('<p class="section-title">🤖 Meet Your AI Team</p>', unsafe_allow_html=True)

# col1, col2 = st.columns(2, gap="large")

# def agent_card(icon: str, title: str, description: str, color: str = "#22C55E"):
#     with st.container(border=True):
#         st.markdown(f"### {icon} {title}\n{description}")
#         st.write("")
#         st.markdown(
#             f'<span style="color:{color}; font-weight:700; font-size:15px;">🟢 Ready</span>',
#             unsafe_allow_html=True
#         )

# with col1:
#     agent_card(
#         "🔎",
#         "Search Agent",
#         "Searches trusted web sources using Tavily Search and collects reliable information."
#     )
#     st.write("")
#     agent_card(
#         "✍️",
#         "Writer Agent",
#         "Generates a detailed and structured research report from collected information."
#     )

# with col2:
#     agent_card(
#         "📖",
#         "Reader Agent",
#         "Reads webpages and extracts clean, relevant content using BeautifulSoup."
#     )
#     st.write("")
#     agent_card(
#         "⭐",
#         "Critic Agent",
#         "Reviews the report, evaluates quality, and provides constructive feedback."
#     )

# st.divider()

# # ==========================================================
# # RESEARCH PIPELINE FLOW CHART
# # ==========================================================

# st.markdown('<p class="section-title">⚡ Research Pipeline</p>', unsafe_allow_html=True)

# flow_cols = st.columns(7)
# items = ["🔎 Search", "➡️", "📖 Reader", "➡️", "✍️ Writer", "➡️", "⭐ Critic"]

# for col, item in zip(flow_cols, items):
#     with col:
#         st.markdown(
#             f"""
#             <div style="
#                 text-align:center;
#                 padding:14px;
#                 border:1px solid rgba(255,255,255,.08);
#                 border-radius:12px;
#                 background:#162233;
#                 color:white;
#                 font-weight:600;
#             ">
#                 {item}
#             </div>
#             """,
#             unsafe_allow_html=True
#         )

# st.write("")
# st.info("The pipeline updates automatically as each AI agent completes its task.")

# st.divider()

# # ==========================================================
# # RESEARCH REPORT & CRITIC FEEDBACK DISPLAY
# # ==========================================================

# st.markdown('<p class="section-title">📄 Research Report</p>', unsafe_allow_html=True)

# if st.session_state.generated:
#     tab_report, tab_feedback = st.tabs(["📄 Generated Report", "⭐ Critic Review"])

#     with tab_report:
#         with st.container(border=True):
#             st.markdown(st.session_state.report)

#     with tab_feedback:
#         with st.container(border=True):
#             st.markdown(st.session_state.feedback)
# else:
#     with st.container(border=True):
#         st.info("Your generated research report will appear here after you click **Generate Research Report**.")

# st.write("")

# if st.session_state.generated:

#     st.download_button(
#         label="⬇ Download Research Report",
#         data=st.session_state.report,
#         file_name=f"{topic.replace(' ', '_')}_Research_Report.md",
#         mime="text/markdown",
#         use_container_width=True,
#     )