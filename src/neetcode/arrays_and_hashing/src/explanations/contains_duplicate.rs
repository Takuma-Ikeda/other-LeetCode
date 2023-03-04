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

struct Case {
    expected: bool,
    nums: Vec<i32>,
}

struct TestCase {
    data: Vec<Case>,
}

impl TestCase {
    fn new() -> Self {
        TestCase {
            data: vec![
                Case {
                    expected: true,
                    nums: vec![1,2,3,1],
                },
                Case {
                    expected: false,
                    nums: vec![1,2,3,4],
                },
                Case {
                    expected: true,
                    nums: vec![1,1,1,3,3,4,3,2,4,2],
                },
            ],
        }
    }
}

pub fn run() {
    execute();
}

#[test]
fn test() {
    execute();
}

fn execute() {
    let test_cases = TestCase::new();
    for case in test_cases.data.into_iter() {
        assert_eq!(case.expected, Solution::contains_duplicate(case.nums));
    }
}
