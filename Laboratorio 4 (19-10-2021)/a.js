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