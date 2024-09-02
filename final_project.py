import mysql.connector
import mysql
import streamlit as st

# Establish a connection to MySQL Server

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="july"


)
mycursor=mydb.cursor()
print("Connection Established")

# Create Streamlit App

def main():
    st.title("CRUD Operations With MySQL");

    # Display Options for CRUD Operations
    option=st.sidebar.selectbox("Select an Operation",("Create","Read","Update","Delete"))
    # Perform Selected CRUD Operations
    if option=="Create":
        st.subheader("Create a Record")
        name=st.text_input("Enter Name")
        age=st.number_input("Enter age")
        if st.button("Create"):
            sql= "insert into streamlit_data(name,age) values(%s,%s)"
            val= (name,age)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Created Successfully!!!")



    elif option=="Read":
        st.subheader("Read Records")
        mycursor.execute("select * from streamlit_data")
        result = mycursor.fetchall()
        for row in result:
            st.write(row)



    elif option=="Update":
        st.subheader("Update a Record")
        age=st.number_input("Enter age",min_value=1)
        name=st.text_input("Enter New Name")

        if st.button("Update"):
            sql="update streamlit_data set name=%s where age =%s"
            val=(name,age)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Updated Successfully!!!")




    elif option=="Delete":
        st.subheader("Delete a Record")
        age=st.number_input("Enter age",min_value=1)
        if st.button("Delete"):
            sql="delete from streamlit_data where age =%s"
            val=(age,)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Deleted Successfully!!!")
if __name__ == "__main__":
    main()
