import streamlit as st

def sidebar():
    st.sidebar.title("Shopper Spectrum")

    with st.sidebar:

        # ----------------------------
        # LOGO
        # ----------------------------

        st.markdown(
            """
            # 🛒 Shopper Spectrum

            **Customer Intelligence Platform**
            """
        )

        st.divider()

        st.success("✔ Machine Learning Enabled")

        st.info("Dataset : Online Retail")

        st.divider()

        st.subheader("📌 Navigation")

        st.page_link(
            "pages/1_Dashboard.py",
            label="Dashboard",
            icon="📊"
        )

        st.page_link(
            "pages/2_Customer_Segmentation.py",
            label="Customer Segmentation",
            icon="👥"
        )

        st.page_link(
            "pages/3_Product_Recommendation.py",
            label="Product Recommendation",
            icon="🛍"
        )

        st.page_link(
            "pages/4_Business_Insights.py",
            label="Business Insights",
            icon="📈"
        )

        st.page_link(
            "pages/5_About.py",
            label="About",
            icon="ℹ"
        )

        st.divider()

        st.subheader("📊 Project Details")

        st.write("**Algorithm** : KMeans")

        st.write("**Recommendation** : Collaborative Filtering")

        st.write("**Framework** : Streamlit")

        st.write("**Dataset** : Online Retail")

        st.divider()

        st.caption("© 2026 Shopper Spectrum")