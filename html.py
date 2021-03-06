class element:
    def __init__(self, text = None, subelement = None):
        self.subelement = subelement
        self.text = text
    def __str__(self):
        value = "<{}>\n".format(self.__class__.__name__)
        if self.text:
            value += "{}\n".format(self.text)
        if self.subelement:
            value += str(self.subelement)
        value += "</{}>\n".format(self.__class__.__name__)
        return value

class html(element):
    def __init__(self, text = None, subelement = None):
        super().__init__(text, subelement)
    def __str__(self):
        return super().__str__()
    
class body(element):
    def __init__(self, text = None, subelement = None):
        super().__init__(text, subelement)
    def __str__(self):
        return super().__str__()

class p(element):
    def __init__(self, text = None, subelement = None):
        super().__init__(text, subelement)
    def __str__(self):
        return super().__str__()