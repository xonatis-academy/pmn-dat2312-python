class LcsService:
    def extract_longest_common_sequence(self, text1: str, text2: str) -> int:
        '''
        TODO: setup memoization because it is not yet done. But the following algo is working fine.
        '''

        if text1 == '' or text2 == '':
            return 0
        else:
            result = 0
            
            first_letter_1 = text1[0]
            first_letter_2 = text2[0]
            rest1 = text1[1:]
            rest2 = text2[1:]

            if first_letter_1 == first_letter_2:
                result = 1 + self.extract_longest_common_sequence(rest1, rest2)
            else:
                possibility1 = self.extract_longest_common_sequence(text1, rest2)
                possibility2 = self.extract_longest_common_sequence(rest1, text2)
                if possibility1 > possibility2:
                    result = possibility1
                else:
                    result = possibility2

            return result