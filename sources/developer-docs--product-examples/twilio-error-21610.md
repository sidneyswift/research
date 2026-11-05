# Documentation evidence: twilio-error-21610

Canonical URL: https://www.twilio.com/docs/api/errors/21610
Retrieved: 2026-11-05
Resolved URL: https://www.twilio.com/docs/api/errors/21610
Extraction: server-provided Markdown
Version: n/a (living page)

---

---
"@context": https://schema.org
"@type": TechArticle
"@id": https://www.twilio.com/docs/api/errors/21610#article
headline: "21610: Attempt to send to unsubscribed recipient"
url: https://www.twilio.com/docs/api/errors/21610
inLanguage: en
dateModified: 2026-03-11T18:38:39.000Z
author:
  "@type": Organization
  name: Twilio Developer Education Team
publisher:
  "@type": Organization
  name: Twilio
---

# 21610: Attempt to send to unsubscribed recipient

Log Type: APPLICATION

Log Level: ERROR

## Description

The person you are trying to message has opted out of receiving messages from your Twilio phone number, Channels sender, or Messaging Service.

You have attempted to message a 'To' number that has replied with "STOP" to one of your previous messages. You will not be able to send to the phone number specified in the 'To' parameter until the subscriber identified by the phone number has responded with "START".

Please see [this FAQ](https://support.twilio.com/hc/en-us/articles/223134027-Twilio-support-for-opt-out-keywords-SMS-STOP-filtering-) for more information about how Twilio handles opt-out and opt-in.

### Possible causes

* The end user handset has responded with "STOP" or [another opt-out keyword](https://support.twilio.com/hc/en-us/articles/223134027-Twilio-support-for-opt-out-keywords-SMS-STOP-filtering-).
* The phone number has been reassigned to a different end user recently.

### Possible solutions

* Consider removing this phone number from your list of recipients.
* Request the recipient to resubscribe to your messages by texting in "START" or [another opt-in keyword](https://support.twilio.com/hc/en-us/articles/223134027-Twilio-support-for-opt-out-keywords-SMS-STOP-filtering-) to your Twilio sender.
* Before sending messages to a recipient, ensure they have consented to receive messages from you. Please read these guidelines to understand [messaging opt-in requirements and best practices](https://www.twilio.com/blog/ctia-messaging-principles-and-best-practices).

