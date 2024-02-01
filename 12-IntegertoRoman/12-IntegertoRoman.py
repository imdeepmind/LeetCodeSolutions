            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        
        if num in mapper:
            return mapper[num]
        
        keys = list(mapper.keys())[::-1]
        roman = ""
        
        for k in keys:
            for _ in range(num // k):
                roman += mapper[k]
                num -= k
        
        return roman

3
