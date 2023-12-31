
class PracticeFormPageLocators:
    # student registration form fields
    FIRST_NAME = ('id', 'firstName')
    LAST_NAME = ('id', 'lastName')
    EMAIL = ('id', 'userEmail')
    GENDERS = ('css selector', '#genterWrapper .custom-control-label')
    MOBILE = ('id', 'userNumber')
    DATE_OF_BIRTH = ('id', 'dateOfBirthInput')
    SUBJECTS = ('id', 'subjectsInput')
    HOBBIES = ('css selector', '#hobbiesWrapper .custom-control-label')
    UPLOAD_PICTURE = ('id', 'uploadPicture')
    CURRENT_ADDRESS = ('id', 'currentAddress')
    INPUT_STATE = ('id', 'react-select-3-input')
    INPUT_CITY = ('id', 'react-select-4-input')
    SUBMIT_BUTTON = ('css selector', 'button#submit')

    # result table
    RESULT_TABLE = ('css selector', 'div.table-responsive td:nth-child(2)')
