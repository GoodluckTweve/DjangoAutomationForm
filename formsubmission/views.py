from os import name
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import EmailMessage
from django import forms



import logging

logger = logging.getLogger(__name__)  # Get logger for current module

def send_email(request):
    if request.method == 'POST':
        # ... existing processing code ...

        try:
            # Step 3: Prepare the email message body
            # ...

            EmailMessage.send()

            logger.info("Email sent successfully for form submission by %s", name)
        except Exception as e:
            logger.error("Error sending email: %s", str(e))

        # ... existing code ...

  
def index(request):
    if request.method == 'POST':
        # Get the form fields
        name = request.POST.get('full-name')
        your_email = request.POST.get('Youremail')
        tin = request.POST.get('tin')
        vrn_registered = request.POST.get('vrnRegistered')
        vrn_no = request.POST.get('vrnRegisteredNo')
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        company_email = request.POST.get('email')

        # Collect all CC emails
        cc_emails = request.POST.getlist('cc-email')

        # Handle multiple file uploads
        tin_document_files = request.FILES.getlist('tinDocument')
        tira_cert_files = request.FILES.getlist('tiraCert')
        brela_document_files = request.FILES.getlist('BrelaDocument')
        vrn_document_files = request.FILES.getlist('vrnDocument')

        # Prepare the email message body
        message = f'''
        Greetings,

        Please find below the details submitted via the Intermediary Cloud Access form:

        Broker/Agent Name: {name}
        TIN No: {tin}
        VRN Registered: {vrn_registered}
        VRN No (if registered): {vrn_no if vrn_registered == 'yes' else 'N/A'}
        Address: {address}
        Mobile Number: {mobile}
        Company Email: {company_email}

        CC Emails: {", ".join(cc_emails) if cc_emails else 'N/A'}

        Best regards,
        {name}
        '''

        # Create an email message object with CC
        email_message = EmailMessage(
            subject="Intermediary Cloud Access Submission",  # Subject of the email
            body=message,                                    # Email body
            from_email='no-reply@yourdomain.com',            # Sender's email
            to=['crdbinsurancecompany@gmail.com'],                       # Main recipient's email
            cc=[your_email] + cc_emails                      # CC to the sender's email and any additional CC emails
        )

        # Attach each uploaded file to the email
        all_files = tin_document_files + tira_cert_files + brela_document_files + vrn_document_files
        for attached_file in all_files:
            email_message.attach(attached_file.name, attached_file.read(), attached_file.content_type)

        # Send the email
        email_message.send()

        # After sending the email, render the success page
        return render(request, 'contactform/success.html')

    # If not a POST request, render the contact form
    return render(request, 'contactform/index.html')
