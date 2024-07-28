import streamlit as st
import math
import pandas as pd
import numpy as np
st.title('SPHERE CALCULATION')
number = st.number_input("Insert a number")
def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume
def sphere_surface_area(radius):
    surface_area = 4 * math.pi * (radius ** 2)
    return surface_area
def main():
    st.title('SPHERE CALCULATION')
    number = st.number_input("Insert a number")
if st.button("Calculate"):
    vol = sphere_volume(number)
    area = sphere_surface_area(number)
    st.write("The volume is ", vol)
    st.write("The area  is ", area)  

