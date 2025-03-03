from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from database.models.ReminderHistory import ReminderHistory
from database.db_connection import get_db_session

class ReminderHistoryService:
    def __init__(self, session: Session):
        self.session = session

    def set_reminder(self,  reminder_date: datetime, contract_id: int):   
        try:
            # Raw SQL query to update the ReminderDate
            self.session.execute(
            "INSERT INTO ReminderHistory (ReminderDate, IsReminderSent, ContractID) "
            "VALUES (:reminder_date, 0, :contract_id)",
            {"reminder_date": reminder_date, "contract_id": contract_id}
            )
            self.session.execute(
                "UPDATE NotificationLog SET Processed = 1 WHERE ContractId = :contract_id",
                {"contract_id": contract_id}
            )
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise ValueError(f"Failed to update reminder date for contract with ID {contract_id}: {str(e)}")
        
    def get_unprocessed_emails(self):
        try:
            unprocessed_emails = self.session.query(ReminderHistory).filter(ReminderHistory.IsReminderSent == 0).all()
            return unprocessed_emails
        except SQLAlchemyError as e:
            raise ValueError(f"Failed to get unprocessed emails: {str(e)}")
    
    def mark_email_as_sent(self, reminder_id: int):
        try:
            self.session.query(ReminderHistory).filter(ReminderHistory.ReminderId == reminder_id).update({"IsReminderSent": 1})
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise ValueError(f"Failed to mark email as sent for contract with ID {reminder_id}: {str(e)}")
