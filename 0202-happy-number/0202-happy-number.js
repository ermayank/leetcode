/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function (n) {
  let seenMap = {};

  while (n !== 1 && !seenMap[n]) {
    seenMap[n] = true;
    n = squareSum(n);
  }
  return n === 1 ? true : false;
};

function squareSum(num) {
  let sum = 0;
  num = num.toString();
  for (let i = 0; i < num.length; i++) {
    sum += num[i] * num[i];
  }
  return sum;
}
