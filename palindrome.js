function isPalindrome(text) {
    var leng= text.length;
    for(let i= 0; i < leng; i++){
        if(!(text[i] === text[leng - i - 1])) return false;
    }
    return true;
}

console.log(isPalindrome("racecar"));