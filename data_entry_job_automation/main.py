from properties_finder import PropertiesFinder
from form_filler import FormFiller

# Find properties info
properties = PropertiesFinder()
properties_data = properties.get_properties_data()

# Fill out the form with the results
renting_form = FormFiller()

for data in properties_data.values():
    renting_form.fill_form(data)
