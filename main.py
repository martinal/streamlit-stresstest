import sys
print("Top of main", sys.modules.get("mylib") is not None)
import streamlit as st
import mylib
st.write("Loading main", sys.modules.get("mylib") is not None)
st.write("mylib.f()", mylib.f())
print("Bottom of main", sys.modules.get("mylib") is not None)

st.write('-1')
