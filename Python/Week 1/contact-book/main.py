
from contact_handlers import save_contacts, get_contacts, update_contact, delete_contact

from functions.add_contact import addContacts
from functions.delete_contact import deleteContact
from functions.update_contact import updateContact


all_contacts = get_contacts()
print(f'###### These are your contacts ###### \n {all_contacts}')

print('++++++++++++++++++++++++++++++++++')
print('+++++++++++ PHONE BOOK +++++++++++')
print('++++++++++++++++++++++++++++++++++')
print('Enter 1 to add contacts\nEnter 2 to delete a contact and\nEnter 3 to update a contact')

def getOption():
  option = input('Which option do you choose? (enter a valid option): ')

  if option == '1':
    addContacts(all_contacts)
  elif option == '2':
    deleteContact()
  elif option == '3':
    updateContact(all_contacts)
  else:
    getOption()


getOption()









# deleteContact()

# updateContact(all_contacts)