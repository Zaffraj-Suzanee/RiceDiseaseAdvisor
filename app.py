import streamlit as st
import json
import os
import sys
import re

<<<<<<< Updated upstream
st.set_page_config(
    page_title="Rice Disease Advisory System",
    page_icon="🌾"
)

st.title("🌾 Agentic AI-Powered Rice Disease Advisory System")

st.write(
    "AI assistant for Sri Lankan farmers to get advice about rice diseases."
)

question = st.text_area(
    "Ask your question about rice diseases:"
)

if st.button("Get Advice"):

    if question:
        st.success("Question received!")
        st.write("AI agent response will appear here.")

    else:
        st.warning("Please enter a question.")
=======
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.planner_agent import planner_agent
from agents.router_agent import router_agent
from agents.retrieval_agent import retrieval_agent
from agents.reasoning_agent import reasoning_agent


# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------

st.set_page_config(
    page_title="Rice Disease Advisor",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)
# -------------------------------------------------------
# CSS
# -------------------------------------------------------

st.markdown("""
<style>

.stApp{
    background:#F6FBF4;
}

[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#1B5E20,#2E7D32,#43A047);
}

[data-testid="stSidebar"] > div:first-child{
    background:linear-gradient(180deg,#1B5E20,#2E7D32,#43A047);
}

[data-testid="stSidebar"] *{
    color:white;
}
/* Analyze Crop button */
.stButton > button {
    width: 100%;
    height: 55px;
    background-color: #2E7D32 !important;
    color: white !important;
    border: none !important;
    border-radius: 15px !important;
    font-size: 18px !important;
    font-weight: 700 !important;
}

/* Button color when mouse is over it */
.stButton > button:hover {
    background-color: #1B5E20 !important;
    color: white !important;
    border: none !important;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# SIDEBAR
# -------------------------------------------------------

with st.sidebar:

    if os.path.exists("assets/rice_logo.jpg"):
        st.image("assets/rice_logo.jpg", width=90)

    st.markdown("## 🌾 Rice Disease Advisor")

    st.info("""
Helping Sri Lankan farmers identify rice diseases using AI.
""")

    st.markdown("### 🌱 Features")

    st.success("✅ Multi-Agent AI")
    st.success("✅ RAG Knowledge Base")
    st.success("✅ Disease Diagnosis")
    st.success("✅ Treatment Advice")
    st.success("✅ Prevention Guide")

    st.markdown("---")

    st.markdown("### 💡 Example Questions")

    st.write("• Rice blast symptoms")
    st.write("• Brown spot treatment")
    st.write("• Yellow rice leaves")
    st.write("• Leaf blight disease")

# -------------------------------------------------------
# HEADER
# -------------------------------------------------------

st.markdown("""
<div class="hero">

<h1>🌾 Rice Disease Advisor</h1>

<p>

Agentic AI-powered disease diagnosis and management system
for Sri Lankan rice farmers.

Describe your rice plant symptoms and receive intelligent
disease identification, treatment recommendations and
prevention advice.

</p>

</div>

""", unsafe_allow_html=True)

st.write("")

col1,col2=st.columns([2,1])

with col1:

    st.markdown("""

### 🌱 Why use this system?

This intelligent advisory system is designed to support Sri Lankan rice farmers, agricultural researchers, and extension officers by providing fast and reliable rice disease diagnosis and management recommendations. By analyzing user-described crop symptoms, the system identifies possible diseases and generates practical treatment and prevention advice based on trusted agricultural knowledge.

""")

with col2:

    if os.path.exists("assets/rice_banner.jpg"):
        st.image("assets/rice_banner.jpg", use_container_width=True)

st.write("")

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("Describe Your Rice Plant Symptoms")
question = st.text_area(

    "",

    height=150,

    placeholder="""
Example:

• Brown spots on leaves
• Yellow leaves
• Plant drying
• White fungus on stem
• Rice leaves become narrow and dry
"""
)

analyze = st.button("🌾 Analyze Crop")

st.markdown("</div>", unsafe_allow_html=True)

# ===========================================================
# RESULT SECTION
# ===========================================================

# ===========================================================
# RESULT SECTION
# ===========================================================
def format_text(text):

    if not text:
        return "No information available."

    text = str(text)

    text = text.replace("\n","<br><br>")

    return text
    
if analyze:

    if question.strip() == "":

        st.warning("Please enter your rice plant symptoms.")

    else:

        with st.spinner("🤖 AI agents are analyzing your crop..."):

            state = {
                "question": question,
                "messages": []
            }

            state = planner_agent(state)
            state = router_agent(state)
            state = retrieval_agent(state)
            state = reasoning_agent(state)

        try:

            answer = state["answer"]
            st.subheader("Agentic-AI Diagnosis")
          
            result = None
            
            try:
                answer_clean = answer.replace("```json", "").replace("```","").strip()
                          
                result = json.loads(answer_clean)

            except json.JSONDecodeError:

                import re

                match = re.search(
                    r"\{.*\}",
                    answer,
                    re.DOTALL
                )

                if match:
                    try:
                        result = json.loads(match.group())
                    except:
                        result = None

        except Exception as e:

            st.error("Error processing AI response.")
            st.code(str(e))
            st.stop()

        st.success("✅ Analysis Completed Successfully")

        st.markdown("<br>", unsafe_allow_html=True)

        
        if result is None:

            st.warning("The Agentic-AI returned plain text instead of JSON.")

            st.markdown(answer)

            st.stop()


                # ---------------------------------------------------
        # CARD FUNCTION
        # ---------------------------------------------------

        def info_card(title, icon, text, color):

            st.markdown(f"""
            <div style="
            background:white;
            padding:25px;
            border-radius:20px;
            border-left:8px solid {color};
            box-shadow:0px 5px 15px rgba(0,0,0,.08);
            margin-bottom:20px;
            ">

            <h2 style="color:{color};">
            {icon} {title}
            </h2>

            <div style="
            font-size:17px;
            line-height:1.8;
            text-align:justify;
            color:#444;
            ">

           {text}
 
           </div>

           </div>
           """, unsafe_allow_html=True)

        # ---------------------------------------------------
        # DISEASE
        # ---------------------------------------------------

        info_card(
            "Disease Identification",
            "🦠",
            format_text(result.get("disease")),
            "#D32F2F"
        )

        # ---------------------------------------------------
        # SYMPTOMS & CAUSES
        # ---------------------------------------------------

        left, right = st.columns(2)

        with left:

            info_card(
                "Symptoms",
                "⚠️",
                format_text(result.get("symptoms")),
                "#F57C00"
            )

        with right:

            info_card(
                "Causes",
                "🧬",
                format_text(result.get("causes")),
                "#7B1FA2"
            )

        # ---------------------------------------------------
        # MANAGEMENT & PREVENTION
        # ---------------------------------------------------

        left, right = st.columns(2)

        with left:

            info_card(
                "Recommended Management",
                "💊",
                format_text(result.get("management")),
                "#1976D2"
            )

        with right:

            info_card(
                "Prevention Advice",
                "🌱",
                format_text(result.get("prevention")),
                "#2E7D32"
            )

        # ---------------------------------------------------
        # RETRIEVED KNOWLEDGE
        # ---------------------------------------------------

        with st.expander("📚 Retrieved Agricultural Knowledge", expanded=False):

            docs = state.get("documents", [])

            if len(docs) == 0:

                st.info("No supporting agricultural documents were retrieved.")

            else:

                for i, doc in enumerate(docs, start=1):

                    st.markdown(f"### 📄 Document {i}")

                    st.markdown(f"""
<div style="
background:#F8F9FA;
padding:15px;
border-radius:12px;
border-left:5px solid #2E7D32;
font-size:15px;
line-height:1.7;
text-align:justify;
">
{doc[:1200]}
</div>
""", unsafe_allow_html=True)

                    st.write("")

        st.success(
            "The recommendations above were generated using a Multi-Agent AI workflow with a Retrieval-Augmented Generation (RAG) knowledge base."
        )
        









        
>>>>>>> Stashed changes
