#Read Me:
#Arithmetic Formatter formats your math equations and, with an optional input, solve them. 
#You cannot enter more than 5 problems at a time. See the main for exmample problem formats. 
#Author: Kailee Lesko.
#VERSION:1.0
def Arithmetic_Formatter(problems, show_answers=False):
    if len(problems) >5:
         return 'Error: Too many problems.'
    Formatted_problem=''
    counter=0
    for i in problems:
        problems_array= i.split()
        if problems_array[0].isnumeric()==False or  problems_array[2].isnumeric()==False :
            return 'Error: Numbers must only contain digits.'
        if (problems_array[1]!= '-' and problems_array[1] != '+'):
            return "Error: Operator must be '+' or '-'."
        if (len(problems_array[0]) >4 or len(problems_array[2]) >4):
            return 'Error: Numbers cannot be more than four digits.'
        if len(problems_array[2]) < len(problems_array[0]):
            Formatted_problem+= f"{problems_array[0].strip().ljust(2,' ').rjust(len(problems_array[0])+2,' ')}"
        else:
            Formatted_problem += f"{problems_array[0].strip().rjust(len(problems_array[2]) + 2, ' ')}"
        if counter != len(problems)-1:
            Formatted_problem+='    '
        counter+=1
    Formatted_problem+=('\n')
    counter=0
    for i in problems:
        problems_array= i.split()
        Formatted_problem+= f"{problems_array[1].strip().ljust(len(problems_array[1])+ 1,' ')}"+ f"{problems_array[2].rjust(len(problems_array[0]),' ')}"
        if counter != len(problems) - 1:
            Formatted_problem += '    '
        counter += 1
    Formatted_problem += ('\n')
    counter=0
    for i in problems:
        count=1
        problems_array = i.split()
        if len(problems_array[0]) > len(problems_array[2]):
            while count < len(problems_array[0])+3:
                Formatted_problem+=('-')
                count+=1
        else:
            while count < len(problems_array[2])+3:
                Formatted_problem+=('-')
                count+=1
        if counter != len(problems) - 1:
            Formatted_problem += '    '
        counter += 1
    counter=0

    if show_answers:
        Formatted_problem += '\n'
        for i in problems:
            problems_array = i.split()
            if problems_array[1] == '+':
                ans = int(problems_array[0]) + int(problems_array[2])
            else:
                ans = int(problems_array[0]) - int(problems_array[2])
            if len(problems_array[2]) < len(problems_array[0]):
                Formatted_problem += f"{str(ans).strip().ljust(2, ' ').rjust(len(problems_array[0]) + 2, ' ')}"
            else:
                Formatted_problem += f"{str(ans).strip().rjust(len(problems_array[2]) + 2, ' ')}"
            if counter != len(problems) - 1:
                Formatted_problem += '    '
            counter+=1

    return Formatted_problem


if __name__ == "__main__":
    # run your code here
    # sample problem without answers shown
    print(Arithmetic_Formatter(["3801 - 2", "123 + 49"]))

    #sample problem with answers shown
    print(Arithmetic_Formatter(["3801 - 2", "123 + 49"],True))
