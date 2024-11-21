# import streamlit as st
# import pandas as pd
# import pyodbc
# import json
# import plotly.express as px
# import plotly.subplots as sp
# import matplotlib.pyplot as plt
# import numpy as np
# from streamlit_option_menu import option_menu
# import pathlib

# # # read query params
# # selected = st.query_params["first_key"]
# # print(selected)

# # Function to load CSS from the 'assets' folder
# def load_css(file_path):
#     with open(file_path) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# # Load the external CSS
# css_path = pathlib.Path("assets/styles.css")
# load_css(css_path)

# # Load the config file
# with open('config.json') as f:
#     config = json.load(f)
# connection_string = config['connection_string']

# @st.cache_data
# def getDataUsingQuery(query):
#     try:
#         conn = pyodbc.connect(connection_string)
#         df = pd.read_sql(query, conn)  
#         conn.close() 
#         return df
#     except Exception as e:
#         st.error(f"Error fetching data: {e}")
#         return pd.DataFrame() 


# query = "SELECT * FROM [HOC_Employee_Portal_v2].[dbo].[dashboard_definition] WHERE is_active=1"
# data = getDataUsingQuery(query)

# def plot_chart(chart_config, chart_data):
#         if chart_config['chart_type'] == "Line":
#             additional_args = {}
#             if 'colors' in chart_config: 
#                 additional_args['color_discrete_sequence'] = chart_config['colors']
#             fig = px.line(
#                 chart_data,
#                 x=chart_config['x_axis'],
#                 y=chart_config['y_axis'], 
#                 title=chart_config['chart_title'],
#                 # color_discrete_sequence=chart_config['colors']
#                 **additional_args
#             )

#             fig.update_layout(               
#                     xaxis=dict(
#                         title=dict(
#                             text=chart_config['xaxis_title']
#                         )
#                     ),
#                     yaxis=dict(
#                         title=dict(
#                             text= chart_config['yaxis_title']
#                         )
#                     )
#                     )
#         elif chart_config['chart_type'] == "Bar":
#             fig = px.bar(
#                 chart_data,
#                 x=chart_config['x_axis'],
#                 y=chart_config['y_axis'],  
#                 title=chart_config['chart_title'],
#                 color_discrete_sequence=chart_config['colors']
#             )
#             fig.update_layout(               
#                     xaxis=dict(
#                         title=dict(
#                             text=chart_config['xaxis_title']
#                         )
#                     ),
#                     yaxis=dict(
#                         title=dict(
#                             text= chart_config['yaxis_title']
#                         )
#                     ))
#         elif chart_config['chart_type'] == "Pie":
#             fig = px.pie(
#                 chart_data,
#                 values=chart_config['values'],
#                 names=chart_config['names'],
#                 title=chart_config['chart_title']
#             )
#         elif chart_config['chart_type'] == "Scatter":
#             additional_args = {}
#             if 'color' in chart_config: 
#                 additional_args['color'] = chart_config['color']
#             fig = px.scatter(
#                 chart_data,
#                 x=chart_config['x_axis'],
#                 y=chart_config['y_axis'],
#                 title=chart_config['chart_title'],
#                 **additional_args
#             )
#             fig.update_layout(               
#                     xaxis=dict(
#                         title=dict(
#                             text=chart_config['xaxis_title']
#                         )
#                     ),
#                     yaxis=dict(
#                         title=dict(
#                             text= chart_config['yaxis_title']
#                         )
#                     ))
#         else:
#             st.error(f"Unsupported chart type: {chart_config['chart_type']}")
#             return
        
#         st.plotly_chart(fig,use_container_width=True)

#         # st.markdown("### Data Table")
#         st.write("Table Data")
#         st.dataframe(chart_data,use_container_width=True)


# # Sidebar menu with dynamic options
# with st.sidebar:
#     if not data.empty and 'left_panel_name' in data.columns:
#         # Get unique values of 'left_panel_name'
#         unique_panels = data['left_panel_name'].dropna().unique().tolist()
#         selected = option_menu(
#             menu_title="Main Menu",
#             options= unique_panels,  
#         )
       
#         # st.query_params["first_key"]
#     else:
#         selected = option_menu(
#             menu_title="Main Menu",
#             options=[],
#         )


# if selected in unique_panels:
#     filtered_data = data[data['left_panel_name'] == selected]
    
#     if 'tab_name' in filtered_data.columns:
#         # Get unique tab names for the selected panel
#         unique_tabs = filtered_data['tab_name'].dropna().unique().tolist()
#         tab_objects = st.tabs(unique_tabs)  # Create tabs with tab names
        
#         # Add content to each tab
#         for tab_name, tab_obj in zip(unique_tabs, tab_objects):
#             with tab_obj:
#                 tab_data = filtered_data[filtered_data['tab_name'] == tab_name]
                
#                 # Execute the query for this tab
#                 if not tab_data['data_source_definition_query'].empty:
#                     query = tab_data['data_source_definition_query'].iloc[0]
#                     chart_data = getDataUsingQuery(query)

#                 # Parse and use chart configuration
#                 chart_config_json = tab_data['default_chart_definition'].iloc[0]
#                 if pd.notna(chart_config_json):  # Check if not null or NaN
#                     try:
#                         chart_config = json.loads(chart_config_json) 
#                         plot_chart(chart_config, chart_data)  

#                     except json.JSONDecodeError:
#                         st.error("Invalid JSON in chart configuration.")
#                 else:
#                     st.warning("No valid chart configuration provided for this tab.")
#     else:
#         st.write("No tabs available for the selected panel.")


import pymssql
import streamlit as st

connection = pymssql.connect(
    server='192.168.2.14',
    user='HOC_Portal_DEV_User',   
    password='P@ss123!!',
    database='HOC_Employee_Portal_V2'
)

cursor = connection.cursor()
cursor.execute('SELECT * FROM employees')
result = cursor.fetchall()
print(result)
connection.close()


st.dataframe(result)


