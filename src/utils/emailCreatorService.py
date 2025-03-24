
def create_expiration_reminder_email(contract, contract_type):

    subject = f"Contract Expiration Reminder: {contract.VendorName.title()} Contract Expires on {contract.ExpirationDate.strftime('%m/%d/%Y')}"
    
    body_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Contract Reminder</title>
        <style>
            body {{
                font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
                color: #333;
            }}
            .email-container {{
                max-width: 600px;
                margin: 30px auto;
                background: #ffffff;
                padding: 20px 30px;
                border: 1px solid #e0e0e0;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }}
            .header {{
                border-bottom: 3px solid #592b83;
                margin-bottom: 20px;
                padding-bottom: 10px;
            }}
            .header p {{
                color: #592b83;
                font-size: 1.1em;
                margin: 0;
            }}
            .footer {{
                border-top: 1px solid #e0e0e0;
                margin-top: 20px;
                padding-top: 10px;
                font-size: 0.9em;
                color: #777;
            }}
            ul {{
                list-style-type: none;
                padding: 0;
            }}
            li {{
                margin-bottom: 10px;
            }}
            strong {{
                color: #592b83;
            }}
            .contract-summary {{
                background-color: #f9f9f9;
                border: 1px solid #e0e0e0;
                padding: 15px;
                margin: 15px 0;
            }}
            .action-reminder {{
                color: #a0df6a;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <div class="email-container">
            <div class="header">
                <p><strong>Dear {contract_type.ContractOwner},</strong></p>
            </div>

            <p>This is a reminder regarding the following contract that requires your attention:</p>

            <ul>
                <li><strong>Contract Title:</strong> {contract.Title}</li>
                <li><strong>Vendor:</strong> {contract.VendorName.title()}</li>
                <li><strong>Contract Type:</strong> {contract_type.ContractType}</li>
                <li><strong>Contract ID:</strong> {contract.ContractNumber}</li>
                <li><strong>Expiration Date:</strong> {contract.ExpirationDate.strftime("%m/%d/%Y")}</li>
            </ul>

            <p><strong>Contract Summary:</strong></p>
            <div class="contract-summary">
                <p>{contract.ContractSummary}</p>
            </div>

            <p class="action-reminder">Please review this contract and take the necessary actions before the expiration date.</p>

            <p>Best regards,<br>
            Contract Management System</p>

            <div class="footer">
                <p>This email was sent from the Contract Management System. If you have any questions, please contact App Dev: appdev@wgeld.org.</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    contract_info = {
        "contract_id": contract.ContractId,
        "contract_type": contract_type.ContractType,
        "end_date": contract.ExpirationDate.strftime("%Y-%m-%d") if contract.ExpirationDate else "N/A",
        "title": contract.Title, 
        "manager": contract_type.ContractOwner,
        "vendor": contract.VendorName,
        "summary": contract.ContractSummary,
        "contract_type_id": contract.ContractTypeId
    }
    
    return {
        "subject": subject,
        "body_template": body_template,
        "contract_info": contract_info
    }


def create_start_reminder_email(contract, contract_type):

    subject = f"Contract Start Notification: {contract.VendorName.title()} Contract Starts on {contract.StartDate.strftime('%m/%d/%Y')}"

    body_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Contract Reminder</title>
        <style>
            body {{
                font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
                color: #333;
            }}
            .email-container {{
                max-width: 600px;
                margin: 30px auto;
                background: #ffffff;
                padding: 20px 30px;
                border: 1px solid #e0e0e0;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }}
            .header {{
                border-bottom: 3px solid #592b83;
                margin-bottom: 20px;
                padding-bottom: 10px;
            }}
            .header p {{
                color: #592b83;
                font-size: 1.1em;
                margin: 0;
            }}
            .footer {{
                border-top: 1px solid #e0e0e0;
                margin-top: 20px;
                padding-top: 10px;
                font-size: 0.9em;
                color: #777;
            }}
            ul {{
                list-style-type: none;
                padding: 0;
            }}
            li {{
                margin-bottom: 10px;
            }}
            strong {{
                color: #592b83;
            }}
            .contract-summary {{
                background-color: #f9f9f9;
                border: 1px solid #e0e0e0;
                padding: 15px;
                margin: 15px 0;
            }}
            .action-reminder {{
                color: #a0df6a;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <div class="email-container">
            <div class="header">
                <p><strong>Dear {contract_type.ContractOwner},</strong></p>
            </div>

            <p>This is a notification regarding the following contract that requires your attention:</p>

            <ul>
                <li><strong>Contract Title:</strong> {contract.Title}</li>
                <li><strong>Vendor:</strong> {contract.VendorName.title()}</li>
                <li><strong>Contract Type:</strong> {contract_type.ContractType}</li>
                <li><strong>Contract ID:</strong> {contract.ContractNumber}</li>
                <li><strong>Start Date:</strong> {contract.StartDate.strftime("%m/%d/%Y")}</li>
            </ul>

            <p><strong>Contract Summary:</strong></p>
            <div class="contract-summary">
                <p>{contract.ContractSummary}</p>
            </div>

            <p class="action-reminder">Please review this contract and ensure you are prepared for its start date.</p>

            <p>Best regards,<br>
            Contract Management System</p>

            <div class="footer">
                <p>This email was sent from the Contract Management System. If you have any questions, please contact App Dev: appdev@wgeld.org.</p>
            </div>
        </div>
    </body>
    </html>
    """
    contract_info = {   
        "contract_id": contract.ContractId,
    "contract_type": contract_type.ContractType,
        "end_date": contract.ExpirationDate.strftime("%Y-%m-%d"),
        "title": contract.Title, 
        "manager": contract_type.ContractOwner,
        "vendor": contract.VendorName,
        "summary": contract.ContractSummary,
        "contract_type_id": contract.ContractTypeId
    }
    
    return {
        "subject": subject,
        "body_template": body_template,
        "contract_info": contract_info
    }

def create_auto_reminder_email(contract, contract_type):
   
    subject = f"60-Day Contract Renewal Notice: {contract.VendorName.title()} Contract Auto-Renews on {contract.ExpirationDate.strftime('%m/%d/%Y')}"

    body_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Contract Reminder</title>
        <style>
            body {{
                font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
                color: #333;
            }}
            .email-container {{
                max-width: 600px;
                margin: 30px auto;
                background: #ffffff;
                padding: 20px 30px;
                border: 1px solid #e0e0e0;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }}
            .header {{
                border-bottom: 3px solid #592b83;
                margin-bottom: 20px;
                padding-bottom: 10px;
            }}
            .header p {{
                color: #592b83;
                font-size: 1.1em;
                margin: 0;
            }}
            .footer {{
                border-top: 1px solid #e0e0e0;
                margin-top: 20px;
                padding-top: 10px;
                font-size: 0.9em;
                color: #777;
            }}
            ul {{
                list-style-type: none;
                padding: 0;
            }}
            li {{
                margin-bottom: 10px;
            }}
            strong {{
                color: #592b83;
            }}
            .contract-summary {{
                background-color: #f9f9f9;
                border: 1px solid #e0e0e0;
                padding: 15px;
                margin: 15px 0;
            }}
            .action-reminder {{
                color: #a0df6a;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <div class="email-container">
            <div class="header">
                <p><strong>Dear {contract_type.ContractOwner},</strong></p>
            </div>

            <p>This is a notification regarding the following contract that requires your attention:</p>

            <ul>
                <li><strong>Contract Title:</strong> {contract.Title}</li>
                <li><strong>Vendor:</strong> {contract.VendorName.title()}</li>
                <li><strong>Contract Type:</strong> {contract_type.ContractType}</li>
                <li><strong>Contract ID:</strong> {contract.ContractNumber}</li>
                <li><strong>Next Auto-Renew Date:</strong> {contract.ExpirationDate.strftime("%m/%d/%Y") if contract.ExpirationDate else "N/A"}</li>
            </ul>

            <p><strong>Contract Summary:</strong></p>
            <div class="contract-summary">
                <p>{contract.ContractSummary}</p>
            </div>

            <p class="action-reminder">Please review this contract and ensure you are prepared for its upcoming auto-renew date.</p>

            <p>Best regards,<br>
            Contract Management System</p>

            <div class="footer">
                <p>This email was sent from the Contract Management System. If you have any questions, please contact App Dev: appdev@wgeld.org.</p>
            </div>
        </div>
    </body>
    </html>
    """

    contract_info = {
        "contract_id": contract.ContractId,
        "contract_type": contract_type.ContractType,
        "end_date": contract.ExpirationDate.strftime("%Y-%m-%d"),
        "title": contract.Title,
        "manager": contract_type.ContractOwner,
        "vendor": contract.VendorName,
        "summary": contract.ContractSummary,
        "contract_type_id": contract.ContractTypeId
}
    return {
        "subject": subject,
        "body_template": body_template,
        "contract_info": contract_info
    }



