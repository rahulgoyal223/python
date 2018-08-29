import re
import A

regex_integer_in_range=r"^[0-9]{6}$"

P='9999999'

print(bool(re.match(regex_integer_in_range,P)))

