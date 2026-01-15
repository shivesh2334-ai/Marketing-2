# app.py - Integrated Marketing Strategy & Promotion Mix Tool
import streamlit as st
import urllib.parse

# Page configuration
st.set_page_config(
    page_title="Marketing Strategy & Promotion Mix Tool",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .resource-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin: 0.5rem 0;
    }
    .priority-high {
        background-color: #10b981;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: bold;
    }
    .priority-medium {
        background-color: #f59e0b;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: bold;
    }
    .selected-activity {
        border: 2px solid #3b82f6;
        background-color: #eff6ff;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'app_mode' not in st.session_state:
    st.session_state.app_mode = 'Marketing Strategy'
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'product_type' not in st.session_state:
    st.session_state.product_type = None
if 'product_stage' not in st.session_state:
    st.session_state.product_stage = None
if 'market_type' not in st.session_state:
    st.session_state.market_type = None
if 'segmentation' not in st.session_state:
    st.session_state.segmentation = []
if 'competitive_forces' not in st.session_state:
    st.session_state.competitive_forces = {}
if 'distribution_config' not in st.session_state:
    st.session_state.distribution_config = {'customization': None, 'market_concentration': None}
if 'selected_channel' not in st.session_state:
    st.session_state.selected_channel = None
if 'target_audience' not in st.session_state:
    st.session_state.target_audience = None
if 'selected_activities' not in st.session_state:
    st.session_state.selected_activities = []

# Communication tools with resources
COMMUNICATION_TOOLS = {
    'Advertisements on TV/Newspaper/Magazines/Radio': {
        'partner': 'Partly',
        'customer': 'Largely',
        'type': 'advertising',
        'resources': []
    },
    'Social Media Advertising (Facebook/Instagram/LinkedIn)': {
        'partner': 'Partly',
        'customer': 'Largely',
        'type': 'digital',
        'resources': [
            {'name': 'Canva', 'url': 'https://www.canva.com/create/facebook-ads/', 'icon': '🎨', 'desc': 'Facebook Ad Templates'},
            {'name': 'Canva', 'url': 'https://www.canva.com/create/instagram-posts/', 'icon': '🎨', 'desc': 'Instagram Post Templates'},
            {'name': 'Meta Ads Manager', 'url': 'https://business.facebook.com/adsmanager', 'icon': '📱', 'desc': 'Create & Manage Ads'}
        ]
    },
    'Point of Purchase Promotions in Retail Outlets': {
        'partner': '',
        'customer': 'Largely',
        'type': 'sales-promotion',
        'resources': [
            {'name': 'Canva', 'url': 'https://www.canva.com/create/posters/', 'icon': '🎨', 'desc': 'POS Poster Templates'},
            {'name': 'Canva', 'url': 'https://www.canva.com/create/shelf-talkers/', 'icon': '🎨', 'desc': 'Shelf Talker Designs'}
        ]
    },
    'Display Boards / Billboards': {
        'partner': 'Partly',
        'customer': 'Largely',
        'type': 'advertising',
        'resources': [
            {'name': 'Canva', 'url': 'https://www.canva.com/create/billboards/', 'icon': '🎨', 'desc': 'Billboard Templates'},
            {'name': 'Visme', 'url': 'https://www.visme.co/', 'icon': '📊', 'desc': 'Visual Design Tool'}
        ]
    },
    'Pamphlets/Brochures/Flyers': {
        'partner': 'Partly',
        'customer': 'Largely',
        'type': 'print',
        'resources': [
            {'name': 'Canva', 'url': 'https://www.canva.com/create/brochures/', 'icon': '🎨', 'desc': 'Brochure Templates'},
            {'name': 'Canva', 'url': 'https://www.canva.com/create/flyers/', 'icon': '🎨', 'desc': 'Flyer Templates'},
            {'name': 'Visme', 'url': 'https://www.visme.co/brochure-maker/', 'icon': '📊', 'desc': 'Brochure Maker'},
            {'name': 'Lucidpress', 'url': 'https://www.lucidpress.com/', 'icon': '📄', 'desc': 'Brand Templates'}
        ]
    },
    'Email Marketing Campaigns': {
        'partner': 'Partly',
        'customer': 'Largely',
        'type': 'digital',
        'resources': [
            {'name': 'Canva', 'url': 'https://www.canva.com/create/email-headers/', 'icon': '🎨', 'desc': 'Email Header Templates'},
            {'name': 'Mailchimp', 'url': 'https://mailchimp.com/create/email-templates/', 'icon': '✉️', 'desc': 'Email Templates'},
            {'name': 'Stripo', 'url': 'https://stripo.email/', 'icon': '✉️', 'desc': 'Email Designer'}
        ]
    },
    'Video Marketing (YouTube/TikTok/Reels)': {
        'partner': 'Partly',
        'customer': 'Largely',
        'type': 'digital',
        'resources': [
            {'name': 'Canva', 'url': 'https://www.canva.com/create/videos/', 'icon': '🎨', 'desc': 'Video Templates'},
            {'name': 'InVideo', 'url': 'https://invideo.io/', 'icon': '🎥', 'desc': 'Video Creation Tool'},
            {'name': 'CapCut', 'url': 'https://www.capcut.com/', 'icon': '✂️', 'desc': 'Video Editor'}
        ]
    },
    'Trade Shows': {
        'partner': 'Largely',
        'customer': 'Partly',
        'type': 'events',
        'resources': [
            {'name': 'Canva', 'url': 'https://www.canva.com/create/banners/', 'icon': '🎨', 'desc': 'Banner Templates'},
            {'name': 'Canva', 'url': 'https://www.canva.com/create/presentations/', 'icon': '🎨', 'desc': 'Presentation Templates'}
        ]
    },
    'Fairs/Festivals/Movie Shows': {
        'partner': 'Partly',
        'customer': 'Largely',
        'type': 'events',
        'resources': [
            {'name': 'Canva', 'url': 'https://www.canva.com/create/event-posters/', 'icon': '🎨', 'desc': 'Event Poster Templates'}
        ]
    },
    'Sampling Events': {
        'partner': '',
        'customer': 'Largely',
        'type': 'sales-promotion',
        'resources': [
            {'name': 'Canva', 'url': 'https://www.canva.com/create/invitations/', 'icon': '🎨', 'desc': 'Event Invitations'}
        ]
    },
    'Trade Discount/Rebates': {
        'partner': 'Largely',
        'customer': 'Partly',
        'type': 'sales-promotion',
        'resources': []
    },
    'Loyalty Programs': {
        'partner': 'Partly',
        'customer': 'Largely',
        'type': 'relationship',
        'resources': [
            {'name': 'Canva', 'url': 'https://www.canva.com/create/loyalty-cards/', 'icon': '🎨', 'desc': 'Loyalty Card Templates'}
        ]
    },
    'Direct Mailing/Catalogues/Telemarketing': {
        'partner': '',
        'customer': 'Largely',
        'type': 'direct',
        'resources': [
            {'name': 'Canva', 'url': 'https://www.canva.com/create/catalogs/', 'icon': '🎨', 'desc': 'Catalog Templates'}
        ]
    },
    'Community Relations/CSR Drives': {
        'partner': '',
        'customer': 'Largely',
        'type': 'pr',
        'resources': [
            {'name': 'Canva', 'url': 'https://www.canva.com/create/infographics/', 'icon': '🎨', 'desc': 'Infographic Templates'}
        ]
    }
}

# Data definitions (from original)
PRODUCT_TYPES = {
    'fmcg': {'name': 'FMCG/Consumer Goods', 'desc': 'Fast-moving consumer products'},
    'luxury': {'name': 'Luxury Products', 'desc': 'Premium, high-differentiation items'},
    'electronics': {'name': 'Electronics/Gadgets', 'desc': 'Technology products'},
    'service': {'name': 'Service', 'desc': 'Intangible offerings'}
}

PRODUCT_STAGES = ['Introduction', 'Growth', 'Maturity', 'Decline']

MARKET_TYPES = {
    'new-new': {'name': 'New Market + New Product', 'strategy': 'Diversification'},
    'new-existing': {'name': 'New Market + Existing Product', 'strategy': 'Market Development'},
    'existing-new': {'name': 'Existing Market + New Product', 'strategy': 'Product Development'},
    'existing-existing': {'name': 'Existing Market + Existing Product', 'strategy': 'Market Penetration'}
}

SEGMENTATION_OPTIONS = {
    'user-status': {'name': 'User Status', 'desc': 'Non-users, potential users, regular users'},
    'usage-rate': {'name': 'Usage Rate', 'desc': 'Light, medium, heavy users'},
    'loyalty': {'name': 'Loyalty', 'desc': 'Brand loyal, switchers, competitors'},
    'attitude': {'name': 'Attitude', 'desc': 'Enthusiastic, positive, negative'},
    'demographic': {'name': 'Demographic', 'desc': 'Age, income, education, family size'},
    'psychographic': {'name': 'Psychographic', 'desc': 'Lifestyle, values, personality'}
}

DISTRIBUTION_CHANNELS = {
    'high-concentrated': {
        'name': 'Direct Distribution',
        'model': 'VMS (Vertical Marketing System)',
        'description': 'Direct sales to concentrated customer base',
        'pros': ['Perfect control over placement and quality', 'Enhanced consumer satisfaction', 'Less response time to grievances'],
        'cons': ['Requires huge investments', 'May not be viable for low-margin products', 'Potential loss of flexibility'],
        'examples': ['Company-owned stores', 'Direct sales force', 'E-commerce platform', 'B2B direct sales']
    },
    'high-fragmented': {
        'name': 'Franchise Operations',
        'model': 'Hybrid VMS',
        'description': 'Standardized operations through franchise network',
        'pros': ['Rapid market expansion', 'Controlled brand experience', 'Shared investment with franchisees', 'Local market expertise'],
        'cons': ['Franchisee management complexity', 'Quality control challenges', 'Profit sharing with franchisees'],
        'examples': ['Fast food franchises', 'Retail chain franchises', 'Service franchises', 'Master franchise model']
    },
    'low-concentrated': {
        'name': 'Distribution + Personal Selling',
        'model': 'Hybrid Traditional',
        'description': 'Selected distributors with sales force support',
        'pros': ['Market access without heavy investment', 'Sales force ensures customer relationships', 'Flexibility in market coverage'],
        'cons': ['Moderate control over distribution', 'Coordination complexity', 'Channel conflict potential'],
        'examples': ['Industrial distributors', 'B2B dealers with sales support', 'Authorized dealers', 'Value-added resellers']
    },
    'low-fragmented': {
        'name': 'Third-Party Intensive Distribution',
        'model': 'Traditional Channel',
        'description': 'Maximum market coverage through multiple retailers',
        'pros': ['Better market access by appointing more retailers', 'Low investment in distribution', 'Wide availability'],
        'cons': ['Focus on volume, not customer satisfaction', 'Slow information flow', 'Manufacturer has minimal or no control', 'Frequent conflicts among channel members'],
        'examples': ['Mass retailers', 'Supermarkets', 'Online marketplaces', 'Wholesaler networks', 'Multi-brand outlets']
    }
}

# Helper functions
def get_distribution_recommendation():
    config = st.session_state.distribution_config
    if not config['customization'] or not config['market_concentration']:
        return None
    key = f"{config['customization']}-{config['market_concentration']}"
    return DISTRIBUTION_CHANNELS.get(key)

def get_recommendations():
    recommendations = {
        'strategy': '',
        'pricing': '',
        'promotion': '',
        'distribution': '',
        'messaging': []
    }
    
    if st.session_state.market_type:
        recommendations['strategy'] = MARKET_TYPES[st.session_state.market_type]['strategy']
    
    stage = st.session_state.product_stage
    if stage == 'Introduction':
        recommendations['promotion'] = 'Focus on Information & Advertising to build awareness. Use promotion to induce trial. Less sales promotion, more advertising investment.'
        recommendations['pricing'] = 'Penetration pricing (low to gain market share) or Skimming pricing (high for innovative products)'
    elif stage == 'Growth':
        recommendations['promotion'] = 'Increase advertising to build preference. Sales promotions to attract new consumers and increase consumption.'
        recommendations['pricing'] = 'Maintain or slightly reduce prices to match competition and maximize market share'
    elif stage == 'Maturity':
        recommendations['promotion'] = 'Effort to induce different usages. More sales promotion, less advertising. Focus on attracting marginal customers and brand switching.'
        recommendations['pricing'] = 'Competitive pricing, promotional pricing to defend market share'
    elif stage == 'Decline':
        recommendations['promotion'] = 'Frequent sales promotions to liquidate stock. Extremely low advertising spend. Minimal promotional investment.'
        recommendations['pricing'] = 'Discount pricing to clear inventory, harvest profits'
    
    dist_rec = get_distribution_recommendation()
    if dist_rec:
        recommendations['distribution'] = f"{dist_rec['name']} - {dist_rec['description']}"
    else:
        recommendations['distribution'] = 'Complete distribution configuration to get recommendation'
    
    forces = st.session_state.competitive_forces
    if forces.get('rivalry') == 'High':
        recommendations['messaging'].append('Differentiate strongly - high rivalry requires clear positioning')
    if forces.get('buyers') == 'High':
        recommendations['messaging'].append('Focus on value proposition - buyers have strong bargaining power')
    if forces.get('newEntrants') == 'High':
        recommendations['messaging'].append('Build brand loyalty quickly - threat of new entrants is high')
    if forces.get('substitutes') == 'High':
        recommendations['messaging'].append('Emphasize unique benefits - substitutes pose a threat')
    
    product_type = st.session_state.product_type
    if product_type == 'luxury':
        recommendations['messaging'].append('Premium positioning, emotional branding, exclusivity messaging')
    elif product_type == 'fmcg':
        recommendations['messaging'].append('Mass market appeal, convenience, value for money')
    elif product_type == 'electronics':
        recommendations['messaging'].append('Innovation focus, feature benefits, early adopter targeting')
    
    if 'loyalty' in st.session_state.segmentation:
        recommendations['messaging'].append('Implement loyalty programs and retention marketing')
    if 'usage-rate' in st.session_state.segmentation:
        recommendations['messaging'].append('Tailor messaging for heavy vs. light users differently')
    if 'psychographic' in st.session_state.segmentation:
        recommendations['messaging'].append('Create lifestyle-based campaigns aligned with values')
    
    return recommendations

def get_promotion_recommendations():
    recommendations = []
    focus = st.session_state.target_audience
    
    if not focus:
        return []
    
    focus_lower = focus.lower()
    
    for tool, details in COMMUNICATION_TOOLS.items():
        score = 0
        reasoning = ''
        
        if 'customer' in focus_lower or 'b2c' in focus_lower:
            if details['customer'] == 'Largely':
                score = 3
                reasoning = 'Highly effective for customer-centric approach'
            elif details['customer'] == 'Partly':
                score = 1
                reasoning = 'Moderately effective for customers'
        elif 'partner' in focus_lower or 'b2b' in focus_lower:
            if details['partner'] == 'Largely':
                score = 3
                reasoning = 'Highly effective for partner-centric approach'
            elif details['partner'] == 'Partly':
                score = 1
                reasoning = 'Moderately effective for partners'
        else:
            partner_score = 3 if details['partner'] == 'Largely' else 1 if details['partner'] == 'Partly' else 0
            customer_score = 3 if details['customer'] == 'Largely' else 1 if details['customer'] == 'Partly' else 0
            score = max(partner_score, customer_score)
            reasoning = 'Balanced approach for mixed audience'
        
        if score > 0:
            recommendations.append({
                'tool': tool,
                'score': score,
                'reasoning': reasoning,
                **details
            })
    
    recommendations.sort(key=lambda x: x['score'], reverse=True)
    return recommendations[:12]

def get_stage_advice(stage):
    advice = {
        'Introduction': 'Focus on awareness building through mass media, sampling, and trade shows. Consider promotional pricing.',
        'Growth': 'Expand distribution through trade incentives. Build brand loyalty with loyalty programs and CSR activities.',
        'Maturity': 'Maintain market share through competitive pricing, loyalty programs, and sustained advertising.',
        'Decline': 'Focus on cost efficiency. Use targeted promotions, liquidation sales, and focus on loyal customer base.'
    }
    return advice.get(stage, 'Consider your product lifecycle stage when allocating marketing budget.')

def get_type_advice(product_type):
    type_lower = product_type.lower() if product_type else ''
    
    if 'fmcg' in type_lower or 'consumer' in type_lower:
        return 'Consumer goods benefit from mass media advertising, POP displays, sampling events, and loyalty programs.'
    elif 'industrial' in type_lower or 'b2b' in type_lower:
        return 'Industrial products require trade shows, facility tours, trade discounts, and direct relationship building.'
    elif 'luxury' in type_lower or 'premium' in type_lower:
        return 'Premium products benefit from selective advertising, experiential events, and exclusive partnerships.'
    elif 'service' in type_lower:
        return 'Services require demonstration through sampling, testimonials, community engagement, and relationship marketing.'
    return 'Tailor your communication mix to your product characteristics and target market.'

def generate_whatsapp_message():
    channel = get_distribution_recommendation()
    product_name = PRODUCT_TYPES[st.session_state.product_type]['name'] if st.session_state.product_type else ''
    
    message = f"""Hi! I'd like to discuss distribution channel setup:

Product Type: {product_name}
Product Stage: {st.session_state.product_stage}
Recommended Channel: {channel['name'] if channel else ''}
Channel Model: {channel['model'] if channel else ''}
Selected Option: {st.session_state.selected_channel or ''}

I'm interested in learning more about implementation."""
    
    return f"https://wa.me/?text={urllib.parse.quote(message)}"

# Sidebar navigation
with st.sidebar:
    st.title("📊 Navigation")
    st.session_state.app_mode = st.radio(
        "Select Tool:",
        ["Marketing Strategy", "Promotion Mix"],
        index=0 if st.session_state.app_mode == "Marketing Strategy" else 1
    )
    
    st.markdown("---")
    st.markdown("### About")
    st.info("""
    **Marketing Strategy Tool:**
    Complete 6-step framework for strategic marketing decisions
    
    **Promotion Mix Tool:**
    Get activity recommendations with design resources
    """)

# Main content
if st.session_state.app_mode == "Marketing Strategy":
    st.title("📊 Marketing Strategy Decision Tool")
    st.markdown("*Data-driven marketing decisions using proven frameworks*")
    
    # Progress bar
    progress = (st.session_state.step - 1) / 5
    st.progress(progress)
    
    # Step indicator
    cols = st.columns(6)
    step_names = ['Product', 'Market', 'Segments', 'Forces', 'Distribution', 'Results']
    for i, (col, name) in enumerate(zip(cols, step_names), 1):
        with col:
            if i < st.session_state.step:
                st.markdown(f"**✓ {name}**")
            elif i == st.session_state.step:
                st.markdown(f"**→ {name}**")
            else:
                st.markdown(f"{name}")
    
    st.markdown("---")
    
    # Step 1: Product Information
    if st.session_state.step == 1:
        st.header("Step 1: Product Information")
        st.markdown("Select your product type and lifecycle stage")
        
        st.subheader("Product Type")
        cols = st.columns(2)
        for i, (key, value) in enumerate(PRODUCT_TYPES.items()):
            with cols[i % 2]:
                if st.button(f"**{value['name']}**\n\n{value['desc']}", key=f"prod_{key}", use_container_width=True):
                    st.session_state.product_type = key
        
        if st.session_state.product_type:
            st.success(f"✓ Selected: {PRODUCT_TYPES[st.session_state.product_type]['name']}")
        
        st.subheader("Product Lifecycle Stage")
        cols = st.columns(4)
        for i, stage in enumerate(PRODUCT_STAGES):
            with cols[i]:
                if st.button(stage, key=f"stage_{stage}", use_container_width=True):
                    st.session_state.product_stage = stage
        
        if st.session_state.product_stage:
            st.success(f"✓ Selected: {st.session_state.product_stage}")
    
    # Step 2: Market Strategy
    elif st.session_state.step == 2:
        st.header("Step 2: Market Strategy (Ansoff Matrix)")
        st.markdown("Choose your market-product combination")
        
        cols = st.columns(2)
        for i, (key, value) in enumerate(MARKET_TYPES.items()):
            with cols[i % 2]:
                if st.button(f"**{value['name']}**\n\nStrategy: {value['strategy']}", key=f"market_{key}", use_container_width=True):
                    st.session_state.market_type = key
        
        if st.session_state.market_type:
            st.success(f"✓ Selected: {MARKET_TYPES[st.session_state.market_type]['strategy']}")
    
    # Step 3: Customer Segmentation
    elif st.session_state.step == 3:
        st.header("Step 3: Customer Segmentation")
        st.markdown("Select relevant segmentation criteria for targeting")
        
        for key, value in SEGMENTATION_OPTIONS.items():
            checked = st.checkbox(
                f"**{value['name']}** - {value['desc']}", 
                value=key in st.session_state.segmentation, 
                key=f"seg_{key}"
            )
            if checked and key not in st.session_state.segmentation:
                st.session_state.segmentation.append(key)
            elif not checked and key in st.session_state.segmentation:
                st.session_state.segmentation.remove(key)
        
        if st.session_state.segmentation:
            st.success(f"✓ Selected {len(st.session_state.segmentation)} segmentation criteria")
    
    # Step 4: Competitive Forces
    elif st.session_state.step == 4:
        st.header("Step 4: Porter's 5 Forces Analysis")
        st.markdown("Assess competitive forces in your market")
        
        forces = [
            ('rivalry', 'Existing Rivalry Between Firms'),
            ('suppliers', 'Bargaining Power of Suppliers'),
            ('buyers', 'Bargaining Power of Customers'),
            ('newEntrants', 'Threat of New Entrants'),
            ('substitutes', 'Threat of Substitutes')
        ]
        
        for key, label in forces:
            st.subheader(label)
            cols = st.columns(3)
            for i, option in enumerate(['Low', 'Medium', 'High']):
                with cols[i]:
                    if st.button(option, key=f"force_{key}_{option}", use_container_width=True):
                        st.session_state.competitive_forces[key] = option
            
            if key in st.session_state.competitive_forces:
                st.info("### 📦 Distribution Strategy")
        st.markdown(recommendations['distribution'])
        
        if st.session_state.selected_channel:
            st.markdown(f"**Selected Channel:** {st.session_state.selected_channel}")
            if st.button("📱 Contact via WhatsApp", key="whatsapp_final"):
                whatsapp_url = generate_whatsapp_message()
                st.markdown(f"[Click here to open WhatsApp]({whatsapp_url})")
        
        st.warning("### 💡 Key Messaging Insights")
        for msg in recommendations['messaging']:
            st.markdown(f"- {msg}")
        
        st.caption("*Note: These recommendations are based on established marketing frameworks including Consumer Behavior Model (Engel, Blackwell, Miniard & Harcourt 2001), Porter's 5 Forces, Ansoff Matrix, Product Lifecycle, and Distribution Channel Strategy.*")
        
        # Link to Promotion Mix
        st.markdown("---")
        st.info("### 🎨 Ready to create your promotion materials?")
        if st.button("Go to Promotion Mix Tool →", type="primary", use_container_width=True):
            st.session_state.app_mode = "Promotion Mix"
            st.rerun()
    
    # Navigation buttons
    st.markdown("---")
    cols = st.columns([1, 1])
    
    with cols[0]:
        if st.session_state.step > 1:
            if st.button("← Previous", use_container_width=True):
                st.session_state.step -= 1
                st.rerun()
    
    with cols[1]:
        can_proceed = False
        if st.session_state.step == 1:
            can_proceed = st.session_state.product_type and st.session_state.product_stage
        elif st.session_state.step == 2:
            can_proceed = st.session_state.market_type
        elif st.session_state.step == 3:
            can_proceed = len(st.session_state.segmentation) > 0
        elif st.session_state.step == 4:
            can_proceed = len(st.session_state.competitive_forces) == 5
        elif st.session_state.step == 5:
            can_proceed = st.session_state.distribution_config['customization'] and st.session_state.distribution_config['market_concentration']
        
        if st.session_state.step < 6:
            if st.button("Next →", disabled=not can_proceed, use_container_width=True, type="primary"):
                st.session_state.step += 1
                st.rerun()
        else:
            if st.button("🔄 Start New Analysis", use_container_width=True, type="primary"):
                st.session_state.step = 1
                st.session_state.product_type = None
                st.session_state.product_stage = None
                st.session_state.market_type = None
                st.session_state.segmentation = []
                st.session_state.competitive_forces = {}
                st.session_state.distribution_config = {'customization': None, 'market_concentration': None}
                st.session_state.selected_channel = None
                st.rerun()

# Promotion Mix Tool
else:
    st.title("🎨 Promotion Mix Strategy Tool")
    st.markdown("*Get personalized promotional activity recommendations with design resources*")
    
    # Input section
    with st.container():
        st.subheader("Configure Your Promotion Strategy")
        
        cols = st.columns(3)
        
        with cols[0]:
            product_type_input = st.text_input(
                "📦 Product Type",
                value=PRODUCT_TYPES[st.session_state.product_type]['name'] if st.session_state.product_type else '',
                placeholder="e.g., FMCG, Industrial, Service"
            )
        
        with cols[1]:
            product_stage_input = st.selectbox(
                "📈 Product Stage",
                [''] + PRODUCT_STAGES,
                index=PRODUCT_STAGES.index(st.session_state.product_stage) + 1 if st.session_state.product_stage else 0
            )
        
        with cols[2]:
            st.session_state.target_audience = st.selectbox(
                "👥 Target Audience",
                ['', 'Customer Centric (B2C)', 'Partner Centric (B2B)', 'Mixed Audience'],
                index=0
            )
        
        if st.button("🔍 Generate Promotion Mix Strategy", type="primary", use_container_width=True):
            if product_type_input and product_stage_input and st.session_state.target_audience:
                st.session_state.selected_activities = []
                st.rerun()
    
    # Results section
    if st.session_state.target_audience and product_stage_input:
        st.markdown("---")
        st.header("Your Promotion Mix Strategy")
        
        # Insights
        cols = st.columns(2)
        with cols[0]:
            st.info(f"**📈 Product Stage Insight**\n\n{get_stage_advice(product_stage_input)}")
        with cols[1]:
            st.info(f"**📦 Product Type Insight**\n\n{get_type_advice(product_type_input)}")
        
        st.markdown("---")
        
        # Get recommendations
        recommendations = get_promotion_recommendations()
        
        if recommendations:
            # Header with count
            cols = st.columns([3, 1])
            with cols[0]:
                st.subheader("Recommended Promotional Activities")
            with cols[1]:
                if st.session_state.selected_activities:
                    st.success(f"✓ {len(st.session_state.selected_activities)} Selected")
            
            # Activity cards
            for rec in recommendations:
                with st.expander(f"{'✓ ' if rec['tool'] in st.session_state.selected_activities else ''}**{rec['tool']}** - {rec['reasoning']}", 
                               expanded=False):
                    
                    cols = st.columns([3, 1])
                    with cols[0]:
                        st.markdown(f"**Type:** {rec['type'].replace('-', ' ').title()}")
                        st.markdown(f"**Partner Focus:** {rec['partner'] or 'N/A'}")
                        st.markdown(f"**Customer Focus:** {rec['customer'] or 'N/A'}")
                    with cols[1]:
                        priority_class = "priority-high" if rec['score'] == 3 else "priority-medium"
                        priority_text = "High Priority" if rec['score'] == 3 else "Medium Priority"
                        st.markdown(f'<span class="{priority_class}">{priority_text}</span>', unsafe_allow_html=True)
                    
                    # Toggle selection
                    if rec['tool'] in st.session_state.selected_activities:
                        if st.button(f"Remove from Mix", key=f"remove_{rec['tool']}", use_container_width=True):
                            st.session_state.selected_activities.remove(rec['tool'])
                            st.rerun()
                    else:
                        if st.button(f"Add to Mix", key=f"add_{rec['tool']}", type="primary", use_container_width=True):
                            st.session_state.selected_activities.append(rec['tool'])
                            st.rerun()
                    
                    # Design resources
                    if rec['resources']:
                        st.markdown("---")
                        st.markdown("**🎨 Design Resources:**")
                        for resource in rec['resources']:
                            cols = st.columns([1, 4, 1])
                            with cols[0]:
                                st.markdown(f"{resource['icon']}")
                            with cols[1]:
                                st.markdown(f"**{resource['name']}** - {resource['desc']}")
                            with cols[2]:
                                st.link_button("Open", resource['url'], use_container_width=True)
            
            # Selected activities summary
            if st.session_state.selected_activities:
                st.markdown("---")
                st.success("### 🎯 Your Selected Promotion Mix")
                
                cols = st.columns(3)
                for i, activity in enumerate(st.session_state.selected_activities):
                    with cols[i % 3]:
                        st.markdown(f"**{i+1}.** {activity}")
                
                st.markdown("---")
                cols = st.columns(2)
                with cols[0]:
                    if st.button("📄 Export as PDF", use_container_width=True):
                        st.info("PDF export functionality coming soon!")
                with cols[1]:
                    if st.button("✉️ Share via Email", use_container_width=True):
                        st.info("Email sharing functionality coming soon!")
            
            # Pro tip
            st.markdown("---")
            st.warning("**💡 Pro Tip:** Click on promotional activities to add them to your mix. Use the design resources provided to create professional marketing materials quickly and easily.")
    
    else:
        st.info("👆 Fill in the details above and click 'Generate Promotion Mix Strategy' to get recommendations.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p><strong>Marketing Strategy & Promotion Mix Tool</strong></p>
    <p>Built with Streamlit | Based on established marketing frameworks</p>
</div>
""", unsafe_allow_html=True)(f"✓ Selected: {st.session_state.competitive_forces[key]}")
    
    # Step 5: Distribution Channel
        elif st.session_state.step == 5:
        st.header("Step 5: Distribution Channel Strategy")
        st.markdown("Configure your distribution approach")
        
        st.info("**Distribution Channel Selection Framework**\n\nChoose based on product customization level and target market concentration")
        
        st.subheader("Product Customization Level")
        cols = st.columns(2)
        with cols[0]:
            if st.button("**High Customization**\n\nTailored products, bespoke services", key="cust_high", use_container_width=True):
                st.session_state.distribution_config['customization'] = 'high'
        with cols[1]:
            if st.button("**Low Customization**\n\nStandardized products, mass market", key="cust_low", use_container_width=True):
                st.session_state.distribution_config['customization'] = 'low'
        
        if st.session_state.distribution_config['customization']:
            st.success(f"✓ Selected: {st.session_state.distribution_config['customization'].title()} Customization")
        
        st.subheader("Target Market Concentration")
        cols = st.columns(2)
        with cols[0]:
            if st.button("**Concentrated Market**\n\nFew large customers, B2B, niche segments", key="market_conc", use_container_width=True):
                st.session_state.distribution_config['market_concentration'] = 'concentrated'
        with cols[1]:
            if st.button("**Fragmented Market**\n\nMany small customers, B2C, mass market", key="market_frag", use_container_width=True):
                st.session_state.distribution_config['market_concentration'] = 'fragmented'
        
        if st.session_state.distribution_config['market_concentration']:
            st.success(f"✓ Selected: {st.session_state.distribution_config['market_concentration'].title()} Market")
        
        # Show recommendation
        channel = get_distribution_recommendation()
        if channel:
            st.markdown("---")
            st.success("### 🎯 Recommended Distribution Channel")
            st.markdown(f"## {channel['name']}")
            st.markdown(f"**Model:** {channel['model']}")
            st.markdown(channel['description'])
            
            cols = st.columns(2)
            with cols[0]:
                st.markdown("**✓ Pros:**")
                for pro in channel['pros']:
                    st.markdown(f"- {pro}")
            with cols[1]:
                st.markdown("**⚠ Cons:**")
                for con in channel['cons']:
                    st.markdown(f"- {con}")
            
            st.subheader("Select Specific Channel Type")
            st.session_state.selected_channel = st.selectbox(
                "Choose a channel option:",
                [''] + channel['examples'],
                index=0 if not st.session_state.selected_channel else 
                      channel['examples'].index(st.session_state.selected_channel) + 1 
                      if st.session_state.selected_channel in channel['examples'] else 0
            )
            
            if st.session_state.selected_channel:
                if st.button("📱 Book Channel Setup via WhatsApp", use_container_width=True, type="primary"):
                    whatsapp_url = generate_whatsapp_message()
                    st.markdown(f"[Click here to open WhatsApp]({whatsapp_url})")
    
    # Step 6: Results
    elif st.session_state.step == 6:
        st.header("Complete Marketing Recommendations")
        st.markdown("Strategic recommendations based on your inputs")
        
        recommendations = get_recommendations()
        
        st.success(f"### 🎯 Core Strategy: {recommendations['strategy']}")
        
        cols = st.columns(2)
        with cols[0]:
            st.info("### 📈 Promotion Strategy")
            st.markdown(recommendations['promotion'])
        with cols[1]:
            st.info("### 💰 Pricing Strategy")
            st.markdown(recommendations['pricing'])
        
        st.info
