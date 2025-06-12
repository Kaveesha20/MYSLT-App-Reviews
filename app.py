# # import streamlit as st
# # import pandas as pd
# # import plotly.express as px
# # from pathlib import Path

# # # Set page config
# # st.set_page_config(page_title="Feature Request Comparison", layout="wide")

# # # Load data
# # base_path = Path('D:/Undergraduate/intern/PROJECTS/1- MYSLT review anlysis/Compare')
# # comparison_file = base_path / 'cluster_comparison.csv'
# # app_files = {
# #     'MySLT': base_path / 'clustered_requests_MySLT.csv',
# #     'Mobitel': base_path / 'clustered_requests_Mobitel.csv',
# #     'Dialog': base_path / 'clustered_requests_Dialog.csv'
# # }
# # # Check if comparison file exists
# # if not comparison_file.exists():
# #     st.error("Cluster comparison file not found. Please run the processing script first.")
# #     st.stop()

# # # Load comparison data
# # cluster_summary = pd.read_csv(comparison_file)

# # # Title
# # st.title("Feature Request Comparison: MySLT vs Competitors")

# # # Sidebar for filters
# # st.sidebar.header("Filters")
# # selected_app = st.sidebar.multiselect("Select Apps", options=['MySLT', 'Mobitel', 'Dialog'], default=['MySLT', 'Mobitel', 'Dialog'])
# # min_requests = st.sidebar.slider("Minimum Request Count", 1, int(cluster_summary['request_count'].max()), 1)

# # # Filter data
# # filtered_summary = cluster_summary[
# #     (cluster_summary['app'].isin(selected_app)) &
# #     (cluster_summary['request_count'] >= min_requests)
# # ]

# # # Cluster summary table
# # st.header("Cluster Summary")
# # st.dataframe(filtered_summary[['app', 'cluster', 'request_count', 'request_examples', 'earliest_timestamp', 'latest_timestamp']])

# # # Request count by app and cluster
# # st.header("Request Count by App and Cluster")
# # fig = px.bar(
# #     filtered_summary,
# #     x='app',
# #     y='request_count',
# #     color='cluster',
# #     title="Feature Request Counts",
# #     barmode='group'
# # )
# # st.plotly_chart(fig, use_container_width=True)

# # # Temporal trend
# # st.header("Request Trends Over Time")
# # for app in selected_app:
# #     app_file = app_files.get(app)
# #     if app_file.exists():
# #         app_df = pd.read_csv(app_file)
# #         app_df['timestamp'] = pd.to_datetime(app_df['timestamp'])
# #         app_df['month'] = app_df['timestamp'].dt.to_period('M').astype(str)
# #         trend = app_df.groupby(['month', 'cluster']).size().reset_index(name='count')
# #         fig = px.line(
# #             trend,
# #             x='month',
# #             y='count',
# #             color='cluster',
# #             title=f"Request Trends for {app}",
# #             markers=True
# #         )
# #         st.plotly_chart(fig, use_container_width=True)

# # # Detailed requests
# # st.header("Detailed Requests")
# # for app in selected_app:
# #     app_file = app_files.get(app)
# #     if app_file.exists():
# #         st.subheader(f"Requests for {app}")
# #         app_df = pd.read_csv(app_file)
# #         st.dataframe(app_df[['request', 'cluster', 'timestamp']])

# import streamlit as st
# import pandas as pd
# import plotly.express as px
# from pathlib import Path

# # Set page config
# st.set_page_config(page_title="Feature Request Comparison", layout="wide")

# # Load data
# base_path = Path('D:/Undergraduate/intern/PROJECTS/1- MYSLT review anlysis/Compare')
# comparison_file = base_path / 'cluster_comparison.csv'
# app_files = {
#     'MySLT': base_path / 'clustered_requests_MySLT.csv',
#     'Mobitel': base_path / 'clustered_requests_Mobitel.csv',
#     'Dialog': base_path / 'clustered_requests_Dialog.csv'
# }
# # Check if comparison file exists
# if not comparison_file.exists():
#     st.error("Cluster comparison file not found. Please run the processing script first.")
#     st.stop()

# # Load comparison data
# cluster_summary = pd.read_csv(comparison_file)

# # Title
# st.title("Feature Request Comparison: MySLT vs Competitors")

# # Sidebar for filters
# st.sidebar.header("Filters")
# selected_app = st.sidebar.multiselect("Select Apps", options=['MySLT', 'Mobitel', 'Dialog'], default=['MySLT', 'Mobitel', 'Dialog'])
# min_requests = st.sidebar.slider("Minimum Request Count", 1, int(cluster_summary['request_count'].max()), 1)

# # Filter data
# filtered_summary = cluster_summary[
#     (cluster_summary['app'].isin(selected_app)) &
#     (cluster_summary['request_count'] >= min_requests)
# ]

