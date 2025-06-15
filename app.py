
# # import streamlit as st
# # import pandas as pd

# # st.title("MYSLT App Review Analysis Dashboard")

# # # Load preprocessed data
# # try:
# #     clustered_df = pd.read_csv('clustered_requests.csv')
# #     clustered_df['timestamp'] = pd.to_datetime(clustered_df['timestamp'])
# # except FileNotFoundError:
# #     st.error("clustered_requests.csv not found. Please ensure the file is in the correct directory.")
# #     st.stop()

# # # User input for year
# # year_input = st.text_input("Enter a year or 'all':", "2024").strip().lower()

# # # Button to trigger analysis
# # if st.button("Analyze"):
# #     with st.spinner("Processing..."):
# #         # Filter results based on user input
# #         if year_input == 'all':
# #             filtered_df = clustered_df
# #         else:
# #             try:
# #                 selected_year = int(year_input)
# #                 filtered_df = clustered_df[clustered_df['timestamp'].dt.year == selected_year]
# #                 if filtered_df.empty:
# #                     st.warning(f"No reviews found for {selected_year}.")
# #                     st.stop()
# #             except ValueError:
# #                 st.error("Invalid year input. Please enter a valid year or 'all'.")
# #                 st.stop()

# #         # Display clustered requests
# #         if not filtered_df.empty:
# #             n_clusters = filtered_df['cluster'].nunique()
# #             for cluster in range(n_clusters):
# #                 cluster_data = filtered_df[filtered_df['cluster'] == cluster]
# #                 total_count = len(cluster_data)
# #                 cluster_requests = cluster_data['request'].tolist()
                
                
# #                 # Display all requests for this category
# #                 for req in cluster_requests:
# #                     st.write(f"• {req}")
                
# #                 # Add some spacing between categories
# #                 st.write("")
# #         else:
# #             st.write("No requests available after filtering.")



# # import streamlit as st
# # import pandas as pd
# # from reportlab.lib.pagesizes import letter
# # from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
# # from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# # from reportlab.lib.units import inch
# # from io import BytesIO
# # from datetime import datetime

# # st.title("MYSLT App Review Analysis Dashboard")

# # # Load preprocessed data
# # try:
# #     clustered_df = pd.read_csv('clustered_requests.csv')
# #     clustered_df['timestamp'] = pd.to_datetime(clustered_df['timestamp'])
# # except FileNotFoundError:
# #     st.error("clustered_requests.csv not found. Please ensure the file is in the correct directory.")
# #     st.stop()

# # # User input for year
# # year_input = st.text_input("Enter a year or 'all':", "2024").strip().lower()

# # # Function to generate PDF content using ReportLab
# # def generate_pdf_content(filtered_df, year_input):
# #     buffer = BytesIO()
# #     doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
# #     styles = getSampleStyleSheet()
    
# #     # Define custom styles
# #     title_style = styles['Title']
# #     heading_style = styles['Heading2']
# #     body_style = ParagraphStyle(
# #         name='Body',
# #         parent=styles['Normal'],
# #         fontSize=10,
# #         leading=12,
# #         spaceAfter=6,
# #         bulletFontSize=10,
# #         bulletIndent=10,
# #     )
    
# #     story = []
    
# #     # Add title and metadata
# #     story.append(Paragraph("MYSLT App Review Analysis Report", title_style))
# #     story.append(Spacer(1, 0.2 * inch))
# #     story.append(Paragraph(f"Filtered for: {'Year ' + year_input if year_input != 'all' else 'All Years'}", styles['Normal']))
# #     story.append(Paragraph(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal']))
# #     story.append(Spacer(1, 0.3 * inch))
    
# #     # Add total requests and numbered list of requests
# #     if filtered_df.empty:
# #         story.append(Paragraph("No Data Available", heading_style))
# #         story.append(Paragraph("No requests available after filtering.", body_style))
# #     else:
# #         total_requests = len(filtered_df)
# #         story.append(Paragraph(f"Total Requests: {total_requests}", heading_style))
# #         story.append(Spacer(1, 0.2 * inch))
# #         all_requests = filtered_df['request'].tolist()
# #         for i, req in enumerate(all_requests, 1):
# #             # Escape special characters for safety
# #             req = req.replace('<', '&lt;').replace('>', '&gt;').replace('&', '&amp;')
# #             story.append(Paragraph(f"{i}. {req}", body_style))
# #         story.append(Spacer(1, 0.2 * inch))
    
# #     doc.build(story)
# #     buffer.seek(0)
# #     return buffer

