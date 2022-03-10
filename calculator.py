import divide
import add
import multiply
import substraction
operator=int((input("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")))
if operator==1:
    add.Addition()        
elif operator==2:
    substraction.substraction()        
elif operator==3:
    multiply.multiplication()        
elif operator==4:
    divide.division()        