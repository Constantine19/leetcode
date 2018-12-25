def isValid(s):
    opening = ['(', '[', '{']
    closing = [')', ']', '}']

"""
Input: "()"
Output: true

Input: "()[]{}"
Output: true

Input: "(]"
Output: false

Input: "{[]}"
Output: true
"""