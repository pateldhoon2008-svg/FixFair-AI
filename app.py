import streamlit as st
from dotenv import load_dotenv
import os
import time
from google import genai

# =====================================================
# ENVIRONMENT
# =====================================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


# =====================================================
# PAGE SETTINGS
# =====================================================

st.set_page_config(
    page_title="FixFair AI",
    page_icon="⚖️",
    layout="wide"
)


# =====================================================
# CUSTOM DESIGN
# =====================================================

st.markdown("""
<style>

/* ================================
   MAIN BACKGROUND
================================ */

.stApp {
    background:
        radial-gradient(circle at 10% 10%, #20275c 0%, transparent 30%),
        radial-gradient(circle at 90% 10%, #123b55 0%, transparent 30%),
        #080d1c;
}


/* ================================
   MAIN WIDTH
================================ */

.block-container {
    max-width: 1150px;
    padding-top: 35px;
    padding-bottom: 60px;
}


/* ================================
   GENERAL TEXT
================================ */

p, label, span {
    color: #f8fafc;
}


/* ================================
   HERO
================================ */

.hero-title {
    font-size: 52px;
    font-weight: 800;
    letter-spacing: -2px;
    margin-top: 15px;
    color: #f8fafc !important;
}

.hero-brand {
    color: #f8fafc !important;
}

.hero-ai {
    color: #818cf8 !important;
}

.hero-subtitle {
    color: #cbd5e1 !important;
    font-size: 18px;
    line-height: 1.7;
    margin-top: 8px;
}


/* ================================
   STATUS
================================ */

.status-box {
    background: rgba(34,197,94,0.10);
    border: 1px solid rgba(34,197,94,0.35);
    border-radius: 50px;
    padding: 7px 15px;
    display: inline-block;
    color: #86efac !important;
    font-size: 13px;
    font-weight: 700;
}


/* ================================
   BUTTON
================================ */

.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 14px;
    border: none;
    background: linear-gradient(90deg, #6366f1, #06b6d4);
    color: white !important;
    font-size: 16px;
    font-weight: 800;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #818cf8, #22d3ee);
    color: white !important;
}


/* ================================
   INPUT
================================ */

textarea,
input {
    border-radius: 12px !important;
}


/* ================================
   FILE UPLOAD
================================ */

section[data-testid="stFileUploaderDropzone"] {
    background: rgba(99,102,241,0.08);
    border: 1px dashed #6366f1;
    border-radius: 15px;
}


/* ================================
   METRICS
================================ */

[data-testid="stMetric"] {
    background: rgba(30,41,59,0.65);
    border: 1px solid rgba(148,163,184,0.15);
    padding: 20px;
    border-radius: 18px;
}

[data-testid="stMetricLabel"] {
    color: #cbd5e1 !important;
}

[data-testid="stMetricValue"] {
    color: #ffffff !important;
}


/* ================================
   DIVIDER
================================ */

hr {
    border-color: rgba(148,163,184,0.15);
}


/* ================================
   AI ANALYSIS CARD
================================ */

.analysis-card {
    background: rgba(15, 23, 42, 0.92);
    border: 1px solid rgba(129, 140, 248, 0.35);
    border-radius: 20px;
    padding: 30px;
    margin-top: 20px;
    box-shadow: 0 10px 35px rgba(0,0,0,0.25);
}


/* Analysis title */

.analysis-card h3 {
    color: #ffffff !important;
    font-size: 24px !important;
    margin-top: 20px !important;
    margin-bottom: 12px !important;
}


/* Analysis normal text */

.analysis-card p {
    color: #f1f5f9 !important;
    font-size: 16px !important;
    line-height: 1.75 !important;
}


/* Analysis bullet points */

.analysis-card li {
    color: #f1f5f9 !important;
    font-size: 16px !important;
    line-height: 1.7 !important;
    margin-bottom: 7px;
}


/* Bold text */

.analysis-card strong {
    color: #ffffff !important;
}


/* Block quote */

.analysis-card blockquote {
    color: #e2e8f0 !important;
    border-left: 4px solid #818cf8;
    padding-left: 18px;
    margin-left: 0;
}


/* Analysis headings */

.analysis-card h1,
.analysis-card h2,
.analysis-card h3 {
    color: #ffffff !important;
}


/* ================================
   PIPELINE CARDS
================================ */

.pipeline-card {
    background: rgba(15,23,42,0.85);
    border: 1px solid rgba(129,140,248,0.25);
    border-radius: 16px;
    padding: 18px;
    text-align: center;
}


/* ================================
   WARNING / SUCCESS
================================ */

div[data-testid="stAlert"] {
    border-radius: 14px;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# HERO SECTION
# =====================================================

st.markdown(
    '<div class="status-box">● FIXFAIR AI • SYSTEM READY</div>',
    unsafe_allow_html=True
)

st.markdown(
    '''
    <div class="hero-title">
        ⚖️ <span class="hero-brand">FixFair</span>
        <span class="hero-ai">AI</span>
    </div>
    ''',
    unsafe_allow_html=True
)

st.markdown(
    '''
    <div class="hero-subtitle">
        Evidence-driven AI for fair dispute resolution.<br>
        Turn messy disputes into facts, policy analysis,
        verification, and actionable resolutions.
    </div>
    ''',
    unsafe_allow_html=True
)

st.write("")

st.divider()


# =====================================================
# WORKFLOW
# =====================================================

st.subheader("🔄 How FixFair Works")

w1, w2, w3, w4 = st.columns(4)

with w1:
    st.info(
        "🔍 **1. Evidence**\n\n"
        "Find and organize the facts."
    )

with w2:
    st.info(
        "📜 **2. Policy**\n\n"
        "Identify the rules that apply."
    )

with w3:
    st.info(
        "⚖️ **3. Resolution**\n\n"
        "Determine a fair outcome."
    )

with w4:
    st.info(
        "🛡️ **4. Verification**\n\n"
        "Challenge and verify the result."
    )


st.divider()


# =====================================================
# CASE INFORMATION
# =====================================================

st.header("📋 Start a New Case")

st.caption(
    "Tell FixFair what happened. The AI will structure the dispute "
    "before analyzing it."
)

left, right = st.columns([2, 1])

with left:

    case_type = st.selectbox(
        "What type of dispute is this?",
        [
            "Select case type",
            "E-commerce / Wrong Product",
            "Refund / Payment",
            "Service Complaint",
            "Warranty",
            "Delivery Problem",
            "Other"
        ]
    )

with right:

    amount = st.number_input(
        "Amount involved (₹)",
        min_value=0,
        value=1299,
        step=100
    )


problem = st.text_area(
    "📝 Describe what happened",
    height=160,
    placeholder=(
        "Example: I ordered wireless headphones for ₹1,299 "
        "but received a wired headset. The seller is refusing "
        "to provide a refund."
    )
)


st.divider()


# =====================================================
# EVIDENCE
# =====================================================

st.header("📎 Evidence Vault")

st.caption(
    "Upload evidence so FixFair can verify the claim instead "
    "of relying only on the user's description."
)

e1, e2 = st.columns(2)

with e1:

    st.subheader("📸 Your Evidence")

    st.caption(
        "Invoices, screenshots, photos, receipts or other proof."
    )

    evidence_files = st.file_uploader(
        "Upload evidence",
        type=["png", "jpg", "jpeg", "pdf"],
        accept_multiple_files=True
    )


with e2:

    st.subheader("📜 Relevant Policy")

    st.caption(
        "Return policy, warranty or terms and conditions."
    )

    policy_file = st.file_uploader(
        "Upload policy",
        type=["pdf", "txt", "docx"]
    )


# =====================================================
# CASE READINESS
# =====================================================

if evidence_files or policy_file:

    st.subheader("📊 Case Readiness")

    s1, s2, s3 = st.columns(3)

    with s1:

        evidence_count = (
            len(evidence_files)
            if evidence_files
            else 0
        )

        st.metric(
            "Evidence Files",
            evidence_count
        )

    with s2:

        policy_status = (
            "READY"
            if policy_file
            else "MISSING"
        )

        st.metric(
            "Policy",
            policy_status
        )

    with s3:

        case_status = (
            "READY"
            if evidence_files
            else "WAITING"
        )

        st.metric(
            "Case Status",
            case_status
        )


st.write("")
st.divider()


# =====================================================
# ANALYZE CASE
# =====================================================

st.subheader("🚀 Ready to Analyze?")

st.caption(
    "FixFair will analyze your dispute and generate an "
    "evidence-aware, neutral resolution."
)


if st.button(
    "✨ ANALYZE MY CASE",
    use_container_width=True
):

    if case_type == "Select case type":

        st.warning(
            "⚠️ Please select a case type."
        )

    elif not problem.strip():

        st.warning(
            "⚠️ Please describe your problem."
        )

    elif not evidence_files:

        st.warning(
            "⚠️ Please upload at least one evidence file."
        )

    else:

        st.success(
            "✅ Case received successfully!"
        )

        # =============================================
        # ANALYSIS PIPELINE
        # =============================================

        st.subheader("🔄 Analysis Pipeline")

        p1, p2, p3, p4 = st.columns(4)

        with p1:
            st.success("🔍 Evidence\n\nREADY")

        with p2:
            st.success("📜 Policy\n\nREADY")

        with p3:
            st.info("⚖️ Resolution\n\nANALYZING")

        with p4:
            st.info("🛡️ Verification\n\nPENDING")


        # =============================================
        # AI PROMPT
        # =============================================

        prompt = f"""
You are FixFair AI, an AI assistant for fair and neutral
dispute resolution.

IMPORTANT:
- Do not pretend to be a lawyer.
- Do not invent laws or policies.
- Be objective and evidence-focused.
- Clearly separate facts from claims.
- Suggest reasonable possible resolutions.
- Do not automatically assume either side is correct.

CASE TYPE:
{case_type}

AMOUNT INVOLVED:
₹{amount}

USER'S DESCRIPTION:
{problem}

Analyze the dispute using this exact structure:

### 1. Key Facts

List the important facts from the user's description.

### 2. Main Issue

Clearly explain what the actual dispute is.

### 3. Fair Possible Resolutions

Give 2-3 reasonable options and explain when each option
would be appropriate.

### 4. Evidence Needed

Explain what evidence would strengthen the claim.

### 5. Negotiation Message

Write a short, professional message the user can send
to the seller/service provider.

End with:

### Fairness Note

Mention that the final decision should depend on the actual
evidence and applicable policy.
"""


        # =============================================
        # GEMINI CALL
        # =============================================

        with st.spinner(
            "⚖️ FixFair AI is analyzing your dispute..."
        ):

            try:

                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt
                )

                ai_text = response.text

                st.subheader("⚖️ FixFair AI Analysis")

                st.markdown(
                    f'''
                    <div class="analysis-card">
                    {ai_text}
                    </div>
                    ''',
                    unsafe_allow_html=True
                )


            except Exception as error:

                error_text = str(error)

                if "503" in error_text:

                    st.error(
                        "⚠️ FixFair AI is temporarily busy because "
                        "the Gemini model is experiencing high demand."
                    )

                    st.info(
                        "Please wait 10-20 seconds and click "
                        "**ANALYZE MY CASE** again."
                    )

                else:

                    st.error(
                        "⚠️ FixFair AI could not complete the analysis."
                    )

                    st.caption(
                        "Please check your API key, internet connection, "
                        "and Gemini model availability."
                    )


# =====================================================
# FOOTER
# =====================================================

st.write("")
st.divider()

st.caption(
    "⚖️ FixFair AI  •  Evidence First  •  Policy Aware  •  Human Controlled"
)