# Marketing Strategy & Promotion Mix Tool

A comprehensive integrated marketing platform built with Streamlit that combines strategic marketing planning with tactical promotion mix execution, featuring direct access to design resources.

## 🌟 Features

### Marketing Strategy Tool
- **Product Analysis**: Configure product type and lifecycle stage
- **Market Strategy**: Apply Ansoff Matrix for strategic planning
- **Customer Segmentation**: Select relevant targeting criteria
- **Competitive Analysis**: Assess Porter's 5 Forces
- **Distribution Strategy**: Get channel recommendations based on product and market characteristics
- **WhatsApp Integration**: Direct booking capability for channel setup
- **Complete Recommendations**: Get comprehensive marketing strategy recommendations

### Promotion Mix Tool (NEW!)
- **Activity Recommendations**: Get personalized promotional activity suggestions based on your strategy
- **Design Resources**: Direct links to create marketing materials:
  - 🎨 Canva templates for social media, print, video, and more
  - ✉️ Email marketing templates (Mailchimp, Stripo)
  - 🎥 Video creation tools (InVideo, CapCut)
  - 📊 Visual design tools (Visme, Lucidpress)
- **Interactive Selection**: Build your custom promotion mix
- **Resource Organization**: Activities categorized by type (Digital, Print, Advertising, Events, etc.)
- **Priority Scoring**: High/Medium priority based on effectiveness
- **Export Options**: PDF export and email sharing (coming soon)

## 📊 Marketing Frameworks Used

1. **Consumer Behavior Model** (Engel, Blackwell, Miniard & Harcourt 2001)
2. **Porter's 5 Forces Framework**
3. **Ansoff Matrix**
4. **Product Lifecycle (PLC) Model**
5. **Distribution Channel Strategy Framework**
6. **Promotion Mix Communication Tools Matrix**

## 🚀 Installation

### Local Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/marketing-strategy-tool.git
cd marketing-strategy-tool
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## ☁️ Deployment

### Deploy to Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Select `app.py` as your main file
5. Click "Deploy"

### Deploy to Heroku

1. Create a `Procfile`:
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

2. Create `setup.sh`:
```bash
mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

3. Deploy:
```bash
heroku create your-app-name
git push heroku main
```

## 📖 Usage Guide

### Marketing Strategy Tool

#### Step-by-Step Workflow

1. **Product Information**
   - Select your product type (FMCG, Luxury, Electronics, Service)
   - Choose lifecycle stage (Introduction, Growth, Maturity, Decline)

2. **Market Strategy**
   - Select market-product combination using Ansoff Matrix
   - Get strategic direction (Penetration, Development, Diversification)

3. **Customer Segmentation**
   - Choose relevant segmentation criteria
   - Options: User Status, Usage Rate, Loyalty, Attitude, Demographics, Psychographics

4. **Competitive Forces**
   - Assess all 5 forces in your market
   - Rate each force as Low, Medium, or High

5. **Distribution Channel**
   - Configure customization level (High/Low)
   - Select market concentration (Concentrated/Fragmented)
   - Get channel recommendation with pros/cons
   - Book channel setup via WhatsApp

6. **View Recommendations**
   - Get complete marketing strategy
   - Includes: Core strategy, Promotion, Pricing, Distribution, Messaging
   - Seamlessly transition to Promotion Mix Tool

### Promotion Mix Tool

#### Creating Your Promotion Mix

1. **Configure Strategy**
   - Enter product type (auto-populated from Marketing Strategy Tool)
   - Select product stage
   - Choose target audience (B2C, B2B, or Mixed)

2. **Generate Recommendations**
   - Get personalized promotional activities
   - View effectiveness ratings (High/Medium priority)
   - See partner and customer focus scores

3. **Access Design Resources**
   - Click on any activity to see available design tools
   - Direct links to:
     - **Canva**: Templates for social media, brochures, flyers, videos, billboards, etc.
     - **Email Tools**: Mailchimp, Stripo for email campaigns
     - **Video Tools**: InVideo, CapCut for video marketing
     - **Design Tools**: Visme, Lucidpress for professional designs

4. **Build Your Mix**
   - Click "Add to Mix" on recommended activities
   - Track selected activities in real-time
   - Remove activities as needed

5. **Export & Share**
   - Export your promotion mix as PDF
   - Share strategy via email

## 🎨 Design Resources Integration

The tool provides direct access to these platforms:

| Category | Tools | Use Cases |
|----------|-------|-----------|
| **Social Media** | Canva, Meta Ads Manager | Facebook ads, Instagram posts, LinkedIn content |
| **Print Materials** | Canva, Visme, Lucidpress | Brochures, flyers, pamphlets, posters |
| **Email Marketing** | Canva, Mailchimp, Stripo | Email headers, newsletters, campaigns |
| **Video Content** | Canva, InVideo, CapCut | YouTube videos, TikTok, Instagram Reels |
| **Events** | Canva | Banners, presentations, event posters |
| **Loyalty Programs** | Canva | Loyalty cards, membership materials |

## 📁 Project Structure

```
marketing-strategy-tool/
│
├── app.py                 # Main integrated Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── .gitignore            # Git ignore file
└── config.toml           # Streamlit configuration (optional)
```

## 🔄 Workflow Integration

```
Marketing Strategy Tool
         ↓
    (6 Steps)
         ↓
  View Recommendations
         ↓
    [Go to Promotion Mix Tool] ←─┐
         ↓                        │
  Promotion Mix Tool              │
         ↓                        │
  Select Activities               │
         ↓                        │
  Access Design Resources         │
         ↓                        │
  Create Materials                │
         ↓                        │
  Export/Share ──────────────────┘
