from contact_handlers import save_contacts, update_contact, delete_contact
isUpdating = True

def updateContact(all_contacts):
  updatedContact = {}
  
  numberToUpdate = input('Enter the number you want to update: ' )

  response = update_contact(numberToUpdate)
  

  if response['success']:
    contact = response['data']
    print(response['message'])
    while isUpdating:

      validateOption(contact, all_contacts, numberToUpdate)
    # save_contacts(response['data'])
    print(response['message'])
  else:
    print(response['message'])




def validateOption(contact, all_contacts, numberToUpdate):
    option = input('Enter 1 to update the name, 2 to update the number or 3 to update the email: ')
    match (option):
        case "1":
          # comment: 
          nameUpdate = input('Enter the new name: ')
          contact['name'] = nameUpdate
          saveAndContinue(contact, all_contacts, numberToUpdate)
        case "2":
          # comment: 
          numberUpdate = input('Enter the new number: ')
          contact['number'] = numberUpdate
          saveAndContinue(contact, all_contacts, numberToUpdate)
        case "3":
          # comment: 
          emailUpdate = input('Enter the new email: ')
          contact['email'] = emailUpdate
          saveAndContinue(contact, all_contacts, numberToUpdate)
        case _:
          print('Invalid choice')
          validateOption(contact)
      # end match



def saveAndContinue(contact, all_contacts, numberToUpdate):
  global isUpdating
  updateAnotherField = input('Will you like to update another field? (yes/no)? ')

  if(updateAnotherField.lower() == 'yes'):
    isUpdating = True
    validateOption(contact, all_contacts, numberToUpdate)
  elif updateAnotherField.lower() == 'no':
    isUpdating = False
    response = delete_contact(numberToUpdate)
    newContactList = response['data']
    newContactList.append(contact)
    save_contacts(newContactList)
  else:
    print('Invalid option')
    saveAndContinue(contact)