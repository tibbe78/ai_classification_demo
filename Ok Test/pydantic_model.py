from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from typing import List

class TicketCategory(str, Enum):
    ORDER_ISSUE = "order_issue"
    ACCOUNT_ACCESS = "account_access"
    PRODUCT_INQUIRY = "product_inquiry"
    TECHNICAL_SUPPORT = "technical_support"
    BILLING = "billing"
    OTHER = "other"

class CustomerSentiment(str, Enum):
    ANGRY = "angry"
    FRUSTRATED = "frustrated"
    NEUTRAL = "neutral"
    SATISFIED = "satisfied"

class TicketUrgency(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class Ticket_PII_Category(str, Enum):
    NONE = "no PII data"
    CUSTOMER_NAME = "customer name"
    CUSTOMER_ADDRESS = "customer address"
    SOCIAL_SECURITY_NUMBER = "social security number"
    OTHER = "other"
    UNSURE = "unsure"


class TicketClassification(BaseModel):
    category: TicketCategory
    urgency: TicketUrgency
    sentiment: CustomerSentiment
    
    confidence: float = Field(
        default=0.0,
        ge=0.0, 
        le=1.0, 
        description="Confidence score for the classification 0.0 = none and 1.0 high confidence"
    )
    
    contain_PII_info: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Score off how much and criticality of the Personally identifiable information (PII) the ticket contains. 0.0 for none and 1.0 for lots of PII data such as social security numbers",
    )
    
    pii_type: Ticket_PII_Category
    
    key_information: List[str] = Field(
        default=["N/A"],
        description="List of key points extracted from the ticket"
    )
    
    suggested_action: str = Field(
        default="N/A",
        description="Brief suggestion for handling the ticket"
    )
