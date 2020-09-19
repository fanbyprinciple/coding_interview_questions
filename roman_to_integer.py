def romanToInt( s):
        """
        :type s: str
        :rtype: int
        """
        
        rome_dict = {"I":1, "V":5,"X":10,"L":50, "C":100, "D":500, "M":1000 }

        sum = 0
        for i in range(0, len(s)-1):
            if (rome_dict[s[i]]>rome_dict[s[i+1]]):
                sum += rome_dict[s[i]]
            else :
                sum -= rome_dict[s[i]]
                sum += rome_dict[s[i+1]]
                i = i+1
            print(s[i], sum)
        sum += rome_dict[s[-1]]
        return sum
            

print(romanToInt("MCMXCIV"))