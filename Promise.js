function job(data) {
    return new Promise(function(success, fail) {
        if(data){
            success('yes')
        }else{
            fail('no')
        }
    })
}

let promise= job(true)

promise

.then(function(data){
    console.log(data)
})

.catch(function(data){
    console.log(data)
})