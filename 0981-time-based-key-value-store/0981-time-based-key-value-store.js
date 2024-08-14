
var TimeMap = function() {
        this.map = new Map()
};

/** 
 * @param {string} key 
 * @param {string} value 
 * @param {number} timestamp
 * @return {void}
 */
TimeMap.prototype.set = function(key, value, timestamp) {
    const myMap = this.map
    const keyVal = myMap.has(key) ? myMap.get(key) : []
    keyVal.push([value, timestamp])
    myMap.set(key, keyVal)
};

/** 
 * @param {string} key 
 * @param {number} timestamp
 * @return {string}
 */
TimeMap.prototype.get = function(key, timestamp) {
    const myMap = this.map
    const valsAtKey = myMap.has(key) ? myMap.get(key) : [];
    let res = ""
    
    //Binary Search
    let l = 0
    let r = valsAtKey.length - 1
    
    while(l <= r){
        let mid = l + Math.floor((r - l) / 2)
        if(valsAtKey[mid][1] <= timestamp){
            res = valsAtKey[mid][0]
            l = mid + 1
        }else{
            r = mid - 1
        }
    }
    return res
    
};

/** 
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */