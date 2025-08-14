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
        ge=0.0,
        le=1.0,
        description=(
            "Confidence score for your classification of Ticket Urgency and Customer Sentiment of the ticket. "
            "Must always be a float between 0.0 and 1.0 (never None). "
            "Example: 0.85 means high confidence, 0.0 means no confidence."
        )
    )

    contain_PII_info: float = Field(
        ge=0.0,
        le=1.0,
        description=(
            "Score indicating the likelihood that the ticket contains Personal Identifiable Information (PII). "
            "Must always be a float between 0.0 (no PII present) and 1.0 (definitely contains PII, such as names, addresses, or social security numbers). "
            "Never return None. Example: 0.85 means high likelihood of PII, 0.0 means no PII detected."        )
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
