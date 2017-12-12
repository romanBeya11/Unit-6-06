'''
Created by Roman Beya and Malcom McCarthy
Created on 12-12-17
Created for ICS3U
This program returns the 911 emergency address
'''
class Postal_Service():
	def __init__(self, full_name, city, province, address, street, postal_code):
		self.full_name = full_name
		self.city = city
		self.province = province
		self.address = address
		self.street = street
		self.postal_code = postal_code
		
	def emergency_address(self):
		self.emergency_add = self.address + ' ' + self.street
		return self.emergency_add

FULL_NAME = raw_input("Enter your full name: ")
CITY = raw_input("Enter the city in which you reside: ")
PROVINCE = raw_input("Enter the province that you live in: ")
ADDRESS = raw_input("Enter your house/apt that you live at: ")
STREET = raw_input("Enter your street name: ")
POSTAL_CODE = raw_input("Enter your postal code: ")

canada_post = Postal_Service(FULL_NAME, CITY, PROVINCE, ADDRESS, STREET, POSTAL_CODE)

print(canada_post.emergency_address())
