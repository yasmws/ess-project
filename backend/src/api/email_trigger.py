import smtplib
import email.message
from fastapi import HTTPException

def send_email():
    try:    
        mail_body = """
                    coco
                    """
        
        msg = email.message.Message()
        msg["Subject"] = "Reserva confirmada"
        msg["From"] = "aurore.ltda@gmail.com"
        msg["To"] = "yasmimvitoriasilva001@gmail.com"
        password = "pol.kiuj"
        msg.add_header("Content-Type", "text/html")
        msg.set_payload(mail_body)

        s = smtplib.SMTP("smtp.gmail.com: 587")
        s.starttls()
        s.login(msg["From"], password)
        s.sendmail(msg["From"], msg["To"], msg.as_string().encode("utf-8"))

        return "Email successfully sent"

    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
