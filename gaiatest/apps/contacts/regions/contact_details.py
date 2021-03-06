# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from gaiatest.apps.base import Base


class ContactDetails(Base):

    _contact_name_title_locator = ('id', 'contact-name-title')
    _contact_image_locator = ('id', 'cover-img')
    _call_phone_number_button_locator = ('id', 'call-or-pick-0')
    _send_sms_button_locator = ('id', 'send-sms-button-0')
    _edit_contact_button_locator = ('id', 'edit-contact-button')
    _back_button_locator = ('id', 'details-back')

    def __init__(self, marionette):
        Base.__init__(self, marionette)
        self.wait_for_contact_details_to_load()

    @property
    def full_name(self):
        return self.marionette.find_element(*self._contact_name_title_locator).text

    @property
    def phone_number(self):
        return self.marionette.find_element(*self._call_phone_number_button_locator).text

    @property
    def image_style(self):
        return self.marionette.find_element(*self._contact_image_locator).get_attribute('style')

    def wait_for_contact_details_to_load(self):
        self.wait_for_element_displayed(*self._call_phone_number_button_locator)

    def tap_phone_number(self):
        self.marionette.tap(self.marionette.find_element(*self._call_phone_number_button_locator))
        from gaiatest.apps.phone.regions.call_screen import CallScreen
        return CallScreen(self.marionette)

    def tap_send_sms(self):
        self.marionette.tap(self.marionette.find_element(*self._send_sms_button_locator))
        # TODO: return SMS app when implemented

    def tap_edit(self):
        self.marionette.tap(self.marionette.find_element(*self._edit_contact_button_locator))
        from gaiatest.apps.contacts.regions.contact_form import EditContact
        return EditContact(self.marionette)

    def tap_back(self):
        self.marionette.tap(self.marionette.find_element(*self._back_button_locator))
        from gaiatest.apps.contacts.app import Contacts
        return Contacts(self.marionette)
