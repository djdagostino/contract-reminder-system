from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from database.models.ReminderProcessing import ExpirationReminderProcessing, StartReminderProcessing, AutoRenewalReminderProcessing

class ReminderProcessingService:
    def __init__(self, session: Session):
        self.session = session

    def set_auto_reminder(self, auto_reminder_date: datetime, contract_id: int):   
        try:
            self.session.execute(
            "INSERT INTO AutoRenewalReminderProcessing(AutoReminderDate, IsAutoReminderSent, ContractID) "
            "VALUES (:auto_reminder_date, 0, :contract_id)",
            {"auto_reminder_date": auto_reminder_date, "contract_id": contract_id}
            )
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise ValueError(f"Failed to update reminder date for contract with ID {contract_id}: {str(e)}")
    
    def set_start_reminder(self,  reminder_date: datetime, contract_id: int):
        try:
            self.session.execute(
            "INSERT INTO StartReminderProcessing(StartReminderDate, IsStartReminderSent, ContractID) "
            "VALUES (:reminder_date, 0, :contract_id)",
            {"reminder_date": reminder_date, "contract_id": contract_id}
            )
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise ValueError(f"Failed to update reminder date for contract with ID {contract_id}: {str(e)}")


    def set_expiration_reminder(self,  reminder_date: datetime, contract_id: int):   
        try:
            # Raw SQL query to update the ReminderDate
            self.session.execute(
            "INSERT INTO ExpirationReminderProcessing(ExpReminderDate, IsExpReminderSent, ContractID) "
            "VALUES (:reminder_date, 0, :contract_id)",
            {"reminder_date": reminder_date, "contract_id": contract_id}
            )
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise ValueError(f"Failed to update reminder date for contract with ID {contract_id}: {str(e)}")
        
    def get_expiration_reminder_unprocessed_emails(self):
        try:
            unprocessed_emails = self.session.query(ExpirationReminderProcessing).filter(ExpirationReminderProcessing.IsExpReminderSent == 0).all()
            return unprocessed_emails
        except SQLAlchemyError as e:
            raise ValueError(f"Failed to get unprocessed emails: {str(e)}")
        
    def get_start_reminder_unprocessed_emails(self):
        try:
            unprocessed_emails = self.session.query(StartReminderProcessing).filter(StartReminderProcessing.IsStartReminderSent == 0).all()
            return unprocessed_emails
        except SQLAlchemyError as e:
            raise ValueError(f"Failed to get unprocessed emails: {str(e)}")
    
    def get_auto_reminder_unprocessed_emails(self):
        try:
            unprocessed_emails = self.session.query(AutoRenewalReminderProcessing).filter(AutoRenewalReminderProcessing.IsAutoReminderSent == 0).all()
            return unprocessed_emails
        except SQLAlchemyError as e:
            raise ValueError(f"Failed to get unprocessed emails: {str(e)}")
        
    def mark_expiration_reminder_email_as_sent(self, reminder_id: int):
        try:
            self.session.query(ExpirationReminderProcessing).filter(ExpirationReminderProcessing.ExpReminderId == reminder_id).update({"IsExpReminderSent": 1})
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise ValueError(f"Failed to mark email as sent for contract with ID {reminder_id}: {str(e)}")
        
    def mark_start_reminder_email_as_sent(self, reminder_id: int):
        try:
            self.session.query(StartReminderProcessing).filter(StartReminderProcessing.StartReminderId == reminder_id).update({"IsStartReminderSent": 1})
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise ValueError(f"Failed to mark start reminder email as sent for contract with ID {reminder_id}: {str(e)}")

    def mark_auto_reminder_email_as_sent(self, reminder_id: int):
        try:
            self.session.query(AutoRenewalReminderProcessing).filter(AutoRenewalReminderProcessing.AutoReminderId == reminder_id).update({"IsAutoReminderSent": 1})
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise ValueError(f"Failed to mark auto-renewal email as sent for contract with ID {reminder_id}: {str(e)}")


