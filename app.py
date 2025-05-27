
# import streamlit as st
# import pandas as pd

# st.title("MYSLT App Review Analysis Dashboard")

# # Load preprocessed data
# try:
#     clustered_df = pd.read_csv('clustered_requests.csv')
#     clustered_df['timestamp'] = pd.to_datetime(clustered_df['timestamp'])
# except FileNotFoundError:
#     st.error("clustered_requests.csv not found. Please ensure the file is in the correct directory.")
#     st.stop()

# # User input for year
# year_input = st.text_input("Enter a year or 'all':", "2024").strip().lower()

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

#         # Display clustered requests
#         if not filtered_df.empty:
#             n_clusters = filtered_df['cluster'].nunique()
#             for cluster in range(n_clusters):
#                 cluster_data = filtered_df[filtered_df['cluster'] == cluster]
#                 total_count = len(cluster_data)
#                 cluster_requests = cluster_data['request'].tolist()
                
                
#                 # Display all requests for this category
#                 for req in cluster_requests:
#                     st.write(f"• {req}")
                
#                 # Add some spacing between categories
#                 st.write("")
#         else:
#             st.write("No requests available after filtering.")



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
# year_input = st.text_input("Enter a year or 'all':", "2024").strip().lower()

# # Function to generate PDF content using ReportLab
# def generate_pdf_content(filtered_df, year_input):
#     buffer = BytesIO()
#     doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
#     styles = getSampleStyleSheet()
    
#     # Define custom styles
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
    
#     # Add title and metadata
#     story.append(Paragraph("MYSLT App Review Analysis Report", title_style))
#     story.append(Spacer(1, 0.2 * inch))
#     story.append(Paragraph(f"Filtered for: {'Year ' + year_input if year_input != 'all' else 'All Years'}", styles['Normal']))
#     story.append(Paragraph(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal']))
#     story.append(Spacer(1, 0.3 * inch))
    
#     # Add total requests and numbered list of requests
#     if filtered_df.empty:
#         story.append(Paragraph("No Data Available", heading_style))
#         story.append(Paragraph("No requests available after filtering.", body_style))
#     else:
#         total_requests = len(filtered_df)
#         story.append(Paragraph(f"Total Requests: {total_requests}", heading_style))
#         story.append(Spacer(1, 0.2 * inch))
#         all_requests = filtered_df['request'].tolist()
#         for i, req in enumerate(all_requests, 1):
#             # Escape special characters for safety
#             req = req.replace('<', '&lt;').replace('>', '&gt;').replace('&', '&amp;')
#             story.append(Paragraph(f"{i}. {req}", body_style))
#         story.append(Spacer(1, 0.2 * inch))
    
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

#         # Display total requests and numbered list of requests
#         if not filtered_df.empty:
#             total_requests = len(filtered_df)
#             st.subheader(f"Total Requests: {total_requests}")
#             all_requests = filtered_df['request'].tolist()
#             for i, req in enumerate(all_requests, 1):
#                 st.write(f"{i}. {req}")
#             st.write("")
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
# year_input = st.text_input("Enter a year or 'all':", "2024").strip().lower()

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
        
#         # Categorize and group requests
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

#         # Display categorized results
#         if not filtered_df.empty:
#             total_requests = len(filtered_df)
#             st.subheader(f"Total Requests: {total_requests}")
            
#             # Categorize and group requests for display
#             categorized = {}
#             for req in filtered_df['request'].tolist():
#                 category = categorize_request(req)
#                 if category not in categorized:
#                     categorized[category] = []
#                 categorized[category].append(req)
            
#             for category, requests in categorized.items():
#                 st.subheader(category)
#                 for i, req in enumerate(requests, 1):
#                     st.write(f"{i}. {req}")
#                 st.write("")
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
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from io import BytesIO
from datetime import datetime

st.title("MYSLT App Review Analysis Dashboard")

# Load preprocessed data
try:
    clustered_df = pd.read_csv('clustered_requests.csv')
    clustered_df['timestamp'] = pd.to_datetime(clustered_df['timestamp'])
except FileNotFoundError:
    st.error("clustered_requests.csv not found. Please ensure the file is in the correct directory.")
    st.stop()

# User input for year
year_input = st.text_input("Enter a year or 'all':", "2025").strip().lower()

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
def generate_pdf_content(filtered_df, year_input):
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
    story.append(Paragraph(f"Filtered for: {'Year ' + year_input if year_input != 'all' else 'All Years'}", styles['Normal']))
    story.append(Paragraph(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal']))
    story.append(Spacer(1, 0.3 * inch))
    
    if filtered_df.empty:
        story.append(Paragraph("No Data Available", heading_style))
        story.append(Paragraph("No requests available after filtering.", body_style))
    else:
        total_requests = len(filtered_df)
        story.append(Paragraph(f"Total Requests: {total_requests}", heading_style))
        story.append(Spacer(1, 0.2 * inch))
        
        categorized = {}
        for req in filtered_df['request'].tolist():
            category = categorize_request(req)
            if category not in categorized:
                categorized[category] = []
            categorized[category].append(req)
        
        for category, requests in categorized.items():
            story.append(Paragraph(category, heading_style))
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
        if year_input == 'all':
            filtered_df = clustered_df
        else:
            try:
                selected_year = int(year_input)
                filtered_df = clustered_df[clustered_df['timestamp'].dt.year == selected_year]
                if filtered_df.empty:
                    st.warning(f"No reviews found for {selected_year}.")
                    st.stop()
            except ValueError:
                st.error("Invalid year input. Please enter a valid year or 'all'.")
                st.stop()

        # Display categorized results with expanders
        if not filtered_df.empty:
            total_requests = len(filtered_df)
            st.subheader(f"Total Requests: {total_requests}")
            
            # Categorize and group requests
            categorized = {}
            for req in filtered_df['request'].tolist():
                category = categorize_request(req)
                if category not in categorized:
                    categorized[category] = []
                categorized[category].append(req)
            
            # Display each category in an expander
            for category, requests in categorized.items():
                with st.expander(category):
                    for i, req in enumerate(requests, 1):
                        st.write(f"{i}. {req}")
        else:
            st.write("No requests available after filtering.")

        # Generate PDF
        pdf_buffer = generate_pdf_content(filtered_df, year_input)
        st.download_button(
            label="Download Results as PDF",
            data=pdf_buffer,
            file_name=f"MYSLT_Review_Analysis_{year_input}.pdf",
            mime="application/pdf"
        )