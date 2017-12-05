from django import forms
from .models import Parcel


class NewTopicForm(forms.ModelForm):
    # parcel_id = forms.CharField(max_length=30)
    # description = forms.CharField(max_length=100)
    # destination = forms.CharField(max_length=100)
    # destination_address = forms.CharField()
    # sender_details = forms.ForeignKey(Sender, on_delete=forms.CASCADE)
    # receiver_details = forms.ForeignKey(Receiver, on_delete=forms.CASCADE)
    # arrival_time = forms.DateTimeField(null=True)
    # created_at = forms.DateTimeField(auto_now_add=True)
    # updated_at = forms.DateTimeField(null=True)

    class Meta:
        model = Parcel
        fields = ['parcel_id', 'description', 'destination', 'destination_address', 'sender_details', 'receiver_details', 'arrival_time', 'updated_at']