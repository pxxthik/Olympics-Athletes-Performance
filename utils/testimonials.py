import streamlit as st
import utils.css as css

def show_testimonials():
    st.markdown("### ❤️ What Users Are Saying")
    css.get_testimonials_style()
    st.markdown("""
    <div class="testimonials-container">
        <div class="testimonials-track">
            <!-- Testimonials (duplicated for seamless scroll) -->
            <div class="testimonial">🤖<br><strong>Nanditha JP</strong><br><p>"Loved the LLM insights!"</p></div>
            <div class="testimonial">📊<br><strong>Mina 🇯🇵</strong><br><p>"Beautiful and clean design!"</p></div>
            <div class="testimonial">🔥<br><strong>Carlos 🇧🇷</strong><br><p>"Modular and fast. Great work!"</p></div>
            <div class="testimonial">🚀<br><strong>Emma 🇬🇧</strong><br><p>"Perfect for analysis practice."</p></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
