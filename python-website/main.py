import streamlit as st

def main():
    # Custom HTML and CSS for styling
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f2f6;
            font-family: Arial, sans-serif;
        }
        .main-title {
            color: #4CAF50;
            text-align: center;
            font-size: 2.5em;
            margin-bottom: 20px;
        }
        .section-header {
            color: #333333;
            font-size: 1.5em;
            margin-top: 20px;
        }
        .custom-button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 8px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Title with custom HTML
    st.markdown('<h1 class="main-title">Welcome to Python Website!</h1>', unsafe_allow_html=True)
    st.write("This is a simple web application built with Streamlit.")

    # Interactive Section
    st.markdown('<h2 class="section-header">Interactive Section</h2>', unsafe_allow_html=True)
    name = st.text_input("Enter your name:")
    if name:
        st.success(f"Hello, {name}! Welcome to the app.")

    # Slider Section
    st.markdown('<h2 class="section-header">Age Selector</h2>', unsafe_allow_html=True)
    age = st.slider("Select your age:", 0, 100, 25)
    st.info(f"Your selected age is: {age}")

    # Button Section
    st.markdown('<h2 class="section-header">Fun Button</h2>', unsafe_allow_html=True)
    if st.button("Click Me!"):
        st.balloons()
        st.success("You clicked the button! 🎉")

if __name__ == "__main__":
    main()