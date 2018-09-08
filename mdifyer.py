import sys
import os

'''md
This script can mdfy itself

'''
def mdifyer(input_script_path, output_script_path=None, language='python'):
    block_comment = {
        'python':"'''",
        'javascript': '//' #<-- i think
        # more languages coming whenever
    }[language]


    if output_script_path == None:
        output_script_path = os.path.splitext(input_script)[0]+'.md'

    ## open text file containing script
    new_text = []
    with open(input_script_path, 'r') as file:

        ## check for '''
        text = file.read()
        while text != '':
            try:
                new_text.append(text[:text.index("'''md")])
                text = text[text.index(block_comment+"md")+3:]
                new_text.append(text[:text.index(block_comment)])
                text = text[text.index(block_comment)+3:]
            except:
                new_text.append(text)
                text = ''

    ## write results to new script
    with open(output_script_path, 'w') as new_md_file:

        ## iterate though text blocks
        if new_text[0] == '': new_text = new_text[1:]
        for block in new_text:

        ## check if block starts with "md"
            # if it does, write it to text normally without the "md" string at the beginning
            if block[:2] == 'md':
                new_md_file.write(block[2:])

            # if it doesn't, code block it
            else:
                new_md_file.write('```python\n'+block+'\n```\n')

if __name__ == '__main__':
    input_script_path = 'example_script.py'
    mdifyer(input_script_path, output_script_path='README.md')