# # # Button to trigger analysis
# # if st.button("Analyze"):
# #     with st.spinner("Processing..."):
# #         # Filter results based on user input
# #         if year_input == 'all':
# #             filtered_df = clustered_df
# #         else:
# #             try:
# #                 selected_year = int(year_input)
# #                 filtered_df = clustered_df[clustered_df['timestamp'].dt.year == selected_year]
# #                 if filtered_df.empty:
# #                     st.warning(f"No reviews found for {selected_year}.")
# #                     st.stop()
# #             except ValueError:
# #                 st.error("Invalid year input. Please enter a valid year or 'all'.")
# #                 st.stop()

# #         # Display total requests and numbered list of requests
# #         if not filtered_df.empty:
# #             total_requests = len(filtered_df)
# #             st.subheader(f"Total Requests: {total_requests}")
# #             all_requests = filtered_df['request'].tolist()
# #             for i, req in enumerate(all_requests, 1):
# #                 st.write(f"{i}. {req}")
# #             st.write("")
# #         else:
# #             st.write("No requests available after filtering.")

# #         # Generate PDF
# #         pdf_buffer = generate_pdf_content(filtered_df, year_input)
# #         st.download_button(
# #             label="Download Results as PDF",
# #             data=pdf_buffer,
# #             file_name=f"MYSLT_Review_Analysis_{year_input}.pdf",
# #             mime="application/pdf"
# #         )


# # import streamlit as st
# # import pandas as pd
# # from reportlab.lib.pagesizes import letter
# # from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
# # from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# # from reportlab.lib.units import inch
# # from io import BytesIO
# # from datetime import datetime

# # st.title("MYSLT App Review Analysis Dashboard")

# # # Load preprocessed data
# # try:
# #     clustered_df = pd.read_csv('clustered_requests.csv')
# #     clustered_df['timestamp'] = pd.to_datetime(clustered_df['timestamp'])
# # except FileNotFoundError:
# #     st.error("clustered_requests.csv not found. Please ensure the file is in the correct directory.")
# #     st.stop()

# # # User input for year
# # year_input = st.text_input("Enter a year or 'all':", "2024").strip().lower()

# # # Function to categorize requests
# # def categorize_request(request):
# #     if any(keyword in request.lower() for keyword in ['function', 'package', 'payment', 'change package']):
# #         return 'Functionality'
# #     elif any(keyword in request.lower() for keyword in ['ui', 'interface', 'progress bar', 'view remaining data']):
# #         return 'User Interface (UI)'
# #     elif any(keyword in request.lower() for keyword in ['performance', 'fastest', 'refresh', 'improve']):
# #         return 'Performance'
# #     elif any(keyword in request.lower() for keyword in ['billing', 'balance', 'steal money', 'reloading']):
# #         return 'Billing'
# #     elif any(keyword in request.lower() for keyword in ['support', 'service', 'unavailable', 'communication']):
# #         return 'Customer Support'
# #     return 'Uncategorized'

# # # Function to generate PDF content using ReportLab
# # def generate_pdf_content(filtered_df, year_input):
# #     buffer = BytesIO()
# #     doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
# #     styles = getSampleStyleSheet()
    
# #     title_style = styles['Title']
# #     heading_style = styles['Heading2']
# #     body_style = ParagraphStyle(
# #         name='Body',
# #         parent=styles['Normal'],
# #         fontSize=10,
# #         leading=12,
# #         spaceAfter=6,
# #         bulletFontSize=10,
# #         bulletIndent=10,
# #     )
    
# #     story = []
    
# #     story.append(Paragraph("MYSLT App Review Analysis Report", title_style))
# #     story.append(Spacer(1, 0.2 * inch))
# #     story.append(Paragraph(f"Filtered for: {'Year ' + year_input if year_input != 'all' else 'All Years'}", styles['Normal']))
# #     story.append(Paragraph(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal']))
# #     story.append(Spacer(1, 0.3 * inch))
    
# #     if filtered_df.empty:
# #         story.append(Paragraph("No Data Available", heading_style))
# #         story.append(Paragraph("No requests available after filtering.", body_style))
# #     else:
# #         total_requests = len(filtered_df)
# #         story.append(Paragraph(f"Total Requests: {total_requests}", heading_style))
# #         story.append(Spacer(1, 0.2 * inch))
        
# #         # Categorize and group requests
# #         categorized = {}
# #         for req in filtered_df['request'].tolist():
# #             category = categorize_request(req)
# #             if category not in categorized:
# #                 categorized[category] = []
# #             categorized[category].append(req)
        
