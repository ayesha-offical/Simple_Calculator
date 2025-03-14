import streamlit as st
def main():
    st.title("🧮 Simple Calculator")
    st.write("📌 Enter two numbers and choose an operation:")

    col1, col2 = st.columns(2)     
    #col1, col2 = st.columns(2) with col1: write for ui looks cool
    with col1:
        num1 = col1.number_input("✏️ First Number",value=0.0)
    with col2:
        num2 = col2.number_input("✏️ Second Number",value=0.0)
    operation = st.selectbox("⚙️ Choose Operation", ["Add (+)", "Subtract (-)", "Multiply (x)", "Divide (/)"])
    if st.button("✅ Calculate"):
        try:
            if operation == "Add +":
               result= num1+num2
               symbol="+"
            elif operation == "Subtract -": 
                result= num1-num2
                symbol="-" 
            elif operation == "Multiply x":
                result= num1*num2
                symbol="x"
            else:
                if num2  == 0:
                    st.error("❌ Cannot divide by zero!")
                    return   # return use krne se funtion stop hojata hai
                result= num1/num2
                symbol="/"

            st.success(f"{num1} {symbol} {num2} = {result}")
        except Exception as e:
             st.error(f"An error occured: {str(e)}")

# run the main function if the script is exxcuted directly             
if __name__ == "__main__":
    main()