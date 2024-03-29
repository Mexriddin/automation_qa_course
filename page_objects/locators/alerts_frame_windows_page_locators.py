class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = ('css selector', 'button#tabButton')
    NEW_WINDOW_BUTTON = ('css selector', 'button#windowButton')
    HEADING_IN_PAGE = ('css selector', 'h1#sampleHeading')


class AlertsPageLocators:
    ALERT_BUTTON = ('css selector', 'button#alertButton')
    TIMER_ALERT_BUTTON = ('css selector', 'button#timerAlertButton')
    CONFIRM_ALERT_BUTTON = ('css selector', 'button#confirmButton')
    PROMPT_ALERT_BUTTON = ('css selector', 'button#promtButton')

    CONFIRM_RESULT = ('css selector', 'span#confirmResult')
    PROMPT_RESULT = ('css selector', 'span#promptResult')


class FramesPageLocators:
    FIRST_FRAME = ('css selector', 'iframe#frame1')
    SECOND_FRAME = ('css selector', 'iframe#frame2')
    HEADING_IN_IFRAME = ('css selector', 'h1#sampleHeading')


class NestedFramesPageLocators:
    PARENT_FRAME = ('css selector', 'iframe#frame1')
    CHILD_FRAME = ('tag name', 'iframe')
    PARENT_FRAME_TEXT = ('tag name', 'body')
    CHILD_FRAME_TEXT = ('tag name', 'p')


class ModalDialogsPageLocators:
    SMALL_MODAL_BUTTON = ('css selector', 'button#showSmallModal')
    CLOSE_SMALL_MODAL = ('css selector', 'button#closeSmallModal')
    TITLE_SMALL_MODAL = ('css selector', '.modal-title.h4')
    BODY_SMALL_MODAL = ('css selector', '.modal-body')

    LARGE_MODAL_BUTTON = ('css selector', 'button#showLargeModal')
    CLOSE_LARGE_MODAL = ('css selector', 'button#closeLargeModal')
    TITLE_LARGE_MODAL = ('css selector', '.modal-title.h4')
    BODY_LARGE_MODAL = ('css selector', '.modal-body p')
