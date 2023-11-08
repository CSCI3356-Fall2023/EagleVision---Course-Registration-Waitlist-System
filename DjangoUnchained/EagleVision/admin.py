from django.contrib import admin
from django.apps import apps


# Register your models here.

def change_open_closed(desired_state):
    if desired_state.upper() != 'OPEN' and desired_state.upper() != 'CLOSED':
        return
        
    current_state = {'OPEN' : 'CLOSED', 'CLOSED' : 'OPEN'}
    search_text = f"OPEN_CLOSED = '{current_state[desired_state.upper()]}'"
    replace_text = f"OPEN_CLOSED = '{desired_state.upper()}'"

    with open(r'../DjangoUnchained/settings.py', 'r') as file:
        data = file.read()
        data = data.replace(search_text, replace_text)
    
    with open(r'../DjangoUnchained/settings.py', 'w') as file:
        file.write(data)
# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('eagle_id', 'major_1', 'major_2', 'major_3', 'minor_1', 'minor_2', 'graduation_semester')
#     search_fields = ('eagle_id', 'major_1', 'minor_1')
#     list_filter = ('graduation_semester',)

app_models = apps.get_app_config('EagleVision').get_models()

for model in app_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

