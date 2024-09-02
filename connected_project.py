from mysql.connector import connect
import streamlit as st
try:
    obj=connect(user='root',password='1234',database='july',host='localhost',port=3306)
    if (obj.is_connected()):
        print('Connected')
except:
    print('unable to connect')

myc=obj.cursor()
myc.execute('select * from streamlit_data')
data=myc.fetchall()
for i in data:
    print(i)
import pandas as pd
st.title('MySQL Dataset')
df=pd.DataFrame(data)
st.write(df)

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
            myc.execute(sql,val)
            obj.commit()
            st.success("Record Created Successfully!!!")



    elif option=="Read":
        st.subheader("Read Records")
        myc.execute("select * from streamlit_data")
        result = myc.fetchall()
        for row in result:
            st.write(row)



    elif option=="Update":
        st.subheader("Update a Record")
        age=st.number_input("Enter age",min_value=1)
        name=st.text_input("Enter New Name")

        if st.button("Update"):
            sql="update streamlit_data set name=%s where age =%s"
            val=(name,age)
            myc.execute(sql,val)
            obj.commit()
            st.success("Record Updated Successfully!!!")




    elif option=="Delete":
        st.subheader("Delete a Record")
        age=st.number_input("Enter age",min_value=1)
        if st.button("Delete"):
            sql="delete from streamlit_data where age =%s"
            val=(age,)
            myc.execute(sql,val)
            obj.commit()
            st.success("Record Deleted Successfully!!!")
if __name__ == "__main__":
    main()

