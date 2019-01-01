
def letterCombinations(digits):
    combs = [""]

    if not digits:
        return []

    letters = {1: "",
               2: "abc",
               3: "def",
               4: "ghi",
               5: "jkl",
               6: "mno",
               7: "pqrs",
               8: "tuv",
               9: "wxyz"}

    for digit in digits:
        new_combs = []
        for comb in combs:
            for letter in letters[int(digit)]:
                new_combs.append(comb + letter)
        combs = new_combs

    return combs


digits = "23"
print letterCombinations(digits)