# #         for category, requests in categorized.items():
# #             story.append(Paragraph(category, heading_style))
# #             for i, req in enumerate(requests, 1):
# #                 req = req.replace('<', '<').replace('>', '>').replace('&', '&')
# #                 story.append(Paragraph(f"{i}. {req}", body_style))
# #             story.append(Spacer(1, 0.1 * inch))
    
# #     doc.build(story)
# #     buffer.seek(0)
# #     return buffer

# # # Button to trigger analysis
# # if st.button("Analyze"):
# #     with st.spinner("Processing..."):
# #         # Filter results based on user input
# #         if year_input == 'all':
# #             filtered_df = clustered_df
# #         else:
# #             try:
# #                 selected_year = int(year_input)
# #                 filtered_df = clustered_df[clustered_df['timestamp'].dt.year == selected_year]
# #                 if filtered_df.empty:
# #                     st.warning(f"No reviews found for {selected_year}.")
# #                     st.stop()
# #             except ValueError:
# #                 st.error("Invalid year input. Please enter a valid year or 'all'.")
# #                 st.stop()

# #         # Display categorized results
# #         if not filtered_df.empty:
# #             total_requests = len(filtered_df)
# #             st.subheader(f"Total Requests: {total_requests}")
            
# #             # Categorize and group requests for display
# #             categorized = {}
# #             for req in filtered_df['request'].tolist():
# #                 category = categorize_request(req)
# #                 if category not in categorized:
# #                     categorized[category] = []
# #                 categorized[category].append(req)
            
# #             for category, requests in categorized.items():
# #                 st.subheader(category)
# #                 for i, req in enumerate(requests, 1):
# #                     st.write(f"{i}. {req}")
# #                 st.write("")
# #         else:
# #             st.write("No requests available after filtering.")

# #         # Generate PDF
# #         pdf_buffer = generate_pdf_content(filtered_df, year_input)
# #         st.download_button(
# #             label="Download Results as PDF",
# #             data=pdf_buffer,
# #             file_name=f"MYSLT_Review_Analysis_{year_input}.pdf",
# #             mime="application/pdf"
# #         )




# import streamlit as st
# import pandas as pd
# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
# from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# from reportlab.lib.units import inch
# from io import BytesIO
# from datetime import datetime

# st.title("MYSLT App Review Analysis Dashboard")

# # Load preprocessed data
# try:
#     clustered_df = pd.read_csv('clustered_requests.csv')
#     clustered_df['timestamp'] = pd.to_datetime(clustered_df['timestamp'])
# except FileNotFoundError:
#     st.error("clustered_requests.csv not found. Please ensure the file is in the correct directory.")
#     st.stop()

# # User input for year
# year_input = st.text_input("Enter a year or 'all':", "2025").strip().lower()

# # Function to categorize requests
# def categorize_request(request):
#     if any(keyword in request.lower() for keyword in ['function', 'package', 'payment', 'change package']):
#         return 'Functionality'
#     elif any(keyword in request.lower() for keyword in ['ui', 'interface', 'progress bar', 'view remaining data']):
#         return 'User Interface (UI)'
#     elif any(keyword in request.lower() for keyword in ['performance', 'fastest', 'refresh', 'improve']):
#         return 'Performance'
#     elif any(keyword in request.lower() for keyword in ['billing', 'balance', 'steal money', 'reloading']):
#         return 'Billing'
#     elif any(keyword in request.lower() for keyword in ['support', 'service', 'unavailable', 'communication']):
#         return 'Customer Support'
#     return 'Uncategorized'

# # Function to generate PDF content using ReportLab
# def generate_pdf_content(filtered_df, year_input):
#     buffer = BytesIO()
#     doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
#     styles = getSampleStyleSheet()
    
#     title_style = styles['Title']
#     heading_style = styles['Heading2']
#     body_style = ParagraphStyle(
#         name='Body',
#         parent=styles['Normal'],
#         fontSize=10,
#         leading=12,
#         spaceAfter=6,
#         bulletFontSize=10,
#         bulletIndent=10,
#     )
    
#     story = []
    
#     story.append(Paragraph("MYSLT App Review Analysis Report", title_style))
#     story.append(Spacer(1, 0.2 * inch))
#     story.append(Paragraph(f"Filtered for: {'Year ' + year_input if year_input != 'all' else 'All Years'}", styles['Normal']))
#     story.append(Paragraph(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal']))
#     story.append(Spacer(1, 0.3 * inch))
    
#     if filtered_df.empty:
#         story.append(Paragraph("No Data Available", heading_style))
#         story.append(Paragraph("No requests available after filtering.", body_style))
#     else:
#         total_requests = len(filtered_df)
#         story.append(Paragraph(f"Total Requests: {total_requests}", heading_style))
#         story.append(Spacer(1, 0.2 * inch))
        
