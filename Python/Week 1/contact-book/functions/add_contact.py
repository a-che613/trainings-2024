import re
from contact_handlers import save_contacts
addMoreContacts = True

def addContacts(contacts):
  
  while addMoreContacts:
    
      # receive all the user inputs
      
      new_contact = getUserInput()
      contacts.append(new_contact)


      # either save and exit or add more
      validateOption(contacts)



def getUserInput():
  email_regex = r'^[a-zA-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
  name = input('Enter the contact name: ')

  number = input('Enter the contact number: ')
  while not number.isnumeric():
    number = input('Enter a valid number e.g 654490031: ')

  email = input('Enter the contact email: ')
  while not re.match(email_regex, email):
    email = input('Enter a valid email e.g example@gmail.com: ')


  return {'name': name, 'number': str(number), 'email': email}


def validateOption(contacts):
    global addMoreContacts
    option = input('Enter 1 to save or 2 to add more: ')
    if option == '1':
      
      save_contacts(contacts)
      print('Contact Saved Successfully')
      addMoreContacts = False
    elif option == '2':
      # addContacts()
      pass
    else:
      return validateOption(contacts)
