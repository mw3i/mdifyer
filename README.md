
# MDFYER
The `mdfyer` function transforms a python script into an 'MD' file; kinda like a Jupyter Notebook except way less sophisticated

It works by delineating a script based on "blocked comments" tagged with 'md' (see the `example script` for details)

To use, just put `md` at the beginning of your blocked comments, and anything in that comment block will be formatted as MD text.

So, your blocked comment should look something like this:
 
    ' ' 'md
    ^ except don't include spaces

    md text goes here

    ' ' '

    # python code goes here

    x = 'hi'
    print('hi')        


This README was generated by using mdifyer on the example_script.py. See below for examples about what gets mdfied and what doesnt.

---
```python


print('Test')


'''
This block comment doesn't have the 'md' tag, so it won't get mdified

'''

for i in range(10):
    print(i)


```

This comment block had the md tag, so it got mdfied.

```python



# And whatever's here will be python code
print('bye')
```
