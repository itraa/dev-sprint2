# Enter your answrs for chapter 6 here
# Name: Aarthi Narayan


# Ex. 6.6
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    
    if len(word) <= 1: 
        return True

    if first(word) == last(word):
        return is_palindrome(middle(word))
    else:    
        return False    
        

print is_palindrome('redivider')
print is_palindrome('neon')
# Ex 6.8

def gcd(a,b):

    if b == 0:
        return a
    else:    
        return gcd(b,a % b)


print gcd(12,15)