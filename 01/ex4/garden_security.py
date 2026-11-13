"""
Exercise4
ft_garden_security

Directory: ex4/
Files to Submit: ft_garden_security.py
Authorized: print(), range(), round()

The garden manager is concerned about data integrity. Some volunteers accidentally
corrupted plant data by setting invalid values (negative heights, impossible ages). You
need to create a secure system that protects and encapsulates sensitive data.
Requirements:
• Improve your Plant class in order to protect its data from corruption
• Provide controlled ways to modify plant data: set_height(), set_age()
• Provide safe ways to access plant data: get_height(), get_age()
• Ensure plant height cannot be negative through validation
• Ensure plant age cannot be negative through validation
• Print error messages from the class when invalid values are provided, leaving data
unchanged or creating the plant with default values
• Use encapsulation: prevent your class attributes from being used directly by using
the “protected” convention (not the mangling)

Consider how you might create a system that validates data before storing it, ensuring
data integrity.

15

Code Cultivation Object-Oriented Garden Systems

Example:
$> python3 ft_garden_security.py
=== Garden Security System ===
Plant created: Rose: 15.0cm, 10 days old
Height updated: 25cm
Age updated: 30 days
Rose: Error, height can't be negative
Height update rejected
Rose: Error, age can't be negative
Age update rejected
"""