function merge_sort(arr){
    if (arr.length <= 1)
        return arr;
    const mid = Math.floor(arr.length / 2);  
    let left = merge_sort(arr.slice(0, mid)) 
    let right = merge_sort(arr.slice(mid, arr.length)) 
    //Зливаємо дві половини
    return merge(left, right)  
}
function merge(left, right){
    let merged = [];
    let i = 0, j = 0;
    //Порівнюємо елементи і додаємо менші
    while (i < left.length && j < right.length){
        if(left[i] < right[j]){
            merged.push(left[i])
            i++
        }
        else{
            merged.push(right[j])
            j++
        }
    }
    // Додаємо залишки
    while (i < left.length) {
        merged.push(left[i]);
        i++;
    }
    while (j < right.length) {
        merged.push(right[j]);
        j++;
    }
    return merged;
}

console.log(merge_sort([38, 27, 43, 3, 9, 82, 10]));