```

## 🎯 Distribution Channel Framework

The tool recommends distribution channels based on two dimensions:

| Customization | Market Type | Recommended Channel | Model |
|---------------|-------------|---------------------|--------|
| High | Concentrated | Direct Distribution | VMS |
| High | Fragmented | Franchise Operations | Hybrid VMS |
| Low | Concentrated | Distribution + Personal Selling | Hybrid Traditional |
| Low | Fragmented | Third-Party Intensive Distribution | Traditional Channel |

## 💻 Technologies Used

- **Python 3.8+**
- **Streamlit**: Web application framework
- **urllib**: URL encoding for WhatsApp integration
- **HTML/CSS**: Custom styling for enhanced UI

## 🎨 Key Features

### Interactive UI
- Sidebar navigation between tools
- Progress tracking for multi-step workflows
- Color-coded priority badges
- Expandable activity cards
- Real-time selection tracking

### Resource Management
- Direct links to 15+ design platforms
- Categorized by activity type
- Icon-based visual organization
- One-click access to templates

### Smart Recommendations
- Context-aware activity suggestions
- Audience-specific scoring (B2B vs B2C)
- Product stage considerations
- Effectiveness ratings

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Future Enhancements

- [ ] PDF export functionality for promotion mix
- [ ] Email sharing integration
- [ ] Budget allocation calculator
- [ ] ROI tracking dashboard
- [ ] Campaign performance metrics
- [ ] Multi-language support
- [ ] Mobile app version
- [ ] API integration with marketing platforms

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Marketing frameworks based on established academic research
- Design resource platforms for providing accessible templates
- Streamlit community for excellent documentation and support
- Built with practical marketing strategy needs in mind

## 📧 Contact

For questions, suggestions, or support, please open an issue on GitHub.

## 📸 Screenshots

### Marketing Strategy Tool
![Marketing Strategy](screenshots/marketing-strategy.png)

### Promotion Mix Tool
![Promotion Mix](screenshots/promotion-mix.png)

### Design Resources
![Design Resources](screenshots/design-resources.png)

---

**Note**: This tool provides strategic and tactical recommendations based on established marketing frameworks. Always validate recommendations with market research, A/B testing, and adapt to your specific business context. The design resource links are provided for convenience and are subject to the terms of service of each respective platform.
