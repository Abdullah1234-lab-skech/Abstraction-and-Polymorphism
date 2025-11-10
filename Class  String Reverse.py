class String:
    def __init__(self, text): 
        self.text = text
    def reverse_string(self):
        return self.text[::-1]
user_input = input("Enter a String: ")
string_obj = String(user_input)
print("Reversed String is:", string_obj.reverse_string())
