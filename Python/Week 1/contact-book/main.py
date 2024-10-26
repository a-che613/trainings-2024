
from contact_handlers import save_contacts, get_contacts, update_contact, delete_contact

from functions.add_contact import addContacts
from functions.delete_contact import deleteContact
from functions.update_contact import updateContact


all_contacts = get_contacts()
keepRunning = True



def getOption():
  print("----------------------------")
  print('------- PHONE BOOK ---------')
  print("----------------------------")

  print('Enter 1 to add contacts\nEnter 2 to delete a contact\nEnter 3 to update a contact\nEnter 4 to view all contacts and\nEnter 5 to exit')
  option = input('Which option do you choose? (enter a valid option): ')

  if option == '1':
    addContacts(all_contacts)
  elif option == '2':
    deleteContact()
  elif option == '3':
    updateContact(all_contacts)
  elif option == '4':
    for contact in all_contacts:
      print("----------------------------")
      print(f"Name: {contact['name']}")
      print(f"Number: {contact['number']}")
      print(f"Email: {contact['email']}")
  elif option == '5':
    keepRunning = False
  else:
    getOption()


while keepRunning:
  getOption()









# deleteContact()

# updateContact(all_contacts)