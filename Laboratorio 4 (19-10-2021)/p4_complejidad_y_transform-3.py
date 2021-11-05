# 4. What is the time complexity in term of O() "fgh" "abcdefghi"
'''
def fin_needle(needle,haystack):
    needle_index = 0
    haystack_index = 0

    while haystack_index < haystack.length:
        if needle[needle_index] == haystack[haystack_index]
            found_needle = true
             while needle_index < needle.length:
                if needle[needle_index] != haystack[haystack_index + needle_index]
                    found_needle = false
                break
            end
            needle_index += 1
            end
        return true if found_needle
        needle_index = 0
        end
        haystack_index  += 1
    end
    return false
end
'''


def fin_needle(needle,haystack):
    needle_index = 0
    haystack_index = 0

    while haystack_index < len(haystack):
        if needle[needle_index] == haystack[haystack_index]:
            found_needle = True
            while needle_index < len(needle):
                if needle[needle_index] != haystack[haystack_index + needle_index]:
                    found_needle = False
                break

            needle_index += 1

            if found_needle == True:
                return True

        needle_index = 0
        haystack_index  += 1
    return False

# Caso de prueba
needle = "fgh"
haystack = "abcdefghi"
print(fin_needle(needle,haystack))


# Complejidad O(n^2)