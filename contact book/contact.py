import tkinter as tk
from tkinter import messagebox, simpledialog


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        self.contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
        messagebox.showinfo("Success", "Contact added successfully!")

    def view_contacts(self):
        return self.contacts

    def search_contact(self, query):
        return [c for c in self.contacts if query.lower() in c['name'].lower() or query in c['phone']]

    def update_contact(self, name, updated_details):
        for contact in self.contacts:
            if contact['name'] == name:
                contact.update(updated_details)
                messagebox.showinfo("Success", "Contact updated successfully!")
                return True
        messagebox.showwarning("Error", "Contact not found!")
        return False

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact['name'] == name:
                self.contacts.remove(contact)
                messagebox.showinfo("Success", "Contact deleted successfully!")
                return True
        messagebox.showwarning("Error", "Contact not found!")
        return False


class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.cb = ContactBook()

        # Buttons
        tk.Button(root, text="Add Contact", command=self.add_contact).pack(pady=5)
        tk.Button(root, text="View Contacts", command=self.view_contacts).pack(pady=5)
        tk.Button(root, text="Search Contact", command=self.search_contact).pack(pady=5)
        tk.Button(root, text="Update Contact", command=self.update_contact).pack(pady=5)
        tk.Button(root, text="Delete Contact", command=self.delete_contact).pack(pady=5)

    def add_contact(self):
        name = simpledialog.askstring("Add Contact", "Enter Name:")
        phone = simpledialog.askstring("Add Contact", "Enter Phone Number:")
        email = simpledialog.askstring("Add Contact", "Enter Email:")
        address = simpledialog.askstring("Add Contact", "Enter Address:")

        if name and phone:
            self.cb.add_contact(name, phone, email, address)
        else:
            messagebox.showwarning("Error", "Name and Phone are required!")

    def view_contacts(self):
        contacts = self.cb.view_contacts()
        if contacts:
            result = "\n".join([f"{c['name']} - {c['phone']}" for c in contacts])
        else:
            result = "No contacts available."
        messagebox.showinfo("Contact List", result)

    def search_contact(self):
        query = simpledialog.askstring("Search Contact", "Enter Name or Phone Number:")
        if query:
            results = self.cb.search_contact(query)
            if results:
                result = "\n".join([f"{c['name']} - {c['phone']}" for c in results])
            else:
                result = "No matching contacts found."
            messagebox.showinfo("Search Results", result)
        else:
            messagebox.showwarning("Error", "Search query cannot be empty!")

    def update_contact(self):
        name = simpledialog.askstring("Update Contact", "Enter the Name of the Contact to Update:")
        if name:
            updated_phone = simpledialog.askstring("Update Contact", "Enter New Phone Number:")
            updated_email = simpledialog.askstring("Update Contact", "Enter New Email:")
            updated_address = simpledialog.askstring("Update Contact", "Enter New Address:")
            updated_details = {}
            if updated_phone:
                updated_details['phone'] = updated_phone
            if updated_email:
                updated_details['email'] = updated_email
            if updated_address:
                updated_details['address'] = updated_address
            self.cb.update_contact(name, updated_details)
        else:
            messagebox.showwarning("Error", "Name is required!")

    def delete_contact(self):
        name = simpledialog.askstring("Delete Contact", "Enter the Name of the Contact to Delete:")
        if name:
            self.cb.delete_contact(name)
        else:
            messagebox.showwarning("Error", "Name is required!")


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
