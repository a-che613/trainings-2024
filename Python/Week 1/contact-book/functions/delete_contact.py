from contact_handlers import delete_contact, save_contacts

def deleteContact():
  numberToDelete = input('Enter the number you want to delete: ' )

  response = delete_contact(numberToDelete)

  if response['success']:
    save_contacts(response['data'])
    print(response['success'])
    print(response['message'])
  else:
    print(response['success'])