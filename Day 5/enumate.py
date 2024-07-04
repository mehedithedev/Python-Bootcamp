filenames = ['document', 'report', 'presentation']
for index, filename in enumerate(filenames):
    capitalized_filename = filename.capitalize()
    formatted_output = f"{index} - {capitalized_filename}.txt"
    print(formatted_output)
