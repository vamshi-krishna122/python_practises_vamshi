

# Word Count Probelm Define a function word_count(sentence) 
# that returns the top N frequent words (case-insensitive, ignore punctuation).

def word_count(sentence, N):
    sentence = sentence.lower()
    final_sentence = ""
    for i in range(len(sentence)):
        if (sentence[i]>='a' and sentence[i]<='z'):
            final_sentence += sentence[i]
        else:
            final_sentence+=" "
    
    sentence_list = final_sentence.split()
    dict_sentence = {}
    output = {}
    for i in sentence_list:
        if dict_sentence.get(i) != None:
            dict_sentence[i]+=1
        else:
            dict_sentence[i]=1
    
    for i in dict_sentence:
        if dict_sentence[i]==N:
            output[i]=N
    return output

sentence = input("Enter the Sentence : ")
N = int(input("Enter the Count : "))
print("Output : ")
print(word_count(sentence,N))

# Mini interpreter that reads a string like "5 + 2 * (3 - 1)" and evaluates it using loops, if–else, and functions.

def evaluate(s):
    stack1 = []
    stack2 = []
    idx=0
    while idx < len(s):
        if s[idx].isdigit():
            num=""
            while idx<len(s) and s[idx].isdigit():
                num += s[idx]
                idx+=1
            stack1.append(int(num))
        if s[idx] == ')':
            while stack2[-1]!='(':
                val1 = stack1.pop()
                val2 = stack1.pop()
                ans = operation(val2,val1,stack2.pop())
                stack1.append(ans)
            stack2.pop()
        elif s[idx]=='(':
            stack2.append(s[idx])
        else:
            while(len(stack2)>0 and precendence(s[idx])<=precendence(stack2[-1])):
                val1 = stack1.pop()
                val2 = stack1.pop()
                ans = operation(val2,val1,s[idx])
                stack1.append(ans)
                stack2.pop()
            stack2.append(s[idx])
        idx+=1
            
    while (len(stack2)>0):
        val1 = stack1.pop()
        val2 = stack1.pop()
        ans = operation(val2,val1,stack2.pop())
        stack1.append(ans)

    return stack1[0]

def precendence(c):
    if c=='+' or c=='-':
        return 1
    elif c=='*' or c=='/':
        return 2
    else:
        return -1
        
        
def operation(a,b,c):
    if c=="+":
        return a+b
    elif c=='-':
        return a-b
    elif c=='*':
        return a*b
    else:
        return a/b

s = input()
print(evaluate(s.replace(" ","")))




