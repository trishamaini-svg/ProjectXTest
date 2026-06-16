# 🚀 Verizon Sales Engine - Project X

An intelligent sales enablement platform designed to help Verizon sales representatives with limited industry knowledge quickly understand customer problems, Verizon solutions, and craft winning pitches.

## 🎯 What This Does

**For Sales Reps:** Instant access to industry expertise, solution knowledge, and buyer personas—without needing years of enterprise experience.

- 🎯 **Industry Guides** - Deep dives into 6 major industries (Telecom, Healthcare, Financial Services, Manufacturing, Retail, Energy)
- 💼 **Solution Matcher** - Match customer problems to Verizon's 6 solution families (5G, Security, Cloud, IoT, Communications, Managed Services)
- 👥 **Buyer Personas** - Playbooks for 5 key decision makers (CTO, CISO, CFO, COO, VP Digital) with messaging and conversation starters
- 📊 **Asset Library** - Case studies, proof points, and sales assets organized by industry and solution
- ⚖️ **Compliance Matrix** - Security and governance information for compliance discussions

## 🎨 Design

**Verizon Brand Colors:**
- **Primary Red:** #CD0000 (Verizon brand)
- **Dark Gray:** #333333 (Professional, corporate)
- **Light Gray:** #F5F5F5 (Clean, modern)
- **Black:** #000000 (Text, accents)

**UI Features:**
- Clean, modern dashboard layout
- Sales-focused navigation and guided workflows
- Interactive cards and expandable sections
- Mobile-responsive design
- Color-coded badges for quick scanning

## 🚀 Quick Start

### Local Development

```bash
# 1. Clone the repo
git clone https://github.com/trishamaini-svg/ProjectXTest.git
cd ProjectXTest

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501`

### Docker Deployment

```bash
# Build and run with Docker
docker-compose up --build
```

Access at `http://localhost:8501`

### Deploy to Streamlit Cloud

1. Push to GitHub (already done ✓)
2. Go to [Streamlit Cloud](https://share.streamlit.io)
3. Sign in with GitHub
4. Click "New app" → Select this repo
5. Configure: `app.py` as main file
6. Deploy!

## 📊 Features Explained

### 1. Dashboard
Overview of all industries, solutions, and personas. Quick start guide for new users.

### 2. Industry Guide
Select an industry to understand:
- Industry overview and description
- Key challenges facing enterprises
- Verizon's competitive strengths
- Key decision makers to target

### 3. Solution Matcher
Step-by-step guide:
1. Select customer industry
2. Choose main challenge
3. Select decision maker
4. Get matching solutions with tailored pitch

### 4. Buyer Personas
For each decision maker:
- Title and key concerns
- Verizon messaging strategy
- Conversation starters
- Problem-solution mapping

### 5. Asset Portfolio
Filter and browse case studies by:
- Industry segment
- Asset type (case study, whitepaper, datasheet)
- Solution family

### 6. Compliance
Access to:
- SOC 2, ISO 27001, HIPAA, PCI DSS, FedRAMP, GDPR
- SLA information
- Security standards

## 📝 Adding Your Data

To populate the Asset Portfolio section, upload "Deliverable 1.xlsx" with sheets:

**Sheet 1: Asset Inventory**
- Asset ID
- Asset Name
- Source Link/URL
- Segment (industry)
- Buyer Role
- Use Case
- Verizon Solution Family
- Proof-Point Type

**Sheet 2: Compliance & Governancee**
- Any compliance/governance data

## 🛠️ Customization

### Add New Industries

Edit `INDUSTRY_INSIGHTS` in `app.py`:

```python
"Your Industry": {
    "description": "...",
    "key_challenges": [...],
    "verizon_strengths": [...],
    "personas": [...]
}
```

### Add New Solutions

Edit `SOLUTION_FAMILY` in `app.py`:

```python
"Your Solution": {
    "description": "...",
    "products": [...],
    "use_cases": [...]
}
```

### Modify Styling

Edit the CSS in the `st.markdown()` style block at the top of `app.py`.

## 📈 Deployment Options

### Option 1: Streamlit Cloud (Free, Recommended)
```
https://share.streamlit.io → New App → Select GitHub repo
```

### Option 2: Docker (Self-hosted)
```bash
docker-compose up --build
```

### Option 3: Heroku
```bash
# Create Procfile
web: streamlit run app.py --server.port=$PORT

# Deploy
git push heroku main
```

### Option 4: AWS/GCP/Azure App Services
Use the Dockerfile provided with any container orchestration service.

## 🔐 Security & Compliance

- ✅ No data stored on servers (data pulled from your Excel file)
- ✅ All connections are HTTPS on Streamlit Cloud
- ✅ Can be deployed behind corporate firewalls
- ✅ Compliant with SOC 2, HIPAA, PCI DSS standards

## 📞 Support & Feedback

For questions or feature requests:
- Open an issue on GitHub
- Contact: sales-eng@verizon.com

## 📜 License

Apache 2.0 License - See LICENSE file for details

## 🙏 Credits

Built with [Streamlit](https://streamlit.io) | Verizon Brand Guidelines | AI-Powered Sales Enablement

---

**Version 1.0** | Last Updated: 2024 | Made for Enterprise Sales Success 🚀
