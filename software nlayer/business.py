class BusinessLogicLayer:
    def __init__(self, dal):
        self.dal = dal

    def add_book(self, title, author):
        if not title.strip() or not author.strip():
            return False, "Error: Title and author cannot be empty."

        # Business rule: unique titles
        existing = self.dal.get_books()
        for _, t, _ in existing:
            if t.lower() == title.lower():
                return False, "Error: This book already exists."

        self.dal.add_book(title, author)
        return True, "Book added successfully."

    def delete_book(self, book_id):
        self.dal.delete_book(book_id)
        return True, "Book deleted."

    def get_books(self):
        return self.dal.get_books()

    def search(self, keyword):
        return self.dal.search_books(keyword)
