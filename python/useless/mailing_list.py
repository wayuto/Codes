class MailingList:
    def __init__(self) -> None:
        self._nationality: str = None
        self._name: str = None
        self.email:str  = None
        self._mailing_list: list = []

    def get_list(self) -> list:
        for i in range(len(self._mailing_list)):
            if self._mailing_list[i][0] in "Russian":
                self._mailing_list.pop(i)
        return self._mailing_list

    def add(self, nationality: str, name: str, email: str) -> bool:
        if nationality in "Russian":
            return False
        else:
            self._mailing_list.append([nationality, name, email])
            return True

    def rem(self, email: str) -> bool:
        for i in range(len(self._mailing_list)):
            if self._mailing_list[i][2] == email or self._mailing_list[i][0] in "Russian":
                self._mailing_list.pop(i)
                return True
        return False

linus = MailingList()
linus.add("Finland", "Linus Torvalds", "torvalds@linux-foundation.org")
linus.add("Russia", "Putin", "putin@email.com")
linus.get_list()
print(linus.get_list())