function isPalindrome(word) {
    var len= word.length;
    if(len < 3) return false;

    word= String(word).toLowerCase();
    for(let i= 0; i < len; i++){
        if(!(word[i] === word[len - i - 1])) return false;
    }
    return true;
}

function getPalindromes(word){
    let len= word.length;
    if(len < 3) return "Must be more than 2 characters."
    word= String(word).toLowerCase();
    word= String(word).split(' ');
    let new_word = '';

    word.forEach(element => {
        new_word+= element;
    });

    if(isPalindrome(new_word)) return new_word;
    let palindrome_list= [];
    let first_half= String(new_word).substr(0, Math.floor(len / 2));
    let second_half= String(new_word).substr(Math.floor(len / 2), len);
    if(isPalindrome(first_half)) palindrome_list.push(first_half);
    if(isPalindrome(second_half)) palindrome_list.push(second_half);
    // console.log(first_half);
    // console.log(second_half);
    palindrome_list.push(selfCheck(first_half));
    palindrome_list.push(selfCheck(second_half));
    return palindrome_list;
}

function selfCheck(word){
    for(let i = 0; i < word.length-1; i++){
        for(let j = word.length; j > i; j--){
            if(word[i] == word[j]){
                if(isPalindrome(String(word).substr(i, j))){
                    return String(word).substr(i,j);
                }
            }
        }
    }
}

console.log(isPalindrome("racecar"));
console.log(isPalindrome("nn"));
console.log(getPalindromes("Hello anna"));