# # Cluster summary table
# st.header("Cluster Summary")
# st.dataframe(filtered_summary[['app', 'cluster', 'request_count', 'request_examples', 'earliest_timestamp', 'latest_timestamp']])

# # Request count by app and cluster
# st.header("Request Count by App and Cluster")
# fig = px.bar(
#     filtered_summary,
#     x='app',
#     y='request_count',
#     color='cluster',
#     title="Feature Request Counts",
#     barmode='group'
# )
# st.plotly_chart(fig, use_container_width=True)

# # Temporal trend
# st.header("Request Trends Over Time")
# for app in selected_app:
#     app_file = app_files.get(app)
#     if app_file.exists():
#         app_df = pd.read_csv(app_file)
#         app_df['timestamp'] = pd.to_datetime(app_df['timestamp'])
#         app_df['month'] = app_df['timestamp'].dt.to_period('M').astype(str)
#         trend = app_df.groupby(['month', 'cluster']).size().reset_index(name='count')
#         fig = px.line(
#             trend,
#             x='month',
#             y='count',
#             color='cluster',
#             title=f"Request Trends for {app}",
#             markers=True
#         )
#         st.plotly_chart(fig, use_container_width=True)

# # Detailed requests
# st.header("Detailed Requests")
# for app in selected_app:
#     app_file = app_files.get(app)
#     if app_file.exists():
#         st.subheader(f"Requests for {app}")
#         app_df = pd.read_csv(app_file)
#         st.dataframe(app_df[['request', 'cluster', 'timestamp']])



import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

  # Set page config
st.set_page_config(page_title="Feature Request Comparison", layout="wide")

     # Load data
base_path = Path.cwd()  # Use current working directory for Streamlit Cloud
comparison_file = base_path / 'cluster_comparison.csv'
app_files = {
         'MySLT': base_path / 'clustered_requests_MySLT.csv',
         'Mobitel': base_path / 'clustered_requests_Mobitel.csv',
         'Dialog': base_path / 'clustered_requests_Dialog.csv'
     }

     # Check if comparison file exists
if not comparison_file.exists():
         st.error("Cluster comparison file not found. Please ensure 'cluster_comparison.csv' is in the repository.")
         st.stop()

     # Load comparison data
try:
         cluster_summary = pd.read_csv(comparison_file)
except Exception as e:
         st.error(f"Error loading cluster_comparison.csv: {e}")
         st.stop()

     # Title
st.title("Feature Request Comparison: MySLT vs Competitors")

     # Sidebar for filters
st.sidebar.header("Filters")
selected_app = st.sidebar.multiselect("Select Apps", options=['MySLT', 'Mobitel', 'Dialog'], default=['MySLT', 'Mobitel', 'Dialog'])
min_requests = st.sidebar.slider("Minimum Request Count", 1, int(cluster_summary['request_count'].max()), 1)

     # Filter data
filtered_summary = cluster_summary[
         (cluster_summary['app'].isin(selected_app)) &
         (cluster_summary['request_count'] >= min_requests)
     ]

     # Cluster summary table
st.header("Cluster Summary")
st.dataframe(filtered_summary[['app', 'cluster', 'request_count', 'request_examples', 'earliest_timestamp', 'latest_timestamp']])

     # Request count by app and cluster
st.header("Request Count by App and Cluster")
fig = px.bar(
         filtered_summary,
         x='app',
         y='request_count',
         color='cluster',
         title="Feature Request Counts",
         barmode='group',
         color_discrete_sequence=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
     )
st.plotly_chart(fig, use_container_width=True)

     # Temporal trend
st.header("Request Trends Over Time")
for app in selected_app:
         app_file = app_files.get(app)
         if app_file.exists():
             try:
                 app_df = pd.read_csv(app_file)
                 app_df['timestamp'] = pd.to_datetime(app_df['timestamp'])
                 app_df['month'] = app_df['timestamp'].dt.to_period('M').astype(str)
                 trend = app_df.groupby(['month', 'cluster']).size().reset_index(name='count')
                 fig = px.line(
                     trend,
                     x='month',
                     y='count',
                     color='cluster',
                     title=f"Request Trends for {app}",
                     markers=True,
                     color_discrete_sequence=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
                 )
                 st.plotly_chart(fig, use_container_width=True)
             except Exception as e:
                 st.warning(f"Error processing trends for {app}: {e}")

     # Detailed requests
st.header("Detailed Requests")
for app in selected_app:
         app_file = app_files.get(app)
         if app_file.exists():
             try:
                 st.subheader(f"Requests for {app}")
                 app_df = pd.read_csv(app_file)
                 st.dataframe(app_df[['request', 'cluster', 'timestamp']])
             except Exception as e:
                 st.warning(f"Error loading requests for {app}: {e}")
     