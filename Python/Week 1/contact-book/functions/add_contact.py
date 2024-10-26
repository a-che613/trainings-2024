from contact_handlers import save_contacts

def addContacts(contacts):
  addMoreContacts = True
  addOptions = {'1': 'Save', '2': 'Add more'}
  # contacts = get_contacts();

  while addMoreContacts:
    
    # this try-exception handles validation errors, for instance "strings" in the number field
    try:
      # receive all the user inputs
      name = input('Enter the contact name: ')
      number = int(input('Enter the contact number: '))
      email = input('Enter the contact email: ')

      if not '@gmail.com' in email:
        print('Invalid email')
        raise Exception('Invalid email')
      
      contacts.append({'name': name, 'number': str(number), 'email': email})


      # end the function if the save option was selected, otherwise handle the error
      try:
        response = validateOption(contacts)

        if response['success']:
          print(response['message'])
          addMoreContacts = False

      except Exception as e:
        raise e
      # end try


    except Exception as e:
      if 'invalid literal for int()' in str(e):
        print('Please enter a valid phoneNumber e.g 654490031')
      if str(e) is 'Invalid email':
        print('Please Enter a valid email')
    # end try

def validateOption(contacts):
    option = input('Enter 1 to save or 2 to add more: ')
    if option == '1':
      
      save_contacts(contacts)
      
      return {"success": True, "message": "Contact's saved", "data": contacts}
      
    elif option == '2':
      # addContacts()
      pass
    else:
      return validateOption(contacts)
