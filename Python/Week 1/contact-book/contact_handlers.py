import csv


def save_contacts(contacts):
  with open('Python/Week 1/contact-book/contacts.csv', 'w') as contacts_file:
    fieldnames = ['name', 'number', 'email']

    writer = csv.DictWriter(contacts_file, fieldnames=fieldnames, delimiter='\t')

    writer.writeheader()

    writer.writerows(contacts);


def get_contacts():
  with open('Python/Week 1/contact-book/contacts.csv', 'r') as contacts_file:
    reader = csv.DictReader(contacts_file, delimiter='\t')

    contacts = list(reader)


    return contacts


def update_contact(phoneNumber):
  with open('Python/Week 1/contact-book/contacts.csv', 'r') as contacts_file:
    reader = csv.DictReader(contacts_file, delimiter='\t')

    contacts = list(reader)

    contactToUpdate = {}
    foundContact = False

    for contact in contacts:
      if contact['number'] == phoneNumber:
        foundContact = True
        contactToUpdate = contact
        break
      else:
        foundContact = False

    return {
      "success": foundContact,
      "message": f"trying to update {contactToUpdate}" if foundContact else f"Didn't find a contact with the number {phoneNumber}",
      "data": contactToUpdate
    }


def delete_contact(phoneNumber):
  with open('Python/Week 1/contact-book/contacts.csv', 'r') as contacts_file:
    reader = csv.DictReader(contacts_file, delimiter='\t')

    contacts = list(reader)
    foundNumber = True

    for contact in contacts:
      if contact['number'] == phoneNumber:
        print(f'Deleting {contact}')
        contacts.remove(contact)
        foundNumber = True
        break
      else:
        foundNumber = False

    return {"success": foundNumber, "message": f"{phoneNumber} deleted successfully" if foundNumber else f"Didn't find a contact with the number {phoneNumber}", "data": contacts}