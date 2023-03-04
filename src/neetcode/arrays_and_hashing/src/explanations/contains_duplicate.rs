struct Solution;

use std::collections::HashSet;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut map = HashSet::new();

        for &n in nums.iter() {
            if map.contains(&n){
                return true;
            }
            map.insert(n);
        };
        false
    }
}

struct Nums {
    case1: Vec<i32>,
    case2: Vec<i32>,
    case3: Vec<i32>,
}

impl Nums {
    fn new() -> Self {
        Nums {
            case1 : vec![1,2,3,1],
            case2 : vec![1,2,3,4],
            case3 : vec![1,1,1,3,3,4,3,2,4,2],
        }
    }
}

pub fn execute() {
    let nums = Nums::new();
    Solution::contains_duplicate(nums.case1);
    Solution::contains_duplicate(nums.case2);
    Solution::contains_duplicate(nums.case3);
}

#[test]
fn case1() {
    let nums = Nums::new();
    assert_eq!(true, Solution::contains_duplicate(nums.case1));
}

#[test]
fn case2() {
    let nums = Nums::new();
    assert_eq!(false, Solution::contains_duplicate(nums.case2));
}

#[test]
fn case3() {
    let nums = Nums::new();
    assert_eq!(true, Solution::contains_duplicate(nums.case3));
}
