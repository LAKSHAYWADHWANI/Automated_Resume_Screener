import io
import pandas as pd
import plotly_express as px
def csv_to_excel(df):
    output = io.BytesIO()
    writer = pd.ExcelWriter(output, engine = "xlsxwriter")
    df.to_excel(writer, index = False, sheet_name = "All_results")
    writer.close()
    processed_data = output.getvalue()
    return processed_data
def score_bar_plotly(df):
    df  =df.sort_values(by  = "Score (%)", ascending =False)
    fig  = px.bar(
        df,
        x = "Name",
        y = "Score (%)",
        text = "Score (%)",
        title  = "Resume Scores"
    )
    fig.update_layout(
        xaxis_tickangle =-90,
        xaxis_title = "Candidates Name",
        yaxis_title = "Score (%)",
        uniformtext_minsize = 8,
        uniformtext_mode = 'hide'
    ) 
    fig.update_traces(texttemplate='%{text:.2s}%', textposition='outside')
    fig.update_layout(
        xaxis=dict(tickfont=dict(family='Arial Black', size=12)),
        yaxis=dict(title_font_family='Arial Black')
    )
    
    return fig