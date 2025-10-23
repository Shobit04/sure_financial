import re
from datetime import datetime


def clean_amount(s: str) -> str:
    """Clean and format currency amounts - works with any format"""
    if not s:
        return s
    
    # Remove whitespace and special characters
    s = s.replace('\xa0', ' ').strip()
    
    # Extract numbers with optional decimal
    # Handle formats: ₹25,340.75, Rs. 25340.75, 25,340, etc.
    s = s.replace('Rs.', '').replace('Rs', '').replace('INR', '').strip()
    
    # Extract numeric part (digits, commas, and decimal point)
    match = re.search(r'([\d,]+\.?\d*)', s)
    if match:
        amount = match.group(1)
        # Keep commas for readability
        return f"₹{amount}"
    
    return s


def parse_date(s: str) -> str:
    """Parse date from multiple formats and return ISO format"""
    if not s:
        return s
    
    s = s.strip()
    
    # Common date formats in Indian bank statements
    formats = [
        "%d %b %Y",        # 15 Oct 2025
        "%d %B %Y",        # 15 October 2025
        "%d %b, %Y",       # 15 Oct, 2025
        "%d %B, %Y",       # 15 October, 2025
        "%d-%b-%Y",        # 15-Oct-2025
        "%d-%B-%Y",        # 15-October-2025
        "%d/%m/%Y",        # 15/10/2025
        "%d-%m-%Y",        # 15-10-2025
        "%Y-%m-%d",        # 2025-10-15
        "%d.%m.%Y",        # 15.10.2025
        "%b %d, %Y",       # Oct 15, 2025
        "%B %d, %Y",       # October 15, 2025
        "%d %b,%Y",        # 15 Oct,2025 (no space before year)
        "%d %B,%Y",        # 15 October,2025
    ]
    
    for f in formats:
        try:
            d = datetime.strptime(s, f)
            return d.strftime('%Y-%m-%d')
        except Exception:
            continue
    
    # If no format matches, return original
    return s
