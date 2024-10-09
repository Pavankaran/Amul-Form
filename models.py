from django.db import models

# Create your models here.
class MyModel(models.Model):
    # Sr. No: Automatically incremented integer field
    sr_no = models.AutoField(primary_key=True)

    # Date: Automatically generated date when the record is created
    date = models.DateField(auto_now_add=True)

    # Category: Dropdown options (choices)
    CATEGORY_CHOICES = [
        ('Approval', 'Approval'),
        ('External Circular', 'External Circular'),
        ('Internal Circular', 'Internal Circular'),
        ('Inquiry', 'Inquiry'),
        ('Letters', 'Letters'),
        ('Payment Advice', 'Payment Advice'),
        ('Work Orders', 'Work Orders'),
    ]
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='Approval'  # Default category (optional)
    )

    # Remarks: Details of the entry
    remarks = models.TextField()

    # Start Date and End Date: Date fields
    start_date = models.DateField()
    end_date = models.DateField()

    # Executive Name: Dropdown options (choices)
    EXECUTIVE_CHOICES = [
        ('Account', 'Account'),
        ('Purchase', 'Purchase'),
        ('ADM', 'ADM'),
        ('GMO', 'GMO'),
        ('ISD', 'ISD'),
        ('Marketing', 'Marketing'),
        ('GRB', 'GRB'),
    ]
    executive_name = models.CharField(
        max_length=50,
        choices=EXECUTIVE_CHOICES,
        default='Account'  # Default executive (optional)
    )

    # User Box: Could be a TextField or CharField (depending on your need)
    user_box = models.CharField(max_length=255)

    # Entry Name: Name of the person who entered the record
    entry_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Sr. No: {self.sr_no} | Category: {self.category} | Executive: {self.executive_name}"
