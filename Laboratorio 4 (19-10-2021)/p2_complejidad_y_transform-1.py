# 2. What is the time complexity of this code
# def every_other(array):
#     array.each_with_index do |number,index|
#         if index.even?
#             array.each do  |other_number|
#                 puts number + other_number
#             end
#         end
#     end
# end

# Transformación de código
def every_other(array):
    for i in range(len(array)):
        if i % 2 == 0:
            for j in array:
                print(f"{array[i]} + {j} = {array[i]+j}" )

    
# Casos de prueba
array = [1,2,3]
every_other(array)

# Complejidad O(n^2)