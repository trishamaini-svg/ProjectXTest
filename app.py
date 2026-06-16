import os
import pandas as pd
import streamlit as st
from datetime import datetime

# 1. Page Configuration & Custom Verizon Theme
st.set_page_config(
    page_title="Verizon Sales Engine - Project X",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Verizon Red/Gray/Black Custom Styling
st.markdown("""
    <style>
        /* Main color scheme: Verizon Red (#CD0000), Dark Gray (#333333), Black (#000000) */
        .main-title {
            font-size: 42px;
            font-weight: 800;
            color: #CD0000;
            margin-bottom: 5px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .sub-title {
            font-size: 18px;
            color: #666666;
            margin-bottom: 30px;
            font-weight: 500;
        }
        
        .metric-card {
            background: linear-gradient(135deg, #F5F5F5 0%, #FFFFFF 100%);
            border-left: 6px solid #CD0000;
            padding: 20px;
            border-radius: 6px;
            margin-bottom: 15px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            transition: all 0.3s ease;
        }
        
        .metric-card:hover {
            box-shadow: 0 4px 16px rgba(205,0,0,0.15);
            transform: translateY(-2px);
        }
        
        .metric-card h3 {
            color: #CD0000;
            font-size: 32px;
            margin: 0;
            font-weight: 700;
        }
        
        .metric-card p {
            color: #333333;
            margin: 5px 0 0 0;
            font-size: 14px;
            font-weight: 600;
        }
        
        .tab-header {
            font-size: 24px;
            font-weight: 700;
            color: #000000;
            margin-top: 25px;
            margin-bottom: 15px;
            border-bottom: 4px solid #CD0000;
            padding-bottom: 10px;
            display: inline-block;
        }
        
        .sales-card {
            background-color: #FFFFFF;
            border: 2px solid #CD0000;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.1);
        }
        
        .sales-card-title {
            font-size: 18px;
            font-weight: 700;
            color: #CD0000;
            margin-bottom: 12px;
        }
        
        .sales-card-content {
            font-size: 14px;
            color: #333333;
            line-height: 1.6;
        }
        
        .persona-badge {
            display: inline-block;
            background-color: #CD0000;
            color: white;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
            margin-right: 8px;
            margin-bottom: 8px;
        }
        
        .industry-badge {
            display: inline-block;
            background-color: #333333;
            color: white;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
            margin-right: 8px;
            margin-bottom: 8px;
        }
        
        .solution-badge {
            display: inline-block;
            background-color: #666666;
            color: white;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
            margin-right: 8px;
            margin-bottom: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Sales Enablement Data & Knowledge Base
INDUSTRY_INSIGHTS = {
    "Telecommunications": {
        "description": "Network infrastructure, mobile services, broadband delivery",
        "key_challenges": ["Network congestion", "Infrastructure aging", "5G deployment costs", "Customer experience"],
        "verizon_strengths": ["5G leadership", "Network reliability", "Enterprise solutions", "IoT capabilities"],
        "personas": ["CTO", "VP of Operations", "Network Director"]
    },
    "Healthcare": {
        "description": "Medical devices, patient connectivity, data security, telemedicine",
        "key_challenges": ["HIPAA compliance", "Data security", "Legacy systems", "Downtime costs"],
        "verizon_strengths": ["Secure networks", "99.99% uptime SLA", "Edge computing", "Cloud integration"],
        "personas": ["CIO", "Chief Medical Officer", "Operations Director"]
    },
    "Financial Services": {
        "description": "Payment processing, data centers, regulatory compliance, fraud prevention",
        "key_challenges": ["Regulatory requirements", "Cyber threats", "High availability", "Legacy modernization"],
        "verizon_strengths": ["Enterprise security", "Compliance expertise", "Mission-critical services", "DDoS protection"],
        "personas": ["CISO", "CTO", "Chief Compliance Officer"]
    },
    "Manufacturing": {
        "description": "IoT sensors, supply chain tracking, predictive maintenance, factory automation",
        "key_challenges": ["Production downtime", "Supply chain visibility", "Workforce connectivity", "Real-time monitoring"],
        "verizon_strengths": ["Industrial IoT", "5G for factories", "Network reliability", "Managed services"],
        "personas": ["Plant Manager", "Operations VP", "Manufacturing Engineer"]
    },
    "Retail": {
        "description": "Point of sale, inventory management, customer analytics, omnichannel",
        "key_challenges": ["PCI compliance", "Network reliability", "Customer data", "Scalability"],
        "verizon_strengths": ["Secure networks", "Scalable infrastructure", "Analytics platform", "Edge computing"],
        "personas": ["Retail CTO", "Store Operations Manager", "E-commerce Director"]
    },
    "Energy & Utilities": {
        "description": "Smart grid, asset monitoring, field workforce management, reliability",
        "key_challenges": ["Grid modernization", "Cybersecurity", "Remote monitoring", "Regulatory compliance"],
        "verizon_strengths": ["Network coverage", "Mission-critical services", "Industrial solutions", "Security"],
        "personas": ["CISO", "Chief Engineering Officer", "Operations VP"]
    }
}

SOLUTION_FAMILY = {
    "5G & Wireless": {
        "description": "Next-gen wireless connectivity and edge computing",
        "products": ["5G Ultra Wideband", "5G Edge", "Fixed Wireless Access", "Private 5G"],
        "use_cases": ["Factory automation", "Remote healthcare", "Smart cities", "Logistics tracking"]
    },
    "Network & Security": {
        "description": "Enterprise networking, security, and DDoS protection",
        "products": ["Managed Network Security", "DDoS Protection", "Firewall Services", "Secure SD-WAN"],
        "use_cases": ["Network modernization", "Threat prevention", "Compliance", "Branch connectivity"]
    },
    "Cloud & Edge": {
        "description": "Multi-cloud management, edge computing, and hybrid infrastructure",
        "products": ["Verizon Cloud Connect", "Edge Computing Platform", "Hybrid Cloud", "Kubernetes Services"],
        "use_cases": ["Application modernization", "Data processing", "AI/ML workloads", "Real-time analytics"]
    },
    "IoT & Connectivity": {
        "description": "Device connectivity, sensor management, and IoT platforms",
        "products": ["ThingSpace Platform", "IoT Device Management", "LTE-M/NB-IoT", "Managed IoT"],
        "use_cases": ["Asset tracking", "Predictive maintenance", "Environmental monitoring", "Supply chain"]
    },
    "Communications Platform": {
        "description": "Unified communications, collaboration, and customer engagement",
        "products": ["Verizon Business Talk", "Contact Center Solutions", "Collaboration Tools", "API Platform"],
        "use_cases": ["Remote workforce", "Customer service", "Team collaboration", "Omnichannel engagement"]
    },
    "Managed Services": {
        "description": "Fully managed IT and networking services with 24/7 support",
        "products": ["Network Management", "Security Operations", "IT Managed Services", "NOC Services"],
        "use_cases": ["IT transformation", "Cost optimization", "Compliance management", "24/7 monitoring"]
    }
}

BUYER_PERSONAS = {
    "CTO": {
        "title": "Chief Technology Officer",
        "concerns": ["Technology roadmap", "Scalability", "Innovation", "ROI"],
        "messaging": "Verizon helps you build future-proof enterprise architectures with 5G, cloud, and edge technologies.",
        "conversation_starter": "How are you addressing your 5G and cloud transformation roadmap?"
    },
    "CISO": {
        "title": "Chief Information Security Officer",
        "concerns": ["Cyber threats", "Compliance", "Data protection", "Risk management"],
        "messaging": "Verizon's security-first approach protects your enterprise with advanced threat detection and compliance expertise.",
        "conversation_starter": "What are your top cybersecurity priorities for the next 12 months?"
    },
    "CFO": {
        "title": "Chief Financial Officer",
        "concerns": ["Cost optimization", "CapEx vs OpEx", "ROI", "Budget efficiency"],
        "messaging": "Verizon managed services reduce costs by 30-40% through operational efficiency and consumption-based pricing.",
        "conversation_starter": "How can you optimize your IT infrastructure costs while maintaining performance?"
    },
    "COO": {
        "title": "Chief Operations Officer",
        "concerns": ["Operational efficiency", "Uptime", "Scalability", "Performance"],
        "messaging": "Verizon delivers 99.99% uptime SLAs with mission-critical reliability and performance optimization.",
        "conversation_starter": "What's your target for operational uptime and reliability?"
    },
    "VP of Digital": {
        "title": "VP of Digital Transformation",
        "concerns": ["Digital transformation", "Customer experience", "Agility", "Time-to-market"],
        "messaging": "Verizon accelerates your digital journey with cloud, IoT, and advanced analytics capabilities.",
        "conversation_starter": "How are you accelerating your digital transformation initiatives?"
    }
}

# 4. Data Loading Function
@st.cache_data
def load_and_compile_dataset(file_name="Deliverable 1.xlsx"):
    if not os.path.exists(file_name):
        return None, None
    
    try:
        excel_file = pd.ExcelFile(file_name)
        inventory_df = pd.DataFrame()
        governance_df = pd.DataFrame()
        
        if "Asset Inventory" in excel_file.sheet_names:
            inventory_df = pd.read_excel(file_name, sheet_name="Asset Inventory")
            inventory_df.columns = [str(col).strip().lower() for col in inventory_df.columns]
            
        if "Compliance & Governancee" in excel_file.sheet_names:
            governance_df = pd.read_excel(file_name, sheet_name="Compliance & Governancee")
            governance_df.columns = [str(col).strip().lower() for col in governance_df.columns]
            
        return inventory_df, governance_df
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None, None

# 5. Helper Functions
def get_real_column_name(keyword, df):
    for col in df.columns:
        if keyword.lower() in col.lower():
            return col
    return None

# 6. Main UI
st.markdown('<p class="main-title">🚀 Verizon Sales Engine</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Project X - Intelligent Sales Enablement Platform</p>', unsafe_allow_html=True)

# Load data
inventory_df, governance_df = load_and_compile_dataset("Deliverable 1.xlsx")

# Sidebar Navigation
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/8/82/Verizon_2015_logo.svg", width=150)
st.sidebar.markdown("---")
st.sidebar.markdown("## 📚 Sales Guides")

app_mode = st.sidebar.radio(
    "Select Your Guide:",
    ["🏠 Dashboard", "🎯 Industry Guide", "💼 Solution Matcher", "👥 Buyer Personas", "📊 Asset Portfolio", "⚖️ Compliance"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📞 Support")
st.sidebar.info("Need help? Contact the sales enablement team at sales-eng@verizon.com")

# 7. Main Content Rendering

if app_mode == "🏠 Dashboard":
    st.markdown('<p class="tab-header">📊 Sales Dashboard Overview</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div class="metric-card"><h3>{len(INDUSTRY_INSIGHTS)}</h3><p>Industries Covered</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metric-card"><h3>{len(SOLUTION_FAMILY)}</h3><p>Solution Families</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="metric-card"><h3>{len(BUYER_PERSONAS)}</h3><p>Buyer Personas</p></div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown('<p class="tab-header">⚡ Quick Start</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### For Sales Reps:
        1. **Explore Industries** - Understand customer challenges
        2. **Match Solutions** - Find the right Verizon offering
        3. **Prepare Pitch** - Get tailored messaging for decision makers
        4. **Review Assets** - Access case studies and proof points
        
        **Goal:** Close deals faster with industry expertise
        """)
    
    with col2:
        st.markdown("""
        ### Key Features:
        - 🎯 **Sales Guides** - Industry-specific insights
        - 💼 **Solution Matcher** - Match problems to Verizon solutions
        - 👥 **Persona Playbooks** - Messaging by decision maker
        - 📊 **Asset Library** - Case studies, datasheets, proof points
        - ⚖️ **Compliance Matrix** - Governance and security info
        
        **Your sales superpower**: Instant access to product and industry knowledge
        """)

elif app_mode == "🎯 Industry Guide":
    st.markdown('<p class="tab-header">🎯 Industry Deep Dives</p>', unsafe_allow_html=True)
    
    selected_industry = st.selectbox("Choose an Industry:", list(INDUSTRY_INSIGHTS.keys()))
    
    if selected_industry:
        industry_data = INDUSTRY_INSIGHTS[selected_industry]
        
        st.markdown(f"### {selected_industry}")
        st.markdown(f"**Overview:** {industry_data['description']}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🔴 Key Challenges")
            for challenge in industry_data['key_challenges']:
                st.markdown(f"- {challenge}")
        
        with col2:
            st.markdown("#### 💪 Verizon Strengths")
            for strength in industry_data['verizon_strengths']:
                st.markdown(f"- {strength}")
        
        st.markdown("#### 👥 Key Decision Makers")
        for persona in industry_data['personas']:
            st.markdown(f'<span class="persona-badge">{persona}</span>', unsafe_allow_html=True)

elif app_mode == "💼 Solution Matcher":
    st.markdown('<p class="tab-header">💼 Match Problems to Solutions</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        customer_industry = st.selectbox("Customer Industry:", list(INDUSTRY_INSIGHTS.keys()))
    with col2:
        customer_challenge = st.selectbox("Main Challenge:", INDUSTRY_INSIGHTS[customer_industry]['key_challenges'])
    with col3:
        customer_persona = st.selectbox("Decision Maker:", list(BUYER_PERSONAS.keys()))
    
    if st.button("🔍 Find Matching Solutions", use_container_width=True):
        st.markdown("---")
        st.success("✅ Solution Match Found!")
        
        for family_name, family_data in SOLUTION_FAMILY.items():
            st.markdown(f"""<div class="sales-card">
                <div class="sales-card-title">{family_name}</div>
                <div class="sales-card-content">
                    <b>Description:</b> {family_data['description']}<br><br>
                    <b>Products:</b> {', '.join(family_data['products'])}<br><br>
                    <b>Relevant Use Cases:</b> {', '.join(family_data['use_cases'])}
                </div>
            </div>""", unsafe_allow_html=True)

elif app_mode == "👥 Buyer Personas":
    st.markdown('<p class="tab-header">👥 Executive Buyer Playbooks</p>', unsafe_allow_html=True)
    
    selected_persona = st.selectbox("Select Persona:", list(BUYER_PERSONAS.keys()))
    persona_data = BUYER_PERSONAS[selected_persona]
    
    st.markdown(f"### {persona_data['title']}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 🎯 Key Concerns")
        for concern in persona_data['concerns']:
            st.markdown(f'<span class="industry-badge">{concern}</span>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("#### 💬 Messaging")
        st.info(persona_data['messaging'])
    
    st.markdown("---")
    st.markdown("#### 📋 Conversation Starter")
    st.write(persona_data['conversation_starter'])

elif app_mode == "📊 Asset Portfolio":
    st.markdown('<p class="tab-header">📊 Case Studies & Sales Assets</p>', unsafe_allow_html=True)
    
    if inventory_df is not None and not inventory_df.empty:
        id_col = get_real_column_name('id', inventory_df) or 'asset id'
        name_col = get_real_column_name('name', inventory_df) or 'asset name'
        segment_col = get_real_column_name('segment', inventory_df) or 'segment'
        type_col = get_real_column_name('type', inventory_df) or 'proof-point type'
        
        available_segments = sorted([str(x).strip() for x in inventory_df[segment_col].dropna().unique() if str(x).strip() != ''])
        selected_segments = st.multiselect("Industry Segment:", available_segments, default=available_segments)
        
        available_types = sorted([str(x).strip() for x in inventory_df[type_col].dropna().unique() if str(x).strip() != ''])
        selected_types = st.multiselect("Asset Type:", available_types, default=available_types)
        
        mask = inventory_df[segment_col].isin(selected_segments) & inventory_df[type_col].isin(selected_types)
        filtered_df = inventory_df[mask]
        
        st.markdown(f"### Found {len(filtered_df)} Assets")
        
        if not filtered_df.empty:
            for idx, row in filtered_df.iterrows():
                asset_title = row.get(name_col, "Unnamed Asset")
                asset_id = row.get(id_col, "VER-GEN")
                
                with st.expander(f"📄 [{str(asset_id).upper()}] {asset_title}"):
                    st.write(row)
        else:
            st.warning("No assets match your filters.")
    else:
        st.error("No asset data available. Please upload 'Deliverable 1.xlsx' file.")

elif app_mode == "⚖️ Compliance":
    st.markdown('<p class="tab-header">⚖️ Governance & Compliance</p>', unsafe_allow_html=True)
    
    if governance_df is not None and not governance_df.empty:
        st.dataframe(governance_df, use_container_width=True, hide_index=True)
    else:
        st.markdown("""
        ### Verizon Compliance & Security Standards
        
        - **SOC 2 Type II** - Secure and available infrastructure
        - **ISO 27001** - Information security management
        - **HIPAA** - Healthcare data protection
        - **PCI DSS** - Payment card industry compliance
        - **FedRAMP** - Government cloud services
        - **GDPR** - Data privacy and protection
        - **HITRUST** - Healthcare security framework
        
        All services backed by 99.99% uptime SLA and enterprise-grade security.
        """)

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666666; font-size: 12px; padding: 20px;">
    <p>Verizon Sales Engine | Project X | Built with ❤️ for Enterprise Sales</p>
    <p>Version 1.0 | 2024</p>
</div>
""", unsafe_allow_html=True)
