import streamlit as st

st.set_page_config(page_title="Nitec Pathways Progression Planner", page_icon="🎓", layout="centered")

st.markdown("## 🎓 Nitec Pathways Progression Planner")

st.write("This App is specific for Nitec Students who started in 2024 or 2025.<br>Check your progression options after Nitec based on your GPA and intake year!", unsafe_allow_html=True)

gpa = st.number_input("Enter your GPA:", min_value=0.0, max_value=4.0, step=0.01)
col1, col2 = st.columns(2)
intake_year = None
with col1:
    if st.button("📅 2024 Intake"):
        intake_year = 2024
with col2:
    if st.button("📅 2025 Intake"):
        intake_year = 2025

hn_courses = """
- Engineering with Business
- Mechanical Engineering
- AI Applications
- Applied Food Science
- Architectural Technology
- Automotive Engineering
- Bio-Chemical Technology
- Business Information Systems
- Chemical Process Technology
- Civil & Structural Engineering Design
- Communication Design
- Cyber & Network Security
- Data Engineering
- Electrical Engineering
- Electronics Engineering
- Facilities Management & Engineering
- Film & Video Production
- Immersive Applications & Game
- IT Applications Development
- IT Systems & Networks
- Integrated Mechanical & Electrical Design
- Interior & Product Design
- Landscape Management & Design
- Marine Engineering
- Marine & Offshore Technology
- Mechatronics Engineering
- Offshore & Marine Engineering Design
- Operational & Information Technology
- Rapid Transit Engineering
- Robotics & Smart Systems
- Security System Integration
- Technical Theatre & Production
- Vertical Transportation
- Visual Merchandising
"""

def display_pathway(title, intake, graduation, curriculum, duration, courses=None):
    st.markdown(f"""
    | ➡️ **Recommended Pathway** | {title} |
    |----------------------------|-----|
    | 📅 **Next Intake** | {intake} |
    | 🎓 **Graduation** | {graduation} |
    | 🗂️ **Curriculum** | {curriculum} |
    | ⏱️ **Duration** | {duration} |
    """)
    if courses:
        st.markdown(f"**Available Courses:**\n{courses}")
    st.markdown("---")  # Separator for clarity after each pathway

if intake_year and gpa:
    pathway_count = 0
    st.markdown("---")

    if gpa >= 3.5:
        pathway_count += 1
        display_pathway("Polytechnic Progression", f"Apr {intake_year + 2}", f"Mar {intake_year + 5}", "Polytechnic Diploma", "3 years")

    if gpa >= 3.0:
        pathway_count += 1
        display_pathway("Technical Diploma (TED)", f"Apr {intake_year + 2}", f"Mar {intake_year + 4}", "Technical Engineer Diploma", "2 years", "- Automotive Engineering\n- Civil & Structural Engineering\n- Electrical Engineering (Clean Energy)\n- Machine Technology")

    if gpa >= 3.0:
        pathway_count += 1
        display_pathway("Accelerated Higher Nitec (Old Curriculum)", f"Apr {intake_year + 2}", f"Mar {intake_year + 3}", "Higher Nitec", "1 year", "- Engineering with Business\n- Mechanical Engineering")

    if 2.8 <= gpa < 3.0 and intake_year == 2024:
        pathway_count += 1
        display_pathway("NEW Higher Nitec (Selective: ECE & Sport Mgmt)", "Apr 2026", "Mar 2028", "Higher Nitec", "2 years", "- Early Childhood Education\n- Sport Management")

    if gpa >= 2.3:
        pathway_count += 1
        grad_year = 2028 if intake_year == 2024 else 2029
        display_pathway("NEW Higher Nitec", f"Apr {intake_year + 2}", f"Mar {grad_year}", "Higher Nitec", "2 years", hn_courses)

    if gpa >= 1.9:
        pathway_count += 1
        display_pathway("ITE Work-Study Diploma", "Within 6 months post-graduation", "2.5 years from intake", "Work-Study Diploma", "2.5 years")

    if gpa < 1.9:
        st.warning("Currently not eligible for Higher Nitec, Work-Study Diploma or Polytechnic progression. Explore National Service, workforce entry, or alternative skill upgrading pathways.")
    else:
        st.success(f"✅ You have {pathway_count} possible progression pathway(s). Keep pushing forward on your educational journey!")
