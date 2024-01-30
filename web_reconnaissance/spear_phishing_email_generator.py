# spear_phishing_email.py

def craft_spear_phishing_email(target_email, payload):
    print("Crafting spear-phishing email...")
    try:
        # Example: Craft email using a template and insert payload
        email_content = f"""
        Dear {target_email},

        Please find the attached document as requested.

        Regards,
        [Your Name]
        """
        # Attach payload (e.g., malicious document) to the email
        # Example: attachment = open('malicious_document.docx', 'rb').read()

        # Send email using an SMTP library or service
        # Example: smtplib.SMTP('smtp.example.com').sendmail(sender_email, target_email, email_content)
        print("Spear-phishing email crafted and sent successfully!")
    except Exception as e:
        print(f"Error crafting spear-phishing email: {e}")

if __name__ == "__main__":
    target_email = input("Enter target email address: ")
    payload = input("Enter payload file path (e.g., malicious_document.docx): ")
    craft_spear_phishing_email(target_email, payload)
