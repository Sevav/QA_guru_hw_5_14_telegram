import os
import allure
from selene import be, have, by


@allure.title("Successful fill form")
def test_successful(setup_browser):
    browser = setup_browser

    with allure.step("Open registrations form"):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))
        browser.driver.execute_script("$('#fixedban').remove()")

    with allure.step("Fill form"):
       browser.element("#firstName").type('Sergey')
       browser.element("#lastName").type('Petrov')
       browser.element("#userEmail").type('Petrov@mail.ru')
       browser.element("[value=Male]").double_click()
       browser.element("#userNumber").type('8999777777')
       browser.element('[id=dateOfBirthInput]').click()
       browser.element('.react-datepicker__month-select').click()
       browser.element('.react-datepicker__month-select').element('[value = "9"]').click()
       browser.element('.react-datepicker__year-select').click()
       browser.element('.react-datepicker__year-select').element('[value = "1991"]').click()
       browser.element('.react-datepicker__day--019').click()
       browser.element("#subjectsInput").type('History').press_enter()
       browser.element("#hobbiesWrapper").element(by.text("Sports")).click()
       # browser.element('#uploadPicture').send_keys(os.getcwd() + '/picture.jpg')
       browser.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
       browser.element('#currentAddress').type('Moscow')
       browser.element('#state').click()
       browser.element('#react-select-3-input').set_value('NCR').press_tab()
       browser.element('#react-select-4-input').type('Delhi').press_enter()
       browser.driver.execute_script("$('footer').remove()")
       browser.driver.execute_script("$('#submit').click()")

    with allure.step("Check form results"):
       browser.element('.modal-title').should(have.text('Thanks for submitting the form'))
       browser.all('tbody tr').should(have.exact_texts('Student Name Sergey Petrov', 'Student Email Petrov@mail.ru',
                                                    'Gender Male', 'Mobile 8999777777',
                                                    'Date of Birth 19 October,1991', 'Subjects History',
                                                    'Hobbies Sports', 'Picture',
                                                    'Address Moscow', 'State and City NCR Delhi'))
    #browser.driver.execute_script("$('#closeLargeModal').click()")
