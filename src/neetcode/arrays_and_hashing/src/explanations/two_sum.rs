struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map = HashMap::new();

        for (i, n) in nums.into_iter().enumerate() {
            let diff = target - n;

            if let Some(&j) = map.get(&diff) {
                return vec![i as i32, j as i32];
            } else {
                map.insert(n, i);
            }
        }

        unreachable!()
    }
}

struct Case {
    expected: Vec<i32>,
    nums: Vec<i32>,
    target: i32,
}

struct TestCase {
    data: Vec<Case>,
}

impl TestCase {
    fn new() -> Self {
        TestCase {
            data: vec![
                Case {
                    expected: vec![1, 0],
                    nums: vec![2, 7, 11, 15],
                    target: 9,
                },
                Case {
                    expected: vec![2, 1],
                    nums: vec![3, 2, 4],
                    target: 6,
                },
                Case {
                    expected: vec![1, 0],
                    nums: vec![3, 3],
                    target: 6,
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
        assert_eq!(case.expected, Solution::two_sum(case.nums, case.target));
    }
}
