# nitec_pathways_app.py

import streamlit as st

st.title("🎓 Nitec Pathways Planner")
st.write(
    "This App is specific for Nitec Students who started Nitec in 2024 or 2025."
    "<br>"
    "Check your progression options after Nitec based on your GPA and intake year!",
    unsafe_allow_html=True
)

# Input collection
gpa = st.number_input("📊 Enter your GPA (e.g., 2.8):", min_value=0.0, max_value=4.0, step=0.1)

# Intake year buttons
st.write("📅 What year did you start your Nitec journey?")
col1, col2 = st.columns(2)

if 'intake_year' not in st.session_state:
    st.session_state['intake_year'] = None

with col1:
    if st.button("2024"):
        st.session_state['intake_year'] = 2024
with col2:
    if st.button("2025"):
        st.session_state['intake_year'] = 2025

if st.session_state['intake_year']:
    intake_year = st.session_state['intake_year']
    st.success(f"✅ Intake Year Selected: {intake_year}")

    if st.button("Check My Pathways"):
        pathway_count = 0  # Initialize counter

        def display_pathway(content):
            st.markdown(f"""
<p style='font-size:16px'>
{content}
</p>
<hr>
""", unsafe_allow_html=True)

        if gpa >= 3.5:
            grad_year = intake_year + 2
            poly_grad_year = grad_year + 3
            display_pathway(f"""
<b>➡️ Recommended Pathway:</b> Polytechnic (via EAE/JPAE)<br>
<b>📅 Next Intake:</b> Apr {grad_year}<br>
<b>🎓 Graduation:</b> Mar {poly_grad_year}<br>
<b>🗂️ Curriculum:</b> Polytechnic Diploma<br>
<b>⏱️ Duration:</b> 3 years
""")
            pathway_count += 1

        if intake_year == 2024:
            if gpa >= 3.0:
                display_pathway(f"""
<b>➡️ Recommended Pathway:</b> Accelerated Higher Nitec (Old Curriculum)<br>
<b>📅 Next Intake:</b> Apr 2026<br>
<b>🎓 Graduation:</b> Mar 2027<br>
<b>🗂️ Curriculum:</b> Higher Nitec<br>
<b>⏱️ Duration:</b> 1 year
""")
                pathway_count += 1

            if gpa >= 2.3:
                display_pathway(f"""
<b>➡️ Recommended Pathway:</b> NEW Higher Nitec<br>
<b>📅 Next Intake:</b> Apr 2026<br>
<b>🎓 Graduation:</b> Mar 2028<br>
<b>🗂️ Curriculum:</b> Higher Nitec<br>
<b>⏱️ Duration:</b> 2 years
""")
                pathway_count += 1

        if intake_year == 2025:
            if gpa >= 3.0:
                display_pathway(f"""
<b>➡️ Recommended Pathway:</b> Accelerated NEW Higher Nitec<br>
<b>📅 Next Intake:</b> Apr 2027<br>
<b>🎓 Graduation:</b> Mar 2028<br>
<b>🗂️ Curriculum:</b> Higher Nitec<br>
<b>⏱️ Duration:</b> 1 year
""")
                pathway_count += 1

            if gpa >= 2.3:
                display_pathway(f"""
<b>➡️ Recommended Pathway:</b> NEW Higher Nitec<br>
<b>📅 Next Intake:</b> Apr 2027<br>
<b>🎓 Graduation:</b> Mar 2029<br>
<b>🗂️ Curriculum:</b> Higher Nitec<br>
<b>⏱️ Duration:</b> 2 years
""")
                pathway_count += 1

        if gpa >= 1.9:
            display_pathway(f"""
<b>➡️ Recommended Pathway:</b> ITE Work-Study Diploma<br>
<b>📅 Next Intake:</b> Every April<br>
<b>🎓 Graduation:</b> 2.5 years from intake<br>
<b>🗂️ Curriculum:</b> Work-Study Diploma<br>
<b>⏱️ Duration:</b> 2.5 years
""")
            pathway_count += 1

        if pathway_count > 0:
            st.subheader(f"🎓 You have {pathway_count} Progression Pathway{'s' if pathway_count != 1 else ''} available")
        else:
            st.warning("⚠️ Currently not eligible for Higher Nitec or Work-Study Diploma progression. Explore workforce entry or alternative skill upgrading pathways.")

        st.success("🌻 Keep pushing forward on your educational journey! Every step counts towards your success!")

else:
    st.info("👆 Please select your intake year to proceed.")

