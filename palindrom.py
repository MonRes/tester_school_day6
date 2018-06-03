def is_palindrome(text):

    for i in range(len(text) // 2):

        """ Cheks if text is a palindrome. 
        Args:
            text: string to be checked
        Return:
            True if text is a palindrome, False otherwise
        """

        text = text.lower() #zmiana zmiennej działa tylko lokalnie w funkcji
        if text[i] != text[len(text)-i-1]:
            return False
        return True

text = 'Oko'
print(is_palindrome(text))
print(text)


