from email import message_from_string
from uuid import UUID
from app.database.models.messages import Message
from app.database.repositories.session_repository import SessionRepository
from app.database.repositories.message_repository import MessageRepository
from app.llm.provider import LLMProvider
from app.services.session_service import SessionService


class ChatService:
    def __init__(self, session_repository: SessionRepository, message_repository: MessageRepository, llm: LLMProvider):
        self.session_repository = session_repository
        self.message_repository = message_repository
        self.llm = llm
        
    def generate_response(self, session_id: UUID, prompt: str) -> str:
        # Generate a response using the LLM
        response = self.llm.generate(prompt)
        message = Message(session_id=session_id, content=prompt, role='user')
        self.message_repository.create(message)
        return response
    
    def get_history(self, session_id: UUID) -> list[Message]:
        # Retrieve the chat history for a given session
        messages = self.message_repository.get(session_id, 25) # Limit to the last 25 messages
        return messages
    
    def create_user_message(self, session_id: UUID, content: str) -> Message:
        # Create a new user message
        message = Message(session_id=session_id, content=content, role='user')
        self.message_repository.create(message)
        return message