#         categorized = {}
#         for req in filtered_df['request'].tolist():
#             category = categorize_request(req)
#             if category not in categorized:
#                 categorized[category] = []
#             categorized[category].append(req)
        
#         for category, requests in categorized.items():
#             story.append(Paragraph(category, heading_style))
#             for i, req in enumerate(requests, 1):
#                 req = req.replace('<', '<').replace('>', '>').replace('&', '&')
#                 story.append(Paragraph(f"{i}. {req}", body_style))
#             story.append(Spacer(1, 0.1 * inch))
    
#     doc.build(story)
#     buffer.seek(0)
#     return buffer

# # Button to trigger analysis
# if st.button("Analyze"):
#     with st.spinner("Processing..."):
#         # Filter results based on user input
#         if year_input == 'all':
#             filtered_df = clustered_df
#         else:
#             try:
#                 selected_year = int(year_input)
#                 filtered_df = clustered_df[clustered_df['timestamp'].dt.year == selected_year]
#                 if filtered_df.empty:
#                     st.warning(f"No reviews found for {selected_year}.")
#                     st.stop()
#             except ValueError:
#                 st.error("Invalid year input. Please enter a valid year or 'all'.")
#                 st.stop()

#         # Display categorized results with expanders
#         if not filtered_df.empty:
#             total_requests = len(filtered_df)
#             st.subheader(f"Total Requests: {total_requests}")
            
#             # Categorize and group requests
#             categorized = {}
#             for req in filtered_df['request'].tolist():
#                 category = categorize_request(req)
#                 if category not in categorized:
#                     categorized[category] = []
#                 categorized[category].append(req)
            
#             # Display each category in an expander
#             for category, requests in categorized.items():
#                 with st.expander(category):
#                     for i, req in enumerate(requests, 1):
#                         st.write(f"{i}. {req}")
#         else:
#             st.write("No requests available after filtering.")

#         # Generate PDF
#         pdf_buffer = generate_pdf_content(filtered_df, year_input)
#         st.download_button(
#             label="Download Results as PDF",
#             data=pdf_buffer,
#             file_name=f"MYSLT_Review_Analysis_{year_input}.pdf",
#             mime="application/pdf"
#         )






import streamlit as st
import pandas as pd
import plotly.express as px  # Ensure this import is present
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from io import BytesIO
from datetime import datetime
from pathlib import Path

st.title("MYSLT App Review Analysis Dashboard")

# Load data
base_path = Path.cwd()
comparison_file = base_path / 'cluster_comparison.csv'
app_files = {
    'MySLT': base_path / 'clustered_requests_MySLT.csv',
    'Mobitel': base_path / 'clustered_requests_Mobitel.csv',
    'Dialog': base_path / 'clustered_requests_Dialog.csv'
}

# Check if comparison file exists
if not comparison_file.exists():
    st.error("cluster_comparison.csv not found. Please ensure the file is in the repository.")
    st.stop()

# Load comparison data
try:
    cluster_summary = pd.read_csv(comparison_file)
except Exception as e:
    st.error(f"Error loading cluster_comparison.csv: {e}")
    st.stop()

# Load individual app data
app_data = {}
for app, file in app_files.items():
    if file.exists():
        try:
            app_data[app] = pd.read_csv(file)
            app_data[app]['timestamp'] = pd.to_datetime(app_data[app]['timestamp'])
        except Exception as e:
            st.warning(f"Error loading {app} data: {e}")
    else:
        st.warning(f"{app} data file not found: {file}")

# Sidebar filters
st.sidebar.header("Filters")
selected_apps = st.sidebar.multiselect("Select Apps", options=['MySLT', 'Mobitel', 'Dialog'], default=['MySLT', 'Mobitel', 'Dialog'])
year_input = st.sidebar.text_input("Enter a year or 'all':", "2025").strip().lower()

# Function to categorize requests
def categorize_request(request):
    if any(keyword in request.lower() for keyword in ['function', 'package', 'payment', 'change package']):
        return 'Functionality'
    elif any(keyword in request.lower() for keyword in ['ui', 'interface', 'progress bar', 'view remaining data']):
        return 'User Interface (UI)'
    elif any(keyword in request.lower() for keyword in ['performance', 'fastest', 'refresh', 'improve']):
        return 'Performance'
    elif any(keyword in request.lower() for keyword in ['billing', 'balance', 'steal money', 'reloading']):
        return 'Billing'
    elif any(keyword in request.lower() for keyword in ['support', 'service', 'unavailable', 'communication']):
        return 'Customer Support'
    return 'Uncategorized'

