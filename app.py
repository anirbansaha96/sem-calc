import streamlit as st

def main():
    st.title("Final Grade Required")
    sem1= st.number_input("Enter the first semester GPA - ")
    sem2= st.number_input("Enter the second semester GPA - ")
    sem3= st.number_input("Enter the third semester GPA - ")
    target= st.number_input("Enter the target CGPA - ")
    if target!=0:
        required = (target*82 - 19*sem1 - 23*sem2 - 20*sem3)/20;
        st.write("The GPA required in your fourth semester is : ", required)   
    
if __name__ == '__main__':
    main()
