#!/usr/bin/env python
# coding: utf-8

# In[8]:


import streamlit as st
import math

# Initialize session state if not already done
if "expression" not in st.session_state:
    st.session_state["expression"] = ""

# Define calculator functions
def button_click(item):
    st.session_state["expression"] += str(item)

def clear():
    st.session_state["expression"] = ""

def clear_last():
    st.session_state["expression"] = st.session_state["expression"][:-1]

def evaluate():
    try:
        # Evaluate the expression safely
        st.session_state["expression"] = str(eval(st.session_state["expression"]))
    except:
        st.error("Invalid Input")

def reciprocal():
    try:
        st.session_state["expression"] = str(1 / float(st.session_state["expression"]))
    except:
        st.error("Cannot divide by zero")

def square():
    try:
        st.session_state["expression"] = str(float(st.session_state["expression"]) ** 2)
    except:
        st.error("Invalid Input")

def square_root():
    try:
        st.session_state["expression"] = str(math.sqrt(float(st.session_state["expression"])))
    except:
        st.error("Invalid Input")

def plus_minus():
    try:
        st.session_state["expression"] = str(-1 * float(st.session_state["expression"]))
    except:
        st.error("Invalid Input")

# Display the calculator title and input field
st.title("Calculator")
st.text_input("Input", st.session_state["expression"], key="display", disabled=True)

# Define the button layout with custom labels for operations
button_labels = [
    ["%", "CE", "C", "⌫"],
    ["1/x", "x^2", "√", "/"],
    ["7", "8", "9", "MUL"],
    ["4", "5", "6", "SUB"],
    ["1", "2", "3", "ADD"],
    ["+/-", "0", ".", "="]
]

# Map labels to actions
button_functions = {
    "%": lambda: button_click("%"), "CE": clear, "C": clear, "⌫": clear_last,
    "1/x": reciprocal, "x^2": square, "√": square_root, "/": lambda: button_click("/"),
    "7": lambda: button_click("7"), "8": lambda: button_click("8"), "9": lambda: button_click("9"), "MUL": lambda: button_click("*"),
    "4": lambda: button_click("4"), "5": lambda: button_click("5"), "6": lambda: button_click("6"), "SUB": lambda: button_click("-"),
    "1": lambda: button_click("1"), "2": lambda: button_click("2"), "3": lambda: button_click("3"), "ADD": lambda: button_click("+"),
    "+/-": plus_minus, "0": lambda: button_click("0"), ".": lambda: button_click("."), "=": evaluate
}

# Render the calculator buttons
for row in button_labels:
    cols = st.columns(4)
    for i, label in enumerate(row):
        if cols[i].button(label, key=label, use_container_width=True):
            button_functions[label]()


# In[ ]:




