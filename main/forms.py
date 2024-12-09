from django import forms

class JobForm(forms.Form):
    WEIGHT_CHOICES = [(f"{i:02}", f"{i:02}") for i in range(10)]
    weight_type = forms.ChoiceField(choices=WEIGHT_CHOICES, initial="00")
    random_seed = forms.IntegerField(min_value=0, max_value=32000, initial=0)
    num_of_trys = forms.IntegerField(min_value=1, initial=1000000)
    num_of_batch_jobs = forms.IntegerField(min_value=1, initial=1)
    # best_distance_so_far = forms.CharField(
    #     label="Best Distance So Far",
    #     required=False,
    #     initial="NA",
    #     widget=forms.TextInput(attrs={'readonly': 'readonly'})
    # )
