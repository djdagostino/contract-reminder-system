import logging
from datetime import datetime, timedelta
from database.services.notificationLogService import NotificationLogService
from database.services.contractDataService import ContractDataService
from database.services.reminderProcessingService import ReminderProcessingService
from database.services.contractTypeService import ContractTypeService
from database.db_connection import get_db_session
from utils.emailSenderService import send_contract_email
from utils.emailCreatorService import create_expiration_reminder_email, create_start_reminder_email, create_auto_reminder_email
from utils.utilityService import generate_reminder_date

def process_contracts():
    try:
        session = get_db_session()
        notification_service = NotificationLogService(session)
        contract_service = ContractDataService(session)
        reminder_processing_service = ReminderProcessingService(session)
        contract_type_service = ContractTypeService(session)
        
        unprocessed_results = notification_service.get_unprocessed_notifications()

        for row in unprocessed_results:
            unprocessed_contracts = contract_service.get_unprocessed_contracts(row.ContractId)
            for contract in unprocessed_contracts:
                if contract.AutoRenew == True:
                    auto_reminder_date = contract.ExpirationDate - timedelta(days=60)
                    reminder_processing_service.set_auto_reminder(auto_reminder_date, contract.ContractId)
                reminder_processing_service.set_start_reminder(contract.StartDate, contract.ContractId)
                days_before_reminder = contract_type_service.get_contract_type_days_before_reminder(contract.ContractTypeId) 
                reminder_dates = generate_reminder_date(contract.ExpirationDate, days_before_reminder)
                for reminder_date in reminder_dates:
                    reminder_processing_service.set_expiration_reminder(reminder_date, contract.ContractId)
                notification_service.mark_notification_processed(row.NotificationId)

    except Exception as e:
        logging.error(f"An error occurred in process_contracts: {e}")
        print(f"An error occurred: {e}")



def send_reminders():
    try:
        session = get_db_session()
        contract_service = ContractDataService(session)
        reminder_processing_service = ReminderProcessingService(session)
        contract_type_service = ContractTypeService(session)

        exp_unprocessed_results = reminder_processing_service.get_expiration_reminder_unprocessed_emails()
        start_unprocessed_results = reminder_processing_service.get_start_reminder_unprocessed_emails()
        auto_unprocessed_results = reminder_processing_service.get_auto_reminder_unprocessed_emails()


        for row in exp_unprocessed_results:
            exp_reminder_date = row.ExpReminderDate
            current_time = datetime.now().date()
            if row.IsExpReminderSent == 0 and exp_reminder_date <= current_time:
                unprocessed_contracts = contract_service.get_unprocessed_contracts(row.ContractID)
                for contract in unprocessed_contracts:
                    contract_type = contract_type_service.get_contract_type(contract.ContractTypeId)          
                    email_content = create_expiration_reminder_email(contract, contract_type)
                                
                    email_sent = send_contract_email(
                        recipient_email=contract_type.ContractOwnerEmail,
                        sender_email="automation@wgeld.org",  
                        contract_info=email_content["contract_info"],
                        subject=email_content["subject"],
                        body_template=email_content["body_template"],
                    )
                    if email_sent:
                        reminder_processing_service.mark_expiration_reminder_email_as_sent(row.ExpReminderId)
                        print(f"Email sent successfully to {contract_type.ContractOwner} for contract {contract.Title}")
        
        for row in start_unprocessed_results:
            start_reminder_date = row.StartReminderDate
            current_time = datetime.now().date()
            if row.IsStartReminderSent == 0 and start_reminder_date <= current_time:
                unprocessed_contracts = contract_service.get_unprocessed_contracts(row.ContractID)
                for contract in unprocessed_contracts:
                    contract_type = contract_type_service.get_contract_type(contract.ContractTypeId)
                    email_content = create_start_reminder_email(contract, contract_type)
                                
                    email_sent = send_contract_email(
                        recipient_email=contract_type.ContractOwnerEmail,
                        sender_email="automation@wgeld.org",  
                        contract_info=email_content["contract_info"],
                        subject=email_content["subject"],
                        body_template=email_content["body_template"],
                    )
                    if email_sent:
                        reminder_processing_service.mark_start_reminder_email_as_sent(row.StartReminderId)
                        print(f"Email sent successfully to {contract_type.ContractOwner} for contract {contract.Title}")
        
        for row in auto_unprocessed_results:
            auto_reminder_date = row.AutoReminderDate
            current_time = datetime.now().date()
            if row.IsAutoReminderSent == 0 and auto_reminder_date <= current_time:
                unprocessed_contracts = contract_service.get_unprocessed_contracts(row.ContractID)
                for contract in unprocessed_contracts:
                    contract_type = contract_type_service.get_contract_type(contract.ContractTypeId)
                    email_content = create_auto_reminder_email(contract, contract_type) 
                    
                    email_sent = send_contract_email(
                        recipient_email=contract_type.ContractOwnerEmail,
                        sender_email="automation@wgeld.org",  
                        contract_info=email_content["contract_info"],
                        subject=email_content["subject"],
                        body_template=email_content["body_template"],
                    )
                    if email_sent:
                        reminder_processing_service.mark_auto_reminder_email_as_sent(row.AutoReminderId)
                        print(f"Email sent successfully to {contract_type.ContractOwner} for contract {contract.Title}")
                                
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        process_contracts()
        send_reminders()
    except Exception as e:
        print(f"Error: {e}")


