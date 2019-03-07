class Solution(object):
    def __init__(self):
        self.result = 0

    def recursion(self, employees, id):

        for item in employees:
            if item.id == id:
                self.result += item.importance

                if not item.subordinates:
                    return

                for j in item.subordinates:
                    self.recursion(employees, j)

    def getImportance(self, employees, id):

        self.recursion(employees, id)
        return self.result


employees = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
id = 1
print Solution().getImportance(employees, id)
