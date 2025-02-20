
class Employee:
    def __init__(self, full_name, date_of_birth, address, contact_number, emergency_contact):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.address = address
        self.contact_number = contact_number
        self.emergency_contact = emergency_contact

    def to_dict(self):
        """Convert employee object to dictionary format."""
        return {
            "Full Name": self.full_name,
            "Date of Birth": self.date_of_birth,
            "Address": self.address,
            "Contact Number": self.contact_number,
            "Emergency Contact": self.emergency_contact
        }
