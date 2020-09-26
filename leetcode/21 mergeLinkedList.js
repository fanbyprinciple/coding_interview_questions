//https://leetcode.com/problems/merge-two-sorted-lists

// Runtime: 88 ms, faster than 67.83% of JavaScript online submissions for Merge Two Sorted Lists.
// Memory Usage: 40.1 MB, less than 5.04% of JavaScript online submissions for Merge Two Sorted Lists.



/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
    let l = new ListNode()
    let head = l
    while(l1 != null && l2 != null){
        
//         console.log("l: ", l)
//         console.log("l1 ", l1)
//         console.log("l2 ", l2)
//         console.log("l1.next ", l1.next)
//         console.log("l2.next ", l2.next)
//         console.log("l1.val ", l1.val)
//         console.log("l2.val ", l2.val)
        
        if(l1.val< l2.val){
            l.next = new ListNode(l1.val)
            l1 = l1.next
            
        } else {
            l.next = new ListNode(l2.val)
            l2 = l2.next
            //console.log(l)
        }
        
        l = l.next    
        
    }
    
    if(l1 != null){
        l.next = l1
    }
    
    if(l2 != null){
        l.next = l2
    }
    
    return head.next    
};