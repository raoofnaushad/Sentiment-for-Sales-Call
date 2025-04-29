from app.models.report import Report

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import os
from datetime import datetime


def generate_pdf(report: Report) -> str:
    # Create a directory for storing PDFs if it doesn't exist
    pdf_dir = "app/static/reports"
    os.makedirs(pdf_dir, exist_ok=True)
    
    # Generate unique filename
    filename = f"{pdf_dir}/report_{report.id}_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.pdf"
    
    # Create the PDF document
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    
    # Title
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        alignment=1,  # Center alignment
    )
    story.append(Paragraph("Agepro Health Assessment Report", title_style))
    story.append(Spacer(1, 20))
    
    # Basic Information
    basic_info = [
        ["Name:", report.name],
        ["Age:", str(report.age)],
        ["Weight:", f"{report.weight} kg"],
        ["Height:", f"{report.height} cm"],
        ["BMI:", f"{report.bmi} kg/m²"],
        ["Health Score:", f"{report.health_score}/100"],
        ["Biological Age:", f"{report.bio_age} years"],
        ["Risk Level:", report.risk_level.upper()]
    ]
    
    table = Table(basic_info, colWidths=[2.5*inch, 4*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.grey),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Times-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 12),
        ('BACKGROUND', (1, 0), (-1, -1), colors.lightgrey),
        ('TEXTCOLOR', (1, 0), (-1, -1), colors.black),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    story.append(table)
    story.append(Spacer(1, 30))
    
    # Section-wise Insights
    section_title = ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading2'],
        fontSize=18,
        spaceAfter=15
    )
    story.append(Paragraph("Detailed Insights", section_title))
    
    for insight in report.section_wise_micro_insights:
        story.append(Paragraph(f"Section: {insight['section']}", styles['Heading3']))
        story.append(Paragraph(f"Key Inputs: {', '.join(insight['inputs'])}", 
                             ParagraphStyle('Inputs', parent=styles['Normal'], textColor=colors.grey)))
        story.append(Paragraph(f"Insight: {insight['insight']}", 
                             ParagraphStyle('Content', parent=styles['Normal'], fontSize=12)))
        story.append(Paragraph(f"Recommendation: {insight['recommendation']}", 
                             ParagraphStyle('Recommendation', parent=styles['Normal'])))
        story.append(Spacer(1, 15))
    
    # Comorbidity Warnings
    if report.comorbidity_warnings:
        story.append(Paragraph("Health Risk Warnings", section_title))
        warning_style = ParagraphStyle(
            'Warning',
            parent=styles['Normal'],
            fontSize=12,
            leftIndent=20
        )
        for warning in report.comorbidity_warnings:
            story.append(Paragraph(f"• {warning}", warning_style))
        story.append(Spacer(1, 20))
    
    # Relatable Statistics
    if report.relatable_statistics:
        story.append(Paragraph("Statistical Insights", section_title))
        stats_style = ParagraphStyle(
            'Statistics',
            parent=styles['Normal'],
            fontSize=12,
            leftIndent=20
        )
        for stat in report.relatable_statistics:
            story.append(Paragraph(f"• {stat}", stats_style))
        story.append(Spacer(1, 20))
    
    # Build the PDF
    doc.build(story)
    return filename