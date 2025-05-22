# esempio 1
import re
text : str = "My email is lacumarchi@gmail.com"
result : list[str] = re.findall(r'/S+@/S+', text)
print(result) # Output : ['lacumarchi@gmail.com']

# esempio 2
import re
text : str = "Rome Paris"
result = re.match(r'[A-Z][a-z]+', text)
print(result.group()) # Output : 'Rome'

# esempio 3
import re
text : str = "I have 20 cats and 3 dogs"
numbers : list[str] = re.findall(r'\d+', text)
print(numbers)