# Function to generate PDF content using ReportLab
def generate_pdf_content(filtered_data, year_input, selected_apps):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
    styles = getSampleStyleSheet()
    
    title_style = styles['Title']
    heading_style = styles['Heading2']
    body_style = ParagraphStyle(
        name='Body',
        parent=styles['Normal'],
        fontSize=10,
        leading=12,
        spaceAfter=6,
        bulletFontSize=10,
        bulletIndent=10,
    )
    
    story = []
    story.append(Paragraph("MYSLT App Review Analysis Report", title_style))
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph(f"Apps: {', '.join(selected_apps)}", styles['Normal']))
    story.append(Paragraph(f"Filtered for: {'Year ' + year_input if year_input != 'all' else 'All Years'}", styles['Normal']))
    story.append(Paragraph(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal']))
    story.append(Spacer(1, 0.3 * inch))
    
    total_requests = sum(len(df) for df in filtered_data.values() if not df.empty)
    if total_requests == 0:
        story.append(Paragraph("No Data Available", heading_style))
        story.append(Paragraph("No requests available after filtering.", body_style))
    else:
        story.append(Paragraph(f"Total Requests: {total_requests}", heading_style))
        story.append(Spacer(1, 0.2 * inch))
        
        for app, df in filtered_data.items():
            if not df.empty:
                story.append(Paragraph(f"{app} Requests", heading_style))
                categorized = {}
                for req in df['request'].tolist():
                    category = categorize_request(req)
                    if category not in categorized:
                        categorized[category] = []
                    categorized[category].append(req)
                
                for category, requests in categorized.items():
                    story.append(Paragraph(f"{category} ({app})", heading_style))
                    for i, req in enumerate(requests, 1):
                        req = req.replace('<', '<').replace('>', '>').replace('&', '&')
                        story.append(Paragraph(f"{i}. {req}", body_style))
                    story.append(Spacer(1, 0.1 * inch))
    
    doc.build(story)
    buffer.seek(0)
    return buffer

# Button to trigger analysis
if st.button("Analyze"):
    with st.spinner("Processing..."):
        # Filter results based on user input
        filtered_data = {}
        for app in selected_apps:
            if app in app_data:
                df = app_data[app]
                if year_input == 'all':
                    filtered_data[app] = df
                else:
                    try:
                        selected_year = int(year_input)
                        filtered_df = df[df['timestamp'].dt.year == selected_year]
                        if not filtered_df.empty:
                            filtered_data[app] = filtered_df
                        else:
                            st.warning(f"No reviews found for {selected_year} in {app}.")
                    except ValueError:
                        st.error("Invalid year input. Please enter a valid year or 'all'.")
                        st.stop()

        # Display categorized results with expanders
        if any(df.empty for df in filtered_data.values()):
            st.write("No requests available after filtering for some apps.")
        else:
            total_requests = sum(len(df) for df in filtered_data.values())
            st.subheader(f"Total Requests: {total_requests}")
            
            for app in selected_apps:
                if app in filtered_data and not filtered_data[app].empty:
                    st.subheader(f"{app} Requests")
                    categorized = {}
                    for req in filtered_data[app]['request'].tolist():
                        category = categorize_request(req)
                        if category not in categorized:
                            categorized[category] = []
                        categorized[category].append(req)
                    
                    for category, requests in categorized.items():
                        with st.expander(category):
                            for i, req in enumerate(requests, 1):
                                st.write(f"{i}. {req}")

        # Generate and offer PDF download
        if any(df.empty for df in filtered_data.values()):
            st.warning("No data to generate PDF due to filtering.")
        else:
            pdf_buffer = generate_pdf_content(filtered_data, year_input, selected_apps)
            st.download_button(
                label="Download Results as PDF",
                data=pdf_buffer,
                file_name=f"MYSLT_Review_Analysis_{'_'.join(selected_apps)}_{year_input}.pdf",
                mime="application/pdf"
            )

        # Visualization: Request count by app and cluster
        st.header("Request Count by App and Cluster")
        if not cluster_summary.empty:
            filtered_summary = cluster_summary[
                (cluster_summary['app'].isin(selected_apps)) &
                (cluster_summary['request_count'] >= 1)
            ]
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

        # Visualization: Temporal trend (simplified)
        st.header("Request Trends Over Time")
        for app in selected_apps:
            if app in filtered_data and not filtered_data[app].empty:
                df = filtered_data[app]
                df['month'] = df['timestamp'].dt.to_period('M').astype(str)
                trend = df.groupby(['month', 'cluster']).size().reset_index(name='count')
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