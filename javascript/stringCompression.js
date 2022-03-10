/*
String Compression
Implement a method to perform ....
*/

const stringCompression = function (str) {
    let strArray = [];
    let count = 1;

    // Check if next letter is same
    for (let i = 0; i < str.length; i++) {
        if (str[i] === str[i + 1]) {
            count++;
        }
        else {
            strArray.push(str[i] + count);
            count = 1;
        }
    }

    // Concat letter and counts 
    let newStr = strArray.join('');

    return newStr.length < str.length ? newStr : str;
}

// Test Cases
console.log(stringCompression('aabccccaaa'), 'a2b1c4a3');
console.log(stringCompression('abc'), 'abc');
console.log(stringCompression('aabbcc'), 'aabbcc');