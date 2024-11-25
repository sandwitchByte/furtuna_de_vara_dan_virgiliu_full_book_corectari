import re

def replace_letter(file_path, target_char):
    # Open the input file in read mode
    with open(file_path, 'r') as file:
        content = file.read()

    updated_content = re.sub(r'(?<=[a-zA-Z])î(?=[a-zA-Z])', 'â', content)

    # Save the modified content to a new file
    with open('updated_' + file_path, 'w') as output_file:
        output_file.write(updated_content)

replace_letter('FDV_capitol01_cenusa.txt', 'î') 

#this little script is meant to replace î with ă, according to new grammar rules
#it does NOT consider possible exceptions (ex. 'preÎntâmpinare', 'supraÎncărcat')
#check these sort of words manually
