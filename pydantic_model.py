from pydantic import BaseModel, Field
from enum import Enum
from typing import List

# --------------------------------------------------------------
# Step 3: Define Pydantic data models
# --------------------------------------------------------------

"""
This code defines a structured data model for classifying customer support tickets using Pydantic and Python's Enum class. 
It specifies categories, urgency levels, customer sentiments, and other relevant information as predefined options or constrained fields. 
This structure ensures data consistency, enables automatic validation, and facilitates easy integration with AI models and other parts of a support ticket system.
"""


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


class TicketNeedToGoToToilet(str, Enum):
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
    need_to_go_to_toilet: TicketNeedToGoToToilet
    confidence: float = Field(
        ge=0, le=1, description="Confidence score for the classification"
    )
    contain_PII_info: float = Field(
        ge=0,
        le=1,
        description="Score off how much and criticality of the Personally identifiable information (PII) the ticket contains. 0.0 for none and 1.0 for social security numbers",
    )
    pii_type: Ticket_PII_Category
    key_information: List[str] = Field(
        description="List of key points extracted from the ticket"
    )
    suggested_action: str = Field(
        description="Brief suggestion for handling the ticket"
    )
