# 3. What is the time complexity in term of O()
'''
function twoSum(array){
    for (let i = 0; i < array.length; i++) {
        for (let j = 0; j < array.length; i++) {
            if (i !== j && array[i] + array[j] === 10) {
                return true
            }
        }
    }
    return false
}
'''
# Código convertido a python
def twoSum(array):
    for i in range(len(array)):
        for j in range(len(array)): 
            # Verificación de lo tipos de variable
            if i != j and array[i] + array[j] == 10 and type(i) == type(j) and type(array[i] + array[j]) == type(10):
                # i and j mismo tipo de variable, diferentes valores en número
                return True
    return False

# Casos de prueba
array = [1,2,3,8,5]
print(twoSum(array))

# Complejidad O(n^2)