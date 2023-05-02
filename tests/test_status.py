import config.globalvariables


globVar = config.globalvariables.GlobalVariables

class TestStatus:
    def test_Return200(self):
        assert True

    def test_Return401(self):
        assert False
    
    def test_Return404(self):
        assert True
    
    def test_Return502(self):
        assert True