class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for operation in operations:
            if operation == "+":
                record.append(int(record[len(record)-1]) + int(record[len(record)-2]))
            elif operation == "C" and record:
                record.pop()
            elif operation == "D":
                record.append(int(record[len(record)-1]) * 2)
            else:
                record.append(int(operation))
        return sum(record)