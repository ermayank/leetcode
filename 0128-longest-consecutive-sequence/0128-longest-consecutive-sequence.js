/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
   const numSet = new Set(nums);         /* Time O(N) | Space O(N) */
   let maxScore = 0;

    for (const num of [ ...numSet ]) {
        const prevNum = num - 1;

        if (numSet.has(prevNum)) continue;

        let [ currNum, score ] = [ num, 1 ];

        const isStreak = () => numSet.has(currNum + 1)
        while (isStreak()) {              
            currNum++;
            score++;
        }

        maxScore = Math.max(maxScore, score);
    }

    return maxScore;
};