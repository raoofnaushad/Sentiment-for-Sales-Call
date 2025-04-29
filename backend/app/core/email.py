from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pathlib import Path
from pydantic import EmailStr
from typing import List
import os

from app.core.config import settings


email_conf = ConnectionConfig(
    MAIL_USERNAME = settings.mail_username,
    MAIL_PASSWORD = settings.mail_password,
    MAIL_FROM = settings.mail_from,
    MAIL_PORT = settings.mail_port,
    MAIL_SERVER = settings.mail_server,
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True
)

async def send_report_email(email_to: str, full_name: str, pdf_path: str):
    message = MessageSchema(
        subject="Your Health Assessment Report from AgePro",
        recipients=[email_to],
        body=f"""
        Dear {full_name},
        
        Your health assessment report has been approved and is now available. 
        Please find the attached PDF report for your records.
        
        Best regards,
        AgeProAI Team
        """,
        subtype="plain",  # Add this line
        attachments=[{
            "file": pdf_path,
            "filename": Path(pdf_path).name,
            "headers": {"Content-Type": "application/pdf"}
        }]
    )
    
    fm = FastMail(email_conf)
    await fm.send_message(message)