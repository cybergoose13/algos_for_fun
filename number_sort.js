var arr = [5,7,9,3,3,2];

function sort(arr){

    if(arr.length < 1) return 0;
    
    for(let i = 0; i < arr.length; i++){
        for(let j = i + 1; j < arr.length; j++){
            if(arr[i] > arr[j]){
                var temp = arr[j];
                arr[j] = arr[i];
                arr[i] = temp;
            }
        }
    }

    return arr;
}

console.log(sort(arr));