class Solution:
    def isValid(self, s: str) -> bool:
        OpenBra = ['(','{','[']
        CloseBra = [')','}',']']
        stack_data = []
        for i in s:
            if i in CloseBra:
                tmp = stack_data.pop(-1) if len(stack_data) != 0 else None
                if tmp == OpenBra[CloseBra.index(i)]:
                    continue
                else:
                    return False
            stack_data.append(i)
        if stack_data:
            return False
        return True
