/*
One Away
There are three types of edits that can be performed on strings: insert a character,
remove a character, and replace a character. Given two strings, write a function to check
if they are one edit (or zero edits) away.
*/

const oneAway = function (str1, str2) {
    // Return false if length differs by more than 1
    if (Math.abs(str1.length - str2.length) > 1) {
        return false;
    }

    let hash = {};
    let notChar = 0;

    // Add first string to hash table
    for (let i = 0; i < str1.length; i++) {
        hash[str1[i]] = i;
    }

    console.log('hash', hash);

    for (let k = 0; k < str2.length; k++) {
        if (hash[str2[k]] === undefined) {
            notChar++;
            console.log('noChar at k=', k, ': ', notChar)
            if (notChar > 1) {
                return false;
            }
        }
    }
    return true;
}

// Test Cases
console.log(oneAway('pale', 'ple'), 'TRUE');
console.log(oneAway('pale', 'pales'), 'TRUE');
console.log(oneAway('pale', 'bale'), 'TRUE');
console.log(oneAway('pale', 'bake'), 'FALSE');