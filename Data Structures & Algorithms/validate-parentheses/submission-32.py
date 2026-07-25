class Solution:
    def isValid(self, s: str) -> bool:
        pret = sqr = crl = None
        pret_open = pret_closed = sqr_open = sqr_closed = crl_open = crl_closed = False
        list_open = []
        for bracket in s:
            if bracket == "(" :# and pret_closed:
                pret_open = True
                list_open.append("(")
            elif bracket ==")" and list_open and list_open[-1]== "(":
                pret_closed = True
                list_open.pop()
            elif bracket == "[": # and sqr_closed:
                sqr_open = True
                list_open.append("[")
            elif bracket == "]" and list_open and list_open[-1]== "[":
                sqr_closed = True
                list_open.pop()
            elif bracket == "{":
                crl_open = True
                list_open.append("{")
            elif bracket == "}"and list_open and list_open[-1]== "{":
                crl_closed = True
                list_open.pop()
            else:
                return False
        if len(list_open) != 0:
            return False
        elif pret_open and pret_closed:
            pret = True
        elif sqr_open and sqr_closed:
            sqr = True
        elif crl_open and crl_closed:
            crl = True
        if (pret and pret_open==True) or (sqr and sqr_open==True) or (crl and crl_open==True):
            return True
        else:
            return False