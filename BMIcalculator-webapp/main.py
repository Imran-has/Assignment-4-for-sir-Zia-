import streamlit as st

def calculate_bmi(weight, height):
    """Calculate BMI given weight (kg) and height (m)."""
    return weight / (height ** 2)

def main():
    st.title("BMI Calculator")
    st.write("Enter your weight and height to calculate your BMI.")

    # Input fields for weight and height
    weight = st.number_input("Weight (kg)", min_value=0.0, step=0.1)
    height = st.number_input("Height (m)", min_value=0.0, step=0.01)

    if st.button("Calculate BMI"):
        if height > 0:
            bmi = calculate_bmi(weight, height)
            st.success(f"Your BMI is {bmi:.2f}")
        else:
            st.error("Height must be greater than 0.")

if __name__ == "__main__":
    main()
