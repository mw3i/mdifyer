import sys
import os

'''md
This script can mdify itself

'''
language_info = {
    'python': {
        'block_comment': ["'''", "'''"],
        'extension': '.py'
    },
    'javascript': {
        'block_comment': ["//","//"],
        'extension': '.js'
    }
}
def mdifyer(input_script_path, output_script_path=None, language='python'):
    block_comment = language_info[language]['block_comment']

    if output_script_path == None:
        output_script_path = os.path.splitext(input_script)[0]+'.md'

    ## open text file containing script
    new_text = []
    with open(input_script_path, 'r') as file:
        ## check for '''
        text = file.read()
        while text != '':
            try:
                new_text.append(text[:text.index(block_comment[0] + "md")])
                text = text[text.index(block_comment[0] + "md") + len(block_comment[0]):]
                new_text.append(text[:text.index(block_comment[1])])
                text = text[text.index(block_comment[1])+len(block_comment[1]):]
            except Exception as e:
                # raise(e)
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
                new_md_file.write('```'+language+'\n'+block+'\n```\n')



def dmdifyer(input_script_path, output_script_path=None, language='python'):
    block_comment = language_info[language]['block_comment']
    extension = language_info[language]['extension']

    if output_script_path == None:
        output_script_path = os.path.splitext(input_script)[0]+extension

    ## open text file containing script
    new_text = []
    with open(input_script_path, 'r') as file:

        ## check for '''
        text = file.read()
        while text.replace('\n','').replace('\t','').replace(' ','') != '':
            try:
                new_text.append(text[:text.index("```"+language)])
                text = text[text.index("```"+language)+3:]
                new_text.append(text[:text.index("```")])
                text = text[text.index("```")+3:]
            except:
                new_text.append(text)
                text = ''

    ## write results to new script
    with open(output_script_path, 'w') as new_script:

        ## iterate though text blocks
        if new_text[0] == '': new_text = new_text[1:]
        for block in new_text:

        ## check if block is an md code block
            # if it is, write it to text normally
            if block[:len(language)] == language:
                new_script.write(block[len(language):])

            # if it isn't, block comment it
            else:
                new_script.write(block_comment[0] + 'md\n' + block + '\n' + block_comment[1] + '\n')



if __name__ == '__main__':
    mdifyer('example_mdify_script.py', output_script_path='README.md', language='python')

    dmdifyer('README.md', output_script_path='example_dmdify_script.py', language='python')